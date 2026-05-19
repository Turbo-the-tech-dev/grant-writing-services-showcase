# Refined Build Prompts

These prompts are rewritten to fit this repository, its `seeking/` research structure, and a local-first grant operations workflow.

## 1. Architecture Prompt

Act as a senior full-stack developer and grant writing operations architect. Design a local-first Grant Writing Codex in Python with a FastAPI backend and a Streamlit frontend. The codex must fit into an existing repository that already stores grant research in `seeking/` subfolders with one primary markdown file per topic. Add modules for client management, directory automation under `Clients/[client]/01_PreAward`, California Grants Portal alert ingestion through forwarded emails or portal exports, an opportunity tracker in SQLite with a path to PostgreSQL later, AI proposal drafting, file naming enforcement using `YYYY-MM-DD_Description_Version.ext`, document templates, and post-award reporting. Output the project structure, key files, database entities, and the shortest path to a usable MVP for a solo grant writer in Gardena, California.

## 2. Database And Tracker Prompt

Create a full SQLAlchemy and Alembic schema for a grant management system. Include `clients`, `grant_opportunities`, `proposals`, `documents`, and `portal_alerts`. The opportunities table must cover tracker fields such as `date_received`, `deadline`, `fit_score`, `status`, `funding_amount`, `focus`, `eligibility`, and `notes`. Add relationships, indexes worth creating for deadline and status filtering, and example queries that surface high-fit Gardena small business opportunities.

## 3. Directory Automation Prompt

Write a Python module with `pathlib` and `shutil` that creates a standard client workspace under `Clients/[client]/` with subfolders for `01_PreAward`, `02_Award`, `03_PostAward`, `Templates_Resources`, and `Research_Database`. Add file renaming enforcement so uploaded files are normalized to `YYYY-MM-DD_Description_Version.ext`, and show how to route drafts into `01_PreAward/Proposal_Drafts`.

## 4. California Grants Portal Prompt

Build a Python ingestion module for California Grants Portal alerts. Prefer email-forward parsing or importable alert exports over fragile scraping. Parse title, deadline, amount, eligibility, and source metadata, log the raw alert into `portal_alerts`, create or update opportunity records, and move downloaded PDFs into the correct `Research_Database` location using the enforced naming convention.

## 5. AI Proposal Prompt

Create a reusable AI proposal drafting system using a simple provider abstraction for OpenAI or Anthropic APIs. Inputs must include RFP text, client background, past proposals or wins, and compliance rules. Generate section-specific prompts for Needs Statement, Project Narrative, Budget Justification, and Evaluation Plan. Require voice consistency, citation or evidence placeholders for unsupported claims, and explicit compliance checks against funder instructions.

## 6. Dashboard Prompt

Create a Streamlit dashboard for the Grant Writing Codex with a live tracker table, client workspace browser, AI draft launcher, and embedded codex manual. The tracker should support at least local editing-ready data display and filtering by deadline, status, and fit score.

## 7. Templates Prompt

Build a lightweight template engine that loads markdown boilerplate sections from `Templates_Resources/`, replaces placeholders with client data, and saves generated files into the appropriate client draft directory with versioned names.

## 8. Post-Award Prompt

Add modules for post-award reporting, financial tracking hooks, closeout checklists, and reminder generation. Keep the first version local and lightweight, but structure it so exported reports can later be generated to PDF or Excel.

## 9. Documentation Prompt

Generate a living Markdown manual for the full Grant Writing Codex. Include installation, directory rules, tracker workflow, AI prompt examples, source validation guidance, and California-focused extension ideas.

## 10. MVP Assembly Prompt

Assemble the full MVP repository with FastAPI, Streamlit, SQLAlchemy, Alembic-ready models, client directory automation, a California Grants Portal ingestion stub, AI proposal drafting helpers, tests, and documentation. Optimize for a solo grant writer running locally first, with a clean path to multi-client scaling.

