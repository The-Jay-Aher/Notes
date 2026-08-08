# 10 - CKAD Cheatsheet

## Exam Snapshot

Source checked: Linux Foundation CKAD page on 2026-05-27.

- Current official page lists CKAD as based on Kubernetes v1.35.
- Exam is online, proctored, performance-based, and command-line driven.
- Current official domain weights:
  - Application Design and Build: 20%
  - Application Deployment: 20%
  - Application Observability and Maintenance: 15%
  - Application Environment, Configuration and Security: 25%
  - Services and Networking: 20%

## Fast Generation

```bash
kubectl run app --image=nginx --restart=Never --dry-run=client -o yaml > pod.yaml
kubectl create deployment app --image=nginx --replicas=3 --dry-run=client -o yaml > deploy.yaml
kubectl expose deployment app --port=80 --target-port=8080 --dry-run=client -o yaml > svc.yaml
kubectl create configmap app-config --from-literal=KEY=value --dry-run=client -o yaml > cm.yaml
kubectl create secret generic app-secret --from-literal=PASSWORD=secret --dry-run=client -o yaml > secret.yaml
```

## Verification Chain

```text
get -> describe -> logs -> events -> rollout status -> connectivity test
```

## Workload Choice

| Need | Object |
| --- | --- |
| replicated stateless app | Deployment |
| run once to completion | Job |
| scheduled task | CronJob |
| one Pod per node | DaemonSet |
| stable identity/storage | StatefulSet |
| direct simple task/debug | Pod |

## Common Traps

- wrong namespace
- Service selector mismatch
- `targetPort` wrong
- liveness used where readiness is needed
- Secret value put in ConfigMap
- missing resource requests
- ConfigMap/Secret key typo
- image tag typo
- mounted file path wrong
- NetworkPolicy accidentally blocks traffic

