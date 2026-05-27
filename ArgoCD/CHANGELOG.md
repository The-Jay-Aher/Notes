# ArgoCD Changelog

## 2026-05-26

- Created folder from the `everything` scope.
- Added index and roadmap/source backbone for GitOps and ArgoCD expansion.

## 2026-05-27

- Added `01 - GitOps Foundations and Reconciliation.md`.
- Covered manual deployment pain, CI/CD drift, Git as desired state, pull-based reconciliation, desired/live state comparison, sync and health status, prune, self-heal, mutable-image risks, and a troubleshooting decision flow.
- Added official-source assumptions from current Argo CD documentation and marked version-sensitive behavior.
- Added `02 - Argo CD Architecture and Control Loops.md`.
- Covered `argocd-server`, `argocd-repo-server`, `argocd-application-controller`, `argocd-applicationset-controller`, Redis, Dex/OIDC, Kubernetes API dependency, HA/scale concerns, and component-first troubleshooting.
- Added `03 - Applications Projects and Deployment Boundaries.md`.
- Covered Application fields, AppProject source/destination/resource boundaries, project roles, default-project risks, finalizers, Argo CD RBAC vs Kubernetes RBAC, and multi-team deployment safety.
- Added `04 - Sync Drift Rollback Waves and Hooks.md`.
- Covered manual sync, automated sync, prune, allow-empty, self-heal, rollback limitations, hook phases, sync waves, migration ordering, and current auto-sync semantics from official docs.
- Added `05 - Troubleshooting OutOfSync Degraded and Failed Syncs.md`.
- Covered source/render/project/compare/apply/health/scale classification, status interpretation, diff-first diagnosis, repo-server vs controller vs Kubernetes API boundaries, and production runbook commands.
- Added `06 - Security RBAC Secrets and Tenant Boundaries.md`.
- Covered identity, global RBAC, default policy risk, AppProject security, repository and cluster credentials, Kubernetes RBAC, secret-management patterns, and tenant blast-radius controls.
- Added `07 - Multi Cluster ApplicationSet and App of Apps Patterns.md`.
- Covered ApplicationSet generators, app-of-apps, multi-cluster deployment planes, generated Application deletion risks, promotion strategy, and fleet troubleshooting.
- Added `10 - Cheatsheet.md` and `11 - Glossary.md` for revision and terminology.
