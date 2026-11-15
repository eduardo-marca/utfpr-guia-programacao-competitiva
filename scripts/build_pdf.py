#!/usr/bin/env python3
"""Gera a referência PDF a partir da página única do mkdocs-print-site."""

from __future__ import annotations

import argparse
import asyncio
import html
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "mkdocs-pdf.yml"
DEFAULT_OUTPUT = ROOT / "output" / "pdf" / "guia-programacao-competitiva-utfpr.pdf"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gera a referência de competição em PDF a partir do guia MkDocs."
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Caminho do PDF final.")
    parser.add_argument("--paper", default="A4", choices=("A4", "Letter"), help="Formato do papel.")
    parser.add_argument(
        "--orientation",
        default="portrait",
        choices=("portrait", "landscape"),
        help="Orientação da folha.",
    )
    parser.add_argument("--margin-mm", type=float, default=10, help="Margem física da página em mm.")
    parser.add_argument("--title", default="Guia de Programação Competitiva UTFPR", help="Título no rodapé.")
    parser.add_argument("--no-cover", action="store_true", help="Remove a capa do PDF.")
    parser.add_argument(
        "--keep-site", action="store_true", help="Mantém o HTML intermediário em tmp/pdfs para depuração."
    )
    return parser.parse_args()


async def render_pdf(args: argparse.Namespace, print_page: Path, output: Path) -> None:
    from playwright.async_api import async_playwright

    chrome = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
    if chrome is None:
        raise RuntimeError("Chrome ou Chromium não encontrado no PATH.")

    margin = f"{args.margin_mm}mm"
    safe_title = html.escape(args.title)
    header = '<div style="width:100%;font-size:7px;color:#64748b;padding:0 10mm"></div>'
    footer = (
        '<div style="width:100%;font-size:7px;color:#475569;padding:0 10mm;display:flex;justify-content:space-between">'
        f"<span>{safe_title}</span><span>Página <span class=\"pageNumber\"></span> de <span class=\"totalPages\"></span></span>"
        "</div>"
    )

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(executable_path=chrome, headless=True)
        page = await browser.new_page()
        try:
            await page.goto(print_page.as_uri(), wait_until="networkidle")
            await page.emulate_media(media="print")
            await page.evaluate(
                """async () => {
                    await document.fonts.ready;
                    await Promise.all([...document.images].map(image => image.complete ? null : new Promise(resolve => {
                        image.addEventListener('load', resolve, {once: true});
                        image.addEventListener('error', resolve, {once: true});
                    })));
                    if (window.MathJax?.typesetPromise) await window.MathJax.typesetPromise();
                }"""
            )
            if args.no_cover:
                await page.add_style_tag(content="#print-site-cover-page { display: none !important; }")
            await page.pdf(
                path=str(output),
                format=args.paper,
                landscape=args.orientation == "landscape",
                print_background=True,
                display_header_footer=True,
                header_template=header,
                footer_template=footer,
                margin={"top": margin, "right": margin, "bottom": margin, "left": margin},
                prefer_css_page_size=False,
            )
        finally:
            await browser.close()


def main() -> int:
    args = parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)

    temporary_root = ROOT / "tmp" / "pdfs"
    temporary_root.mkdir(parents=True, exist_ok=True)
    site_dir = Path(tempfile.mkdtemp(prefix="cp-guide-pdf-", dir=temporary_root))
    # markdown-katex tenta executar ``npx --no-install katex`` quando npx está
    # no PATH. Em instalações sem o pacote npm isso pode ficar aguardando uma
    # resolução de rede. Um PATH propositalmente vazio faz a extensão usar o
    # binário KaTeX que ela própria distribui.
    environment = os.environ | {"CP_GUIDE_PDF": "1", "PATH": "/__cp_guide_no_npx__"}
    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "mkdocs",
                "build",
                "--clean",
                "--config-file",
                str(PROFILE),
                "--site-dir",
                str(site_dir),
            ],
            cwd=ROOT,
            env=environment,
            check=True,
        )
        print_page = site_dir / "print_page" / "index.html"
        if not print_page.is_file():
            raise RuntimeError(f"Página de impressão não encontrada: {print_page}")
        asyncio.run(render_pdf(args, print_page, output))
    finally:
        if args.keep_site:
            print(f"HTML intermediário preservado em {site_dir}")
        else:
            shutil.rmtree(site_dir, ignore_errors=True)

    print(f"PDF gerado em {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
