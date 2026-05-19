import re
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ParsedAlert:
    title: str
    deadline_text: str | None
    amount_text: str | None
    eligibility: str | None
    source_identifier: str
    raw_payload: str


DEADLINE_RE = re.compile(r"deadline[:\s]+([A-Za-z0-9, /-]+)", re.IGNORECASE)
AMOUNT_RE = re.compile(r"(?:amount|funding)[:\s]+\$?([A-Za-z0-9,.\- ]+)", re.IGNORECASE)
ELIGIBILITY_RE = re.compile(r"eligibility[:\s]+(.+)", re.IGNORECASE)


def parse_forwarded_email(subject: str, body: str) -> ParsedAlert:
    deadline = _match_group(DEADLINE_RE, body)
    amount = _match_group(AMOUNT_RE, body)
    eligibility = _match_group(ELIGIBILITY_RE, body)
    title = subject.replace("Fwd:", "").strip() or f"Portal Alert {datetime.utcnow().date()}"
    return ParsedAlert(
        title=title,
        deadline_text=deadline,
        amount_text=amount,
        eligibility=eligibility,
        source_identifier=subject,
        raw_payload=body,
    )


def _match_group(pattern: re.Pattern[str], text: str) -> str | None:
    match = pattern.search(text)
    return match.group(1).strip() if match else None

