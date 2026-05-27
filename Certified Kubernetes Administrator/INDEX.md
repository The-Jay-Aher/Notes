# Certified Kubernetes Administrator

## Quick Summary

The Certified Kubernetes Administrator (CKA) path focuses on operating Kubernetes clusters. It is about cluster architecture, installation, configuration, RBAC, scheduling, networking, storage, and troubleshooting.

The exam is performance-based: you solve tasks from the command line in a real Kubernetes environment. This means practice matters more than memorizing definitions.

If you are new to Kubernetes, start with [0 - Kubernetes Beginner Foundation](0%20-%20Kubernetes%20Beginner%20Foundation.md). It explains the vocabulary and object relationships used by every other note in this folder.

## Current Exam Snapshot

Checked against the Linux Foundation CKA page on 2026-05-27.

| Domain | Weight | Notes In This Folder |
| --- | ---: | --- |
| Beginner foundation | Not an exam domain | [0 - Kubernetes Beginner Foundation](0%20-%20Kubernetes%20Beginner%20Foundation.md) |
| Cluster Architecture, Installation and Configuration | 25% | [2 - Cluster Architecture Installation and Configuration](2%20-%20Cluster%20Architecture%20Installation%20and%20Configuration.md) |
| Workloads and Scheduling | 15% | [3 - Workloads and Scheduling](3%20-%20Workloads%20and%20Scheduling.md) |
| Services and Networking | 20% | [4 - Services and Networking](4%20-%20Services%20and%20Networking.md) |
| Storage | 10% | [5 - Storage](5%20-%20Storage.md) |
| Troubleshooting | 30% | [6 - Troubleshooting](6%20-%20Troubleshooting.md) |

Needs verification before booking: the Linux Foundation page listed the CKA exam as based on Kubernetes v1.34 when this note was refreshed, and says the environment aligns with recent Kubernetes minor versions after release. Always re-check the official exam page before scheduling.

## Suggested Study Order

1. Read [0 - Kubernetes Beginner Foundation](0%20-%20Kubernetes%20Beginner%20Foundation.md) until cluster, node, Pod, Service, Deployment, namespace, label, selector, RBAC, and PVC make sense.
2. Practice `kubectl` until common inspection/editing commands are fast.
3. Study cluster architecture and RBAC.
4. Learn workloads and scheduling.
5. Learn Services, CoreDNS, Ingress/Gateway API, and NetworkPolicies.
6. Learn PersistentVolumes, PersistentVolumeClaims, StorageClasses, access modes, and reclaim policies.
7. Practice troubleshooting every day.
8. Take timed mock labs and review failures carefully.

## Deep Practice And Revision Files

- [7 - Command Labs and Verification Playbook](7%20-%20Command%20Labs%20and%20Verification%20Playbook.md)
- [10 - Cheatsheet](10%20-%20Cheatsheet.md)
- [11 - Glossary](11%20-%20Glossary.md)
- [CHANGELOG](CHANGELOG.md)

## CKA Command Muscle Memory

```bash
# Set a default namespace for the current context
kubectl config set-context --current --namespace=<namespace>

# Show cluster and context
kubectl config current-context
kubectl cluster-info

# Fast inspection
kubectl get nodes -o wide
kubectl get pods -A -o wide
kubectl get svc -A
kubectl get events -A --sort-by=.lastTimestamp

# Explain resources
kubectl explain pod.spec.containers
kubectl explain deployment.spec.strategy

# Generate YAML quickly
kubectl create deployment web --image=nginx --dry-run=client -o yaml > deploy.yaml
kubectl run debug --image=busybox:1.36 --restart=Never --dry-run=client -o yaml > pod.yaml

# Logs and exec
kubectl logs <pod>
kubectl logs <pod> -c <container>
kubectl exec -it <pod> -- sh

# Edit and patch
kubectl edit deployment <name>
kubectl patch deployment <name> -p '{"spec":{"replicas":3}}'
```

## Practical Exam Habits

- Read the question twice and identify the namespace, context, resource name, and required final state.
- Switch context only when instructed.
- Set the namespace with `kubectl config set-context --current --namespace=...` to avoid repeated `-n`.
- Use `--dry-run=client -o yaml` to generate manifests quickly.
- Use official docs during practice so searching docs becomes natural.
- Validate results with `kubectl get`, `kubectl describe`, logs, events, and direct connectivity tests.
- Save generated YAML when the task asks for a manifest path.
- Do not spend too long on one task. Mark it mentally and return later.

## Related Notes

- [Networking Fundamentals](../Networking%20Fundamentals/1%20-%20Fundamentals%20of%20Networking.md)
- [Internet Protocol (IP)](../Networking%20Fundamentals/2%20-%20Internet%20Protocol%20%28IP%29.md)
- [Docker](../Docker/INDEX.md)
- [Certified Kubernetes Application Developer](../Certified%20Kubernetes%20Application%20Developer/INDEX.md)

## Official References

- CKA exam page: <https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/>
- Kubernetes documentation: <https://kubernetes.io/docs/>
- kubectl reference: <https://kubernetes.io/docs/reference/kubectl/>
- kubectl cheat sheet: <https://kubernetes.io/docs/reference/kubectl/quick-reference/>
