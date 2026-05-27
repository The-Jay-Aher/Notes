# 11 - CKAD Glossary

| Term | Meaning | CKAD trap |
| --- | --- | --- |
| Pod | Smallest deployable unit. | Direct Pods lack rollout management. |
| Deployment | Manages ReplicaSets/Pods with rollout. | Selector/template labels must match. |
| Job | Runs task to completion. | Restart/backoff behavior matters. |
| CronJob | Scheduled Jobs. | Time/schedule and concurrency policy matter. |
| ConfigMap | Non-secret config. | Not for sensitive data. |
| Secret | Sensitive config object. | Base64 is not encryption. |
| Readiness probe | Controls traffic eligibility. | Failing readiness removes endpoints. |
| Liveness probe | Restarts unhealthy containers. | Bad probe causes restart loop. |
| Startup probe | Protects slow startup. | Useful before liveness begins. |
| Service | Stable access to Pods. | Selector/targetPort mistakes. |
| Ingress | HTTP routing into cluster. | Needs controller. |
| NetworkPolicy | Pod traffic policy. | Requires enforcing CNI. |
| SecurityContext | Pod/container security settings. | Scope matters: Pod vs container. |
| ServiceAccount | Pod identity. | Token/access depends on RBAC. |
| Resource request | Scheduling reservation. | Missing request affects scheduling/QoS. |
| Resource limit | Runtime cap. | CPU throttle or memory OOM kill. |

## Questions to Test Understanding

1. What object gives rolling updates?
2. What object should store non-sensitive config?
3. What probe controls Service endpoints?
4. What must exist for Ingress to work?
5. What policy controls Pod-to-Pod traffic?

## Answers and Reasoning

1. Deployment.
2. ConfigMap.
3. Readiness probe.
4. An Ingress controller plus Ingress resource.
5. NetworkPolicy, if CNI enforces it.

