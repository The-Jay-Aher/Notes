# DevOps Notes Index

## Quick Summary

This Obsidian vault is a practical knowledge base for DevOps, cloud, infrastructure, CI/CD, security, networking, and certification revision. The notes are organized as topic folders, with numbered course notes where the subject has a natural learning order.

Use this index as the first stop when revising. It shows what each folder contains, the suggested learning path, and the areas that still need deeper notes.

## How To Use This Vault

- Start with the suggested learning order below if you are building fundamentals.
- Use folder notes for revision before interviews or certification practice.
- Keep new notes short enough to scan, but detailed enough to explain the "why", "how", commands, mistakes, and real-world use.
- Prefer internal links when one note depends on another note.
- Mark uncertain facts with `Needs verification` instead of guessing.

## Suggested Learning Order

| Order | Area | Why It Comes Here |
| --- | --- | --- |
| 1 | [Networking Fundamentals](Networking%20Fundamentals/INDEX.md) | Networking is required for cloud, Kubernetes, security, and troubleshooting. |
| 2 | [Bash](Bash.md) | Shell fluency is needed for Linux operations, automation, and CI/CD work. |
| 3 | [Docker](Docker/INDEX.md) | Containers are required for Kubernetes, CI/CD packaging, and modern deployment workflows. |
| 4 | [GitHub Actions](Learning%20GitHub%20Actions.md) | Learn basic automation before larger CI/CD platforms. |
| 5 | [Jenkins](Jenkins/INDEX.md) | Useful for enterprise CI/CD and pipeline design. |
| 6 | [Ansible](Ansible/INDEX.md) | Configuration management and repeatable operations complement CI/CD and IaC. |
| 7 | [Terraform](Terraform/INDEX.md) | Infrastructure as Code ties cloud, review workflow, and repeatable environments together. |
| 8 | [AWS Cloud Practitioner](AWS%20Cloud%20Practitioner/INDEX.md) | Builds AWS vocabulary and service awareness. |
| 9 | [AWS Solutions Architect](AWS%20Solution%20Architect/INDEX.md) | Goes deeper into design choices, reliability, networking, storage, databases, messaging, security, and disaster recovery. |
| 10 | [Introduction to DevSecOps for Cloud](Introduction%20to%20DevSecOps%20for%20Cloud/INDEX.md) | Adds secure SDLC, supply chain security, monitoring, and response thinking. |
| 11 | [Certified Kubernetes Administrator](Certified%20Kubernetes%20Administrator/INDEX.md) | Focuses on cluster operations, networking, scheduling, storage, and troubleshooting. |
| 12 | [Certified Kubernetes Application Developer](Certified%20Kubernetes%20Application%20Developer/INDEX.md) | Focuses on application design, deployment, config, services, observability, and debugging. |

## Topic Map

### Networking Fundamentals

| Note | What It Covers |
| --- | --- |
| [1 - Fundamentals of Networking](Networking%20Fundamentals/1%20-%20Fundamentals%20of%20Networking.md) | Network purpose, LAN/WAN, OSI and TCP/IP models, switching, routing, DNS, DHCP, NAT, firewalls, troubleshooting flow. |
| [2 - Internet Protocol (IP)](Networking%20Fundamentals/2%20-%20Internet%20Protocol%20%28IP%29.md) | IPv4, IPv6, subnetting, CIDR, private/public IPs, routing, NAT, ARP, ICMP, common IP mistakes. |

### Cloud And AWS

| Folder | Notes |
| --- | --- |
| [AWS Cloud Practitioner](AWS%20Cloud%20Practitioner/INDEX.md) | Cloud foundations, compute, storage, networking, databases, deployment, migration, AI, monitoring, security, pricing, and terminology. |
| [AWS Solution Architect](AWS%20Solution%20Architect/INDEX.md) | SAA design coverage across IAM, EC2, ELB/ASG, RDS/Aurora, S3, Route 53, CloudFront, storage migration, messaging, containers, serverless, analytics, ML, monitoring, security, VPC, and DR. |
| [AWS SAA Trading Bot Plan](aws_saa_trading_bot_plan_checklist.md) | Six-week AWS SAA and trading bot study checklist. |
| [AWS SAA Trading Bot Plan V2](aws_saa_trading_bot_plan_checklist_v2.md) | Expanded six-week plan that includes Terraform cadence. |

### Containers And Configuration Management

| Note | What It Covers |
| --- | --- |
| [Docker](Docker/INDEX.md) | Containers, images, Docker CLI, Dockerfiles, builds, volumes, networking, Compose, security, and best practices. |
| [Ansible](Ansible/INDEX.md) | Ansible fundamentals, inventory, configuration, playbooks, tasks, modules, variables, facts, templates, handlers, roles, collections, Vault, troubleshooting, and best practices. |

### Infrastructure As Code

| Note | What It Covers |
| --- | --- |
| [Terraform Course Notes](Terraform/INDEX.md) | IaC concepts, Terraform workflow, variables, state, modules, functions, CLI, HCP Terraform, and Terraform Enterprise. |
| [Terraform Deep Notes](Terraform/Terraform.md) | Longer Terraform reference from basic to advanced usage, including workflow, settings, variables, expressions, state, modules, and operational patterns. |

### CI/CD And Automation

| Note | What It Covers |
| --- | --- |
| [Learning GitHub Actions](Learning%20GitHub%20Actions.md) | Workflow syntax, events, jobs, steps, runners, actions, secrets, permissions, artifacts, caching, matrices, environments, and troubleshooting. |
| [Jenkins Notes](Jenkins/INDEX.md) | CI/CD practices, Jenkins installation, plugins, Docker usage, Declarative Pipeline, and Groovy automation. |
| [Bash](Bash.md) | Shell basics, file operations, grep, redirection, pipes, help system, scripting basics. |

### Cloud Security And DevSecOps

| Folder | What It Covers |
| --- | --- |
| [Introduction to DevSecOps for Cloud](Introduction%20to%20DevSecOps%20for%20Cloud/INDEX.md) | Secure SDLC, threat modeling, SAST, SCA, CVE/CVSS, SLSA, release controls, deployment security, logging, SIEM, and incident response. |

### Kubernetes

| Folder | What It Covers |
| --- | --- |
| [Certified Kubernetes Administrator](Certified%20Kubernetes%20Administrator/INDEX.md) | Beginner Kubernetes foundation plus CKA-oriented cluster administration: architecture, installation, upgrades, workloads, scheduling, services, networking, storage, and troubleshooting. |
| [Certified Kubernetes Application Developer](Certified%20Kubernetes%20Application%20Developer/INDEX.md) | Beginner application foundation plus CKAD-oriented app work: Pods, Deployments, Jobs, ConfigMaps, Secrets, probes, resources, Services, NetworkPolicies, Helm/Kustomize, and debugging. |

### Reference And Personal Planning

| Note | What It Covers |
| --- | --- |
| [Markdown Cheatsheet](Markdown%20Cheatsheet.md) | Markdown syntax reference. |
| [Mentor Meet](Mentor%20Meet.md) | DevOps career planning, progress, learning sequence, doubts, and short-term tasks. |
| [Todo's](Todo%27s.md) | Personal task list. |
| [Fundamental Analysis](Fundamental%20Analysis.md) | Long-form framework for stock or index fundamental analysis. |
| [Financial Jargon Glossary](Financial%20Jargon%20Glossary.md) | Beginner-friendly glossary for stock market, futures, options, commodities, macro, valuation, and trading terms. |
| [Positional Trader](Positional%20Trader.md) | Detailed framework for positional stock, futures, and options trading with risk management. |
| [Probabilistic Trading Guide](Probabilistic%20Trading%20Guide.md) | Probability-first trading guide covering expectancy, R-multiples, setup scoring, manual decision trees, and review systems. |
| [Trading Notes Audit Report](trading_notes_audit_report.md) | Blunt audit of the finance notes, strategy-readiness gaps, risk issues, and improvement plan. |
| [Misunderstanding Register](misunderstanding_register.md) | Register of weak, vague, incomplete, or dangerous trading ideas to fix before live risk. |
| [Professional Trading Workbook Template](pro_trading_workbook_template.md) | Ready-to-use templates for strategy research, trade plans, journals, reviews, and live-readiness checks. |
| [Trading Action Plan](action_plan.md) | Practical 7-day, 30-day, 60-day, and 90-day plan for turning notes into testable process. |
| [UPSC Monthly GK](UPSC/Monthly%20GK/May%20-%202026.md) | May 2026 current-affairs capture template with explicit source-verification markers. |
| [UPSC Polity](UPSC/Polity/Democratic%20Politics%20-%20I.md) | Democracy fundamentals for polity revision. |

## Current Gaps

These areas now have structure, but still deserve a deeper second pass if the vault is being made fully complete:

- AWS Cloud Practitioner notes are useful, but some service details should be checked against current AWS exam guide language before exam revision.
- AWS Solutions Architect notes now cover the main SAA service areas, but hands-on labs should be added for VPC, S3, RDS/Aurora, Route 53, SQS/SNS, Lambda/API Gateway, IAM policy debugging, and DR failover.
- Terraform notes are strong, but provider-specific examples such as AWS VPC, S3 backend, IAM, and module versioning should be expanded with hands-on labs.
- DevSecOps notes are clear but short; add concrete CI/CD security examples for GitHub Actions, Jenkins, containers, IaC scanning, and secrets handling.
- Kubernetes notes now include beginner foundations, but hands-on labs with real `kubectl` outputs and failure scenarios should be added after practice.
- UPSC Monthly GK still needs source-filled current-affairs entries; it is intentionally marked with `Needs verification` until primary/current sources are added.

## Maintenance Rules

- Keep filenames consistent: numbered course notes use `N - Title.md`; general references use `Title Case.md`.
- Avoid storing secrets, tokens, account IDs, private endpoints, or real credentials.
- Prefer official documentation links in reference sections for fast verification.
- When renaming files, update this index and any Obsidian links that reference the old path.
