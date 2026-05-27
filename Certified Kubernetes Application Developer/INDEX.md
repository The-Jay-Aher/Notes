# Certified Kubernetes Application Developer

## Quick Summary

The Certified Kubernetes Application Developer (CKAD) path focuses on designing, building, configuring, deploying, exposing, observing, and debugging applications on Kubernetes. It is more application-focused than CKA.

The exam is performance-based and terminal-driven. You need to be comfortable creating and modifying Kubernetes manifests quickly.

If you are new to Kubernetes application manifests, start with [0 - Kubernetes Beginner Foundation](0%20-%20Kubernetes%20Beginner%20Foundation.md). It explains the app-focused basics before the exam-domain notes.

## Current Exam Snapshot

Checked against the Linux Foundation CKAD page on 2026-05-27.

| Domain | Weight | Notes In This Folder |
| --- | ---: | --- |
| Beginner foundation | Not an exam domain | [0 - Kubernetes Beginner Foundation](0%20-%20Kubernetes%20Beginner%20Foundation.md) |
| Application Design and Build | 20% | [2 - Application Design and Build](2%20-%20Application%20Design%20and%20Build.md) |
| Application Deployment | 20% | [3 - Application Deployment](3%20-%20Application%20Deployment.md) |
| Application Observability and Maintenance | 15% | [4 - Observability Maintenance and Troubleshooting](4%20-%20Observability%20Maintenance%20and%20Troubleshooting.md) |
| Application Environment, Configuration and Security | 25% | [5 - Configuration Security Services and Networking](5%20-%20Configuration%20Security%20Services%20and%20Networking.md) |
| Services and Networking | 20% | [5 - Configuration Security Services and Networking](5%20-%20Configuration%20Security%20Services%20and%20Networking.md) |

Needs verification before booking: the Linux Foundation page listed the CKAD exam as based on Kubernetes v1.35 when this note was refreshed, and says the environment aligns with recent Kubernetes minor versions after release. Always re-check the official exam page before scheduling.

## Suggested Study Order

1. Read [0 - Kubernetes Beginner Foundation](0%20-%20Kubernetes%20Beginner%20Foundation.md) until Pods, Deployments, Services, ConfigMaps, Secrets, probes, resources, and rollouts make sense.
2. Learn Deployments, ReplicaSets, Jobs, CronJobs, DaemonSets, and StatefulSets at a practical level.
3. Practice ConfigMaps, Secrets, environment variables, volumes, and probes.
4. Practice Services, Ingress, and basic NetworkPolicies.
5. Learn resource requests, limits, quotas, ServiceAccounts, SecurityContexts, and capabilities.
6. Practice rolling updates, rollbacks, Helm, and Kustomize.
7. Drill logs, events, exec, port-forward, and debugging until they are fast.

## Deep Practice And Revision Files

- [6 - Application Command Labs and Verification Playbook](6%20-%20Application%20Command%20Labs%20and%20Verification%20Playbook.md)
- [10 - Cheatsheet](10%20-%20Cheatsheet.md)
- [11 - Glossary](11%20-%20Glossary.md)
- [CHANGELOG](CHANGELOG.md)

## CKAD Command Muscle Memory

```bash
# Generate Pod YAML
kubectl run app --image=nginx --restart=Never --dry-run=client -o yaml > pod.yaml

# Generate Deployment YAML
kubectl create deployment app --image=nginx --replicas=3 --dry-run=client -o yaml > deploy.yaml

# Expose a Deployment
kubectl expose deployment app --port=80 --target-port=8080

# Create ConfigMap and Secret
kubectl create configmap app-config --from-literal=LOG_LEVEL=info
kubectl create secret generic app-secret --from-literal=PASSWORD=change-me

# Rollout
kubectl set image deployment/app nginx=nginx:1.27
kubectl rollout status deployment/app
kubectl rollout undo deployment/app

# Debug
kubectl describe pod <pod>
kubectl logs <pod>
kubectl logs <pod> --previous
kubectl exec -it <pod> -- sh
```

## Practical Exam Habits

- Always check namespace and context.
- Use `--dry-run=client -o yaml` to generate skeletons.
- Use `kubectl explain` when unsure about a field.
- Prefer editing YAML for precise tasks.
- Validate every answer with `get`, `describe`, logs, or connectivity tests.
- Know how to quickly create a temporary curl/busybox Pod.

## Related Notes

- [Certified Kubernetes Administrator](../Certified%20Kubernetes%20Administrator/INDEX.md)
- [Docker](../Docker/INDEX.md)
- [Networking Fundamentals](../Networking%20Fundamentals/1%20-%20Fundamentals%20of%20Networking.md)
- [Learning GitHub Actions](../Learning%20GitHub%20Actions.md)

## Official References

- CKAD exam page: <https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/>
- Kubernetes documentation: <https://kubernetes.io/docs/>
- kubectl reference: <https://kubernetes.io/docs/reference/kubectl/>
- kubectl cheat sheet: <https://kubernetes.io/docs/reference/kubectl/quick-reference/>
