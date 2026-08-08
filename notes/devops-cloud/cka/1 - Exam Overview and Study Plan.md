# 1 - Exam Overview and Study Plan

## Quick Summary

CKA proves that you can administer Kubernetes clusters in practical scenarios. It is not a theory-only exam. You need to create, inspect, modify, fix, and validate Kubernetes resources from a terminal.

## Start Here If You Are New

If the words cluster, node, Pod, Deployment, Service, namespace, label, selector, kubelet, RBAC, or PVC feel unclear, read [0 - Kubernetes Beginner Foundation](0%20-%20Kubernetes%20Beginner%20Foundation.md) before continuing.

The CKA exam looks like an administrator exam, but the first real skill is understanding object relationships:

```text
kubectl sends desired state -> API server stores it -> controllers/scheduler/kubelet act on it
```

When studying, always connect a command back to this model. For example, `kubectl describe pod` is not magic; it asks the API server for the Pod object, including status and events that controllers and kubelet have reported.

## What The Exam Tests

The exam focuses on the administrator side of Kubernetes:

- Cluster architecture and control-plane components.
- Cluster creation and lifecycle operations.
- RBAC and access control.
- Workload behavior and scheduling.
- Services, DNS, Ingress/Gateway, and NetworkPolicies.
- Storage classes, PersistentVolumes, and PersistentVolumeClaims.
- Troubleshooting nodes, components, workloads, services, and networking.

## What You Should Already Know

Before serious CKA preparation, know:

- Basic Linux commands.
- YAML indentation and structure.
- Containers and images.
- Networking basics: IP, DNS, ports, routing, firewalls.
- Basic shell editing with `vi`, `nano`, or another terminal editor.

## Study Plan

### Phase 1 - Foundation

Goals:

- Understand the Kubernetes object model.
- Practice creating Pods, Deployments, Services, ConfigMaps, Secrets, and Jobs.
- Learn common `kubectl get`, `describe`, `logs`, `exec`, `apply`, `delete`, and `edit` commands.

Daily practice:

```bash
kubectl get pods -A -o wide
kubectl describe pod <pod>
kubectl logs <pod>
kubectl explain deployment.spec.template.spec.containers
```

### Phase 2 - Administrator Domains

Goals:

- Learn control plane components.
- Practice RBAC.
- Understand kubeadm cluster lifecycle.
- Understand CNI, CSI, CRI, and extension interfaces.
- Practice scheduling controls and resource limits.
- Practice PV/PVC/StorageClass tasks.

### Phase 3 - Troubleshooting

Goals:

- Break workloads intentionally and fix them.
- Read events, logs, and component status.
- Diagnose DNS, Service, NetworkPolicy, and node problems.
- Practice under time pressure.

### Phase 4 - Timed Labs

Goals:

- Complete mock tasks quickly.
- Verify final state after every answer.
- Build speed with documentation search.

## Exam Strategy

1. Confirm the current context.
2. Confirm the namespace.
3. Generate YAML quickly when useful.
4. Apply the smallest correct change.
5. Verify the result.
6. Move on.

Example verification habit:

```bash
kubectl get deploy,rs,pod,svc -n <namespace> -o wide
kubectl describe pod -n <namespace> <pod>
kubectl get events -n <namespace> --sort-by=.lastTimestamp
```

## High-Value Skills

| Skill | Why It Matters |
| --- | --- |
| `kubectl explain` | Helps write correct YAML without memorizing every field. |
| `--dry-run=client -o yaml` | Generates manifests quickly. |
| JSONPath/custom columns | Extracts exact values fast. |
| Events/logs/describe | Most troubleshooting starts here. |
| RBAC commands | Common admin task and easy to get wrong. |
| Service/DNS debugging | Common real-world cluster issue. |
| Static Pod knowledge | Important for control-plane troubleshooting. |

## Common Mistakes

- Forgetting the namespace.
- Editing the wrong context.
- Creating a resource imperatively but forgetting the required labels.
- Applying YAML with wrong indentation.
- Ignoring events.
- Not validating after a change.
- Spending too much time memorizing YAML instead of learning how to find and generate it.

## Before The Exam, Remember This

- You are allowed to use official documentation, but you still need to know what to search for.
- Speed comes from repeated practice, not from reading alone.
- Always validate the final object state.
- A working answer matters more than a perfect-looking manifest.
- Troubleshooting questions usually have evidence in events, logs, resource status, or component logs.

## Related Notes

- [2 - Cluster Architecture Installation and Configuration](2%20-%20Cluster%20Architecture%20Installation%20and%20Configuration.md)
- [6 - Troubleshooting](6%20-%20Troubleshooting.md)

## Official References

- [CKA exam page](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/)
- [Kubernetes documentation](https://kubernetes.io/docs/)
- [kubectl quick reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
