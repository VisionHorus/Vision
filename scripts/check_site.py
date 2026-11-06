#!/usr/bin/env python3
"""Run dependency-free structural checks against the static Vision site."""
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.description = ""
        self.keywords = ""
        self.h1_texts = []
        self.h2_texts = []
        self.ids = set()
        self.references = []
        self.json_ld = []
        self.meta_names = {}
        self.meta_properties = {}
        self._in_title = False
        self._in_json = False
        self._heading = None
        self._svg_depth = 0
        self._title_parts = []
        self._heading_parts = []
        self._json_parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "svg":
            self._svg_depth += 1
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if "style" in attrs:
            raise AssertionError("inline style attribute found")
        if tag == "title" and self._svg_depth == 0:
            self._in_title = True
            self._title_parts = []
        if tag in ("h1", "h2"):
            self._heading = tag
            self._heading_parts = []
        if tag == "meta":
            name = attrs.get("name", "").lower()
            prop = attrs.get("property", "").lower()
            if name:
                self.meta_names[name] = attrs.get("content", "")
            if prop:
                self.meta_properties[prop] = attrs.get("content", "")
            if name == "description":
                self.description = attrs.get("content", "")
            if name == "keywords":
                self.keywords = attrs.get("content", "")
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self._in_json = True
            self._json_parts = []
        for key in ("href", "src"):
            value = attrs.get(key)
            if value:
                self.references.append(value)

    def handle_endtag(self, tag):
        if tag == "title" and self._in_title:
            self._in_title = False
            self.title = "".join(self._title_parts).strip()
        if tag in ("h1", "h2") and self._heading == tag:
            text = " ".join("".join(self._heading_parts).split())
            (self.h1_texts if tag == "h1" else self.h2_texts).append(text)
            self._heading = None
        if tag == "script" and self._in_json:
            self._in_json = False
            self.json_ld.append("".join(self._json_parts))
        if tag == "svg":
            self._svg_depth = max(0, self._svg_depth - 1)

    def handle_data(self, data):
        if self._in_title:
            self._title_parts.append(data)
        if self._heading:
            self._heading_parts.append(data)
        if self._in_json:
            self._json_parts.append(data)


def local_target(page: Path, reference: str):
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc:
        return None, parsed.fragment
    if not parsed.path:
        target = page.resolve()
    elif parsed.path.startswith("/"):
        target = PUBLIC / parsed.path.lstrip("/")
    else:
        target = page.parent / parsed.path
    if parsed.path.endswith("/") or (target.exists() and target.is_dir()):
        target = target / "index.html"
    return target.resolve(), parsed.fragment


def parse_page(page: Path) -> PageParser:
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))
    return parser


def main():
    manifest = json.loads((PUBLIC / "manus-routes.json").read_text(encoding="utf-8"))
    route_pages = {}
    for route in manifest["routes"]:
        path = route["path"]
        page = PUBLIC / ("index.html" if path == "/" else path.strip("/") + "/index.html")
        assert page.exists(), f"Missing route file: {path}"
        route_pages[path] = page

    errors = []
    parsed_pages = {}
    for route, page in route_pages.items():
        parser = parse_page(page)
        parsed_pages[page.resolve()] = parser
        if not (30 <= len(parser.title) <= 60):
            errors.append(f"{route}: title length should be 30–60, got {len(parser.title)}")
        if not (50 <= len(parser.description) <= 160):
            errors.append(f"{route}: description length should be 50–160, got {len(parser.description)}")
        keyword_count = len([word for word in parser.keywords.split(",") if word.strip()])
        if not (3 <= keyword_count <= 8):
            errors.append(f"{route}: meta keywords should contain 3–8 terms, got {keyword_count}")
        if len(parser.h1_texts) != 1:
            errors.append(f"{route}: expected one H1, found {len(parser.h1_texts)}")
        if any(len(text) > 80 for text in parser.h1_texts + parser.h2_texts):
            errors.append(f"{route}: H1/H2 must stay at or below 80 characters")
        for required in ("og:type", "og:title", "og:description", "og:site_name"):
            if not parser.meta_properties.get(required):
                errors.append(f"{route}: {required} missing")
        for required in ("twitter:card", "twitter:title", "twitter:description"):
            if not parser.meta_names.get(required):
                errors.append(f"{route}: {required} missing")
        for block in parser.json_ld:
            try:
                json.loads(block)
            except json.JSONDecodeError as exc:
                errors.append(f"{route}: invalid JSON-LD: {exc}")
        for reference in parser.references:
            target, fragment = local_target(page, reference)
            if target is None:
                continue
            if not target.exists():
                errors.append(f"{route}: broken local reference {reference}")
                continue
            if fragment and target.suffix == ".html":
                target_parser = parsed_pages.get(target) or parse_page(target)
                parsed_pages[target] = target_parser
                if fragment not in target_parser.ids:
                    errors.append(f"{route}: missing fragment #{fragment} in {reference}")

    diagnostic = (PUBLIC / "diagnostico" / "index.html").read_text(encoding="utf-8")
    form_script = (PUBLIC / "assets" / "js" / "diagnostic-form.js").read_text(encoding="utf-8")
    if 'data-diagnostic-form' not in diagnostic or 'type="submit">Continuar no WhatsApp' not in diagnostic:
        errors.append("diagnostico: WhatsApp submit action should be available")
    if 'https://wa.me/${whatsappNumber}' not in form_script or 'const whatsappNumber = "000000000"' not in form_script:
        errors.append("diagnostico: form should open WhatsApp with the configured destination")
    if "em preparação" in diagnostic.lower() or "envio ainda não disponível" in diagnostic.lower():
        errors.append("diagnostico: remove obsolete under-construction contact notices")

    if 'id="site" name="site" type="text" inputmode="url"' not in diagnostic:
        errors.append("diagnostico: Site/Instagram should accept URLs and @profiles as text")
    for slug in ("criacao-de-sites", "seo-local", "inteligencia-digital"):
        page_html = (PUBLIC / slug / "index.html").read_text(encoding="utf-8")
        if 'aria-current="page">Soluções' in page_html:
            errors.append(f"{slug}: generic Soluções link must not be marked as the current page")
    not_found = (PUBLIC / "404.html").read_text(encoding="utf-8")
    if "data-menu-toggle" not in not_found or "data-primary-nav" not in not_found:
        errors.append("404: mobile navigation toggle and expandable nav are required")

    catalog = json.loads((ROOT / "content" / "projects.json").read_text(encoding="utf-8"))
    projects_page = route_pages.get("/projetos/")
    if projects_page:
        project_parser = parse_page(projects_page)
        project_html = projects_page.read_text(encoding="utf-8")
        item_list = None
        for block in project_parser.json_ld:
            try:
                candidate = json.loads(block)
            except json.JSONDecodeError:
                continue
            if candidate.get("@type") == "ItemList":
                item_list = candidate
                break
        expected_names = [item["name"] for item in catalog]
        schema_names = [item.get("name") for item in item_list.get("itemListElement", [])] if item_list else []
        if schema_names != expected_names:
            errors.append("projetos: JSON-LD ItemList must match the central catalog order and names")
        if any(name not in project_html for name in expected_names):
            errors.append("projetos: visible cards must contain every project from the central catalog")

    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print(f"PASS: {len(route_pages)} routes; SEO thresholds, social metadata, JSON-LD, links and fragments verified.")
    print("WhatsApp contact form and links verified in source. Absolute canonical/sitemap URLs need a real domain; the WebDev published gateway handles sitemap/robots, while this Preview returned 404 for those paths.")


if __name__ == "__main__":
    main()
