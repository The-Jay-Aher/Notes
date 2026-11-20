# Obsidian Setup Changelog

## 2026-11-18: Personal learning plan

### Added

- `notes/revision/Learning Plan.md`: a phased plan from November 2026 to April 2027, built from the owner's resume, mentor notes, to-do list and the vault's coverage. Phase 0 placement quiz, Phase 1 networking and AWS SAA, Phase 2 Kubernetes and CKA, Phase 3 a capstone platform project, plus a running interview-readiness track. It states its assumptions and lists the exam facts to verify. Because the repository is public, it carries no contact details, employer or client names, or resume metrics.

### Changed

- Filled the Learner Profile in `notes/revision/Learning Tracker.md` with the proposed focus, goals, session length, strengths and weak areas, each marked as proposed or untested.
- Linked the plan from the Revision row of `notes/INDEX.md`.
- The plan supersedes the schedule and daily Terraform cadence of `notes/finance-trading/study-plans/aws_saa_trading_bot_plan_checklist_v2.md`; that checklist is kept as a task list and for its trading safety gate.

## 2026-11-18: Obsidian setup improvements

### Improved

- Added `.gitattributes`: text is stored and checked out as LF on every device, so the phone (LF) and Windows git (`core.autocrlf=true`, CRLF) no longer show phantom changes on the same note. Plugin and theme code is marked `-text` and stays byte-for-byte as released. Three files stored with CRLF were renormalized with no content change, and on-disk copies on the PC were rewritten as LF.
- Linter: enabled seven whitespace-only rules (trailing spaces with two-space line breaks kept, consecutive blank lines, final newline, space after list markers, blank lines around code fences, tables and headings), so `Ctrl+Alt+L` does something useful. Lint-on-save and lint-on-change remain off.
- Rewrote `_System/Obsidian Setup Guide.md` to match the real setup. It now covers Git sync between the PC and the phone, rules that keep the phone's in-app Git working, all 11 plugins (Minimal Theme Settings, Style Settings and Typewriter Scroll were missing), all five hotkeys (it said four), the Linter rules, first launch on a new device, the learning workflow (Learning Tracker and `/teach`, `/quiz`, `/revise`), and new troubleshooting entries for phone pull crashes and phantom line-ending changes.

### Replaced

- The guide's old advice to use Obsidian Sync for live sync and Git for history no longer described this vault, which uses Git on both devices. It is now an explicit "never run two transports at once" rule, with notes on what to switch off if Obsidian Sync or Syncthing is ever adopted.

## 2026-11-18: Learning-first AGENTS.md and agent skills

### Changed

- Rewrote `AGENTS.md` from about 1,100 lines down to a short core. It now makes learning the primary goal and routes each request to a mode (teach, quiz, revise, write notes) and to a subject skill. It keeps the teacher voice, the causal-chain rule and the non-negotiables (upgrade rather than duplicate, accuracy, "Small Details That Matter Later", changelog, privacy).

### Moved, with nothing deleted

- Moved the detailed note-writing procedure (workflow, upgrade rules, chapter structure, small-details rule, source rules, required files, command and diagram rules, exam-notes requirements, quality bar) into `.claude/skills/deep-notes/SKILL.md`.
- Moved each subject's coverage checklist, word for word, into subject skills: `subject-kubernetes`, `subject-aws`, `subject-devops-tools`, `subject-programming` and `subject-indian-exams`. Each one also gained a short "teaching and quizzing" section for its subject.

### Added

- Learning skills: `teach` (diagnose, teach in chunks, check, explain-back, apply, log), `quiz` (retrieval practice and mock tests with honest grading) and `revise` (Leitner-box spaced review).
- `notes/revision/Learning Tracker.md`: learner profile, review queue and session log, shared by the learning skills.
- `deep-notes` now asks for chapter answers to go in collapsed `> [!question]-` callouts, so the questions work for self-testing.

### Git hygiene

- `*.pdf` is now gitignored. A commit of about 56 MB of book PDFs crashed Obsidian Git on mobile, so it was rewritten without the PDFs. The PDFs remain on disk in `notes/finance-trading/book-notes/`.

## 2026-08-08 — Subject-based repository reorganization

### Rearranged

- Moved study material from the crowded vault root into five clear branches: `notes/devops-cloud/`, `notes/programming/`, `notes/competitive-exams/`, `notes/shared-foundations/`, and `notes/finance-trading/`.
- Moved career, planning, astrology, and miscellaneous private references into `personal/` so they no longer appear as study subjects.
- Moved repository prompts and coverage records into `_System/Instructions/` and `_System/Repository/` while preserving Obsidian templates, daily notes, and root-level attachments.
- Separated the misplaced bag-lock reference from the AWS Solutions Architect notes and placed the standalone CKA result note inside the CKA track.

### Added

- Added vault-wide and category-level `INDEX.md` files for predictable navigation.
- Added an idempotent migration utility and a local-link validator under `_System/Scripts/`.
- Replaced the DevOps-only root README with a complete repository map and filing rules.

### Link maintenance

- Recalculated relative Markdown links after moves and updated path-qualified Obsidian wikilinks.
- Preserved useful note content and existing user edits; the reorganization changes location and navigation, not the substantive teaching material.

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
