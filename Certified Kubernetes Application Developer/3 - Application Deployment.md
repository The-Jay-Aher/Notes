# 3 - Application Deployment

## Quick Summary

Application deployment in Kubernetes is about changing running applications safely. CKAD expects you to understand Deployments, rolling updates, rollbacks, common deployment strategies, Helm, and Kustomize.

## Beginner Bridge

A deployment is a controlled change from one desired state to another.

```text
Old desired state: image nginx:1.26, replicas 3
New desired state: image nginx:1.27, replicas 3
```

Kubernetes creates a new ReplicaSet for the new version and gradually moves Pods from old to new based on the rollout strategy. If the new version fails, rollout status and events tell you where it got stuck, and rollback can return to a previous ReplicaSet revision.

## Deployment Resource

Create:

```bash
kubectl create deployment web --image=nginx:1.27 --replicas=3
```

Inspect:

```bash
kubectl get deploy,rs,pod -l app=web
kubectl describe deployment web
```

Scale:

```bash
kubectl scale deployment web --replicas=5
```

## Rolling Updates

Update image:

```bash
kubectl set image deployment/web nginx=nginx:1.28
kubectl rollout status deployment/web
```

Strategy example:

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1
    maxUnavailable: 0
```

Meaning:

- `maxSurge: 1` allows one extra Pod above desired replicas during update.
- `maxUnavailable: 0` requires all desired replicas to remain available during update.

## Rollbacks

```bash
kubectl rollout history deployment/web
kubectl rollout undo deployment/web
kubectl rollout undo deployment/web --to-revision=2
```

Rollbacks restore an earlier Deployment revision. They do not roll back database migrations, external services, or other systems automatically.

## Deployment Strategies

| Strategy | Kubernetes Shape | Use Case |
| --- | --- | --- |
| Rolling update | Native Deployment strategy. | Normal gradual replacement. |
| Recreate | Stop old Pods, then start new Pods. | Apps that cannot run two versions together. |
| Blue/green | Two environments, switch Service/Ingress traffic. | Safer release with quick rollback. |
| Canary | Send small traffic portion to new version. | Risk-controlled rollout. |

### Recreate

```yaml
strategy:
  type: Recreate
```

Use when old and new versions cannot run at the same time.

### Blue/Green Concept

```text
Service selector -> blue version
Deploy green version separately
Test green
Switch Service selector -> green version
```

### Canary Concept

Kubernetes alone can run a small canary Deployment, but traffic splitting usually needs an ingress controller, Gateway implementation, service mesh, or external load balancer support.

Simple concept:

```text
stable Deployment replicas: 9
canary Deployment replicas: 1
same Service selector matches both
approximately 10% Pod-level distribution
```

This is rough traffic distribution, not precise request weighting.

## Helm

Helm is a package manager for Kubernetes.

Common commands:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm search repo nginx
helm install web bitnami/nginx
helm list
helm upgrade web bitnami/nginx --set replicaCount=3
helm rollback web 1
helm uninstall web
```

Use Helm when:

- Installing existing packaged applications.
- Managing chart values.
- Reusing deployment templates.

Watch-outs:

- Always inspect chart values.
- Understand what resources a chart creates.
- Avoid blindly installing charts with broad permissions.

## Kustomize

Kustomize customizes raw YAML using overlays.

Example structure:

```text
base/
  deployment.yaml
  service.yaml
  kustomization.yaml
overlays/
  dev/
    kustomization.yaml
  prod/
    kustomization.yaml
```

Apply:

```bash
kubectl apply -k overlays/prod
```

Example `kustomization.yaml`:

```yaml
resources:
  - ../../base
namePrefix: prod-
replicas:
  - name: web
    count: 5
```

Use Kustomize when:

- You want environment overlays.
- You want YAML-native customization.
- You do not need full templating.

## Benefits

- Deployments support gradual updates and rollbacks.
- Helm makes complex app packaging reusable.
- Kustomize keeps overlays close to raw Kubernetes YAML.
- Strategies such as blue/green and canary reduce release risk.

## Drawbacks / Limitations

- Rollback only covers Kubernetes object revision, not all application state.
- Canary traffic splitting is not precise with only basic Services.
- Helm charts can hide complexity.
- Kustomize overlays can become hard to follow if deeply layered.
- Bad readiness probes can break rollout behavior.

## Hidden Details / Caveats

- A Deployment rollout is considered successful based on Pod readiness and strategy settings.
- `kubectl rollout restart deployment/name` restarts Pods by updating Pod template metadata.
- Deployment revision history can be limited by `revisionHistoryLimit`.
- Blue/green often depends on label selectors or traffic routing resources.
- Helm release state is stored in the cluster, usually as Secrets.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Updating image but not verifying rollout | Use `kubectl rollout status`. |
| Rollback expected to undo DB changes | Plan app/data rollback separately. |
| Canary with same selector but no replica math | Control stable/canary replica counts carefully. |
| Installing Helm chart without reading values | Run `helm show values` first. |
| Kustomize overlay patches wrong resource name | Check final output with `kubectl kustomize` or `kustomize build`. |

## Troubleshooting

```bash
kubectl rollout status deployment/<name>
kubectl rollout history deployment/<name>
kubectl describe deployment <name>
kubectl get rs,pod -l app=<label>
kubectl get events --sort-by=.lastTimestamp
helm status <release>
helm get values <release>
```

## Interview Notes

- Deployment manages ReplicaSets.
- Rolling update is the default Deployment strategy.
- Rollback returns a Deployment to a previous revision.
- Blue/green switches traffic between two versions.
- Canary sends limited traffic to a new version.
- Helm packages Kubernetes apps as charts.
- Kustomize applies overlays to YAML.

## Related Topics

- [2 - Application Design and Build](2%20-%20Application%20Design%20and%20Build.md)
- [4 - Observability Maintenance and Troubleshooting](4%20-%20Observability%20Maintenance%20and%20Troubleshooting.md)

## Official References

- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Updating a Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment)
- [Helm documentation](https://helm.sh/docs/)
- [Kustomize documentation](https://kubectl.docs.kubernetes.io/references/kustomize/)
