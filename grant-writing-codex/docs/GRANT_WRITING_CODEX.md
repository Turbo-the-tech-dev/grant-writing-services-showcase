# Grant Writing Software Codex

This manual defines a practical MVP for running grant research, opportunity tracking, proposal drafting, and post-award reporting from this repository.

## Purpose

The repository already contains research under `seeking/`. This codex adds the operating layer needed to turn that research into a repeatable grant writing system for actual client work.

## MVP Components

### Backend

- FastAPI service for health checks and opportunity records
- SQLAlchemy models for clients, opportunities, proposals, documents, and portal alerts
- SQLite default storage in `grant-writing-codex/data/grant_codex.db`

### Frontend

- Streamlit dashboard for tracker review, AI draft prompting, file visibility, and manual access

### Operations

- Client workspace automation under `Clients/[client]/`
- File naming enforcement with `YYYY-MM-DD_Description_Version.ext`
- Portal alert parsing stub for forwarded California Grants Portal emails
- Template merge helpers for boilerplate proposal sections
- Basic post-award reporting helpers

## Suggested Directory Standard

```text
Clients/
  gardena-example-llc/
    01_PreAward/
      Opportunity_Research/
      Proposal_Drafts/
      Budgets/
      Attachments/
    02_Award/
    03_PostAward/
      Reports/
      Financials/
    Templates_Resources/
    Research_Database/
```

## Usage Workflow

1. Research opportunities in `seeking/` and keep topic summaries current.
2. Create a client workspace with `scripts/create_client_workspace.py`.
3. Ingest new portal alerts or tracker rows into the database.
4. Review fit score, deadline, and status in the dashboard.
5. Generate proposal section prompt seeds from the AI drafting tab.
6. Store draft outputs in the client `01_PreAward/Proposal_Drafts/` folder with enforced names.
7. After award, log progress reports and closeout materials under `03_PostAward/`.

## Database Outline

### Clients

- One record per client organization
- Stores location, sector, and notes

### Grant Opportunities

- Captures date received, deadline, funding amount, fit score, status, eligibility, and focus
- Links to client when an opportunity is being actively pursued for a specific client

### Proposals

- Tracks proposal stage, narrative location, budget location, and submission date

### Documents

- Stores normalized file metadata and paths

### Portal Alerts

- Preserves raw alert content for traceability and future parser improvements

## AI Drafting Guidance

The current AI module builds section-specific prompt seeds instead of calling a provider directly. This keeps the MVP safe for local use while preserving a clean integration point for OpenAI or Anthropic later.

Prompt design rules:

- Use source-backed facts only
- Flag missing data instead of fabricating it
- Keep a consistent professional voice
- Check section content against funder compliance rules

## Security Notes

- Store API keys outside the repo when provider integrations are added
- Avoid placing confidential client source documents in public sync locations
- Keep raw portal alerts for auditability, but review them for personal data before sharing

## California-Focused Extension Ideas

- Add parser rules tuned for California Grants Portal email formats
- Create saved tracker filters for California state agencies
- Link local Gardena, Los Angeles County, and Southern California funder research into the tracker

## Included STEP Package

The repository now includes a concrete California STEP example package that can be reused for client work:

- Research summary in [step-grants.md](/home/turbotheturtle77/01_Business/11_Grants/seeking/sba-step-california/step-grants.md)
- Proposal outline in [step_proposal_outline.md](/home/turbotheturtle77/01_Business/11_Grants/grant-writing-codex/templates/step_proposal_outline.md)
- AI prompts in [STEP_PROMPTS.md](/home/turbotheturtle77/01_Business/11_Grants/grant-writing-codex/docs/STEP_PROMPTS.md)

## Near-Term Build Order

1. Seed a few real opportunities into the tracker
2. Add Alembic migrations
3. Add CSV or Excel import for the existing tracker
4. Plug in one AI provider behind environment-based configuration
5. Add editable dashboard actions for status changes and document linking
