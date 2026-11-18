---
name: subject-kubernetes
description: Coverage and teaching requirements for Kubernetes Architecture, CKA and CKAD in this vault - the topic checklist, the per-object explanation checklist, the mandatory diagrams, and how to drill the hands-on exams. Load it whenever creating, upgrading, teaching or quizzing anything about Kubernetes, kubectl, kubeadm, CKA or CKAD, together with deep-notes (writing) or teach/quiz/revise (learning).
---

# Kubernetes, CKA and CKAD

Folders: `notes/devops-cloud/kubernetes/`, `notes/devops-cloud/cka/`, `notes/devops-cloud/ckad/`.

Version assumption: state the Kubernetes minor version a note or lesson assumes. CKA and CKAD follow a recent Kubernetes release and the curriculum changes over time, so verify exam-specific claims against the current Linux Foundation / CNCF curriculum before writing them down.

## What the notes must cover

- **Foundations:** why Kubernetes exists; containers from first principles; Linux namespaces; cgroups; OCI basics; container runtime; CRI; CNI; CSI.
- **Architecture:** cluster architecture; control plane; worker nodes; API server; etcd; scheduler; controller manager; cloud controller manager; kubelet; kube-proxy.
- **Workloads:** Pods; ReplicaSets; Deployments; StatefulSets; DaemonSets; Jobs; CronJobs.
- **Networking:** Services; ClusterIP; NodePort; LoadBalancer; ExternalName; DNS; CoreDNS; Ingress; Gateway API where relevant; NetworkPolicies.
- **Configuration and security:** ConfigMaps; Secrets; ServiceAccounts; RBAC; admission controllers; TLS; kubeconfig; contexts.
- **Scheduling and resources:** scheduling; taints and tolerations; affinity; resource requests and limits; QoS classes.
- **Pod lifecycle and node behavior:** probes; init containers; sidecars; static pods; mirror pods; node pressure; eviction.
- **Observability:** logs; events; metrics; debugging.
- **Operations:** cluster upgrades; etcd backup and restore; kubeadm; production failure scenarios.

## For every Kubernetes object, explain

- what it is
- why it exists
- when to use it
- when not to use it
- important fields
- lifecycle
- controller behavior
- relationship with other objects
- common YAML mistakes
- useful kubectl commands
- debugging commands
- production gotchas
- CKA/CKAD traps

## Mandatory diagrams (Mermaid)

- cluster architecture
- API request lifecycle
- Pod creation lifecycle
- scheduling lifecycle
- Service networking flow
- DNS resolution flow
- storage provisioning flow
- RBAC authorization flow
- troubleshooting flow

## Teaching and quizzing Kubernetes

- **Anchor every idea in reconciliation.** Desired state goes in through the API server and is stored in etcd. Controllers compare it with actual state and act on the difference. When a student is lost, bring them back to "who is watching this object, and what does it do when reality differs?"
- **CKA and CKAD are hands-on, timed exams.** Multiple-choice questions alone build the wrong skill. Most practice should be tasks: "make this Pod schedule only on nodes labelled `disk=ssd`", "this Deployment's Pods are Pending, find out why". The student types the commands; you check the commands and the reasoning.
- **Make the student predict before running.** Ask what `kubectl get`, `describe` or `events` will show before revealing it. Being wrong about the output is where the learning happens.
- **Drill the fast paths the exam rewards:** imperative creation (`kubectl create`, `kubectl run`), generating YAML with `--dry-run=client -o yaml`, `kubectl explain <resource>.<field>` instead of guessing fields, and switching context before every task.
- **Use a fixed debugging order** for Pods: Pending means scheduling or resources; ContainerCreating means image, volume or CNI; CrashLoopBackOff means the application, its command or its probes. Ask the student which branch they are in before they touch anything.
- **Log misconceptions precisely.** "Thinks Service selects Deployments" is useful; "weak on Services" is not.
