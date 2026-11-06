#!/usr/bin/env python3
"""Render project cards and their JSON-LD from one central catalog."""
import html
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "content" / "projects.json"
CARD_MARKER = re.compile(r"<!-- PROJECTS:START -->.*?<!-- PROJECTS:END -->", re.DOTALL)
SCHEMA_MARKER = re.compile(r"<!-- PROJECTS-JSONLD:START -->.*?<!-- PROJECTS-JSONLD:END -->", re.DOTALL)


def esc(value: str) -> str:
    return html.escape(str(value), quote=True)


def catalog() -> list[dict]:
    return json.loads(DATA.read_text(encoding="utf-8"))


def render_card(project: dict, full: bool) -> str:
    name = esc(project["name"])
    url = esc(project["url"])
    image = esc(project["image"])
    alt = esc(project["imageAlt"])
    category = esc(project["category"])
    description = esc(project["description"] if full else project["shortDescription"])
    link_label = "Ver site do projeto" if full else "Ver projeto"
    media_modifier = " project-card__media--euro" if project["slug"] == "eurogenesis" else ""
    source_note = f'<p class="project-source-note">Fonte: site público de {name}.</p>' if full else ""
    return f'''<article class="project-card">
  <a href="{url}" target="_blank" rel="noopener noreferrer" aria-label="Abrir o site de {name}, em nova aba">
    <div class="project-card__media{media_modifier}"><img src="/assets/images/{image}" alt="{alt}" width="{int(project['imageWidth'])}" height="{int(project['imageHeight'])}" loading="lazy" decoding="async"></div>
  </a>
  <div class="project-card__body"><span class="project-card__category">{category}</span><h3>{name}</h3><p>{description}</p><a class="text-link" href="{url}" target="_blank" rel="noopener noreferrer">{link_label}</a>{source_note}</div>
</article>'''


def update_cards(relative_path: str, full: bool) -> None:
    path = ROOT / relative_path
    source = path.read_text(encoding="utf-8")
    if not CARD_MARKER.search(source):
        raise SystemExit(f"Project card markers not found in {path}")
    cards = "\n".join(render_card(item, full) for item in catalog())
    replacement = f"<!-- PROJECTS:START -->\n{cards}\n      <!-- PROJECTS:END -->"
    path.write_text(CARD_MARKER.sub(lambda _: replacement, source, count=1), encoding="utf-8")
    print(f"Updated cards in {path.relative_to(ROOT)}")


def update_schema() -> None:
    path = ROOT / "projetos" / "index.html"
    source = path.read_text(encoding="utf-8")
    if not SCHEMA_MARKER.search(source):
        raise SystemExit(f"Project JSON-LD markers not found in {path}")
    items = [
        {"@type": "ListItem", "position": index, "name": project["name"], "url": project["url"]}
        for index, project in enumerate(catalog(), start=1)
    ]
    schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Projetos digitais apresentados pela Vision",
        "itemListElement": items,
    }
    json_ld = json.dumps(schema, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    replacement = f"<!-- PROJECTS-JSONLD:START -->\n  <script type=\"application/ld+json\">{json_ld}</script>\n  <!-- PROJECTS-JSONLD:END -->"
    path.write_text(SCHEMA_MARKER.sub(lambda _: replacement, source, count=1), encoding="utf-8")
    print("Updated project JSON-LD")


if __name__ == "__main__":
    update_cards("index.html", full=False)
    update_cards("projetos/index.html", full=True)
    update_schema()
