"""Diretivas de conteúdo para a versão impressa do guia.

O hook também roda no site normal: blocos ``pdf:only`` permanecem invisíveis na
tela por CSS, mas o restante do conteúdo não é alterado.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

from mkdocs_print_site_plugin.exclude import exclude as is_excluded


_BLOCK = re.compile(
    r"^\s*<!--\s*pdf:(exclude|only):(start|end)\s*-->\s*$", re.IGNORECASE
)
_BREAK = re.compile(r"^\s*<!--\s*pdf:page-break\s*-->\s*$", re.IGNORECASE)
_SKIP = re.compile(r"^\s*<!--\s*pdf:exclude-page\s*-->\s*$", re.IGNORECASE)
_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def _outside_fenced_code(lines: list[str]):
    """Yield lines and whether each is outside a fenced code block."""
    in_fence = False
    for line in lines:
        if _FENCE.match(line):
            yield line, not in_fence
            in_fence = not in_fence
            continue
        yield line, not in_fence


def _has_page_exclusion(markdown: str) -> bool:
    return any(outside and _SKIP.match(line) for line, outside in _outside_fenced_code(markdown.splitlines()))


def _replace_directives(markdown: str, source: str) -> str:
    output: list[str] = []
    opened: list[str] = []

    for line, outside in _outside_fenced_code(markdown.splitlines(keepends=True)):
        if not outside:
            output.append(line)
            continue

        block = _BLOCK.match(line)
        if block:
            kind, action = (part.lower() for part in block.groups())
            if action == "start":
                opened.append(kind)
                output.append(f'<div class="pdf-{kind}">\n')
            else:
                if not opened or opened[-1] != kind:
                    raise ValueError(
                        f"Diretiva pdf:{kind}:end sem abertura correspondente em {source}."
                    )
                opened.pop()
                output.append("</div>\n")
            continue

        if _BREAK.match(line):
            output.append('<div class="pdf-page-break" aria-hidden="true"></div>\n')
            continue

        output.append(line)

    if opened:
        raise ValueError(f"Diretiva pdf:{opened[-1]}:start sem fechamento em {source}.")
    return "".join(output)


def on_files(files, config, **kwargs):
    """Acrescenta ao print-site as páginas marcadas para não sair no PDF."""
    if os.environ.get("CP_GUIDE_PDF") != "1":
        return files

    print_site = config["plugins"].get("print-site")
    if print_site is None:
        return files

    excluded = list(print_site.config.get("exclude", []))
    for file in files.documentation_pages():
        source = Path(file.abs_src_path)
        if _has_page_exclusion(source.read_text(encoding="utf-8")):
            excluded.append(file.src_path.replace("\\", "/"))
    print_site.config["exclude"] = excluded
    return files


def on_page_markdown(markdown, page, **kwargs):
    """Converte as diretivas Markdown em elementos que o CSS de impressão controla."""
    return _replace_directives(markdown, page.file.src_path)


def on_nav(nav, config, **kwargs):
    """Remove também as seções que ficaram sem páginas depois das exclusões."""
    if os.environ.get("CP_GUIDE_PDF") != "1":
        return nav

    print_site = config["plugins"].get("print-site")
    if print_site is None:
        return nav
    excluded = print_site.config.get("exclude", [])

    def keep(items):
        kept = []
        for item in items:
            if item.is_page:
                if not is_excluded(item.file.src_path, excluded):
                    kept.append(item)
            elif item.is_section:
                item.children[:] = keep(item.children)
                if item.children:
                    kept.append(item)
            else:
                kept.append(item)
        return kept

    nav.items[:] = keep(nav.items)
    return nav
