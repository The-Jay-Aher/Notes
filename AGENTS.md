# Repository Guidelines

## Purpose
This repository is an Obsidian vault (`.obsidian/`) containing Markdown notes on DevOps topics (AWS, Terraform, GitHub Actions, etc.). Treat the Markdown files as the “source of truth”; there is no runnable application code.

## Project Structure & Module Organization
- `DevOps/` — topic areas and course notes.
  - `DevOps/AWS Solution Architect/` — sequential notes named `N - Topic.md` (example: `3 - Networking.md`).
- `*.md` at repo root — evergreen references and checklists (example: `Terraform.md`).
- `.obsidian/` — Obsidian settings. Commit intentional changes only; avoid noisy workspace-only edits.

## Build, Test, and Development Commands
There is no build or test pipeline. Useful contributor commands:
- `git status` / `git diff` — review changes before committing.
- `rg "search term" .` — fast full-text search across notes.
- Open the folder in Obsidian to preview formatting and verify links.

## Writing Style & Naming Conventions
- Prefer ATX headings: `#` for the note title, then `##/###` for sections.
- Use fenced code blocks with a language tag (examples: `bash`, `hcl`, `terraform`, `powershell`).
- Filenames:
  - Ordered series: `N - Title.md`
  - General notes: `Title Case.md`
  - Automation-oriented checklists: `lower_snake_case.md`

## Testing Guidelines
There are no automated tests. Validate changes by:
- Opening notes in Obsidian and checking internal links.
- Skimming rendered Markdown for broken lists, headings, or code fences.

## Commit & Pull Request Guidelines
- Keep commits small and descriptive. Existing history uses simple messages like `Adding basic files` and timestamped backups like `vault backup: YYYY-MM-DD HH:MM:SS`.
- PRs should include a short summary, the main paths touched, and any notable link/structure changes.

## Security & Configuration Tips
- Do not store secrets (AWS keys, tokens, private URLs) in notes—use placeholders and redact sensitive identifiers.
- If `.obsidian/` changes are unintentional (layout/theme churn), revert them before committing.

