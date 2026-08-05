---
cssclasses:
  - dashboard
aliases:
  - Home
tags:
  - system/dashboard
---

# Vault Dashboard

> [!tip] Start here
> Use **Ctrl+Shift+O** for full-vault search, **Ctrl+Alt+N** to create from a template, and **Ctrl+Shift+T** to edit a task. Open the command palette for every other workflow.

## Study Areas

- **Cloud and platform:** [[AWS Solution Architect/INDEX|AWS SAA]] · [[AWS Solutions Architect Professional/INDEX|AWS SAP]] · [[Kubernetes Architecture/INDEX|Kubernetes Architecture]] · [[Certified Kubernetes Administrator/INDEX|CKA]] · [[Certified Kubernetes Application Developer/INDEX|CKAD]] · [[Docker/INDEX|Docker]] · [[Ansible/INDEX|Ansible]] · [[ArgoCD/INDEX|Argo CD]] · [[Jenkins/INDEX|Jenkins]]
- **Programming:** [[Java/INDEX|Java]] · [[Python/INDEX|Python]] · [[C++/INDEX|C++]] · [[Competitive Programming/INDEX|Competitive Programming]]
- **Competitive exams:** [[UPSC/Notes/00_Master_Index|UPSC]] · [[MPSC/INDEX|MPSC]] · [[RBI Assistant/INDEX|RBI Assistant]] · [[RBI Grade B/INDEX|RBI Grade B]] · [[SEBI Grade A/INDEX|SEBI Grade A]]

## Open Tasks

```tasks
not done
path does not include .trash
path does not include _System/Templates
sort by priority
sort by due
limit 25
```

## Recently Updated Notes

```dataview
TABLE WITHOUT ID file.link AS "Note", file.folder AS "Area", file.mtime AS "Updated"
FROM ""
WHERE file.path != this.file.path
  AND !startswith(file.path, ".")
  AND !startswith(file.path, "_System/Templates")
SORT file.mtime DESC
LIMIT 15
```

## Notes That Need Development

```dataview
TABLE WITHOUT ID file.link AS "Note", area AS "Area", topic AS "Topic", updated AS "Updated"
FROM ""
WHERE status = "seedling" OR status = "developing"
SORT updated ASC
LIMIT 20
```

## System

- [[_System/Obsidian Setup Guide|Obsidian Setup Guide]]
- [[_System/CHANGELOG|Setup Changelog]]
- Templates: [[_System/Templates/Study Chapter|Study Chapter]] · [[_System/Templates/Concept Note|Concept Note]] · [[_System/Templates/Exam Topic|Exam Topic]] · [[_System/Templates/Revision Sheet|Revision Sheet]]
