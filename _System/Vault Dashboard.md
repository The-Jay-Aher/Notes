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

- **All notes:** [[notes/INDEX|Study Notes Index]] · [[README|Repository Guide]]
- **Cloud and platform:** [[notes/devops-cloud/aws-solutions-architect-associate/INDEX|AWS SAA]] · [[notes/devops-cloud/aws-solutions-architect-professional/INDEX|AWS SAP]] · [[notes/devops-cloud/kubernetes/INDEX|Kubernetes Architecture]] · [[notes/devops-cloud/cka/INDEX|CKA]] · [[notes/devops-cloud/ckad/INDEX|CKAD]] · [[notes/devops-cloud/docker/INDEX|Docker]] · [[notes/devops-cloud/ansible/INDEX|Ansible]] · [[notes/devops-cloud/argocd/INDEX|Argo CD]] · [[notes/devops-cloud/jenkins/INDEX|Jenkins]]
- **Programming:** [[notes/programming/java/INDEX|Java]] · [[notes/programming/python/INDEX|Python]] · [[notes/programming/cpp/INDEX|C++]] · [[notes/programming/competitive-programming/INDEX|Competitive Programming]]
- **Competitive exams:** [[notes/competitive-exams/upsc/Notes/00_Master_Index|UPSC]] · [[notes/competitive-exams/mpsc/INDEX|MPSC]] · [[notes/competitive-exams/rbi-assistant/INDEX|RBI Assistant]] · [[notes/competitive-exams/rbi-grade-b/INDEX|RBI Grade B]] · [[notes/competitive-exams/sebi-grade-a/INDEX|SEBI Grade A]]
- **Other study areas:** [[notes/shared-foundations/INDEX|Shared Foundations]] · [[notes/finance-trading/INDEX|Finance and Trading]]
- **Personal:** [[personal/INDEX|Personal Notes]]

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
- Repository records: [[_System/Repository/00 - Master Coverage and Source Backbone|Master Coverage]]
- Instructions: [[_System/Instructions/master-subject-prompts|Subject Prompts]] · [[_System/Instructions/upsc-note-generation-instructions|UPSC Note Generation]]
- Templates: [[_System/Templates/Study Chapter|Study Chapter]] · [[_System/Templates/Concept Note|Concept Note]] · [[_System/Templates/Exam Topic|Exam Topic]] · [[_System/Templates/Revision Sheet|Revision Sheet]]
