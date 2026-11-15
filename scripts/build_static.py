#!/usr/bin/env python3
"""Build a validated, dependency-free static release into dist/."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist"
PUBLIC_ORIGIN = "https://www.visionintelligence.com.br"
PAGE_DIRECTORIES = (
    "agenciamento-digital",
    "criacao-de-sites",
    "seo-local",
    "inteligencia-digital",
    "projetos",
    "diagnostico",
    "privacidade",
    "termos",
    "cookies",
)
ROOT_FILES = (
    "index.html",
    "404.html",
    "manus-routes.json",
    "robots.txt",
    "sitemap.xml",
)
REFERENCE_IMAGES = {"reference-owl.webp", "reference-woman-orange.webp"}


def run_script(filename: str, *arguments: str) -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / filename), *arguments],
        cwd=ROOT,
        check=True,
    )


def ignore_assets(directory: str, names: list[str]) -> set[str]:
    if Path(directory).name == "images":
        return set(names) & REFERENCE_IMAGES
    return set()


def main() -> None:
    run_script("build_projects.py")
    run_script("generate_sitemap.py", PUBLIC_ORIGIN)
    run_script("check_site.py")

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    for filename in ROOT_FILES:
        source = ROOT / filename
        if source.is_file():
            shutil.copy2(source, OUTPUT / filename)
    for directory in PAGE_DIRECTORIES:
        source = ROOT / directory
        if not (source / "index.html").is_file():
            raise SystemExit(f"Página pública ausente: {directory}/index.html")
        shutil.copytree(source, OUTPUT / directory)
    shutil.copytree(ROOT / "assets", OUTPUT / "assets", ignore=ignore_assets)

    manifest = json.loads((OUTPUT / "manus-routes.json").read_text(encoding="utf-8"))
    page_count = len(manifest["routes"])
    print(f"Build estático concluído: {page_count} rotas públicas em {OUTPUT.relative_to(ROOT)}/.")


if __name__ == "__main__":
    main()
