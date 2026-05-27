# Kubernetes Architecture Changelog

## 2026-05-26

- Created folder from the `everything` scope.
- Added index and roadmap/source backbone.
- Added `01 - Desired State and Reconciliation.md` as the first full deep chapter.
- Added `02 - Control Plane Internals.md`.
- Added `03 - Pod Creation Lifecycle.md`.

## 2026-05-27

- Added `04 - Scheduling Placement and Node Pressure.md` for scheduler filter/score/bind flow, requests/limits, taints/tolerations, affinity, QoS, and eviction reasoning.
- Added `05 - Service Networking DNS and Traffic Flow.md` for Pod networking, Services, EndpointSlices, CoreDNS, NetworkPolicy, Ingress, and Gateway API.
- Added `06 - Storage Volumes PV PVC StorageClass and CSI.md` for durable storage, dynamic provisioning, access modes, reclaim policy, topology, and mount failures.
- Added `07 - Security RBAC ServiceAccounts TLS and Admission.md` for API security flow, RBAC, ServiceAccounts, Secrets, admission, and Pod security.
- Added `08 - Failure Modes and Troubleshooting Flowcharts.md` for layered debugging across API, scheduler, node, storage, network, security, and app layers.
- Added `10 - Cheatsheet.md` and `11 - Glossary.md`.
- Future depth can add provider-specific CNI/CSI labs, autoscaling internals, upgrade strategy, and Gateway API controller-specific examples.
