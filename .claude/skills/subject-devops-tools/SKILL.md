---
name: subject-devops-tools
description: Coverage and teaching requirements for Docker, Ansible, Jenkins, Chef and Argo CD in this vault, plus the general shape to follow for Terraform, GitHub Actions and DevSecOps. Load it whenever creating, upgrading, teaching or quizzing anything about containers and images, configuration management, CI/CD pipelines, GitOps or infrastructure as code, together with deep-notes (writing) or teach/quiz/revise (learning).
---

# DevOps Tools: Docker, Ansible, Jenkins, Chef, Argo CD

Folders: `notes/devops-cloud/docker/`, `ansible/`, `jenkins/`, `argocd/`, and `chef/` if created. The vault also has `terraform/`, `github-actions/` and `devsecops/`; those have no dedicated checklist yet, so use the general shape at the end of this file.

Version assumption: always state the tool version a note assumes, and say when behavior depends on a plugin, provider, collection or distribution. Never invent commands, flags or module parameters. If unsure, write "verify against current docs".

## Docker

- containers from first principles
- images
- layers
- Dockerfile
- build context
- caching
- registries
- volumes
- bind mounts
- networks
- bridge networking
- host networking
- container lifecycle
- environment variables
- multi-stage builds
- Docker Compose
- image security
- slim images
- scanning
- logs
- debugging
- Docker vs Kubernetes
- production limitations

## Ansible

- configuration management
- agentless architecture
- inventory
- modules
- playbooks
- tasks
- handlers
- variables
- facts
- templates
- roles
- collections
- vault
- idempotency
- conditionals
- loops
- error handling
- privilege escalation
- dynamic inventory
- testing
- real infrastructure automation patterns

Always explain idempotency deeply. It is one of those words people repeat in interviews while secretly hoping nobody asks a follow-up.

## Jenkins

- CI/CD fundamentals
- Jenkins architecture
- controller and agents
- jobs
- pipelines
- scripted pipeline
- declarative pipeline
- Jenkinsfile
- stages
- steps
- credentials
- plugins
- webhooks
- distributed builds
- artifact management
- Docker integration
- Kubernetes agents
- security
- backup
- scaling
- debugging failed builds
- real pipeline design

## Chef

- configuration management
- Chef architecture
- workstation
- Chef server
- nodes
- cookbooks
- recipes
- resources
- attributes
- run lists
- roles
- environments
- data bags
- idempotency
- testing
- compliance
- Chef vs Ansible
- real-world use cases

## Argo CD

- GitOps from first principles
- desired state vs live state
- Argo CD architecture
- applications
- projects
- repositories
- sync
- auto-sync
- manual sync
- health
- drift detection
- pruning
- self-healing
- rollback
- Helm integration
- Kustomize integration
- RBAC
- secrets
- multi-cluster deployment
- app-of-apps pattern
- sync waves
- hooks
- troubleshooting

## General shape for Terraform, GitHub Actions, DevSecOps and any new tool

Cover: the problem the tool solves and what came before it; architecture; core objects and their lifecycle; configuration and code examples; state, secrets and credentials handling; debugging; security; scaling; failure modes; production scenarios; interview questions; hands-on labs; a cheatsheet.

## Teaching and quizzing DevOps tools

- **Predict, then run.** Before a command, playbook, pipeline or sync runs, the student says what it will do and what output they expect. Then compare with what actually happened.
- **Make idempotency testable.** Running an Ansible playbook a second time should report `changed=0` in the PLAY RECAP. When it doesn't, the student finds the task that is not idempotent and explains why. The same habit applies to Chef runs and Terraform plans: a second run with no real change should do nothing.
- **Docker cache drills.** Show a Dockerfile, change one line, and ask which layers rebuild and why. Then ask how reordering the Dockerfile would avoid the rebuild.
- **Failure-first labs.** Hand the student a broken pipeline log, an OutOfSync Argo CD application or a container that exits immediately. They diagnose it from the evidence before you explain anything.
- **Compare tools by their models,** not by feature lists: push vs pull (Ansible vs Chef), imperative vs declarative pipelines, CI-driven deploys vs GitOps reconciliation.
