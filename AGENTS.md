# Repository Guidelines

## Project Structure & Module Organization
This repository is organized by business function at the top level: `01_Strategy_Planning/`, `02_Financials/`, `03_Legal_Compliance/`, and related folders. The current active research set lives under `seeking/`.

Inside `seeking/`, each topic has its own folder and a single primary markdown file:
- `seeking/federal-tech-ai/tech-ai-grants.md`
- `seeking/electrical-ev-towing/ev-towing-grants.md`
- `seeking/maritime-towing/maritime-grants.md`

Use `seeking/README.md` as the directory index. Keep new grant research in a dedicated subfolder with one clearly named `.md` file.

## Build, Test, and Development Commands
There is no application build or automated test pipeline in this workspace. The main development tasks are file editing, review, and link validation.

Useful commands:
- `find seeking -maxdepth 3 -type f | sort` to inventory research files.
- `sed -n '1,120p' seeking/README.md` to inspect a document quickly.
- `rg "Deadline|Funding|Focus" seeking/` to check consistency across grant summaries.

## Coding Style & Naming Conventions
Write in Markdown with short sections, scannable bullets, and factual language. Prefer title-style headings and bold labels for structured fields such as `Funding`, `Focus`, and `Deadline`.

Name folders by topic in lowercase kebab-case, for example `state-ai-adoption/`. Name the main document to match the topic, such as `state-ai-grants.md`. Keep one subject per file rather than mixing unrelated programs.

## Testing Guidelines
Quality control is manual. Before submitting changes:
- Verify links and relative paths from `seeking/README.md`.
- Check dates, funding amounts, and agency names against source material.
- Confirm heading levels render cleanly in Markdown preview.

If a file becomes large, scan it with `rg '^## ' seeking/<topic>/<file>.md` to verify section structure.

## Commit & Pull Request Guidelines
No local git history is available in this directory, so use a simple imperative commit style such as `Add Maine maritime grant updates` or `Revise AI grant deadlines`.

Pull requests should include:
- A short summary of changed grant topics.
- Source links or references for updated facts.
- Notes on expired opportunities, renamed programs, or removed items.
