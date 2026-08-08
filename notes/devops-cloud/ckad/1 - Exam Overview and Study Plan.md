# 1 - Exam Overview and Study Plan

## Quick Summary

CKAD validates hands-on Kubernetes application skills. You should be able to create, configure, deploy, expose, observe, and debug cloud-native applications using Kubernetes primitives.

## Start Here If You Are New

If Pods, Deployments, Services, ConfigMaps, Secrets, probes, resources, or rollouts feel unclear, read [0 - Kubernetes Beginner Foundation](0%20-%20Kubernetes%20Beginner%20Foundation.md) first.

CKAD is application-focused. The exam is less about installing Kubernetes and more about accurately describing how an app should run:

```text
image + command + config + secret + ports + probes + resources + Service = runnable app definition
```

When practicing, do not only make YAML pass validation. Verify that the app behaves correctly with `get`, `describe`, `logs`, rollouts, and connectivity checks.

## CKAD Versus CKA

| Area | CKAD | CKA |
| --- | --- | --- |
| Main focus | Applications on Kubernetes. | Administering Kubernetes clusters. |
| Common tasks | Pods, Deployments, Services, config, probes, rollouts, debugging. | Cluster architecture, RBAC, nodes, storage, networking, troubleshooting. |
| Cluster installation | Usually not a focus. | Important. |
| Application YAML speed | Very important. | Important, but broader admin scope. |

## What The Exam Tests

- Container image awareness.
- Choosing workload resources.
- Multi-container Pod patterns.
- Persistent and ephemeral volumes.
- Deployment strategies.
- Rolling updates and rollbacks.
- Helm and Kustomize basics.
- Probes and health checks.
- Logs, CLI monitoring, and debugging.
- API deprecations.
- ConfigMaps, Secrets, requests, limits, quotas, ServiceAccounts, and SecurityContexts.
- Services, Ingress, and NetworkPolicies.

## What You Should Already Know

- Linux command line basics.
- YAML syntax.
- Container images and tags.
- Environment variables.
- HTTP basics.
- Kubernetes object basics.

## Study Plan

### Phase 1 - Pod And Deployment Basics

Practice:

```bash
kubectl run nginx --image=nginx --restart=Never
kubectl create deployment web --image=nginx --replicas=3
kubectl expose deployment web --port=80
kubectl get pod,deploy,rs,svc -o wide
```

Understand:

- Pod spec.
- Labels and selectors.
- Container image, command, args, ports.
- Restart policy.
- Deployment to ReplicaSet to Pod relationship.

### Phase 2 - Configuration And Runtime Behavior

Practice:

- ConfigMaps.
- Secrets.
- Environment variables.
- Mounted config files.
- Probes.
- Resources.
- SecurityContext.
- ServiceAccounts.

### Phase 3 - Deployment And Packaging

Practice:

- Rolling updates.
- Rollbacks.
- Blue/green and canary concepts.
- Helm install/upgrade/list/rollback.
- Kustomize overlays.

### Phase 4 - Networking And Debugging

Practice:

- Services.
- Ingress.
- NetworkPolicy.
- DNS tests.
- `logs`, `exec`, `describe`, `events`, `port-forward`.

## High-Value CKAD Skills

| Skill | Why It Matters |
| --- | --- |
| Generate YAML quickly | Saves time and avoids syntax mistakes. |
| Understand labels/selectors | Services and controllers depend on them. |
| Configure probes | Affects health, rollouts, and traffic routing. |
| Use ConfigMaps and Secrets correctly | Common app configuration task. |
| Debug application failures | Large part of real Kubernetes development. |
| Know resource requests/limits | Required for scheduling and safe app operation. |
| Use Services and Ingress | Exposes apps inside/outside cluster. |

## Common Mistakes

- Forgetting namespace.
- Using wrong labels in Service selector.
- Putting sensitive data in ConfigMaps.
- Using liveness probe where readiness probe is needed.
- Setting resource limits without understanding app behavior.
- Editing generated YAML without validating indentation.
- Not checking `kubectl describe` events.

## Before The Exam, Remember This

- Practice under a timer.
- Learn `kubectl explain`.
- Learn fast YAML generation.
- Always verify final state.
- Do not memorize every field; know how to find and apply the right field quickly.

## Related Notes

- [2 - Application Design and Build](2%20-%20Application%20Design%20and%20Build.md)
- [4 - Observability Maintenance and Troubleshooting](4%20-%20Observability%20Maintenance%20and%20Troubleshooting.md)

## Official References

- [CKAD exam page](https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/)
- [Kubernetes documentation](https://kubernetes.io/docs/)
- [kubectl quick reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
