# 11 - CKA Glossary

| Term | Meaning | CKA trap |
| --- | --- | --- |
| API server | Front door for Kubernetes API. | If down, normal kubectl fails. |
| etcd | Cluster state store. | No backup means cluster-state loss risk. |
| Scheduler | Assigns unscheduled Pods to nodes. | Pending Pods often reveal scheduling events. |
| Controller | Reconciles desired and actual state. | Controllers do not run containers directly. |
| kubelet | Node agent that runs assigned Pods. | Node-level logs matter. |
| kube-proxy | Implements Service networking. | Service issues may be endpoint or proxy path. |
| CRI | Runtime interface. | Runtime behavior depends on installed runtime. |
| CNI | Network plugin interface. | NetworkPolicy behavior depends on plugin support. |
| CSI | Storage plugin interface. | Dynamic provisioning depends on CSI/provisioner. |
| RBAC | Role-based access control. | Binding scope and subject are common mistakes. |
| Static Pod | Pod manifest watched directly by kubelet. | Control-plane components often run this way in kubeadm. |
| Taint | Node repels Pods. | Needs matching toleration. |
| Affinity | Scheduling preference/requirement. | Required vs preferred matters. |
| PV | Cluster storage resource. | Reclaim policy matters. |
| PVC | Namespaced storage claim. | Bound does not guarantee mounted. |
| EndpointSlice | Service backend endpoint set. | No endpoints means no matched ready Pods. |

## Questions to Test Understanding

1. Which component persists cluster state?
2. Which component starts containers on nodes?
3. What object grants a Role to a ServiceAccount?
4. What usually creates Service endpoints?
5. What should you inspect when a Pod is Pending?

## Answers and Reasoning

1. etcd.
2. kubelet through the container runtime.
3. RoleBinding.
4. EndpointSlice controller based on Service selector and ready Pods.
5. `kubectl describe pod` events, node resources, taints, affinity, PVCs, and scheduler clues.

