---
tags:
  - system/documentation
status: active
updated: 2026-08-05
---

# Obsidian Setup Guide

## What This Setup Optimizes For

This vault is configured for long-form technical and exam study notes. The design keeps Markdown portable while adding fast retrieval, consistent templates, queryable metadata, task tracking, and Git-backed history.

## Installed Community Plugins

| Plugin | Role | Important safety or usage note |
| --- | --- | --- |
| Dataview | Builds live indexes from files, properties, and tasks | JavaScript queries are disabled; ordinary Dataview queries are enabled. |
| Templater | Creates structured notes with dates and reusable layouts | Shell commands remain off in Templater's device-local security settings; automatic matching is not configured. |
| Tasks | Queries and manages checkboxes across the vault | JavaScript-based task filters remain disabled by the plugin's secure default. |
| Omnisearch | Relevance-ranked full-vault search | Use `Ctrl+Shift+O`; first indexing can take a moment. |
| QuickAdd | Provides capture and note-creation workflows | No AI provider or external command is configured. Add choices only when a repeated workflow is clear. |
| Linter | Normalizes Markdown on demand | Lint-on-save is intentionally not enabled, preventing a huge rewrite of old notes. Use `Ctrl+Alt+L` on selected files after reviewing its rules. |
| Advanced Tables | Improves Markdown table editing | Keep Git history available before large table sorts or formula operations. |
| Obsidian Git | Pull, diff, commit, and push inside Obsidian | Automatic commits remain off. Pull before work; commit and sync when a coherent change is ready. |

## First Launch After This Upgrade

1. Update Obsidian to the current stable desktop release. The installed Templater and QuickAdd releases require Obsidian 1.13 or newer.
2. Restart Obsidian or run **Reload app without saving** so all plugin manifests are loaded.
3. Open [[_System/Vault Dashboard|Vault Dashboard]] and bookmark it as the first bookmark.
4. Open Settings → Community plugins and confirm the listed plugins are enabled.
5. Let Omnisearch and Dataview finish their initial index.
6. Open Settings → Hotkeys and check that the four configured shortcuts do not collide with operating-system shortcuts.

## Everyday Workflow

1. Start from [[_System/Vault Dashboard|Vault Dashboard]].
2. Search before creating. Use Omnisearch to avoid duplicate notes.
3. Create major chapters with the **Study Chapter** template, focused explanations with **Concept Note**, exam material with **Exam Topic**, and compressed review material with **Revision Sheet**.
4. Give new notes a few stable properties: `area`, `topic`, `status`, `source`, `version`, `created`, and `updated`.
5. Use links for relationships and tags for broad workflow/state categories. A link says *this concept relates to that concept*; a tag says *this note belongs to this cross-vault class*.
6. Run Linter manually only after previewing its effect in Git source control.

## Metadata Vocabulary

Use a small controlled vocabulary so Dataview and Bases remain dependable:

- `status`: `seedling`, `developing`, `review`, `mastered`, `archived`
- `difficulty`: `foundation`, `intermediate`, `advanced`
- `priority`: `low`, `medium`, `high`, `critical`
- `area`: a stable subject family such as `kubernetes`, `aws`, `java`, or `rbi-grade-b`
- `version`: a technical version assumption such as `Kubernetes 1.35` or an exam cycle such as `2026 notification`
- `source`: the principal official document or documentation set used

## Git and Sync Safety

Obsidian Sync and Git can both move the same files between devices. Use only one as the active real-time transport. A safe pattern is Obsidian Sync for live device synchronization and Git for deliberate history:

- keep Git auto-commit, auto-push, and timed auto-pull disabled;
- pull when starting work on a device;
- commit and sync after a coherent editing session;
- never resolve a conflict by deleting both copies before comparing them;
- keep `workspace.json`, `workspace-mobile.json`, and `.trash/` out of Git because they are device-local or transient.

## Small Details That Matter Later

- Community plugins execute code inside Obsidian. Install only from the official community registry and keep them updated.
- Templater system commands and Dataview JavaScript are powerful but expand the security boundary. They are off until a specific trusted workflow requires them.
- Linter can produce thousands of harmless-looking diffs. Configure rules first, test on one file, inspect the diff, and only then apply it broadly.
- `Ctrl+Alt+N` creates a note through Templater; the core New Note command does not automatically insert a template.
- The core Daily Notes plugin and Templater share `_System/Templates`, but automatic Templater execution on every new file is disabled.
- Do not place secrets, API keys, private certificates, or cloud credentials in Markdown properties or plugin `data.json` files.
- The dashboard depends on Dataview and Tasks. Its source remains readable Markdown if either plugin is temporarily disabled.

## Troubleshooting

### A plugin appears installed but does not load

Check its `minAppVersion` in `.obsidian/plugins/<plugin-id>/manifest.json`, update Obsidian if needed, then reload the app. If Restricted Mode is enabled, approve community plugins in Settings.

### Search results are incomplete

Wait for first indexing, then use the Omnisearch command to rebuild its index. Check whether the folder or file type is excluded in plugin settings.

### A template displays `<% ... %>` literally

The note was created with the core Templates command rather than Templater, or Templater was not enabled. Use **Templater: Create new note from template**.

### A Dataview block is blank

Confirm Dataview is enabled, inspect the query's path and property names, and remember that YAML/property spelling must match. An empty result may simply mean old notes do not yet have the queried property.

### Git reports a conflict

Open the conflicted file and compare both conflict sections before editing. Keep the meaningful content from each side, remove the conflict markers, then stage and commit the resolved file.

## Connected Improvements

The next useful upgrade is gradual metadata adoption. Add properties when a note is already being revised; do not mass-edit the entire vault merely to make a dashboard look full. Later, native Bases can provide visual filtered views over the same properties without changing the underlying Markdown.
