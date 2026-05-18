# 3 - Workloads and Scheduling

## Quick Summary

Kubernetes workloads describe how applications should run. Scheduling decides where Pods should run. For CKA, know Deployments, rolling updates, rollbacks, ConfigMaps, Secrets, autoscaling, resource requests/limits, taints, tolerations, node selectors, affinity, and self-healing behavior.

## Beginner Bridge

Workloads are Kubernetes objects that create or manage Pods. A Pod is usually too low-level to manage by hand in production, so you use a controller.

```text
Deployment -> good for stateless replicated apps
StatefulSet -> good for apps that need stable identity/storage
DaemonSet -> one Pod per matching node
Job -> run work until completion
CronJob -> run Jobs on a schedule
```

Scheduling is the placement decision: "which node should run this Pod?" If a Pod is stuck in `Pending`, Kubernetes accepted the desired state but could not place the Pod. The reason is usually in `kubectl describe pod <name>` under Events.

## Main Workload Resources

| Resource | Purpose |
| --- | --- |
| Pod | Smallest deployable unit. Usually managed by a controller. |
| ReplicaSet | Maintains a number of identical Pods. Usually managed by Deployment. |
| Deployment | Manages stateless app rollouts and rollbacks. |
| StatefulSet | Manages stateful Pods with stable identity and storage. |
| DaemonSet | Runs one Pod per matching node, commonly for agents. |
| Job | Runs task Pods to completion. |
| CronJob | Runs Jobs on a schedule. |

## Deployment Basics

Create a Deployment:

```bash
kubectl create deployment web --image=nginx --replicas=3
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

Update image:

```bash
kubectl set image deployment/web nginx=nginx:1.27
```

Roll back:

```bash
kubectl rollout history deployment/web
kubectl rollout undo deployment/web
kubectl rollout status deployment/web
```

## Rolling Update Strategy

Deployment rolling updates control how Pods are replaced.

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 1
    maxSurge: 1
```

| Field | Meaning |
| --- | --- |
| `maxUnavailable` | How many Pods can be unavailable during rollout. |
| `maxSurge` | How many extra Pods can be created above desired replicas. |

## ConfigMaps And Secrets

ConfigMaps store non-secret configuration.

```bash
kubectl create configmap app-config \
  --from-literal=APP_MODE=prod \
  --from-literal=LOG_LEVEL=info
```

Secrets store sensitive values, but they are not automatically a complete secret-management solution. Use RBAC, encryption at rest, and external secret systems where required.

```bash
kubectl create secret generic db-secret \
  --from-literal=username=app \
  --from-literal=password='change-me'
```

Consume as environment variables:

```yaml
envFrom:
  - configMapRef:
      name: app-config
  - secretRef:
      name: db-secret
```

Consume as files:

```yaml
volumes:
  - name: config
    configMap:
      name: app-config
containers:
  - name: app
    image: nginx
    volumeMounts:
      - name: config
        mountPath: /etc/app
```

## Resource Requests And Limits

Requests influence scheduling. Limits cap usage.

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "500m"
    memory: "512Mi"
```

Important:

- CPU is measured in cores. `500m` means half a core.
- Memory is measured in bytes with suffixes like `Mi` and `Gi`.
- If a container exceeds memory limit, it may be killed.
- If a container exceeds CPU limit, it is throttled.

## Quality Of Service Classes

| QoS | Condition |
| --- | --- |
| Guaranteed | Every container has equal CPU/memory requests and limits. |
| Burstable | At least one request exists, but not all requests equal limits. |
| BestEffort | No CPU or memory requests/limits. |

QoS can affect eviction priority under node pressure.

## Scheduling Controls

### nodeSelector

Simple key/value node selection.

```yaml
nodeSelector:
  disk: ssd
```

### Node Affinity

More expressive scheduling rules.

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: disk
              operator: In
              values:
                - ssd
```

### Pod Anti-Affinity

Avoid placing Pods together.

Useful for high availability across nodes or zones.

### Taints And Tolerations

Taints repel Pods from nodes unless Pods tolerate them.

```bash
kubectl taint nodes node1 dedicated=gpu:NoSchedule
```

Pod toleration:

```yaml
tolerations:
  - key: dedicated
    operator: Equal
    value: gpu
    effect: NoSchedule
```

Taints are on nodes. Tolerations are on Pods.

## Workload Autoscaling

Horizontal Pod Autoscaler scales replicas based on metrics.

```bash
kubectl autoscale deployment web --min=2 --max=10 --cpu-percent=70
kubectl get hpa
```

Requirements:

- Metrics must be available, commonly through metrics-server.
- Pods need resource requests for CPU-based autoscaling.

## Self-Healing Behavior

Kubernetes self-healing examples:

- Deployment recreates Pods when they are deleted.
- kubelet restarts containers according to restart policy and probe results.
- ReplicaSet maintains desired replica count.
- Node controller reacts to node failures.

But Kubernetes cannot fix:

- Bad application code.
- Incorrect image tags.
- Wrong config values.
- Missing permissions.
- Broken external dependencies.

## Benefits

- Declarative workload management.
- Rolling updates and rollbacks.
- Self-healing through controllers.
- Scheduling controls for performance, isolation, and availability.
- Autoscaling support.

## Drawbacks / Limitations

- Incorrect labels/selectors can break controllers.
- Bad probes can cause restart loops or route traffic too early.
- Resource limits can cause throttling or OOM kills.
- Scheduling rules can make Pods unschedulable.
- Secrets need stronger controls than just "create a Secret".

## Hidden Details / Caveats

- A Deployment owns ReplicaSets, and ReplicaSets own Pods.
- Do not edit ReplicaSet Pods directly for long-term changes; update the Deployment.
- ConfigMap/Secret environment variables do not update inside already-running containers automatically.
- Mounted ConfigMap/Secret volumes can update eventually, but apps may still need reload logic.
- `kubectl rollout undo` rolls back Deployment history, not arbitrary external dependencies.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| No resource requests | Add requests so scheduler and autoscaler can make decisions. |
| Wrong selector labels | Ensure Service selectors and Deployment labels match. |
| Over-strict affinity | Relax rules or add matching nodes. |
| Taint without toleration | Add toleration or remove taint. |
| Updating Pods directly | Update controller-owned resources such as Deployment. |
| Putting secrets in ConfigMaps | Use Secrets and proper external secret handling. |

## Troubleshooting

```bash
kubectl get pods -o wide
kubectl describe pod <pod>
kubectl logs <pod>
kubectl get events --sort-by=.lastTimestamp
kubectl rollout status deployment/<name>
kubectl rollout history deployment/<name>
```

| Symptom | Likely Cause |
| --- | --- |
| `Pending` | Insufficient resources, taints, affinity, PVC not bound. |
| `CrashLoopBackOff` | App exits repeatedly, bad config, missing dependency. |
| `ImagePullBackOff` | Wrong image, missing registry auth, network issue. |
| Rollout stuck | New Pods not becoming ready. |
| HPA not scaling | Metrics unavailable or missing resource requests. |

## Interview Notes

- Deployment manages ReplicaSets and supports rolling updates/rollbacks.
- DaemonSet runs Pods on matching nodes.
- StatefulSet gives stable identity and persistent storage patterns.
- Requests affect scheduling; limits cap runtime usage.
- Taints repel; tolerations permit.
- Node affinity attracts; anti-affinity separates.
- ConfigMaps are for non-secret config; Secrets are for sensitive values.

## Related Topics

- [2 - Cluster Architecture Installation and Configuration](2%20-%20Cluster%20Architecture%20Installation%20and%20Configuration.md)
- [6 - Troubleshooting](6%20-%20Troubleshooting.md)

## Official References

- [Workloads](https://kubernetes.io/docs/concepts/workloads/)
- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Assign Pods to nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [Resource management for Pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
