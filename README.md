# Legendary Deep Notes Vault

This repository is a structured learning vault for cloud and platform engineering, programming, competitive examinations, shared technical foundations, finance and trading, and personal planning. Start from the subject indexes below instead of searching through the vault root.

## Start Here

| Area | Index | What belongs there |
| --- | --- | --- |
| All study notes | [Notes index](notes/INDEX.md) | Entry point for every learning track. |
| Cloud and platform engineering | [DevOps and cloud](notes/devops-cloud/INDEX.md) | AWS, Kubernetes, Docker, Terraform, Ansible, Jenkins, Argo CD, GitHub Actions, and DevSecOps. |
| Programming and computer science | [Programming](notes/programming/INDEX.md) | Java, Python, C++, competitive programming, and low-level design. |
| Competitive examinations | [Competitive exams](notes/competitive-exams/INDEX.md) | UPSC, MPSC, RBI Assistant, RBI Grade B, and SEBI Grade A. |
| Shared foundations | [Shared foundations](notes/shared-foundations/INDEX.md) | Networking, Linux/Bash, and authoring references used by several tracks. |
| Finance and trading | [Finance and trading](notes/finance-trading/INDEX.md) | Foundations, strategies, research governance, workbooks, and study plans. |
| Personal material | [Personal index](personal/INDEX.md) | Career notes, planning, astrology, and miscellaneous personal references. |
| Vault operations | [_System](_System/Vault%20Dashboard.md) | Dashboard, templates, instructions, scripts, and repository records. |

## Repository Layout

```text
Notes/
├── notes/
│   ├── devops-cloud/
│   ├── programming/
│   ├── competitive-exams/
│   ├── shared-foundations/
│   └── finance-trading/
├── personal/
├── _System/
│   ├── Templates/
│   ├── Daily Notes/
│   ├── Instructions/
│   ├── Repository/
│   └── Scripts/
├── Attachments/
├── README.md
├── AGENTS.md
└── LICENSE
```

The root is intentionally quiet. Subject content belongs under `notes/`; private or non-study material belongs under `personal/`; vault machinery belongs under `_System/`; shared media remains in `Attachments/` because Obsidian is configured to use that location.

## Suggested Technical Learning Path

```text
Networking and Bash
        ↓
GitHub Actions, Docker, and Terraform
        ↓
AWS, Jenkins, Ansible, and DevSecOps
        ↓
Kubernetes architecture
        ↓
CKA, CKAD, and Argo CD
```

This is a dependency path, not a mandatory schedule. Each topic index contains its own roadmap and revision material.

## Filing Rules

- Put a note in the folder for its primary learning objective; use links for secondary relationships.
- Keep one canonical explanation and cross-link it instead of duplicating weaker versions.
- Each substantial topic should have an `INDEX.md`, a roadmap or source-backbone file, deep chapters, practice material, a revision sheet or cheatsheet, a glossary, and a `CHANGELOG.md` where appropriate.
- Use numbered filenames for an intentional learning sequence. Use descriptive Title Case for standalone references.
- Keep changing facts and version-sensitive behavior visibly marked for verification.
- Keep secrets, credentials, private endpoints, and account identifiers out of the vault.
- When moving or renaming notes, update both Markdown links and Obsidian wikilinks, then run the link validator in `_System/Scripts/`.

## Obsidian

Open [_System/Vault Dashboard.md](_System/Vault%20Dashboard.md) as the home note. Templates and daily notes remain under `_System`, and attachments remain at the vault root so the existing Obsidian settings continue to work.
