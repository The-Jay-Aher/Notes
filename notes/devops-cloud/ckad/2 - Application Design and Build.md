# 2 - Application Design and Build

## Quick Summary

Application design in Kubernetes means choosing the right workload resource, defining container behavior clearly, using multi-container patterns when needed, and attaching the right kind of storage. CKAD expects you to build and modify resource definitions quickly.

## Beginner Bridge

Kubernetes application design starts with one question: what should keep this container running?

```text
One always-on replicated web app -> Deployment
One task that should finish -> Job
One scheduled task -> CronJob
One Pod per node -> DaemonSet
Stable identity/storage -> StatefulSet
```

After choosing the workload, define the container clearly: image, command, args, ports, env vars, mounted files, and resources. Most CKAD mistakes happen because one of these small fields is missing, misspelled, or in the wrong namespace.

## Container Image Basics

Kubernetes runs containers from images.

Important image fields:

```yaml
containers:
  - name: app
    image: nginx:1.27
    imagePullPolicy: IfNotPresent
```

Common image pull policies:

| Policy | Meaning |
| --- | --- |
| `Always` | Always pull before starting. |
| `IfNotPresent` | Use local image if available, otherwise pull. |
| `Never` | Never pull; image must already exist on node. |

Use explicit tags for predictable deployments. Avoid relying on `latest` for production.

## Commands And Args

Docker image entrypoint and command can be overridden.

```yaml
containers:
  - name: worker
    image: busybox:1.36
    command: ["sh", "-c"]
    args: ["echo starting; sleep 3600"]
```

Common mistake: confusing `command` and `args`.

- `command` maps to container entrypoint.
- `args` maps to command arguments.

## Choosing The Right Workload

| Workload | Use When |
| --- | --- |
| Pod | Direct single-Pod task or exam/lab object. Rarely direct in production. |
| Deployment | Stateless app with rolling updates and replicas. |
| StatefulSet | Stable identity/storage, ordered deployment, stateful systems. |
| DaemonSet | One Pod per node or per matching node. |
| Job | One-time task that runs to completion. |
| CronJob | Scheduled repeated task. |

## Pods

Pod example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web
  labels:
    app: web
spec:
  containers:
    - name: nginx
      image: nginx:1.27
      ports:
        - containerPort: 80
```

Use direct Pods for:

- Debugging.
- Simple exam tasks.
- Static examples.

Use controllers for real application management.

## Multi-Container Pod Patterns

Containers in the same Pod share:

- Network namespace.
- Pod IP.
- Volumes defined in the Pod.
- Lifecycle.

Common patterns:

| Pattern | Purpose |
| --- | --- |
| Sidecar | Adds helper behavior such as logging, proxying, syncing. |
| Init container | Runs setup before app containers start. |
| Adapter | Converts output/interface for another system. |
| Ambassador | Handles outbound connection/proxy behavior. |

### Init Container

```yaml
initContainers:
  - name: wait-for-db
    image: busybox:1.36
    command: ["sh", "-c", "until nslookup db; do sleep 2; done"]
containers:
  - name: app
    image: nginx
```

Init containers must complete before normal containers start.

### Sidecar

```yaml
containers:
  - name: app
    image: nginx
    volumeMounts:
      - name: shared
        mountPath: /usr/share/nginx/html
  - name: content
    image: busybox:1.36
    command: ["sh", "-c"]
    args: ["while true; do date > /html/index.html; sleep 5; done"]
    volumeMounts:
      - name: shared
        mountPath: /html
volumes:
  - name: shared
    emptyDir: {}
```

## Volumes

| Volume Type | Use |
| --- | --- |
| `emptyDir` | Temporary shared storage for containers in one Pod. |
| `configMap` | Config files from ConfigMap. |
| `secret` | Sensitive files from Secret. |
| `persistentVolumeClaim` | Durable storage. |

Ephemeral `emptyDir`:

```yaml
volumes:
  - name: scratch
    emptyDir: {}
```

PVC volume:

```yaml
volumes:
  - name: data
    persistentVolumeClaim:
      claimName: app-data
```

## Labels And Selectors

Labels are key/value metadata. Selectors match labels.

Deployment selector:

```yaml
selector:
  matchLabels:
    app: web
template:
  metadata:
    labels:
      app: web
```

Service selector:

```yaml
selector:
  app: web
```

If labels and selectors do not match, controllers and Services will not target the expected Pods.

## Benefits

- Workloads express desired application state.
- Controllers keep applications running.
- Multi-container Pods support tightly coupled helpers.
- Volumes separate data/config from container image.
- Labels make grouping and selection flexible.

## Drawbacks / Limitations

- Multi-container Pods can become too tightly coupled.
- Direct Pods lack rollout and self-healing behavior from higher controllers.
- Stateful applications need careful storage and backup design.
- Wrong selectors are easy to miss.
- Image tags and pull policy choices can make deployments unpredictable.

## Hidden Details / Caveats

- Containers in one Pod can reach each other through `localhost`.
- A Pod is scheduled as one unit; all containers land on the same node.
- Init containers run sequentially.
- Deployment selectors are effectively immutable in normal use; plan labels carefully.
- Pod IPs are temporary. Use Services for stable access.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Using a bare Pod for an app that needs replicas | Use a Deployment. |
| Relying on `latest` tag | Use explicit immutable tags where possible. |
| Selector does not match labels | Compare selectors and template labels. |
| Sidecar doing unrelated work | Keep sidecars tightly coupled to the app. |
| Using `emptyDir` for durable data | Use PVC-backed storage. |

## Troubleshooting

```bash
kubectl get pod -o wide --show-labels
kubectl describe pod <pod>
kubectl logs <pod> -c <container>
kubectl exec -it <pod> -c <container> -- sh
kubectl get deploy,rs,pod
```

## Interview Notes

- Pod is the smallest deployable unit.
- Deployment is best for stateless replicated applications.
- StatefulSet provides stable identity and storage patterns.
- DaemonSet runs node-level agents.
- Job runs to completion; CronJob runs on schedule.
- Sidecars share Pod network and volumes with the main container.
- Init containers run before app containers.

## Related Topics

- [3 - Application Deployment](3%20-%20Application%20Deployment.md)
- [5 - Configuration Security Services and Networking](5%20-%20Configuration%20Security%20Services%20and%20Networking.md)

## Official References

- [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Workloads](https://kubernetes.io/docs/concepts/workloads/)
- [Init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)
- [Images](https://kubernetes.io/docs/concepts/containers/images/)
