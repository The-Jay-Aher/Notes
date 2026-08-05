# Obsidian Setup Changelog

## 2026-08-05 — Study-vault upgrade

### Added

- Dataview, Templater, Tasks, Omnisearch, QuickAdd, Linter, and Advanced Tables from their official GitHub releases.
- A query-driven vault dashboard, five reusable templates, daily-note configuration, keyboard shortcuts, metadata types, graph color groups, and study-vault CSS.
- A setup and troubleshooting guide documenting the security model and daily workflow.

### Improved

- Preserved the existing Minimal theme, typography snippet, core-plugin selection, and manual Git workflow.
- Expanded the command-palette pins around high-frequency search, creation, task, lint, and Git commands.
- Kept existing notes untouched; metadata can be adopted during normal revision instead of through a noisy bulk rewrite.

### Safety decisions

- Disabled Templater shell commands and automatic execution on file creation.
- Disabled Dataview JavaScript and inline JavaScript queries.
- Left Linter and Git automatic writes off so existing notes are not rewritten or committed unexpectedly.
