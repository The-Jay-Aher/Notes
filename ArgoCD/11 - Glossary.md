# 11 - Argo CD Glossary

## Why This Chapter Matters

Argo CD vocabulary is compact, but each word hides operational behavior. This glossary gives precise meanings and the mistake each term helps avoid.

## Glossary

| Term | Meaning | Common trap |
| --- | --- | --- |
| Argo CD | Kubernetes GitOps continuous delivery controller. | Treating it as just a deployment UI. |
| GitOps | Operational model where Git stores desired state. | Thinking it means all syncs must be automatic. |
| Desired state | Rendered manifests from configured source. | Assuming source templates are the same as rendered output. |
| Live state | Actual Kubernetes resources. | Assuming live manual edits are durable under self-heal. |
| Application | Argo CD CR linking source, destination, project, and sync policy. | Making app scope too broad. |
| AppProject | Argo CD policy boundary for apps. | Leaving production apps in permissive default project. |
| Sync | Apply desired state to live cluster. | Treating sync as proof of business success. |
| Prune | Delete tracked resources absent from desired state. | Forgetting prune means deletion. |
| Self-heal | Revert live drift back to Git. | Fighting emergency manual fixes. |
| Sync wave | Numeric ordering for sync resources/hooks. | Using waves as a full dependency management system. |
| Hook | Resource that runs during sync phases. | Writing non-idempotent migration hooks. |
| Repo server | Component that fetches and renders source. | Debugging Pods when render failed. |
| Application controller | Component that compares, reports, and syncs Applications. | Blaming UI when controller queue is slow. |
| Argo CD API server | UI/CLI/API/auth front door. | Confusing it with Kubernetes API server. |
| Redis | Cache layer used by Argo CD. | Treating cache as desired-state storage. |
| Dex | Optional identity broker. | Assuming SSO alone defines permissions. |
| ApplicationSet | CR/controller that generates Applications. | Directly editing generated apps without changing generator/template. |
| App-of-apps | Parent Application manages child Application manifests. | Giving one parent too much blast radius. |
| `OutOfSync` | Desired and live differ. | Assuming the app is broken without reading diff. |
| `Synced` | Desired and live match. | Assuming users are fine. |
| `Healthy` | Argo CD health checks look good. | Treating it as full business SLO proof. |
| `Degraded` | Resource health indicates failure. | Trying to fix Git when runtime is broken. |
| `ComparisonError` | Compare failed, often render/source. | Retrying sync without fixing render. |
| `InvalidSpecError` | App spec or policy boundary invalid. | Debugging Kubernetes Pods too early. |
| Target revision | Branch, tag, commit, chart version, or source revision. | Using floating branch for production without controls. |
| Destination | Cluster and namespace Argo CD deploys to. | Deploying to the wrong cluster. |
| Project role | AppProject-scoped Argo CD role. | Confusing it with Kubernetes Role. |
| `policy.default` | Default role for authenticated Argo CD users. | Granting broad default permissions. |
| Secret management | How sensitive data enters GitOps desired state safely. | Committing raw secrets to Git. |
| Immutable image | Image reference that cannot change bytes under same name, often digest. | Using `latest` and losing auditability. |

## Small Details That Matter Later

- Argo CD's "Application" is not your business application; it is a deployment control object.
- AppProject names appear in RBAC policy and audit conversations.
- `Synced` and `Healthy` answer different questions.
- Generated Applications are still normal Applications after creation.
- Secret plugins increase the trusted computing base.
- Git commit history is only useful if deployment repos and image references are disciplined.

## Questions to Test Understanding

1. What word tells you desired and live differ?
2. What word tells you runtime health is bad?
3. Which component renders Helm/Kustomize?
4. Which resource limits where apps may deploy?
5. Which setting deletes resources removed from Git?
6. Which pattern generates Applications from templates?
7. Which setting can reverse manual cluster edits?
8. Which role setting affects every authenticated Argo CD user?

## Answers and Reasoning

1. `OutOfSync`.
2. `Degraded`.
3. `argocd-repo-server`.
4. `AppProject`.
5. `prune`.
6. `ApplicationSet`.
7. `selfHeal`.
8. `policy.default`.

