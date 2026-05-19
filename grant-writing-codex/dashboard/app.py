from pathlib import Path

import streamlit as st

from app.ai import DraftRequest, generate_section_stubs
from app.database import SessionLocal, init_db
from app.models import GrantOpportunity


BASE_DIR = Path(__file__).resolve().parents[1]
init_db()

st.set_page_config(page_title="Grant Writing Codex", layout="wide")
st.title("Grant Writing Codex")
st.caption("Local-first MVP for grant tracking, client structure, and AI drafting.")

tab_tracker, tab_drafting, tab_files, tab_manual = st.tabs(
    ["Opportunity Tracker", "AI Drafting", "File Browser", "Manual"]
)

with tab_tracker:
    st.subheader("Opportunity Tracker")
    with SessionLocal() as db:
        rows = db.query(GrantOpportunity).order_by(GrantOpportunity.deadline).all()
    if rows:
        st.dataframe(
            [
                {
                    "Title": row.title,
                    "Agency": row.agency_name,
                    "Deadline": row.deadline,
                    "Funding": row.funding_amount,
                    "Fit Score": row.fit_score,
                    "Status": row.status,
                }
                for row in rows
            ],
            use_container_width=True,
        )
    else:
        st.info("No opportunities loaded yet.")

with tab_drafting:
    st.subheader("AI Proposal Draft Generator")
    client_name = st.text_input("Client name", "Gardena Example LLC")
    opportunity_title = st.text_input("Opportunity title", "Sample Community Grant")
    rfp_text = st.text_area("RFP text")
    client_context = st.text_area("Client context")
    prior_successes = st.text_area("Past successes")
    compliance_rules = st.text_area("Compliance rules")
    if st.button("Generate Draft Seeds"):
        request = DraftRequest(
            client_name=client_name,
            opportunity_title=opportunity_title,
            rfp_text=rfp_text,
            client_context=client_context,
            prior_successes=prior_successes,
            compliance_rules=compliance_rules,
        )
        sections = generate_section_stubs(request)
        for name, content in sections.items():
            st.markdown(content)

with tab_files:
    st.subheader("File Browser")
    for path in sorted((BASE_DIR / "docs").rglob("*.md")):
        st.write(path.relative_to(BASE_DIR).as_posix())

with tab_manual:
    st.subheader("Codex Manual")
    manual_path = BASE_DIR / "docs" / "GRANT_WRITING_CODEX.md"
    st.markdown(manual_path.read_text(encoding="utf-8"))

