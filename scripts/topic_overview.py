"""Insere o resumo padronizado nas páginas de tópicos."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from main import TOPIC_OVERVIEWS, render_topic_overview


def on_page_markdown(markdown, *, page, config, files):
    """Adiciona a visão geral configurada imediatamente após o título da página."""
    topic = TOPIC_OVERVIEWS.get(page.file.src_path)
    if not topic:
        return markdown

    heading = re.search(r"^# .+$", markdown, flags=re.MULTILINE)
    if not heading:
        return markdown

    overview = render_topic_overview(topic)
    return f"{markdown[:heading.end()]}\n\n{overview}\n{markdown[heading.end():]}"
