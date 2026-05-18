# 0 - Kubernetes Beginner Foundation

## Quick Summary
- Kubernetes runs containers across a group of machines called a cluster.
- A cluster has control plane components that make decisions and worker nodes that run application containers.
- The smallest deployable unit is usually a Pod, not a single container.
- You describe the desired state in YAML, send it to the Kubernetes API, and controllers work to make the real state match.
- Most Kubernetes learning becomes easier once you understand these words: cluster, node, Pod, Deployment, Service, namespace, label, selector, volume, RBAC, and controller.

## Why This Note Exists
Kubernetes documentation and exam notes often assume you already understand containers, networking, Linux processes, and YAML.

This note starts from the beginner level.

Read this before the CKA or CKAD domain notes if Kubernetes feels confusing. After this note, the rest of the Kubernetes notes should feel like deeper chapters instead of random vocabulary.

## The Problem Kubernetes Solves
Imagine you have a web application packaged as a container image.

Running one container manually is easy:

```bash
docker run nginx
```

But production has harder questions:
- What if the container crashes?
- What if you need 5 copies?
- What if one server dies?
- How do users reach the right container?
- How do you update the application without downtime?
- How do you pass configuration and secrets?
- How do you attach storage?
- How do you restrict permissions?
- How do you debug the system?

Kubernetes solves these orchestration problems.

## Kubernetes In One Sentence
Kubernetes is a system where you declare how applications should run, and Kubernetes continuously tries to make the real cluster match that declaration.

Example:

```text
You say: "Run 3 copies of nginx."
Kubernetes checks: "Only 2 are running."
Kubernetes acts: "Start 1 more."
```

This is called desired state management.

## Cluster
A cluster is the whole Kubernetes environment.

It includes:
- Control plane: the brain of the cluster.
- Worker nodes: machines that run application Pods.
- Networking: lets Pods and Services communicate.
- Storage integrations: lets Pods use persistent storage.

Simple picture:

```text
Kubernetes Cluster
  Control Plane
    API Server
    Scheduler
    Controllers
    etcd

  Worker Node 1
    kubelet
    container runtime
    Pods

  Worker Node 2
    kubelet
    container runtime
    Pods
```

## Node
A node is a machine in the cluster.

It can be:
- A virtual machine.
- A physical server.
- A cloud instance.

Worker node components:
- kubelet: talks to the control plane and manages Pods on the node.
- container runtime: runs containers.
- kube-proxy or equivalent networking component: helps implement Service networking.

Check nodes:

```bash
kubectl get nodes -o wide
kubectl describe node <node-name>
```

## Control Plane
The control plane is the decision-making part of Kubernetes.

Important components:

| Component | Beginner explanation |
|---|---|
| kube-apiserver | Front door of Kubernetes. `kubectl` talks to this. |
| etcd | Cluster database that stores desired state and current state. |
| kube-scheduler | Chooses which node should run a new Pod. |
| kube-controller-manager | Runs controllers that repair drift from desired state. |
| cloud-controller-manager | Integrates with cloud provider features such as load balancers and disks. |

## Kubernetes API
Almost everything in Kubernetes is an API object.

Examples:
- Pod.
- Deployment.
- Service.
- ConfigMap.
- Secret.
- PersistentVolumeClaim.
- Role.
- Namespace.

You usually create or update objects using YAML:

```bash
kubectl apply -f app.yaml
```

Kubernetes stores the desired state, then controllers work on it.

## YAML Basics
Kubernetes manifests are usually YAML files.

Example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  containers:
    - name: nginx
      image: nginx:1.27
      ports:
        - containerPort: 80
```

Important fields:

| Field | Meaning |
|---|---|
| `apiVersion` | Which API version defines this object |
| `kind` | Type of object, such as Pod or Deployment |
| `metadata` | Name, namespace, labels, annotations |
| `spec` | Desired state you want |
| `status` | Current state reported by Kubernetes |

You write `spec`. Kubernetes writes `status`.

## Pod
A Pod is the smallest deployable unit in Kubernetes.

A Pod can contain:
- One container.
- Multiple tightly coupled containers.
- Shared network namespace.
- Shared volumes.

Most beginner examples use one container per Pod.

Important: you normally do not create standalone Pods for production apps. You use a Deployment, Job, StatefulSet, or DaemonSet to manage Pods.

## Container
A container is a running process from an image.

Kubernetes does not build your image by default. You build and push the image separately, then Kubernetes pulls it.

Flow:

```text
Dockerfile -> image -> registry -> Kubernetes Pod pulls image -> container runs
```

Common image registries:
- Docker Hub.
- Amazon ECR.
- Google Artifact Registry.
- Azure Container Registry.
- Private registries.

## Deployment
A Deployment manages replicas of an application.

You say:

```text
Run 3 replicas of this app image.
```

The Deployment creates a ReplicaSet. The ReplicaSet creates Pods.

```text
Deployment -> ReplicaSet -> Pods
```

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
        - name: nginx
          image: nginx:1.27
          ports:
            - containerPort: 80
```

Notice that the selector and Pod labels match:

```yaml
selector:
  matchLabels:
    app: web
template:
  metadata:
    labels:
      app: web
```

If labels and selectors do not match, the Deployment cannot manage the Pods correctly.

## ReplicaSet
A ReplicaSet makes sure a certain number of Pods exist.

You rarely manage ReplicaSets directly. Deployments manage them for you.

During a rolling update:

```text
Old ReplicaSet: nginx:1.26
New ReplicaSet: nginx:1.27
```

Kubernetes gradually scales the new one up and the old one down.

## Service
Pods are temporary. Their IP addresses can change.

A Service gives stable networking in front of Pods.

```text
Client -> Service stable name/IP -> matching Pods
```

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

The Service finds Pods using labels.

If the Service selector is `app: web`, it sends traffic to Pods with label `app=web`.

## Service Types
| Type | Beginner explanation |
|---|---|
| ClusterIP | Internal-only stable service inside the cluster |
| NodePort | Opens a port on each node |
| LoadBalancer | Asks cloud provider for an external load balancer |
| ExternalName | DNS alias to an external name |

For most internal communication, use ClusterIP.

For cloud public traffic, LoadBalancer or Ingress/Gateway is common.

## Ingress and Gateway API
Services expose network endpoints. Ingress and Gateway API manage HTTP routing.

Ingress example idea:

```text
app.example.com/api -> api-service
app.example.com/web -> web-service
```

Important:
- Ingress is only a Kubernetes API object.
- You need an Ingress controller to make it work.
- Gateway API is a newer, more expressive networking API family.

## Namespace
A namespace divides cluster resources into logical groups.

Examples:
- `default`
- `kube-system`
- `dev`
- `staging`
- `prod`

Use namespaces for:
- Separating teams.
- Separating environments.
- Applying quotas.
- Applying RBAC.
- Reducing clutter.

Commands:

```bash
kubectl get pods -n prod
kubectl get pods -A
kubectl config set-context --current --namespace=prod
```

## Labels and Selectors
Labels are key-value tags on Kubernetes objects.

Example:

```yaml
metadata:
  labels:
    app: web
    env: prod
```

Selectors find objects by labels.

Services use selectors to find Pods. Deployments use selectors to manage Pods.

Common command:

```bash
kubectl get pods -l app=web
```

Beginner rule: when traffic does not reach Pods, check labels and selectors early.

## ConfigMap
A ConfigMap stores non-secret configuration.

Examples:
- Log level.
- Feature flag.
- Config file.
- Environment name.

Example:

```bash
kubectl create configmap app-config --from-literal=LOG_LEVEL=info
```

Use it in a Pod as environment variables or files.

Do not store passwords in ConfigMaps.

## Secret
A Secret stores sensitive values such as passwords and tokens.

Example:

```bash
kubectl create secret generic db-secret --from-literal=PASSWORD=change-me
```

Important:
- Kubernetes Secrets are base64-encoded by default, not magically secure in every setup.
- Enable encryption at rest for production clusters.
- Restrict access with RBAC.
- Prefer external secret managers in mature environments.

## Volumes
Containers have ephemeral file systems. If a container is replaced, local files can disappear.

Volumes let Pods use storage.

Common types:
- `emptyDir`: temporary storage for a Pod lifetime.
- `configMap`: mount ConfigMap as files.
- `secret`: mount Secret as files.
- `persistentVolumeClaim`: request persistent storage.

## PersistentVolume, PersistentVolumeClaim, StorageClass
For persistent storage, Kubernetes separates the app request from the actual storage backend.

| Object | Meaning |
|---|---|
| PersistentVolume | Actual storage resource |
| PersistentVolumeClaim | Request for storage by a Pod |
| StorageClass | Defines how storage is dynamically provisioned |

Mental model:

```text
Pod asks for PVC -> PVC binds to PV -> PV maps to real storage
```

In cloud clusters, a StorageClass can dynamically create disks.

## Scheduling
Scheduling means choosing which node should run a Pod.

The scheduler considers:
- CPU/memory requests.
- Node availability.
- Taints and tolerations.
- Node selectors and affinity.
- Pod affinity/anti-affinity.
- Volume constraints.

If a Pod is Pending, scheduling is one of the first things to inspect:

```bash
kubectl describe pod <pod>
```

Look at Events.

## Requests and Limits
Containers can declare resource requests and limits.

Requests:
- What the scheduler uses to place Pods.
- "I need at least this much CPU/memory."

Limits:
- Maximum the container can use.
- "Do not let me use more than this."

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

Beginner warning:
- Memory over limit can cause OOMKilled.
- CPU over limit is throttled, not killed.

## Probes
Probes let Kubernetes check container health.

Types:
- Startup probe: has the app started yet?
- Readiness probe: should this Pod receive traffic?
- Liveness probe: should Kubernetes restart this container?

Use readiness for traffic control.
Use liveness carefully because a bad liveness probe can restart healthy apps.

## RBAC
RBAC means Role-Based Access Control.

It controls who can do what.

Core objects:
- Role: permissions inside one namespace.
- ClusterRole: permissions cluster-wide or reusable across namespaces.
- RoleBinding: grants Role/ClusterRole to a subject in a namespace.
- ClusterRoleBinding: grants ClusterRole cluster-wide.

Example idea:

```text
ServiceAccount "builder" can get/list/watch Pods in namespace "dev"
```

RBAC answers:
- Can this user create Deployments?
- Can this ServiceAccount read Secrets?
- Can this controller watch Pods?

## ServiceAccount
A ServiceAccount is an identity for Pods and controllers.

Human users authenticate differently. Workloads usually use ServiceAccounts.

Example:

```yaml
spec:
  serviceAccountName: app-runner
```

Use RBAC to grant the ServiceAccount only the permissions it needs.

## NetworkPolicy
By default, many Kubernetes clusters allow broad Pod-to-Pod communication.

NetworkPolicy lets you restrict traffic.

Example goal:

```text
Only web Pods can talk to api Pods on port 8080.
Only api Pods can talk to database Pods on port 5432.
```

Important:
- NetworkPolicy requires a CNI plugin that enforces it.
- If the network plugin does not support enforcement, policies may not work.

## CNI, CSI, and CRI
These acronyms appear often.

| Acronym | Full name | What it handles |
|---|---|---|
| CNI | Container Network Interface | Pod networking |
| CSI | Container Storage Interface | Storage plugins |
| CRI | Container Runtime Interface | Container runtime integration |

Beginner memory:
- CNI = network.
- CSI = storage.
- CRI = runtime.

## Controllers
Controllers watch the Kubernetes API and make changes.

Example:
- Deployment controller sees desired replicas = 3.
- Current replicas = 2.
- It creates another Pod through a ReplicaSet.

This watch-and-reconcile loop is central to Kubernetes.

## `kubectl`
`kubectl` is the command-line tool for Kubernetes.

Common commands:

```bash
kubectl get pods
kubectl describe pod <pod>
kubectl logs <pod>
kubectl exec -it <pod> -- sh
kubectl apply -f file.yaml
kubectl delete -f file.yaml
kubectl explain deployment.spec
```

Use `get` for summary, `describe` for details/events, `logs` for app output, and `exec` to run commands inside a container.

## Events
Events explain what Kubernetes tried to do.

Examples:
- Image pull failed.
- Pod scheduled.
- Volume mount failed.
- Container restarted.

Check events:

```bash
kubectl get events --sort-by=.lastTimestamp
kubectl describe pod <pod>
```

## Common Object Relationships
### Deployment to Pod to Service
```text
Deployment creates ReplicaSet
ReplicaSet creates Pods
Service selects Pods by label
Ingress/Gateway routes HTTP to Service
```

### Pod to Config
```text
Pod reads ConfigMap for non-secret config
Pod reads Secret for secret config
```

### Pod to Storage
```text
Pod uses PVC
PVC binds to PV
PV is backed by real storage
```

### Pod to Identity
```text
Pod uses ServiceAccount
ServiceAccount gets permissions through RBAC binding
```

## First Debugging Flow
When something does not work, do not guess. Walk the chain.

### Pod Not Running
```bash
kubectl get pods -o wide
kubectl describe pod <pod>
kubectl logs <pod>
kubectl logs <pod> --previous
```

Look for:
- Pending.
- ImagePullBackOff.
- CrashLoopBackOff.
- OOMKilled.
- Failed mounts.
- Failed scheduling.

### Service Not Working
```bash
kubectl get svc
kubectl get endpoints
kubectl get pods --show-labels
kubectl describe svc <service>
```

Look for:
- Service selector mismatch.
- Pods not Ready.
- Wrong targetPort.
- NetworkPolicy blocking traffic.

### Storage Not Working
```bash
kubectl get pvc
kubectl describe pvc <pvc>
kubectl describe pod <pod>
```

Look for:
- PVC Pending.
- StorageClass missing.
- Access mode mismatch.
- Volume mount failure.

## Tiny End-to-End Example
Create a Deployment:

```bash
kubectl create deployment web --image=nginx:1.27 --replicas=2
```

Expose it inside the cluster:

```bash
kubectl expose deployment web --port=80 --target-port=80
```

Inspect:

```bash
kubectl get deployment
kubectl get rs
kubectl get pods -o wide
kubectl get svc
```

What happened:
1. Deployment desired state says 2 nginx replicas.
2. ReplicaSet creates 2 Pods.
3. Service finds Pods with matching labels.
4. Other Pods can reach the Service by name.

## Vocabulary Cheat Sheet
| Term | Simple meaning |
|---|---|
| Cluster | Whole Kubernetes environment |
| Node | Machine that runs cluster workloads |
| Control plane | Brain of Kubernetes |
| Pod | Smallest deployable unit |
| Container | Running process from an image |
| Image | Packaged application filesystem and metadata |
| Deployment | Manages stateless replicated Pods |
| ReplicaSet | Maintains Pod count for a Deployment |
| Service | Stable network endpoint for Pods |
| Ingress | HTTP routing rule, needs controller |
| Namespace | Logical grouping inside cluster |
| Label | Key-value tag |
| Selector | Query that matches labels |
| ConfigMap | Non-secret configuration |
| Secret | Sensitive configuration |
| PVC | Storage request |
| PV | Storage resource |
| StorageClass | Dynamic storage provisioning class |
| RBAC | Permission model |
| ServiceAccount | Identity for Pods |
| CNI | Pod networking plugin interface |
| CSI | Storage plugin interface |
| CRI | Runtime plugin interface |

## How To Read The Other Kubernetes Notes
- Read [1 - Exam Overview and Study Plan](1%20-%20Exam%20Overview%20and%20Study%20Plan.md) for exam structure.
- Read [2 - Cluster Architecture Installation and Configuration](2%20-%20Cluster%20Architecture%20Installation%20and%20Configuration.md) after you understand control plane, node, kubelet, and RBAC.
- Read [3 - Workloads and Scheduling](3%20-%20Workloads%20and%20Scheduling.md) after you understand Pod, Deployment, labels, and resources.
- Read [4 - Services and Networking](4%20-%20Services%20and%20Networking.md) after you understand Service, labels, DNS, and Pod networking.
- Read [5 - Storage](5%20-%20Storage.md) after you understand volumes, PVCs, PVs, and StorageClasses.
- Read [6 - Troubleshooting](6%20-%20Troubleshooting.md) once you can inspect Pods, Services, events, and logs.

## Common Beginner Mistakes
- Thinking a Pod is the same thing as a container.
- Creating a Pod directly when a Deployment is needed.
- Forgetting that Services find Pods using labels.
- Changing Pod labels so the Service selector no longer matches.
- Treating a ConfigMap as a secret store.
- Assuming Kubernetes builds Docker images automatically.
- Ignoring Events in `kubectl describe`.
- Forgetting namespaces when looking for resources.
- Giving broad RBAC permissions to solve errors quickly.
- Using liveness probes before understanding readiness probes.

## Official References
- [Kubernetes overview](https://kubernetes.io/docs/concepts/overview/)
- [Kubernetes components](https://kubernetes.io/docs/concepts/overview/components/)
- [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Storage](https://kubernetes.io/docs/concepts/storage/)
- [RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [kubectl quick reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
