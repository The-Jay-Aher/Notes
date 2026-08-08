# 10 - Argo CD Cheatsheet

## Why This Chapter Matters

This file is for fast revision after the deeper chapters. It is not a replacement for understanding. Use it to recall commands, status meanings, safety checks, and troubleshooting order.

## Core Mental Model

```text
Git/source -> repo-server renders desired state
Kubernetes API -> controller reads live state
application-controller -> compares and syncs
argocd-server -> UI/CLI/API/auth/RBAC
AppProject -> safety boundary
```

## Status Meanings

| Status | Meaning | First action |
| --- | --- | --- |
| `Synced` | Desired and live state match. | Check health if users report issues. |
| `OutOfSync` | Desired and live state differ. | Run `argocd app diff`. |
| `Healthy` | Resource health looks good. | Use app/business monitoring for deeper proof. |
| `Degraded` | Runtime health is bad. | Check Pods, events, logs, dependencies. |
| `Progressing` | Rollout or operation not complete. | Watch rollout, events, controller status. |
| `ComparisonError` | Desired/live comparison failed. | Check source/render/repo-server. |
| `InvalidSpecError` | Application spec or project boundary problem. | Check Application and AppProject YAML. |

## Daily Commands

```bash
argocd app list
argocd app get <app> --refresh
argocd app diff <app>
argocd app manifests <app>
argocd app sync <app>
argocd app wait <app> --sync --health --timeout 600
argocd proj get <project>
argocd cluster list
argocd repo list
```

## Kubernetes-Side Commands

```bash
kubectl get applications.argoproj.io -n argocd
kubectl describe application -n argocd <app>
kubectl get appprojects.argoproj.io -n argocd
kubectl describe appproject -n argocd <project>
kubectl get pods -n argocd
kubectl logs -n argocd deploy/argocd-repo-server
kubectl logs -n argocd statefulset/argocd-application-controller
kubectl logs -n argocd deploy/argocd-server
```

## Sync Policy Quick Reference

| Setting | Meaning | Risk |
| --- | --- | --- |
| Manual sync | Human/API triggers apply. | Slow, forgotten syncs. |
| `automated` | Argo CD syncs OutOfSync apps automatically. | Bad Git change deploys quickly. |
| `prune: true` | Delete tracked live resources absent from desired state. | Wrong scope deletes resources. |
| `selfHeal: true` | Revert live drift back to Git. | Emergency manual edits undone. |
| `allowEmpty: true` | Permit empty desired state with pruning. | Empty render can delete app resources. |

## Safety Before Production Sync

1. Confirm app name, project, source, target revision, destination cluster, and namespace.
2. Run `argocd app diff <app>`.
3. Read delete operations carefully.
4. Confirm AppProject boundaries.
5. Confirm image tag/digest and config values.
6. Confirm migration and rollback plan.
7. Sync.
8. Wait for sync and health.
9. Check application metrics/logs, not only Argo CD health.

## Troubleshooting Order

```text
status
-> diff
-> manifests/render
-> project/RBAC
-> Kubernetes apply/errors
-> runtime health
-> controller/repo-server/cache scale
```

## Component Ownership

| Symptom | Suspect |
| --- | --- |
| UI/login/API broken | `argocd-server`, Dex/OIDC, ingress/TLS, RBAC |
| Manifest generation failed | `argocd-repo-server`, source, Helm, Kustomize, plugin |
| Status stale or sync not happening | `argocd-application-controller`, queues, API access |
| Generated app missing | `argocd-applicationset-controller`, generator/template |
| Sync forbidden | AppProject, Argo CD RBAC, Kubernetes RBAC |
| Degraded after sync | Workload runtime: Pods, events, logs, Services, dependencies |

## Exam / Interview Lines

- Argo CD is a Kubernetes GitOps controller, not merely a UI.
- CI builds and validates artifacts; Argo CD reconciles desired state.
- `Synced` is not the same as `Healthy`.
- Prune is deletion, not harmless cleanup.
- Self-heal enforces Git against live drift.
- AppProjects are security boundaries.
- ApplicationSet generates Applications; it does not directly sync workloads.
- GitOps does not solve secret management by itself.

