# Grant Writing Codex MVP

This folder contains a local-first MVP scaffold for a grant writing software codex. It is designed to complement the existing `seeking/` research directories in this repository rather than replace them.

## What This Includes

- `app/` FastAPI backend modules
- `dashboard/` Streamlit frontend
- `scripts/` directory automation and operational helpers
- `tests/` smoke tests for core logic
- `docs/` living codex manual and refined prompt set

## Core Workflow

1. Create a client workspace with the directory automation script.
2. Load portal alerts or forwarded email data into the tracker database.
3. Review opportunities in the dashboard.
4. Draft proposal sections with the AI module.
5. Save proposal artifacts into the client folder using enforced file names.

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run dashboard/app.py
```

Optional API server:

```bash
uvicorn app.main:app --reload
```

## Existing Repo Alignment

- Current grant research under `seeking/` remains the source of topical opportunity research.
- This MVP adds a structured operating system for client work, opportunity tracking, and proposal generation.

## Included Example Package

- California STEP research file in [step-grants.md](/home/turbotheturtle77/01_Business/11_Grants/seeking/sba-step-california/step-grants.md)
- STEP proposal outline in [step_proposal_outline.md](/home/turbotheturtle77/01_Business/11_Grants/grant-writing-codex/templates/step_proposal_outline.md)
- STEP prompt pack in [STEP_PROMPTS.md](/home/turbotheturtle77/01_Business/11_Grants/grant-writing-codex/docs/STEP_PROMPTS.md)
