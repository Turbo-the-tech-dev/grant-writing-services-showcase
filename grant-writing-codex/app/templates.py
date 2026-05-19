from pathlib import Path


def load_template_sections(template_dir: Path) -> dict[str, str]:
    sections: dict[str, str] = {}
    for path in sorted(template_dir.glob("*.md")):
        sections[path.stem] = path.read_text(encoding="utf-8")
    return sections


def merge_template_with_client_data(template_text: str, replacements: dict[str, str]) -> str:
    result = template_text
    for key, value in replacements.items():
        result = result.replace(f"{{{{{key}}}}}", value)
    return result

