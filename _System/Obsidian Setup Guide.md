---
tags:
  - system/documentation
status: active
updated: 2026-11-18
---

# Obsidian Setup Guide

## What This Setup Optimizes For

This vault is built for long-form technical and exam study notes that you actively learn from, not just store. The design keeps Markdown portable and adds fast retrieval, consistent templates, queryable metadata, task tracking, a learning record, and Git-backed history that syncs between your PC and your phone.

## How Your Devices Stay in Sync

```text
Windows PC (Obsidian desktop + system git)  ──push/pull──►  GitHub  ◄──push/pull──  Phone (Obsidian mobile + Obsidian Git)
```

- **Git is the only sync transport.** Both devices push to and pull from the same GitHub repository. The PC copy also sits inside OneDrive, which acts as a backup, not as the link to the phone.
- **`.obsidian/` is in Git.** Settings, themes, plugins and plugin updates travel between devices. The device-local files `workspace.json`, `workspace-mobile.json` and `.trash/` are ignored.
- **Pull happens on startup** (Obsidian Git `autoPullOnBoot`). Auto-commit, auto-push and timed auto-pull stay off, so history only records deliberate changes.
- **Line endings are LF on every device.** `.gitattributes` enforces this, so a note edited on the phone never shows up as "changed" on Windows just because of invisible CRLF characters.
- **Credentials stay on each device.** Obsidian Git's author name and email and the GitHub token are set separately on each device. The shared `data.json` only names the secret; it never contains the token.

### Rules that keep the phone working

The phone's Git runs inside the Obsidian app's memory, not as a real git program, so:

1. **Keep large files out of Git.** A single commit of book PDFs (about 56 MB) once made the phone crash on every pull. `*.pdf` is now ignored, so PDFs stay on the PC only. Compress screenshots before putting them in `Attachments/`.
2. **Pull before you edit on the other device**, and commit and push when you finish a session. Two devices editing the same note without syncing is the main source of conflicts.
3. **Update plugins on one device, then sync.** Plugin updates rewrite `.obsidian/plugins/` for both devices. After an update, check that the phone's Obsidian version meets every plugin's `minAppVersion`; it is currently **1.14.4**, required by Linter 1.35.
4. **Never run two sync transports on the same files.** The core Sync plugin is switched on but does nothing without a subscription. If you ever subscribe to Obsidian Sync or move the phone to Syncthing over Tailscale, turn Git off on the phone at the same time, and keep Git on the PC for history.

## Installed Community Plugins

| Plugin | Role | Important safety or usage note |
| --- | --- | --- |
| Dataview | Builds live indexes from files, properties, and tasks | JavaScript queries are disabled; ordinary Dataview queries are enabled. |
| Templater | Creates structured notes with dates and reusable layouts | Shell commands remain off in Templater's device-local security settings; automatic matching is not configured. |
| Tasks | Queries and manages checkboxes across the vault | JavaScript-based task filters remain disabled by the plugin's secure default. |
| Omnisearch | Relevance-ranked full-vault search | Use `Ctrl+Shift+O`; first indexing can take a moment, longer on the phone. |
| QuickAdd | Provides capture and note-creation workflows | No AI provider or external command is configured. Add choices only when a repeated workflow is clear. |
| Linter | Normalizes Markdown formatting on demand | Seven whitespace-only rules are on (see below). Lint-on-save and lint-on-change stay off. |
| Advanced Tables | Improves Markdown table editing | Keep Git history available before large table sorts or formula operations. |
| Obsidian Git | Pull, diff, commit, and push inside Obsidian on both devices | Pulls on startup; never commits or pushes by itself. |
| Minimal Theme Settings | Controls the Minimal theme: color schemes, line widths, fonts | Settings are shared, so changing them on one device changes both. |
| Style Settings | Exposes adjustable CSS variables from the theme and snippets | Only cosmetic; safe to change. |
| Typewriter Scroll | Keeps the line you are typing near the middle of the screen | Purely an editor comfort setting. |

**Appearance:** Minimal theme with the `typography-polish` and `study-vault` CSS snippets. The fonts are Inter (text) and Consolas (code); a device that doesn't have them falls back to its system fonts. AnuPpuccin, Obsidian gruvbox and Things are installed but unused.

## Hotkeys

| Shortcut | Action |
| --- | --- |
| `Ctrl+Shift+O` | Omnisearch: search the whole vault |
| `Ctrl+Alt+N` | Templater: create a new note from a template |
| `Ctrl+Shift+T` | Tasks: create or edit a task |
| `Ctrl+Alt+L` | Linter: lint the current file |
| `Ctrl+Shift+P` | Open the command palette |

## Linter Rules

Only rules that change whitespace are enabled, so linting can never change your wording, headings or properties:

- trailing spaces removed, except a deliberate two-space line break
- consecutive blank lines collapsed to one
- exactly one line break at the end of the file
- one space after list markers
- a blank line around code fences
- a blank line around tables, which tables need in order to render
- a blank line around headings

To use it, open one note, press `Ctrl+Alt+L`, check the diff in Obsidian Git's Source Control view, then commit. Lint old notes one at a time as you revise them, not in bulk.

## First Launch on a New Device

1. Install the current stable Obsidian (1.14.4 or newer for the current plugin set).
2. Get the vault:
   - **PC:** `git clone` the repository and open the folder as a vault.
   - **Phone:** create an empty vault, install Obsidian Git, and run **Clone an existing remote repo**.
3. Open Settings → Community plugins, turn off Restricted Mode, and confirm the listed plugins are enabled. They arrive with the repository.
4. In Obsidian Git's settings, set this device's author name and email and the GitHub token.
5. Run **Reload app without saving** so all plugin manifests are loaded.
6. Open [[_System/Vault Dashboard|Vault Dashboard]] and bookmark it as the first bookmark.
7. Let Omnisearch and Dataview finish their first index.

## Everyday Workflow

1. Open Obsidian. Obsidian Git pulls automatically.
2. Start from [[_System/Vault Dashboard|Vault Dashboard]] or the [[notes/revision/Learning Tracker|Learning Tracker]].
3. Search before creating. Use Omnisearch to avoid duplicate notes.
4. Create major chapters with the **Study Chapter** template, focused explanations with **Concept Note**, exam material with **Exam Topic**, and compressed review material with **Revision Sheet**.
5. Give new notes a few stable properties: `area`, `topic`, `status`, `source`, `version`, `created`, and `updated`.
6. Use links for relationships and tags for broad workflow or state categories. A link says *this concept relates to that concept*; a tag says *this note belongs to this cross-vault class*.
7. Study actively. In Claude Code, `/teach <topic>` runs a lesson, `/quiz <topic>` tests you, and `/revise` runs the spaced review of whatever is due in the Learning Tracker.
8. Before you stop, commit and push from Obsidian Git so the other device gets your changes.

## Metadata Vocabulary

Use a small controlled vocabulary so Dataview and Bases remain dependable:

- `status`: `seedling`, `developing`, `review`, `mastered`, `archived`
- `difficulty`: `foundation`, `intermediate`, `advanced`
- `priority`: `low`, `medium`, `high`, `critical`
- `area`: a stable subject family such as `kubernetes`, `aws`, `java`, or `rbi-grade-b`
- `version`: a technical version assumption such as `Kubernetes 1.35`, or an exam cycle such as `2026 notification`
- `source`: the principal official document or documentation set used

Set a topic's `status: mastered` only when its items have reached box 5 in the Learning Tracker. That way the dashboard reflects what you can actually recall, not what you have read.

## Small Details That Matter Later

- Community plugins execute code inside Obsidian. Install only from the official community registry and keep them updated.
- Templater system commands and Dataview JavaScript are powerful but expand the security boundary. They are off until a specific trusted workflow requires them.
- Linter can still produce many harmless-looking diffs on old notes, because headings and tables often lack blank lines. Lint one file at a time and inspect the diff.
- `Ctrl+Alt+N` creates a note through Templater; the core New Note command does not automatically insert a template.
- The core Daily Notes plugin and Templater share `_System/Templates`, but automatic Templater execution on every new file is disabled.
- Do not place secrets, API keys, private certificates, or cloud credentials in Markdown properties or plugin `data.json` files. `data.json` files are committed and reach every device.
- The dashboard depends on Dataview and Tasks. Its source remains readable Markdown if either plugin is temporarily disabled.
- Plugin code (`main.js`, `styles.css`) and themes are stored in Git byte-for-byte as released (`-text` in `.gitattributes`). Never hand-edit them; update through Obsidian.
- `.claude/` is a dot-folder, so Obsidian hides it. It holds the agent skills (teach, quiz, revise, deep-notes, subject-*), not notes.

## Troubleshooting

### A plugin appears installed but does not load

Check its `minAppVersion` in `.obsidian/plugins/<plugin-id>/manifest.json` against the Obsidian version on *that* device. Phones often lag behind the PC. Update Obsidian if needed, then reload the app. If Restricted Mode is enabled, approve community plugins in Settings.

### The phone crashes or hangs as soon as a pull starts

A large file has entered the Git history. Removing it from the latest files is not enough, because the phone still has to download it from history. Find the large files, rewrite the commit that added them, and force-push; see the 2026-11-18 entry in `_System/CHANGELOG.md`. If the phone still crashes afterwards, delete its local `.git` folder and clone again.

### A note shows as changed but looks identical

The cause is almost always line endings. `.gitattributes` should prevent it; if a file still slips through, run `git add --renormalize .` on the PC and commit.

### Search results are incomplete

Wait for first indexing, then use the Omnisearch command to rebuild its index. Check whether the folder or file type is excluded in plugin settings.

### A template displays `<% ... %>` literally

The note was created with the core Templates command rather than Templater, or Templater was not enabled. Use **Templater: Create new note from template**.

### A Dataview block is blank

Confirm Dataview is enabled, inspect the query's path and property names, and remember that YAML and property spelling must match. An empty result may simply mean old notes do not yet have the queried property.

### Git reports a conflict

Open the conflicted file and compare both conflict sections before editing. Keep the meaningful content from each side, remove the conflict markers, then stage and commit the resolved file. Never resolve a conflict by deleting both copies before comparing them.

## Connected Improvements

- **Gradual metadata adoption.** Add properties when a note is already being revised; don't mass-edit the entire vault just to make a dashboard look full. Later, native Bases can provide visual filtered views over the same properties without changing the underlying Markdown.
- **Phone sync without Git.** If the phone's Git ever becomes a burden, Syncthing over Tailscale (Android) or Remotely Save with WebDAV (iPhone) can replace it. The PC keeps Git for history, and the rule about never running two transports at once still applies.
