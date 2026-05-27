# Kubernetes Architecture

## Purpose

This folder explains Kubernetes as a distributed system, not only as certification YAML. It connects why Kubernetes exists to desired state, reconciliation, API machinery, controllers, scheduling, networking, storage, security, and production failure boundaries.

## Learning Order

| Order | Note | Focus |
| --- | --- | --- |
| 0 | [Roadmap and Source Backbone](00%20-%20Roadmap%20and%20Source%20Backbone.md) | Scope, sources, architecture mental model, diagrams, and chapter plan. |
| 1 | [Desired State and Reconciliation](01%20-%20Desired%20State%20and%20Reconciliation.md) | Why Kubernetes is declarative, how controllers reconcile, and why this model changes operations. |
| 2 | [Control Plane Internals](02%20-%20Control%20Plane%20Internals.md) | API server, etcd, scheduler, controllers, admission, watch, and control-plane failure boundaries. |
| 3 | [Pod Creation Lifecycle](03%20-%20Pod%20Creation%20Lifecycle.md) | From manifest submission to scheduled Pod, image pull, container start, probes, and status. |
| 4 | [Scheduling, Placement, and Node Pressure](04%20-%20Scheduling%20Placement%20and%20Node%20Pressure.md) | Scheduler filter/score/bind flow, requests, limits, taints, affinity, QoS, and evictions. |
| 5 | [Service Networking, DNS, and Traffic Flow](05%20-%20Service%20Networking%20DNS%20and%20Traffic%20Flow.md) | Pod IPs, Services, EndpointSlices, CoreDNS, NetworkPolicy, Ingress, and Gateway API. |
| 6 | [Storage: Volumes, PV, PVC, StorageClass, and CSI](06%20-%20Storage%20Volumes%20PV%20PVC%20StorageClass%20and%20CSI.md) | Durable storage model, dynamic provisioning, CSI, access modes, reclaim policy, and mount failures. |
| 7 | [Security: RBAC, ServiceAccounts, TLS, and Admission](07%20-%20Security%20RBAC%20ServiceAccounts%20TLS%20and%20Admission.md) | API security path, RBAC, ServiceAccounts, Secrets, admission, Pod security, and troubleshooting `Forbidden`. |
| 8 | [Failure Modes and Troubleshooting Flowcharts](08%20-%20Failure%20Modes%20and%20Troubleshooting%20Flowcharts.md) | Layered debugging for API, scheduler, node, storage, network, security, and app failures. |
| 10 | [Cheatsheet](10%20-%20Cheatsheet.md) | Fast architecture revision and troubleshooting ladder. |
| 11 | [Glossary](11%20-%20Glossary.md) | Practical Kubernetes architecture terms and traps. |

## Current Status

Started from the `everything` scope on 2026-05-26 and expanded on 2026-05-27. Core architecture coverage now includes desired state, control plane internals, Pod lifecycle, scheduling, networking/DNS, storage/CSI, security/RBAC/admission, failure-mode flowcharts, cheatsheet, and glossary. Future additions can deepen cluster upgrade, autoscaling, Gateway API controller-specific behavior, and provider-specific CNI/CSI labs.
