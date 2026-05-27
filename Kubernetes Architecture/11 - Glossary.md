# 11 - Kubernetes Architecture Glossary

## Purpose

Practical glossary for Kubernetes architecture terms. Definitions focus on how each term helps you understand, debug, or design clusters.

Source snapshot: 2026-05-27.

## Terms

### Admission Controller

API server component that mutates or validates requests after authentication and authorization but before persistence.

Small detail: admission can reject an object even when RBAC allows the user to create it.

### API Server

The Kubernetes control-plane front door. All normal cluster state changes go through it.

### CNI

Container Network Interface. Plugin interface used to set up Pod networking and, depending on plugin, NetworkPolicy enforcement.

### CSI

Container Storage Interface. Standard interface used by storage drivers for provisioning, attach, mount, and related storage operations.

### ClusterIP

Internal virtual IP assigned to a Service.

Small detail: ClusterIP is stable for the Service lifetime, but if the Service is deleted and recreated it may change.

### Controller

A process that watches Kubernetes objects and acts to make actual state match desired state.

### Desired State

What the user or controller declares in object specs.

### EndpointSlice

Object that lists backend endpoints for a Service in a scalable way.

Small detail: Services route to endpoints, not to Deployments directly.

### etcd

Distributed key-value store used by Kubernetes to persist cluster state.

### kube-proxy

Node component that implements Service forwarding in many clusters, commonly through iptables or IPVS. Some clusters replace its role with CNI/eBPF dataplanes.

### kube-scheduler

Control-plane component that assigns unscheduled Pods to Nodes.

Small detail: it does not start containers.

### kubelet

Node agent that watches assigned Pods and asks the runtime, CNI, and CSI components to make them real locally.

### Namespace

Logical partition for namespaced resources.

Small detail: namespaces are API boundaries, not hard security sandboxes by themselves.

### NetworkPolicy

Object that controls allowed Pod traffic when the CNI plugin enforces it.

### Node

Worker machine in the cluster. It runs kubelet, container runtime, and networking/storage node components.

### PersistentVolume

Cluster-scoped storage resource representing actual storage.

### PersistentVolumeClaim

Namespaced request for storage. Pods usually mount PVCs, not PVs directly.

### Pod

Smallest deployable unit in Kubernetes. One or more containers sharing network namespace, volumes, and lifecycle.

### Pod IP

Network address assigned to a Pod by cluster networking.

Small detail: Pod IPs are not stable service identities.

### Reconciliation

The repeated process of comparing desired state to actual state and acting to reduce the difference.

### ReplicaSet

Controller object that maintains a specified number of matching Pods. Deployments manage ReplicaSets.

### Resource Limit

Maximum CPU/memory use enforced at runtime.

### Resource Request

Declared CPU/memory need used by scheduler placement.

### Role

Namespaced RBAC permission object.

### RoleBinding

Namespaced binding that grants a Role or ClusterRole to subjects inside a namespace.

### Secret

Kubernetes object for sensitive values.

Small detail: base64 in Secret YAML is encoding, not encryption.

### Service

Stable network abstraction over Pods/endpoints.

### ServiceAccount

Kubernetes identity for Pods and controllers.

### Spec

Desired state portion of an object.

### Status

Observed state reported by controllers, kubelet, or other components.

### StorageClass

Defines dynamic storage provisioning behavior.

### Taint

Node rule that repels Pods unless they tolerate it.

### Toleration

Pod permission to schedule onto a tainted Node.

Small detail: toleration permits placement but does not force placement.

### VolumeBindingMode

StorageClass setting that influences when volume binding/provisioning happens.

Small detail: `WaitForFirstConsumer` helps align storage with Pod scheduling topology.

## Small Details That Matter Later

- API groups matter in RBAC rules.
- Resource names are plural in many RBAC rules.
- Pod phase is coarse; container state and events are more diagnostic.
- EndpointSlices are often better to inspect than legacy Endpoints in larger clusters.
- Node conditions explain many scheduling and eviction behaviors.
- Admission webhooks can be cluster-critical; bad webhook availability can block API writes.
- A ServiceAccount token inside a Pod is powerful if its RBAC is broad.
- The scheduler makes a placement decision; it does not guarantee successful runtime setup.
- Controllers are level-based; they keep reconciling until actual state changes or constraints block progress.
