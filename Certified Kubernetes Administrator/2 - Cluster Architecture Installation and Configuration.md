# 2 - Cluster Architecture Installation and Configuration

## Quick Summary

A Kubernetes cluster has a control plane that makes decisions and worker nodes that run workloads. CKA expects you to understand the main components, manage access with RBAC, know kubeadm-based cluster lifecycle tasks, understand high availability concepts, and recognize extension points such as CNI, CSI, CRI, CRDs, and operators.

## Beginner Bridge

Before memorizing component names, understand the request flow:

```text
You run kubectl
  -> kube-apiserver receives the request
  -> admission/RBAC checks decide whether it is allowed
  -> etcd stores the desired state
  -> scheduler chooses a node when a Pod needs placement
  -> kubelet on that node starts containers through the runtime
  -> controllers keep checking whether reality matches the desired state
```

The control plane does not directly "SSH into a node and run your app." It records desired state and coordinates components. The kubelet on each node is the local agent that actually makes containers run.

Read this note with one question in mind: which component owns this responsibility?

## Core Components

| Component | Runs On | Purpose |
| --- | --- | --- |
| kube-apiserver | Control plane | Front door of the cluster API. |
| etcd | Control plane | Strongly consistent key-value store for cluster state. |
| kube-scheduler | Control plane | Assigns Pods to nodes. |
| kube-controller-manager | Control plane | Runs controllers that reconcile desired state. |
| cloud-controller-manager | Control plane, when cloud integration is used | Integrates cluster with cloud provider resources. |
| kubelet | Every node | Talks to API server and manages containers on the node. |
| kube-proxy | Usually every node | Implements Service networking using rules or proxying mechanisms. |
| container runtime | Every node | Runs containers through CRI, such as containerd. |

## Mental Model

```text
kubectl -> kube-apiserver -> stored in etcd
                          -> scheduler assigns Pods
                          -> kubelet starts containers
                          -> controllers keep desired state true
```

Kubernetes is declarative. You submit the desired state. Controllers continuously work to make the actual state match it.

## kube-apiserver

The API server:

- Validates requests.
- Authenticates users/service accounts.
- Authorizes actions.
- Runs admission control.
- Reads/writes cluster state in etcd.

If the API server is down, normal `kubectl` operations fail.

Troubleshooting checks:

```bash
kubectl cluster-info
kubectl get --raw=/readyz
```

On kubeadm control-plane nodes, static Pod manifests often live in:

```text
/etc/kubernetes/manifests/
```

## etcd

etcd stores cluster state. Losing etcd without a backup can mean losing the cluster state.

Key points:

- Back up etcd regularly.
- Protect etcd certificates and data directory.
- Use an odd number of members for quorum in HA designs.
- Monitor disk latency and health.

Common backup shape:

```bash
ETCDCTL_API=3 etcdctl snapshot save snapshot.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key
```

Exact paths vary by installation.

## kube-scheduler

The scheduler chooses a node for unscheduled Pods.

It considers:

- Resource requests.
- Node selectors.
- Node affinity and anti-affinity.
- Taints and tolerations.
- Topology spread constraints.
- Pod requirements and plugin scoring.

If a Pod is `Pending`, check scheduler-related events:

```bash
kubectl describe pod <pod>
kubectl get events --sort-by=.lastTimestamp
```

## kube-controller-manager

Controllers reconcile desired and actual state.

Examples:

- Deployment controller.
- ReplicaSet controller.
- Node controller.
- Job controller.
- EndpointSlice controller.
- ServiceAccount controller.

If controllers are unhealthy, resources may stop reconciling.

## kubelet

kubelet runs on each node and manages Pods assigned to that node.

It:

- Watches for assigned Pods.
- Starts containers through the container runtime.
- Runs liveness/readiness/startup probes.
- Reports node and Pod status.
- Mounts volumes.

Useful commands on a node:

```bash
systemctl status kubelet
journalctl -u kubelet -xe
```

## Container Runtime And CRI

Kubernetes uses the Container Runtime Interface (CRI) to talk to runtimes.

Common runtime:

- containerd.

Useful command:

```bash
crictl ps
crictl images
crictl logs <container-id>
```

## CNI, CSI, CRI

| Interface | Full Name | Purpose |
| --- | --- | --- |
| CNI | Container Network Interface | Pod networking. |
| CSI | Container Storage Interface | Storage plugins and volume provisioning. |
| CRI | Container Runtime Interface | Runtime integration. |

Important: Kubernetes provides interfaces, but the exact behavior depends on the installed plugin.

## RBAC

RBAC controls who can do what.

Main objects:

| Object | Scope | Purpose |
| --- | --- | --- |
| Role | Namespace | Permissions inside one namespace. |
| ClusterRole | Cluster-wide or reusable | Permissions across cluster or reusable for RoleBinding. |
| RoleBinding | Namespace | Grants Role/ClusterRole to a subject in one namespace. |
| ClusterRoleBinding | Cluster-wide | Grants ClusterRole across cluster. |

Subjects:

- User.
- Group.
- ServiceAccount.

Example:

```bash
kubectl create role pod-reader \
  --verb=get,list,watch \
  --resource=pods \
  -n dev

kubectl create rolebinding read-pods \
  --role=pod-reader \
  --serviceaccount=dev:app-sa \
  -n dev
```

Check access:

```bash
kubectl auth can-i list pods -n dev --as=system:serviceaccount:dev:app-sa
kubectl auth can-i create deployments -n dev
```

## Admission Control

Admission controllers run after authentication and authorization but before an object is persisted.

They can:

- Validate requests.
- Mutate objects.
- Enforce policy.

Examples:

- NamespaceLifecycle.
- ResourceQuota.
- LimitRanger.
- MutatingAdmissionWebhook.
- ValidatingAdmissionWebhook.

## kubeadm Cluster Lifecycle

kubeadm is a common tool for bootstrapping Kubernetes clusters.

Common tasks:

```bash
# Initialize first control-plane node
kubeadm init

# Join a worker node
kubeadm join <endpoint> --token <token> --discovery-token-ca-cert-hash <hash>

# Show join command again
kubeadm token create --print-join-command

# Upgrade plan
kubeadm upgrade plan

# Apply upgrade
kubeadm upgrade apply <version>
```

Before upgrades:

- Read release notes.
- Back up etcd.
- Check version skew policy.
- Drain nodes safely.
- Upgrade control plane before workers.

## Draining Nodes

Drain a node before maintenance:

```bash
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data
```

Bring it back:

```bash
kubectl uncordon <node>
```

`cordon` prevents new Pods from scheduling:

```bash
kubectl cordon <node>
```

## High Availability Control Plane

An HA control plane usually includes:

- Multiple control-plane nodes.
- Multiple etcd members or external etcd cluster.
- Load-balanced API server endpoint.
- Reliable certificates and bootstrap configuration.

Key risk: etcd quorum. If too many etcd members fail, the cluster cannot safely write state.

## Helm And Kustomize

Helm packages Kubernetes applications as charts.

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install my-nginx bitnami/nginx
helm list
```

Kustomize overlays YAML without templating.

```bash
kubectl apply -k ./overlays/prod
```

Use Helm for packaged applications and Kustomize for environment-specific overlays.

## CRDs And Operators

CRD means CustomResourceDefinition. It extends the Kubernetes API with new resource types.

Operator pattern:

```text
CRD defines a new API type
Custom resource describes desired state
Controller/operator reconciles actual state
```

Example:

- `Prometheus` custom resource managed by Prometheus Operator.
- `Certificate` custom resource managed by cert-manager.

## Benefits

- Kubernetes components have clear responsibilities.
- Declarative APIs make automation and GitOps possible.
- RBAC supports least privilege.
- Extension interfaces allow many networking, storage, runtime, and operator options.

## Drawbacks / Limitations

- Many components mean more failure points.
- Cluster lifecycle work requires careful version and certificate management.
- RBAC errors can look like application failures.
- Operators add power but also add controllers that must be monitored.

## Hidden Details / Caveats

- Static Pods are managed by kubelet directly from manifest files, not by a normal controller.
- If a static Pod manifest has invalid YAML, the component may disappear.
- `kubectl auth can-i` checks authorization, not whether the action will succeed after admission.
- ClusterRole can be bound inside a namespace using RoleBinding.
- kubelet problems often show up as Node `NotReady` or Pods stuck in `ContainerCreating`.

## Common Mistakes

- Granting `cluster-admin` instead of least privilege.
- Forgetting to back up etcd before risky cluster changes.
- Draining a node without considering PodDisruptionBudgets.
- Ignoring version skew rules during upgrade planning.
- Installing CRDs without understanding their controllers.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| `kubectl` cannot connect | Context, kubeconfig, API server health, network path. |
| Pods stuck `Pending` | Scheduler, resources, taints, affinity, PVC binding. |
| Node `NotReady` | kubelet, container runtime, CNI, disk/memory pressure. |
| RBAC forbidden error | Role/ClusterRole and binding subject/namespace. |
| Control-plane component down | Static Pod manifest, kubelet logs, container runtime logs. |

## Interview Notes

- API server is the entry point for Kubernetes API operations.
- etcd stores cluster state.
- Scheduler assigns Pods to nodes.
- kubelet runs Pods on nodes.
- Controllers reconcile actual state toward desired state.
- RBAC uses Roles/ClusterRoles plus RoleBindings/ClusterRoleBindings.
- CNI handles networking, CSI handles storage, CRI handles runtime integration.

## Related Topics

- [3 - Workloads and Scheduling](3%20-%20Workloads%20and%20Scheduling.md)
- [6 - Troubleshooting](6%20-%20Troubleshooting.md)

## Official References

- [Kubernetes components](https://kubernetes.io/docs/concepts/overview/components/)
- [Kubernetes API overview](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
- [RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [kubeadm documentation](https://kubernetes.io/docs/reference/setup-tools/kubeadm/)
