# 0 - Kubernetes Beginner Foundation

## Quick Summary
- CKAD is about running applications on Kubernetes, so the most important beginner concepts are Pod, container image, Deployment, Service, ConfigMap, Secret, probe, resource request, and namespace.
- Kubernetes does not replace application design. Your app still needs good startup behavior, logging, health endpoints, configuration, and graceful shutdown.
- A CKAD candidate must understand what each manifest field does, not only memorize commands.
- The safest learning path is: Pod -> Deployment -> Service -> ConfigMap/Secret -> probes -> resources -> rollout -> debugging.
- For deeper cluster internals, also read [CKA 0 - Kubernetes Beginner Foundation](../Certified%20Kubernetes%20Administrator/0%20-%20Kubernetes%20Beginner%20Foundation.md).

## Why This Note Exists
CKAD notes often jump straight into manifests. That is hard if you do not yet understand what Kubernetes is trying to do for the application.

This note explains Kubernetes from the application developer point of view.

## The CKAD Mental Model
As an application developer, your job is to package and describe the application correctly.

You provide:
- Container image.
- Command and arguments if needed.
- Environment variables.
- ConfigMaps and Secrets.
- Ports.
- Health checks.
- CPU and memory requests.
- Deployment strategy.
- Service exposure.
- Debugging evidence when it fails.

Kubernetes provides:
- Scheduling.
- Restarting failed containers.
- Rolling updates.
- Service discovery.
- Config injection.
- Resource isolation.
- Access control hooks.

## From Source Code To Running Pod
The path usually looks like this:

```text
Source code -> Dockerfile -> container image -> image registry -> Kubernetes manifest -> Pod
```

Kubernetes starts from the image. It does not normally compile your app or build your image.

## Image
An image is a packaged filesystem and startup metadata.

Good image practices:
- Use a specific version tag.
- Keep image small.
- Run as non-root when possible.
- Do not bake secrets into the image.
- Log to stdout/stderr.
- Include only runtime dependencies.

Bad:

```yaml
image: myapp:latest
```

Better for production:

```yaml
image: myregistry.example.com/myapp:1.4.2
```

## Pod
A Pod is the unit Kubernetes schedules.

Most CKAD tasks use Pods either directly or through controllers.

Example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web
spec:
  containers:
    - name: web
      image: nginx:1.27
      ports:
        - containerPort: 80
```

For production-style applications, use a Deployment instead of a standalone Pod.

## Deployment
A Deployment manages stateless application replicas.

It gives you:
- Replica count.
- Rolling updates.
- Rollbacks.
- Self-healing through ReplicaSets.

Example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: nginx:1.27
          ports:
            - containerPort: 80
```

The `template` is the Pod template. Kubernetes creates Pods from it.

## Labels and Selectors
Labels connect objects.

Service selects Pods:

```yaml
selector:
  app: web
```

Pod label:

```yaml
labels:
  app: web
```

If these do not match, traffic will not reach the Pods.

Command:

```bash
kubectl get pods --show-labels
```

## Service
A Service gives stable access to Pods.

Example:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 80
```

Port fields:
- `port`: Service port.
- `targetPort`: container port on the Pod.
- `nodePort`: external node port only for NodePort Services.

## ConfigMap
A ConfigMap stores non-secret app configuration.

Example:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  LOG_LEVEL: info
  FEATURE_X: "true"
```

Use as environment variables:

```yaml
envFrom:
  - configMapRef:
      name: app-config
```

## Secret
A Secret stores sensitive configuration.

Example:

```bash
kubectl create secret generic db-secret --from-literal=PASSWORD=change-me
```

Use as environment variable:

```yaml
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: db-secret
        key: PASSWORD
```

Do not commit real secrets into Git.

## Commands and Args
Docker image startup values can be overridden.

Kubernetes fields:
- `command` overrides image ENTRYPOINT.
- `args` overrides image CMD.

Example:

```yaml
containers:
  - name: worker
    image: busybox:1.36
    command: ["sh", "-c"]
    args: ["echo hello && sleep 3600"]
```

Beginner warning:
- If command/args are wrong, the container may exit immediately and enter CrashLoopBackOff.

## Probes
Probes tell Kubernetes how the app is doing.

| Probe | Question |
|---|---|
| startupProbe | Has the app finished starting? |
| readinessProbe | Can this Pod receive traffic? |
| livenessProbe | Is this container stuck and should it restart? |

Example:

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
```

Use readiness first. It prevents traffic from going to a Pod that is not ready.

## Resource Requests and Limits
Requests help the scheduler place Pods. Limits cap usage.

Example:

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "500m"
    memory: "512Mi"
```

If memory usage exceeds the limit, the container may be killed with OOMKilled.

## Volumes
Use volumes when the container needs files beyond its image.

Common CKAD volume types:
- `emptyDir`: temporary shared storage in a Pod.
- `configMap`: mount config files.
- `secret`: mount secret files.
- `persistentVolumeClaim`: persistent storage request.

Example `emptyDir` shared between containers:

```yaml
volumes:
  - name: work
    emptyDir: {}
containers:
  - name: app
    image: busybox
    volumeMounts:
      - name: work
        mountPath: /work
```

## Rollouts
Deployments support rolling updates.

Commands:

```bash
kubectl set image deployment/web web=nginx:1.27
kubectl rollout status deployment/web
kubectl rollout history deployment/web
kubectl rollout undo deployment/web
```

Always verify after a rollout:

```bash
kubectl get deploy
kubectl get pods
kubectl describe deploy web
```

## Jobs and CronJobs
Use a Job for finite work.

Examples:
- Data migration.
- One-time batch task.
- Report generation.

Use a CronJob for scheduled finite work.

Examples:
- Nightly cleanup.
- Scheduled report.
- Periodic sync.

Do not use a Deployment for a task that should finish and stop.

## Namespaces
Namespaces separate resources.

Commands:

```bash
kubectl get pods -n dev
kubectl create namespace dev
kubectl config set-context --current --namespace=dev
```

CKAD exam habit:
- Always check the namespace in the question.

## Debugging Flow For Developers
### Pod Does Not Start
```bash
kubectl get pods
kubectl describe pod <pod>
kubectl logs <pod>
kubectl logs <pod> --previous
```

Common causes:
- Wrong image name.
- Private image pull secret missing.
- Wrong command.
- App exits immediately.
- Missing ConfigMap or Secret.
- Resource limit too low.

### Service Gets No Traffic
```bash
kubectl get svc
kubectl get endpoints
kubectl get pods --show-labels
kubectl describe svc <service>
```

Common causes:
- Selector does not match Pod labels.
- Pod not Ready.
- Wrong targetPort.
- NetworkPolicy blocks traffic.

### Config Does Not Appear
```bash
kubectl describe pod <pod>
kubectl get configmap <name> -o yaml
kubectl get secret <name> -o yaml
```

Common causes:
- Wrong key name.
- Wrong namespace.
- ConfigMap/Secret was created after Pod and needs restart depending on usage.
- Mounted file path does not match app expectation.

## Manifest Reading Checklist
When reading a Kubernetes YAML file, ask:
- What is the `kind`?
- What namespace does it use?
- What labels does it set?
- What selector does it use?
- What image runs?
- What command and args run?
- What ports are declared?
- What config and secrets are referenced?
- What probes exist?
- What resources are requested/limited?
- What volume mounts exist?

## Common CKAD Beginner Mistakes
- Forgetting namespace.
- Confusing `port` and `targetPort`.
- Creating a Service whose selector matches no Pods.
- Putting secrets into ConfigMaps.
- Using a Deployment for a one-time job.
- Forgetting that `command` and `args` override image defaults.
- Not checking `kubectl describe` events.
- Fixing YAML but not applying it.
- Applying YAML but not verifying the final state.

## Official References
- [Kubernetes Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Kubernetes ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [Kubernetes probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- [kubectl quick reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
