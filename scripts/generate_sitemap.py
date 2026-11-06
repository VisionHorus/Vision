#!/usr/bin/env python3
"""Add absolute SEO URLs only after the real HTTPS site origin is known."""
import argparse
from html import escape
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT


def clean_origin(value: str) -> str:
    parsed = urlsplit(value.strip().rstrip("/"))
    if parsed.scheme != "https" or not parsed.netloc or parsed.path not in ("", "/") or parsed.query or parsed.fragment or parsed.username:
        raise SystemExit("Informe a origem pública real, no formato https://seudominio.com, sem caminho, consulta ou fragmento.")
    return f"https://{parsed.netloc}"


def upsert_tag(source: str, pattern: str, tag: str) -> str:
    if re.search(pattern, source, flags=re.IGNORECASE):
        return re.sub(pattern, lambda _: tag, source, count=1, flags=re.IGNORECASE)
    return re.sub(r"</head>", lambda _: f"  {tag}\n</head>", source, count=1, flags=re.IGNORECASE)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("origin", help="Domínio HTTPS real, por exemplo https://vision.com.br")
    args = parser.parse_args()
    origin = clean_origin(args.origin)
    manifest = json.loads((PUBLIC / "manus-routes.json").read_text(encoding="utf-8"))
    entries = []
    for route in manifest["routes"]:
        path = route["path"]
        url = origin + (path if path.startswith("/") else "/" + path)
        entries.append(f"  <url><loc>{escape(url)}</loc></url>")
        html_path = PUBLIC / ("index.html" if path == "/" else path.strip("/") + "/index.html")
        if not html_path.exists():
            raise SystemExit(f"Página do manifesto não encontrada: {html_path}")
        source = html_path.read_text(encoding="utf-8")
        canonical = f'<link rel="canonical" href="{escape(url, quote=True)}">'
        og_url = f'<meta property="og:url" content="{escape(url, quote=True)}">'
        image_url = escape(origin + "/assets/images/vision-symbol.png", quote=True)
        og_image = f'<meta property="og:image" content="{image_url}">'
        og_alt = '<meta property="og:image:alt" content="Símbolo oficial da Vision">'
        twitter_image = f'<meta name="twitter:image" content="{image_url}">'
        twitter_alt = '<meta name="twitter:image:alt" content="Símbolo oficial da Vision">'
        twitter_card = '<meta name="twitter:card" content="summary_large_image">'
        source = upsert_tag(source, r'<link\s+rel=["\']canonical["\'][^>]*>', canonical)
        source = upsert_tag(source, r'<meta\s+property=["\']og:url["\'][^>]*>', og_url)
        source = upsert_tag(source, r'<meta\s+property=["\']og:image["\'][^>]*>', og_image)
        source = upsert_tag(source, r'<meta\s+property=["\']og:image:alt["\'][^>]*>', og_alt)
        source = upsert_tag(source, r'<meta\s+name=["\']twitter:card["\'][^>]*>', twitter_card)
        source = upsert_tag(source, r'<meta\s+name=["\']twitter:image["\'][^>]*>', twitter_image)
        source = upsert_tag(source, r'<meta\s+name=["\']twitter:image:alt["\'][^>]*>', twitter_alt)
        html_path.write_text(source, encoding="utf-8")
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(entries) + "\n</urlset>\n"
    (PUBLIC / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    robots_path = PUBLIC / "robots.txt"
    robots = "User-agent: *\nAllow: /\nDisallow: /api/*\n"
    robots += f"Sitemap: {origin}/sitemap.xml\n"
    robots_path.write_text(robots, encoding="utf-8")
    print(f"Sitemap and canonical URLs generated for {origin} ({len(manifest['routes'])} routes).")


if __name__ == "__main__":
    main()
