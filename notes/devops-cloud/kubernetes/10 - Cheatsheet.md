# 10 - Kubernetes Architecture Cheatsheet

## Purpose

Fast revision for Kubernetes architecture, control-plane flow, scheduling, networking, storage, security, and troubleshooting.

Source snapshot: 2026-05-27. Verify version-sensitive behavior against current Kubernetes docs and your distribution.

## One Mental Model

```text
desired state in API
  -> etcd stores truth
  -> controllers reconcile
  -> scheduler places Pods
  -> kubelet runs Pods
  -> CNI gives network
  -> CSI gives storage
  -> Services/DNS expose stable identity
```

## Component Map

| Component | Main job | Common failure clue |
| --- | --- | --- |
| API server | Front door to Kubernetes API | auth, validation, admission, API unavailable |
| etcd | Stores cluster state | control-plane outage, restore needed |
| scheduler | Assigns Pods to Nodes | `FailedScheduling`, Pending no Node |
| controller manager | Reconciles built-in resources | missing Pods/ReplicaSets/endpoints |
| kubelet | Runs assigned Pods on a Node | ContainerCreating, node NotReady |
| container runtime | Pulls/runs containers via CRI | ImagePullBackOff, runtime errors |
| CNI plugin | Pod networking and sometimes NetworkPolicy | Pod network/DNS/policy failures |
| CSI driver | Storage provision/attach/mount | PVC Pending, FailedMount |
| kube-proxy/replacement | Service forwarding | ClusterIP traffic failures |
| CoreDNS | Cluster DNS | DNS NXDOMAIN/timeouts |

## Request Lifecycle

```text
kubectl/client
  -> API server
  -> authentication
  -> authorization
  -> admission/defaulting/validation
  -> etcd persistence
  -> watch events to controllers/scheduler/kubelets
```

## Pod Creation Lifecycle

```text
manifest accepted
  -> admission/defaulting
  -> scheduler binds Node
  -> kubelet observes Pod
  -> CSI volumes
  -> CNI network
  -> image pull
  -> containers start
  -> probes update readiness
  -> EndpointSlice updates
```

## Scheduling Traps

| Symptom | Check |
| --- | --- |
| Pending no Node | `kubectl describe pod`, FailedScheduling |
| Insufficient CPU/memory | requests vs node allocatable |
| Untolerated taint | node taints and Pod tolerations |
| Affinity mismatch | node labels and affinity/selector |
| Volume zone conflict | PVC/PV topology and binding mode |
| Evicted | node pressure, QoS class, requests |

## Networking Traps

| Symptom | Check |
| --- | --- |
| Service no endpoints | selector, Pod labels, readiness |
| DNS fails | CoreDNS Pods/Service, name/namespace, NetworkPolicy |
| Connection refused | app listener and targetPort |
| Timeout | NetworkPolicy, CNI/dataplane, firewall |
| Ingress not routing | controller, host/path rules, backend Service |
| LoadBalancer pending | cloud controller/infrastructure integration |

## Storage Traps

| Symptom | Check |
| --- | --- |
| PVC Pending | StorageClass, provisioner, access mode, quota |
| FailedMount | CSI node plugin, permissions, attach |
| Multi-Attach | RWO volume on multiple nodes |
| Data deleted | reclaim policy |
| Pod cannot write | container user, fsGroup, backend permissions |

## Security Traps

| Symptom | Check |
| --- | --- |
| `Forbidden` | `kubectl auth can-i`, RoleBinding/ClusterRoleBinding |
| Admission rejection | PodSecurity labels, validating/mutating webhooks |
| Secret access too broad | RBAC rules for secrets |
| Wrong cluster changed | `kubectl config current-context` |
| Pod has unneeded API token | ServiceAccount automount settings |

## Command Meanings

```bash
kubectl get pod -o wide
```

Shows status, Pod IP, and Node.

```bash
kubectl describe pod NAME
```

Shows events, probes, volumes, node assignment, and container state.

```bash
kubectl logs NAME --previous
```

Shows previous container logs after restart.

```bash
kubectl get events --sort-by=.lastTimestamp
```

Shows recent event sequence.

```bash
kubectl get endpointslice -l kubernetes.io/service-name=SVC
```

Shows Service backends.

```bash
kubectl auth can-i VERB RESOURCE -n NAMESPACE
```

Tests current identity permissions.

## Small Details That Matter Later

- Spec is desired state; status is observed state.
- `kubectl apply` submits intent; it does not directly run containers.
- Scheduler binds; kubelet runs.
- Requests schedule; limits enforce.
- Pod IPs are unstable; Services provide stable identity.
- Service selectors match Pod labels.
- DNS working does not prove app traffic works.
- NetworkPolicy requires CNI support.
- PVCs are namespaced; PVs are cluster-scoped.
- `storageClassName: ""` disables default dynamic provisioning.
- Base64 Secret data is not encryption.
- RoleBinding can bind ClusterRole namespaced; ClusterRoleBinding is cluster-wide.
- Admission can reject after RBAC allows.
- Events are clues, not the source of truth.

## Fast Troubleshooting Ladder

```text
context correct?
  -> object exists?
  -> auth/admission passed?
  -> controller created children?
  -> Pod scheduled?
  -> kubelet started containers?
  -> volumes mounted?
  -> network configured?
  -> readiness true?
  -> Service has endpoints?
  -> DNS/NetworkPolicy/Ingress ok?
  -> app logs ok?
```

## Exam Answer Frame

When explaining a Kubernetes issue:

```text
The symptom is X. The broken layer is Y. Evidence is Z from command/output. The immediate fix is A. The prevention is B.
```

Example:

```text
The Pod is Pending because scheduler cannot place it. `describe pod` shows untolerated taint. Add the correct toleration if the Pod belongs on that node, or remove/change the taint if the node should accept normal workloads.
```
