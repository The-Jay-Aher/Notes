# 4 - Observability Maintenance and Troubleshooting

## Quick Summary

Observability and maintenance in CKAD means knowing how to check app health, read logs, inspect resource status, use probes, understand API deprecations, and debug failed workloads.

## Beginner Bridge

Observability starts before the app fails. A Kubernetes-friendly app should:

- Log to stdout/stderr.
- Expose a readiness endpoint if it receives traffic.
- Expose a liveness endpoint only when restart is the correct recovery.
- Exit with a non-zero status when startup truly fails.
- Handle SIGTERM for graceful shutdown.

CKAD troubleshooting is evidence-driven. `get` tells you the state, `describe` tells you events and configuration, `logs` tells you what the app printed, and `exec` lets you inspect from inside the container.

## Core Observability Tools

| Tool | Use |
| --- | --- |
| `kubectl get` | Quick status. |
| `kubectl describe` | Detailed object state and events. |
| `kubectl logs` | Container stdout/stderr. |
| `kubectl exec` | Run commands inside a container. |
| `kubectl top` | Resource usage if metrics-server exists. |
| `kubectl events` / `kubectl get events` | Recent cluster events. |
| `kubectl port-forward` | Local access to a Pod or Service for debugging. |

## Logs

```bash
kubectl logs <pod>
kubectl logs <pod> -c <container>
kubectl logs <pod> --previous
kubectl logs -f <pod>
```

Use `--previous` for containers that restarted.

For Deployments:

```bash
kubectl logs deployment/web
```

## Probes

Kubernetes uses probes to decide container health and traffic readiness.

| Probe | Purpose |
| --- | --- |
| Startup probe | Gives slow-starting apps time before liveness checks begin. |
| Liveness probe | Determines whether container should be restarted. |
| Readiness probe | Determines whether Pod should receive Service traffic. |

HTTP readiness probe:

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
```

TCP liveness probe:

```yaml
livenessProbe:
  tcpSocket:
    port: 8080
  initialDelaySeconds: 15
  periodSeconds: 20
```

Exec probe:

```yaml
livenessProbe:
  exec:
    command:
      - sh
      - -c
      - test -f /tmp/healthy
```

## Probe Mistakes

| Mistake | Result |
| --- | --- |
| Liveness probe too aggressive | App restarts repeatedly. |
| Readiness probe missing | Traffic may reach app before it is ready. |
| Startup probe missing for slow app | Liveness kills app during startup. |
| Probe path requires auth | Probe fails even when app works for real users. |
| Probe checks dependency too strictly | Temporary dependency issue removes healthy app from traffic. |

## API Deprecations

Kubernetes APIs evolve. Old versions can be deprecated and later removed.

Check resource API versions:

```bash
kubectl api-resources
kubectl explain deployment
```

Good habits:

- Use current `apiVersion` from official docs.
- Avoid copying old manifests blindly.
- Test manifests against the target cluster version.
- Use `kubectl convert` only where available and appropriate.

Examples of version awareness:

- `networking.k8s.io/v1` for current Ingress resources.
- `apps/v1` for Deployments, DaemonSets, StatefulSets, and ReplicaSets.

## Debugging Pods

Basic flow:

```bash
kubectl get pod <pod> -o wide
kubectl describe pod <pod>
kubectl logs <pod>
kubectl logs <pod> --previous
kubectl exec -it <pod> -- sh
kubectl get events --sort-by=.lastTimestamp
```

Common statuses:

| Status | Meaning |
| --- | --- |
| `Pending` | Not scheduled or waiting on dependency. |
| `ContainerCreating` | Container setup, image, mount, or network setup in progress. |
| `CrashLoopBackOff` | App exits repeatedly. |
| `ImagePullBackOff` | Image pull failed. |
| `Running` but not ready | Readiness probe or app readiness issue. |

## Ephemeral Debugging

Temporary debug Pod:

```bash
kubectl run debug --image=busybox:1.36 --restart=Never -it --rm -- sh
```

Temporary curl Pod:

```bash
kubectl run curl --image=curlimages/curl --restart=Never -it --rm -- sh
```

Port forward:

```bash
kubectl port-forward svc/web 8080:80
curl http://127.0.0.1:8080
```

## Resource Monitoring

If metrics-server is installed:

```bash
kubectl top pod
kubectl top node
```

If not installed:

- Use `kubectl describe node`.
- Check events.
- Check app logs.
- Check cloud/node monitoring where available.

## Benefits

- Probes make Kubernetes aware of application state.
- Logs and events give fast root-cause clues.
- Port-forward and debug Pods help test from inside/outside the cluster.
- API version awareness prevents broken manifests during upgrades.

## Drawbacks / Limitations

- `kubectl top` depends on metrics availability.
- Logs are only as good as application logging.
- Events expire.
- Probes can create instability when configured poorly.
- `exec` may fail for minimal images without a shell.

## Hidden Details / Caveats

- Readiness affects Service endpoints; liveness restarts containers.
- A Pod can be `Running` but not `Ready`.
- `kubectl logs` reads one container by default; specify `-c` in multi-container Pods.
- Previous logs disappear after enough restarts or container garbage collection.
- Port-forward is for debugging, not production access.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Looking only at `kubectl get pods` | Use describe, logs, and events. |
| Forgetting `--previous` | Use it after crashes/restarts. |
| Using liveness for dependency readiness | Use readiness for traffic decisions. |
| Assuming `top` always exists | Check metrics-server availability. |
| Debugging from laptop only | Also test from inside the cluster. |

## Troubleshooting Examples

### Image Pull Failure

```bash
kubectl describe pod <pod>
```

Check:

- Image name.
- Tag.
- Registry access.
- Pull secret.

### App Starts But Gets No Traffic

Check:

```bash
kubectl get pod --show-labels
kubectl describe svc <service>
kubectl get endpoints <service>
kubectl describe pod <pod>
```

Likely causes:

- Service selector mismatch.
- Readiness probe failing.
- Wrong target port.

### App Keeps Restarting

Check:

```bash
kubectl logs <pod> --previous
kubectl describe pod <pod>
```

Likely causes:

- App crash.
- Missing config.
- Liveness probe too strict.
- Permission issue.

## Interview Notes

- Readiness controls traffic; liveness controls restarts.
- Startup probe protects slow-starting apps.
- `describe` shows events.
- `logs --previous` is important after restarts.
- API versions can be deprecated and removed.
- `port-forward` is a debugging tool.

## Related Topics

- [3 - Application Deployment](3%20-%20Application%20Deployment.md)
- [5 - Configuration Security Services and Networking](5%20-%20Configuration%20Security%20Services%20and%20Networking.md)

## Official References

- [Debug Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/)
- [Configure liveness, readiness, and startup probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- [Application introspection and debugging](https://kubernetes.io/docs/tasks/debug/debug-application/)
- [kubectl logs](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/)
