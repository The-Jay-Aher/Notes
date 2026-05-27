# ArgoCD

## Purpose

This folder teaches ArgoCD through GitOps first principles: manual deployment pain, CI/CD drift, Git as source of truth, reconciliation, sync, drift detection, pruning, self-healing, rollback, and multi-cluster delivery.

## Learning Order

| Order | Note | Focus |
| --- | --- | --- |
| 0 | [Roadmap and Source Backbone](00%20-%20Roadmap%20and%20Source%20Backbone.md) | GitOps causal chain, ArgoCD architecture, source assumptions, and chapter plan. |
| 1 | [GitOps Foundations and Reconciliation](01%20-%20GitOps%20Foundations%20and%20Reconciliation.md) | Desired state, live state, pull model, reconciliation, sync status, health status, and operational traps. |
| 2 | [Argo CD Architecture and Control Loops](02%20-%20Argo%20CD%20Architecture%20and%20Control%20Loops.md) | API server, repo server, application controller, ApplicationSet controller, Redis, Dex/SSO, Kubernetes API, HA and scale failure boundaries. |
| 3 | [Applications Projects and Deployment Boundaries](03%20-%20Applications%20Projects%20and%20Deployment%20Boundaries.md) | Application specs, AppProjects, source/destination/resource boundaries, project roles, finalizers, and multi-team safety. |
| 4 | [Sync Drift Rollback Waves and Hooks](04%20-%20Sync%20Drift%20Rollback%20Waves%20and%20Hooks.md) | Manual sync, automated sync, pruning, self-healing, allow-empty, rollback, sync phases, waves, hooks, and migration traps. |
| 5 | [Troubleshooting OutOfSync Degraded and Failed Syncs](05%20-%20Troubleshooting%20OutOfSync%20Degraded%20and%20Failed%20Syncs.md) | OutOfSync, degraded health, comparison errors, failed sync, RBAC, Helm/Kustomize errors, stale status, and runbook-style diagnosis. |
| 6 | [Security RBAC Secrets and Tenant Boundaries](06%20-%20Security%20RBAC%20Secrets%20and%20Tenant%20Boundaries.md) | Identity, Argo CD RBAC, AppProject policy, repository and cluster credentials, Kubernetes RBAC, secret workflows, and tenant blast radius. |
| 7 | [Multi Cluster ApplicationSet and App of Apps Patterns](07%20-%20Multi%20Cluster%20ApplicationSet%20and%20App%20of%20Apps%20Patterns.md) | ApplicationSet, generators, multi-cluster deployment, app-of-apps, promotion, generated app deletion, and fleet safety. |
| 10 | [Cheatsheet](10%20-%20Cheatsheet.md) | Fast command, status, sync-policy, troubleshooting, and interview revision. |
| 11 | [Glossary](11%20-%20Glossary.md) | Precise Argo CD terminology and common traps. |

## Current Status

Started from the `everything` scope on 2026-05-26. Core Argo CD coverage is drafted across foundations, architecture, Application/AppProject boundaries, sync policy, troubleshooting, security, multi-cluster/ApplicationSet patterns, cheatsheet, and glossary. Future improvement can add separate Helm/Kustomize and secrets-tool-specific labs.
