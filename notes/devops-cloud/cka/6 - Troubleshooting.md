# 6 - Troubleshooting

## Quick Summary

Troubleshooting is the largest CKA domain. The key is to move from symptoms to evidence: status, events, logs, resource specs, node health, component health, DNS, Services, endpoints, network policies, and storage state.

Do not guess. Inspect.

## Beginner Bridge

Kubernetes failures usually appear as a mismatch between desired state and actual state.

Examples:

```text
Desired: Deployment has 3 replicas.
Actual: only 1 Pod is Ready.

Desired: Service sends traffic to app=web Pods.
Actual: Service has zero endpoints.

Desired: Pod mounts a PVC.
Actual: PVC is Pending or mount failed.
```

Start with the object closest to the symptom, then move outward. For an app failure, check Pod status, events, logs, config, Service endpoints, then node or cluster components only if needed.

## General Troubleshooting Flow

1. Confirm context and namespace.
2. Inspect the resource state.
3. Read events.
4. Read logs.
5. Describe the object.
6. Check dependencies such as ConfigMaps, Secrets, PVCs, Services, and endpoints.
7. Check node health.
8. Check control-plane or kubelet logs if cluster-level behavior is broken.
9. Apply the smallest fix.
10. Verify the final state.

```bash
kubectl config current-context
kubectl get pods -A -o wide
kubectl get events -A --sort-by=.lastTimestamp
```

## Pod Troubleshooting

Useful commands:

```bash
kubectl get pod <pod> -o wide
kubectl describe pod <pod>
kubectl logs <pod>
kubectl logs <pod> -c <container>
kubectl logs <pod> --previous
kubectl exec -it <pod> -- sh
```

Common statuses:

| Status | Meaning |
| --- | --- |
| `Pending` | Pod accepted but not scheduled or waiting on dependencies. |
| `ContainerCreating` | Pod scheduled but container setup is incomplete. |
| `Running` | At least one container is running. |
| `CrashLoopBackOff` | Container repeatedly starts and exits. |
| `ImagePullBackOff` | Image pull failed repeatedly. |
| `ErrImagePull` | Immediate image pull error. |
| `Completed` | Container finished successfully, common for Jobs. |
| `Terminating` | Pod is being deleted. |

## CrashLoopBackOff

Check:

```bash
kubectl logs <pod>
kubectl logs <pod> --previous
kubectl describe pod <pod>
```

Likely causes:

- Application exits due to error.
- Missing environment variable.
- Bad ConfigMap/Secret.
- Wrong command/args.
- Dependency unavailable.
- Liveness probe killing it too early.

## ImagePullBackOff

Check:

```bash
kubectl describe pod <pod>
```

Likely causes:

- Wrong image name or tag.
- Private registry secret missing.
- Registry unavailable.
- Node cannot reach registry.
- Image pull policy mismatch.

## Pending Pods

Check events:

```bash
kubectl describe pod <pod>
kubectl get events --sort-by=.lastTimestamp
```

Likely causes:

- Insufficient CPU/memory.
- Node selector/affinity has no match.
- Taint without toleration.
- PVC not bound.
- Scheduler unavailable.
- Pod quota or limit range issue.

## Node Troubleshooting

Commands:

```bash
kubectl get nodes -o wide
kubectl describe node <node>
```

On the node:

```bash
systemctl status kubelet
journalctl -u kubelet -xe
crictl ps
crictl logs <container-id>
```

Node conditions:

| Condition | Meaning |
| --- | --- |
| Ready | Node can run Pods. |
| MemoryPressure | Node memory is low. |
| DiskPressure | Node disk is low. |
| PIDPressure | Too many processes. |
| NetworkUnavailable | Network not correctly configured. |

## Cluster Component Troubleshooting

On kubeadm clusters, control-plane components are often static Pods:

```bash
ls /etc/kubernetes/manifests/
crictl ps | grep kube
```

Check kubelet because kubelet manages static Pods:

```bash
systemctl status kubelet
journalctl -u kubelet -xe
```

Common failure areas:

- Bad static Pod manifest.
- Certificate expiration or wrong paths.
- etcd unavailable.
- API server cannot start.
- Container runtime unavailable.
- Disk pressure.

## Service Troubleshooting

Flow:

1. Check Service.
2. Check selectors.
3. Check Pod labels.
4. Check endpoints.
5. Check readiness.
6. Test DNS.
7. Test port connectivity.

Commands:

```bash
kubectl get svc <service> -o yaml
kubectl describe svc <service>
kubectl get endpoints <service>
kubectl get endpointslices
kubectl get pods --show-labels
```

Common issue:

```text
Service selector app=web
Pod label app=frontend
Result: Service has no endpoints
```

## DNS Troubleshooting

```bash
kubectl run dns-test --image=busybox:1.36 --restart=Never -it --rm -- nslookup kubernetes.default
kubectl get pods -n kube-system
kubectl get svc -n kube-system
```

Check:

- CoreDNS Pods running.
- kube-dns Service exists.
- NetworkPolicy is not blocking DNS.
- Pod `/etc/resolv.conf` if needed.

## NetworkPolicy Troubleshooting

Check policies:

```bash
kubectl get networkpolicy
kubectl describe networkpolicy <name>
```

Remember:

- NetworkPolicies are namespace-scoped.
- Policies are additive.
- They select destination Pods with `podSelector`.
- They require CNI support.
- Egress policies may block DNS unless allowed.

## Storage Troubleshooting

```bash
kubectl get pv,pvc -A
kubectl describe pvc <pvc>
kubectl describe pod <pod>
kubectl get storageclass
```

Common causes:

- PVC in wrong namespace.
- StorageClass missing.
- Dynamic provisioner unavailable.
- Volume zone conflicts with scheduled node.
- Permission/ownership problem inside mounted volume.

## Resource Usage

If metrics-server is installed:

```bash
kubectl top nodes
kubectl top pods -A
```

If unavailable, use:

```bash
kubectl describe node <node>
kubectl get events -A --sort-by=.lastTimestamp
```

## Container Output Streams

Kubernetes logs usually capture stdout and stderr from containers.

Commands:

```bash
kubectl logs <pod>
kubectl logs <pod> -c <container>
kubectl logs -f <pod>
kubectl logs <pod> --previous
```

For multi-container Pods, always specify `-c` when needed.

## Benefits Of A Systematic Method

- Reduces wasted time.
- Makes the root cause clearer.
- Avoids changing unrelated resources.
- Helps validate that the fix really worked.

## Hidden Details / Caveats

- Events expire; check them early.
- `kubectl logs` without `--previous` may miss the previous crashed container.
- A Service can exist and still have no endpoints.
- A Pod can be `Running` but not `Ready`.
- Readiness affects Service endpoints; liveness affects restarts.
- Metrics commands require metrics-server or another metrics pipeline.
- Control-plane issues on kubeadm clusters often show up through static Pod or kubelet behavior.

## Common Mistakes

| Mistake | Better Approach |
| --- | --- |
| Guessing before reading events | Run `kubectl describe` and `kubectl get events`. |
| Ignoring namespace | Confirm namespace first. |
| Looking only at Pod status | Inspect logs, events, and dependencies. |
| Testing Service without endpoints | Check endpoints first. |
| Forgetting previous logs | Use `kubectl logs --previous`. |
| Changing too much at once | Make one fix and verify. |

## CKA Troubleshooting Checklist

```text
Context correct?
Namespace correct?
Resource exists?
Status clear?
Events reviewed?
Logs reviewed?
Dependencies exist?
Labels/selectors match?
Node healthy?
Service endpoints present?
NetworkPolicy allowing traffic?
PVC bound?
Final state verified?
```

## Interview Notes

- `describe` shows events and resource details.
- `logs --previous` is useful for crashed containers.
- `Pending` often means scheduling or dependency issue.
- `CrashLoopBackOff` means repeated process failure.
- `ImagePullBackOff` means image retrieval failed.
- Service without endpoints usually means selector/label/readiness issue.
- Node `NotReady` often leads to kubelet, runtime, CNI, or resource pressure investigation.

## Related Topics

- [2 - Cluster Architecture Installation and Configuration](2%20-%20Cluster%20Architecture%20Installation%20and%20Configuration.md)
- [3 - Workloads and Scheduling](3%20-%20Workloads%20and%20Scheduling.md)
- [4 - Services and Networking](4%20-%20Services%20and%20Networking.md)
- [5 - Storage](5%20-%20Storage.md)

## Official References

- [Troubleshooting applications](https://kubernetes.io/docs/tasks/debug/debug-application/)
- [Troubleshooting clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/)
- [kubectl debug](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)
- [kubectl quick reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
