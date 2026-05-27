# 10 - CKA Cheatsheet

## Exam Snapshot

Source checked: Linux Foundation CKA page on 2026-05-27.

- Current official page lists CKA as based on Kubernetes v1.34.
- Exam is online, proctored, performance-based, and command-line driven.
- Current official domain weights:
  - Cluster Architecture, Installation and Configuration: 25%
  - Workloads and Scheduling: 15%
  - Services and Networking: 20%
  - Storage: 10%
  - Troubleshooting: 30%

## First Commands

```bash
kubectl config current-context
kubectl config set-context --current --namespace=<namespace>
kubectl get nodes -o wide
kubectl get pods -A -o wide
kubectl get events -A --sort-by=.lastTimestamp
```

## Fast Generation

```bash
kubectl create deployment web --image=nginx --dry-run=client -o yaml > deploy.yaml
kubectl run debug --image=busybox:1.36 --restart=Never --dry-run=client -o yaml > pod.yaml
kubectl expose deployment web --port=80 --target-port=8080 --dry-run=client -o yaml > svc.yaml
```

## Troubleshooting Chain

```text
get -> describe -> events -> logs -> exec -> component/node checks
```

## RBAC Chain

```text
Role/ClusterRole -> RoleBinding/ClusterRoleBinding -> subject -> auth can-i
```

## Networking Chain

```text
Pod labels -> Service selector -> EndpointSlice -> DNS -> NetworkPolicy -> targetPort -> app
```

## Storage Chain

```text
StorageClass -> PVC -> PV binding -> Pod mount -> container path
```

## Common Traps

- wrong context
- wrong namespace
- selector does not match labels
- missing resource requests
- toleration without matching node condition understanding
- ClusterRoleBinding when RoleBinding was enough
- PVC pending due to missing StorageClass
- readiness failure causing Service endpoints to be empty
- ignoring events

