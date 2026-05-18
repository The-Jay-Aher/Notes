# 4 - Services and Networking

## Quick Summary

Kubernetes networking connects Pods, Services, DNS, ingress traffic, and network policy. CKA expects you to understand Pod connectivity, Service types, endpoints, CoreDNS, Ingress, Gateway API, and NetworkPolicies.

## Beginner Bridge

Networking becomes easier if you separate three questions:

```text
1. Pod IP: can Pods talk to each other?
2. Service: is there a stable virtual endpoint for changing Pods?
3. Ingress/Gateway: can users outside the cluster reach HTTP apps cleanly?
```

Pods are temporary and their IPs can change. A Service solves that by selecting Pods with labels and giving them a stable name/IP. If a Service has no endpoints, the usual problem is selector mismatch or Pods not being Ready.

NetworkPolicy is different: it restricts traffic. It does not create connectivity by itself.

## Kubernetes Network Model

Kubernetes expects:

- Pods can communicate with other Pods without NAT in the cluster network model.
- Nodes can communicate with Pods.
- Pods can communicate with Services.
- The exact implementation depends on the CNI plugin.

Common CNI examples:

- Calico.
- Cilium.
- Flannel.
- Weave Net.
- Cloud-provider CNIs.

## Pod Networking

Each Pod gets an IP address. Containers inside the same Pod share the network namespace.

Inside one Pod:

```text
container A -> localhost -> container B
```

Between Pods:

```text
pod A IP -> cluster network -> pod B IP
```

Do not hard-code Pod IPs. Pods are replaceable and IPs can change.

## Services

A Service gives stable access to a changing set of Pods.

Service selector example:

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

The Service selects Pods with:

```yaml
labels:
  app: web
```

## Service Types

| Type | Purpose |
| --- | --- |
| ClusterIP | Internal stable virtual IP. Default type. |
| NodePort | Exposes a port on each node. |
| LoadBalancer | Requests an external load balancer from supported environments. |
| ExternalName | DNS CNAME-style alias to an external name. |

### ClusterIP

Use for internal service-to-service traffic.

```bash
kubectl expose deployment web --port=80 --target-port=8080
```

### NodePort

Use when you need direct node IP plus port access, usually for labs or special cases.

```yaml
type: NodePort
ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080
```

### LoadBalancer

Use in cloud or supported bare-metal environments that can provision/load-balance external traffic.

```yaml
type: LoadBalancer
```

## Endpoints And EndpointSlices

Services route to backend Pod IPs through endpoint data.

Inspect:

```bash
kubectl get endpoints
kubectl get endpointslices
kubectl describe svc <service>
```

If a Service has no endpoints, check:

- Service selector.
- Pod labels.
- Pod readiness.
- Namespace.

## CoreDNS

CoreDNS provides cluster DNS.

Common name forms:

```text
service-name
service-name.namespace
service-name.namespace.svc
service-name.namespace.svc.cluster.local
```

Debug DNS:

```bash
kubectl run dns-test --image=busybox:1.36 --restart=Never -it --rm -- nslookup kubernetes.default
kubectl get pods -n kube-system -l k8s-app=kube-dns
kubectl logs -n kube-system -l k8s-app=kube-dns
```

Labels can vary by installation, so inspect kube-system if the selector does not match.

## Ingress

Ingress exposes HTTP/HTTPS routes into the cluster.

Important: Ingress resources need an Ingress controller. Creating only an Ingress object is not enough.

Example:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
spec:
  rules:
    - host: app.example.com
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

## Gateway API

Gateway API is a newer Kubernetes networking API for managing ingress and service networking with clearer role separation.

Common resources:

| Resource | Purpose |
| --- | --- |
| GatewayClass | Type of Gateway managed by a controller. |
| Gateway | Traffic entry point. |
| HTTPRoute | HTTP routing rules. |

Mental model:

```text
GatewayClass -> Gateway -> Route -> Service -> Pods
```

CKA currently includes Gateway API awareness in the Services and Networking domain, so know the purpose and basic flow even if your practice cluster uses Ingress more often.

## NetworkPolicies

NetworkPolicies restrict Pod traffic. They only work when the CNI plugin enforces them.

Default behavior without NetworkPolicies is usually open Pod-to-Pod communication.

Default deny ingress example:

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

Allow traffic from selected Pods:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend
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

Important:

- NetworkPolicy selects destination Pods with `podSelector`.
- Empty `podSelector: {}` selects all Pods in the namespace.
- Policies are additive.
- DNS egress may need to be allowed in restrictive egress policies.

## Practical Connectivity Tests

Create a temporary test Pod:

```bash
kubectl run net-test --image=busybox:1.36 --restart=Never -it --rm -- sh
```

Inside:

```bash
nslookup web.default.svc.cluster.local
wget -S -O- http://web:80
```

Use curl image if needed:

```bash
kubectl run curl --image=curlimages/curl --restart=Never -it --rm -- sh
```

## Benefits

- Services decouple clients from changing Pod IPs.
- DNS makes service discovery simple.
- Ingress and Gateway API provide HTTP routing entry points.
- NetworkPolicies support least-privilege network access.

## Drawbacks / Limitations

- CNI behavior differs by implementation.
- NetworkPolicies do nothing if the CNI does not enforce them.
- Ingress requires a controller.
- LoadBalancer Services depend on infrastructure support.
- Debugging can involve several layers: DNS, Service, endpoints, CNI, policy, kube-proxy/eBPF, and app readiness.

## Hidden Details / Caveats

- A Service selector mismatch gives a reachable Service with no useful backends.
- Readiness probes affect whether Pods become Service endpoints.
- NodePort exposes a port on nodes and can widen attack surface.
- `targetPort` points to the container port; `port` is the Service port.
- DNS search paths make short names work only from expected namespaces.
- NetworkPolicy namespace selectors and pod selectors can be easy to misread.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Service has wrong selector | Compare Service selector with Pod labels. |
| Ingress created without controller | Install/check Ingress controller. |
| NetworkPolicy blocks DNS | Allow egress to DNS where needed. |
| Using Pod IP in config | Use Service DNS name instead. |
| Exposing everything with NodePort | Prefer ClusterIP internally and controlled ingress externally. |

## Troubleshooting

```bash
kubectl get pod -o wide
kubectl get svc
kubectl describe svc <service>
kubectl get endpoints,endpointslices
kubectl get ingress
kubectl get networkpolicy
kubectl get events --sort-by=.lastTimestamp
```

Flow:

1. Does DNS resolve?
2. Does the Service exist?
3. Does the Service have endpoints?
4. Are Pods ready?
5. Does NetworkPolicy allow the traffic?
6. Is the target application listening on `targetPort`?
7. Is ingress/load balancer/controller configured?

## Interview Notes

- ClusterIP is internal by default.
- NodePort opens a port on each node.
- LoadBalancer depends on infrastructure support.
- Ingress needs an Ingress controller.
- Gateway API separates infrastructure and routing concerns.
- CoreDNS provides service discovery.
- NetworkPolicies require CNI enforcement.
- Service endpoints come from matching ready Pods.

## Related Topics

- [Networking Fundamentals](../Networking%20Fundamentals/1%20-%20Fundamentals%20of%20Networking.md)
- [Internet Protocol (IP)](../Networking%20Fundamentals/2%20-%20Internet%20Protocol%20%28IP%29.md)
- [6 - Troubleshooting](6%20-%20Troubleshooting.md)

## Official References

- [Kubernetes network model](https://kubernetes.io/docs/concepts/services-networking/)
- [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
