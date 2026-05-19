from dataclasses import dataclass


SECTION_NAMES = [
    "Needs Statement",
    "Project Narrative",
    "Budget Justification",
    "Evaluation Plan",
]


@dataclass
class DraftRequest:
    client_name: str
    opportunity_title: str
    rfp_text: str
    client_context: str
    prior_successes: str
    compliance_rules: str


def build_prompt(section_name: str, request: DraftRequest) -> str:
    return f"""You are a senior grant writer.

Section: {section_name}
Client: {request.client_name}
Opportunity: {request.opportunity_title}

Requirements:
- Maintain a consistent professional voice.
- Use only supportable claims from the source materials.
- Flag missing facts instead of inventing them.
- Check compliance against the listed funder rules.

RFP:
{request.rfp_text}

Client Context:
{request.client_context}

Past Successes:
{request.prior_successes}

Compliance Rules:
{request.compliance_rules}
"""


def generate_section_stubs(request: DraftRequest) -> dict[str, str]:
    return {
        section: (
            f"# {section}\n\n"
            f"Prompt seed prepared for {request.client_name} and {request.opportunity_title}.\n\n"
            f"{build_prompt(section, request)}"
        )
        for section in SECTION_NAMES
    }

