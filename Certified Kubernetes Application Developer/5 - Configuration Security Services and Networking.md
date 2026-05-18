# 5 - Configuration Security Services and Networking

## Quick Summary

Kubernetes applications need configuration, secure runtime settings, resources, identity, and network access. CKAD expects you to use ConfigMaps, Secrets, requests, limits, quotas, ServiceAccounts, SecurityContexts, Services, Ingress, and basic NetworkPolicies.

## Beginner Bridge

This note is about everything around the container image that makes the app safe and usable:

```text
ConfigMap -> non-secret settings
Secret -> sensitive settings
requests/limits -> scheduling and resource control
ServiceAccount -> workload identity
SecurityContext -> runtime restrictions
Service/Ingress -> network access
NetworkPolicy -> traffic restrictions
```

When an app works locally but fails in Kubernetes, the cause is often one of these surrounding pieces rather than the image itself.

## ConfigMaps

ConfigMaps store non-secret configuration.

Create:

```bash
kubectl create configmap app-config \
  --from-literal=APP_MODE=prod \
  --from-literal=LOG_LEVEL=info
```

Use as environment variables:

```yaml
envFrom:
  - configMapRef:
      name: app-config
```

Use as files:

```yaml
volumes:
  - name: config
    configMap:
      name: app-config
containers:
  - name: app
    image: nginx
    volumeMounts:
      - name: config
        mountPath: /etc/app
```

## Secrets

Secrets store sensitive values such as tokens or passwords.

Create:

```bash
kubectl create secret generic db-secret \
  --from-literal=username=app \
  --from-literal=password='change-me'
```

Use:

```yaml
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: db-secret
        key: password
```

Important:

- Secrets are base64-encoded in manifests, not magically encrypted everywhere.
- Use RBAC to restrict access.
- Enable encryption at rest where required.
- Prefer external secret management in production when appropriate.

## Requests And Limits

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "500m"
    memory: "512Mi"
```

Requests:

- Used for scheduling.
- Used by HPA for CPU/memory utilization calculations.

Limits:

- CPU limit causes throttling.
- Memory limit can cause OOM kill.

## ResourceQuota And LimitRange

ResourceQuota limits aggregate namespace usage.

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 8Gi
    limits.cpu: "8"
    limits.memory: 16Gi
    pods: "20"
```

LimitRange can set default/min/max resource rules.

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
spec:
  limits:
    - type: Container
      default:
        cpu: "500m"
        memory: "512Mi"
      defaultRequest:
        cpu: "250m"
        memory: "256Mi"
```

## ServiceAccounts

ServiceAccounts provide identity for Pods inside the cluster.

Create:

```bash
kubectl create serviceaccount app-sa
```

Use:

```yaml
spec:
  serviceAccountName: app-sa
```

Permissions are granted through RBAC.

```bash
kubectl auth can-i get pods --as=system:serviceaccount:default:app-sa
```

## SecurityContext

SecurityContext controls Linux/security settings at Pod or container level.

Example:

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  allowPrivilegeEscalation: false
  capabilities:
    drop:
      - ALL
```

Common settings:

| Setting | Purpose |
| --- | --- |
| `runAsNonRoot` | Prevent running as root. |
| `runAsUser` | Set container user ID. |
| `readOnlyRootFilesystem` | Make root filesystem read-only. |
| `allowPrivilegeEscalation` | Prevent gaining extra privileges. |
| `capabilities` | Add/drop Linux capabilities. |

## Services

Service example:

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
      targetPort: 8080
```

Types:

| Type | Use |
| --- | --- |
| ClusterIP | Internal access. |
| NodePort | Expose through node IP and node port. |
| LoadBalancer | External load balancer when supported. |
| ExternalName | DNS alias to external service. |

## Ingress

Ingress routes HTTP/HTTPS traffic to Services.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
spec:
  rules:
    - host: web.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web
                port:
                  number: 80
```

Ingress requires an Ingress controller.

## NetworkPolicy

Basic default deny ingress:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
spec:
  podSelector: {}
  policyTypes:
    - Ingress
```

Allow frontend to API:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-api
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
```

NetworkPolicies require CNI support.

## CRDs And Operators

CRDs extend Kubernetes with new resource types. Operators are controllers that manage those custom resources.

Examples:

- cert-manager uses resources such as `Certificate`.
- Prometheus Operator uses resources such as `Prometheus` and `ServiceMonitor`.

CKAD focus: know that CRDs extend the API and operators reconcile them. You usually do not need deep operator internals for basic app tasks.

## Benefits

- ConfigMaps and Secrets separate configuration from images.
- Requests and limits make scheduling and resource control predictable.
- ServiceAccounts give Pods identity.
- SecurityContext reduces container privilege.
- Services and Ingress expose applications cleanly.
- NetworkPolicies support network least privilege.

## Drawbacks / Limitations

- Secrets need proper encryption, RBAC, and rotation outside basic YAML.
- Resource limits can hurt performance if set poorly.
- SecurityContext support can depend on container image and cluster policy.
- NetworkPolicies do not work without enforcing CNI support.
- Ingress behavior depends on the controller.

## Hidden Details / Caveats

- Environment variables from ConfigMaps/Secrets do not update in running containers automatically.
- Mounted config volumes can update, but apps may need reload logic.
- A Service selects only Pods with matching labels in the same namespace.
- Readiness controls whether Pods become Service endpoints.
- ServiceAccount token behavior depends on Kubernetes version and projected token settings.
- Dropping Linux capabilities is usually safer than adding them.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Storing passwords in ConfigMaps | Use Secrets or external secret management. |
| No resource requests | Add requests for scheduling and autoscaling. |
| Running containers as root by default | Set SecurityContext where possible. |
| Wrong Service selector | Compare Service selector with Pod labels. |
| Ingress without controller | Install/check controller. |
| NetworkPolicy blocks DNS | Allow DNS egress when using restrictive egress policy. |

## Troubleshooting

```bash
kubectl describe configmap <name>
kubectl describe secret <name>
kubectl describe pod <pod>
kubectl auth can-i <verb> <resource> --as=system:serviceaccount:<ns>:<sa>
kubectl get svc,endpoints
kubectl describe ingress <name>
kubectl get networkpolicy
```

| Symptom | Check |
| --- | --- |
| Env var missing | ConfigMap/Secret name and key. |
| Permission denied to Kubernetes API | ServiceAccount and RBAC. |
| Pod OOMKilled | Memory limits and app usage. |
| Service no traffic | Selector, endpoints, readiness, targetPort. |
| Ingress not reachable | Controller, class, rules, DNS, Service backend. |
| Network blocked | NetworkPolicy and CNI support. |

## Interview Notes

- ConfigMaps are for non-secret config.
- Secrets are for sensitive values but still need RBAC/encryption/rotation.
- Requests affect scheduling; limits cap usage.
- ServiceAccount is Pod identity.
- SecurityContext controls runtime privileges.
- ClusterIP is internal; NodePort exposes node port; LoadBalancer needs infra support.
- Ingress needs a controller.
- NetworkPolicies are additive and require CNI enforcement.

## Related Topics

- [2 - Application Design and Build](2%20-%20Application%20Design%20and%20Build.md)
- [4 - Observability Maintenance and Troubleshooting](4%20-%20Observability%20Maintenance%20and%20Troubleshooting.md)
- [Certified Kubernetes Administrator - Services and Networking](../Certified%20Kubernetes%20Administrator/4%20-%20Services%20and%20Networking.md)

## Official References

- [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [ServiceAccounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
- [Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
- [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
