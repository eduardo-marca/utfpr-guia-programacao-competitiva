"""Macros compartilhadas do Guia de Programação Competitiva."""

from collections.abc import Mapping, Sequence
from html import escape

import yaml
from markupsafe import Markup


CATEGORIES = (
    ("recommended", "Recomendados"),
    ("additional", "Adicionais"),
    ("solved", "Resolvidos"),
)

DIFFICULTIES = {
    "easy": "Fácil",
    "medium": "Intermediário",
    "hard": "Avançado",
}


def _text(value: object) -> str:
    return escape(str(value))


def _metadata(label: str, value: str, class_name: str = "") -> str:
    css_class = f" exercise-list__meta--{class_name}" if class_name else ""
    return (
        f'<span class="exercise-list__meta{css_class}">'
        f'<span class="exercise-list__label">{_text(label)}</span>{_text(value)}</span>'
    )


def _render_exercise(exercise: Mapping[str, object]) -> str:
    try:
        name = _text(exercise["name"])
        url = _text(exercise["url"])
    except KeyError as error:
        raise ValueError(f"Cada exercício precisa de '{error.args[0]}'.") from error

    metadata = []
    if platform := exercise.get("platform"):
        metadata.append(_metadata("Plataforma", str(platform)))

    if difficulty := exercise.get("difficulty"):
        try:
            difficulty_label = DIFFICULTIES[str(difficulty)]
        except KeyError as error:
            allowed = ", ".join(DIFFICULTIES)
            raise ValueError(f"Dificuldade '{difficulty}' inválida. Use: {allowed}.") from error
        metadata.append(_metadata("Dificuldade", difficulty_label, str(difficulty)))

    topics = exercise.get("topics", [])
    if topics:
        if not isinstance(topics, Sequence) or isinstance(topics, str):
            raise ValueError("'topics' deve ser uma lista.")
        topic_tags = "".join(
            f'<span class="exercise-list__topic">{_text(topic)}</span>' for topic in topics
        )
        metadata.append(
            '<span class="exercise-list__meta exercise-list__meta--topics">'
            '<span class="exercise-list__label">Tópicos</span>'
            f'<span class="exercise-list__topics">{topic_tags}</span></span>'
        )

    objective = exercise.get("objective")
    objective_html = (
        f'<p class="exercise-list__objective">{_text(objective)}</p>' if objective else ""
    )
    return (
        '<li class="exercise-list__item">'
        f'<a class="exercise-list__link" href="{url}" target="_blank" rel="noopener">'
        f'{name}<span class="exercise-list__external" aria-hidden="true">↗</span></a>'
        f'<div class="exercise-list__details">{"".join(metadata)}</div>'
        f'{objective_html}'
        '</li>'
    )


def define_env(env):
    @env.macro
    def exercise_list(exercises: Mapping[str, object]) -> Markup:
        """Renderiza uma lista de exercícios declarada em YAML na página."""
        if isinstance(exercises, str):
            exercises = yaml.safe_load(exercises) or {}
        if not isinstance(exercises, Mapping):
            raise ValueError("exercise_list espera um mapa de categorias de exercícios.")

        sections = []
        for category, title in CATEGORIES:
            items = exercises.get(category, [])
            if not items:
                continue
            if not isinstance(items, Sequence) or isinstance(items, str):
                raise ValueError(f"A categoria '{category}' deve conter uma lista.")
            rendered_items = "".join(_render_exercise(item) for item in items)
            sections.append(
                f'### {title}\n\n'
                '<ol class="exercise-list">'
                f'{rendered_items}'
                '</ol>'
            )

        if not sections:
            return Markup("")
        return Markup("\n\n".join(sections))
