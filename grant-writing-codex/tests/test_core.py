from pathlib import Path

from app.ai import DraftRequest, generate_section_stubs
from app.portal import parse_forwarded_email
from scripts.create_client_workspace import create_client_workspace, enforce_file_name


def test_file_name_enforcement():
    output = enforce_file_name("budget.DOCX", "Budget Narrative", "v2")
    assert output.endswith("_Budget_Narrative_v2.docx") or output.endswith("_budget_narrative_v2.docx")


def test_workspace_creation(tmp_path: Path):
    client_dir = create_client_workspace(tmp_path, "Gardena Example LLC")
    assert (client_dir / "01_PreAward" / "Proposal_Drafts").exists()
    assert (client_dir / "03_PostAward" / "Reports").exists()


def test_portal_parser_extracts_fields():
    subject = "Fwd: California Energy Grant"
    body = "Deadline: June 30, 2026\nFunding: $50,000\nEligibility: Small businesses"
    parsed = parse_forwarded_email(subject, body)
    assert parsed.title == "California Energy Grant"
    assert parsed.amount_text == "50,000"
    assert parsed.eligibility == "Small businesses"


def test_ai_stubs_generate_all_sections():
    request = DraftRequest(
        client_name="Gardena Example LLC",
        opportunity_title="Sample Grant",
        rfp_text="Provide a narrative and evaluation plan.",
        client_context="A small business serving Gardena.",
        prior_successes="Won one local innovation grant.",
        compliance_rules="Do not exceed page limits.",
    )
    sections = generate_section_stubs(request)
    assert len(sections) == 4
    assert "Needs Statement" in sections

