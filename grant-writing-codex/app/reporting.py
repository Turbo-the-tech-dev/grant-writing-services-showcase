from datetime import date


def build_progress_report(client_name: str, project_name: str, accomplishments: list[str]) -> str:
    bullets = "\n".join(f"- {item}" for item in accomplishments)
    return (
        f"# Progress Report\n\n"
        f"**Client:** {client_name}\n"
        f"**Project:** {project_name}\n"
        f"**Report Date:** {date.today().isoformat()}\n\n"
        f"## Accomplishments\n{bullets}\n"
    )


def build_closeout_checklist() -> list[str]:
    return [
        "Confirm final expenditure reconciliation.",
        "Submit final narrative and performance metrics.",
        "Archive signed agreements and amendments.",
        "Store closeout deliverables in the client post-award folder.",
    ]

