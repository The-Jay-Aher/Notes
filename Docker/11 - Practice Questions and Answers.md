# 11 - Practice Questions and Answers

## Why This Chapter Matters

Docker questions in interviews and exams often look simple but test hidden distinctions: image vs container, build time vs runtime, host port vs container port, volume vs bind mount, tag vs digest, `CMD` vs `ENTRYPOINT`, Compose vs Kubernetes, and process running vs service ready.

Use these questions to test whether you can reason, not merely recite.

## The Big Picture

Question types:

- Conceptual MCQs.
- Scenario debugging.
- Command interpretation.
- Dockerfile review.
- Compose review.
- Security review.
- Kubernetes connection.
- Interview explanation prompts.

## First-Principles Explanation

The answer to most Docker questions can be derived from a small set of principles:

- A container is a process, not a full VM.
- An image is a read-only template.
- A container adds runtime state and a writable layer.
- Volumes and bind mounts place data outside the writable layer.
- Port publishing is host-to-container forwarding.
- Build instructions create layers and cache boundaries.
- Tags are mutable; digests identify content.
- Compose is local multi-service orchestration, not Kubernetes.
- Security depends on image, runtime, host, and supply chain choices.

## Core Vocabulary

Before answering, make sure these pairs are not confused:

| Pair | Key distinction |
| --- | --- |
| Image / container | Template vs running instance. |
| `docker run` / `docker start` | Create new container vs start existing one. |
| `EXPOSE` / `-p` | Document port vs publish host forwarding. |
| Volume / bind mount | Docker-managed storage vs host path. |
| Tag / digest | Mutable name vs content identity. |
| `CMD` / `ENTRYPOINT` | Default command/args vs executable-style entry. |
| Compose / Kubernetes | Local stack definition vs distributed desired-state platform. |
| Liveness / readiness | Should restart vs should receive traffic. |

## Mental Model

When answering, walk the lifecycle:

```text
Dockerfile -> image layers -> registry -> container create -> runtime config -> process -> network/storage/logs -> orchestration
```

If a question mentions failure, ask where in that lifecycle it happens.

## MCQs

### 1. What is a Docker image?

A. A running process with isolated networking
B. A read-only template used to create containers
C. A Docker network driver
D. A persistent storage object

Answer: B.

Reasoning: A running process is a container. An image is the read-only package/template.

### 2. What happens when you run `docker run nginx:1.27` and the image is not local?

A. Docker fails immediately.
B. Docker pulls the image from a configured registry, then creates and starts a container.
C. Docker creates an empty image.
D. Docker starts Kubernetes.

Answer: B.

Reasoning: Docker resolves and pulls missing images from registries such as Docker Hub by default.

### 3. Which statement about `latest` is correct?

A. It always means newest stable version.
B. It is a mutable tag name.
C. It is a digest.
D. Kubernetes rejects it.

Answer: B.

Reasoning: `latest` is a tag. Tags can move.

### 4. What does `EXPOSE 8080` do?

A. Publishes port 8080 on the host.
B. Opens the firewall.
C. Documents that the container listens on port 8080.
D. Creates a Kubernetes Service.

Answer: C.

Reasoning: Host publishing requires `-p` or Compose `ports`.

### 5. Which storage option is best for long-lived database data in local Docker?

A. Container writable layer
B. Named volume
C. Image layer
D. `docker logs`

Answer: B.

Reasoning: Named volumes persist independently of the container lifecycle.

### 6. What is a bind mount?

A. A registry login token
B. A host filesystem path mounted into a container
C. An image digest
D. A network namespace

Answer: B.

Reasoning: Bind mounts directly connect host paths to container paths.

### 7. Why are multi-stage builds useful?

A. They run multiple containers in Compose.
B. They separate build dependencies from final runtime artifacts.
C. They publish all ports automatically.
D. They disable image layers.

Answer: B.

Reasoning: Multi-stage builds can reduce final image size and attack surface.

### 8. What does `docker exec` require?

A. A running container
B. A stopped image
C. A Kubernetes Pod
D. A volume with data

Answer: A.

Reasoning: `exec` runs a command inside an already running container.

### 9. Which command is dangerous if volumes contain databases?

A. `docker ps`
B. `docker logs web`
C. `docker volume prune`
D. `docker inspect web`

Answer: C.

Reasoning: It removes unused volumes, which may contain data.

### 10. What is the main difference between Compose and Kubernetes?

A. Compose uses YAML and Kubernetes does not.
B. Compose defines local multi-container apps; Kubernetes manages desired state across a cluster.
C. Kubernetes cannot run containers.
D. Compose requires Java.

Answer: B.

Reasoning: Both may use YAML, but their control models are different.

## Scenario Questions

### 11. A container exits immediately after `docker run myapp`. What do you check first?

Answer:

Run:

```bash
docker ps -a
docker logs <container>
docker inspect --format '{{.State.ExitCode}} {{json .Config.Cmd}} {{json .Config.Entrypoint}}' <container>
```

Reasoning: You need container state, logs, exit code, and the actual startup command. A container can exit because the command completed successfully, crashed, lacked config, or could not execute.

### 12. A web container is running, but `curl localhost:8080` on the host fails. What are likely causes?

Answer:

- Host port was not published.
- Wrong host port or container port.
- App listens on `127.0.0.1` inside the container instead of `0.0.0.0`.
- Container app is not actually listening.
- Host firewall or local network policy blocks access.
- The container is running but unhealthy.

Commands:

```bash
docker ps
docker port <container>
docker logs <container>
docker exec <container> sh -c 'ss -lntp || netstat -lntp'
```

### 13. Two containers cannot communicate using `localhost`. Why?

Answer:

`localhost` means the same network namespace. Inside container A, `localhost` means container A, not container B. Put both containers on the same user-defined network and connect using the peer container or Compose service name.

### 14. A database loses data after `docker rm`. What went wrong?

Answer:

The database probably wrote into the container writable layer instead of a named volume or external storage. The fix is to mount the image's data directory to a named volume and test backup/restore.

### 15. A Docker build is slow every time after small source changes. What should you inspect?

Answer:

Inspect Dockerfile layer order and build context. Dependency installation should be separated from frequently changing source files. Add `.dockerignore` to reduce context size.

Better pattern:

```dockerfile
COPY package*.json .
RUN npm ci
COPY . .
```

### 16. A secret was copied into a Docker image and deleted in a later layer. Is it safe?

Answer:

No. Files added in earlier layers may remain in image history or layer data. Rotate the secret, remove it from the Dockerfile/build context, rebuild, and consider registry cleanup based on policy.

### 17. A container works as root but fails as non-root. What do you check?

Answer:

- file ownership in the image
- bind mount ownership
- writable directories such as `/tmp`, cache, logs, uploads
- privileged ports
- package manager or runtime assumptions
- `USER` instruction and runtime `--user`

### 18. Compose `depends_on` is used, but the app still fails connecting to the database. Why?

Answer:

Startup order is not dependency readiness. The database container can be started while the database process is still initializing. The app needs retry logic and optionally Compose health conditions where supported.

### 19. CI builds an image on `amd64`, but production nodes are `arm64`. What is the issue?

Answer:

Platform mismatch. Build or pull a multi-architecture image, or specify platform deliberately. Verify base image support and native dependencies.

### 20. An app works in Compose but fails in Kubernetes. What assumptions may have leaked?

Answer:

- local bind mounts
- Compose service names
- startup order assumptions
- missing readiness probes
- missing resource limits
- different secrets/config injection
- image pull policy/tag behavior
- filesystem write paths
- non-root security context

## Dockerfile Review Questions

### 21. Review this Dockerfile.

```dockerfile
FROM node:22
WORKDIR /app
COPY . .
RUN npm install
CMD ["npm", "start"]
```

What should be improved?

Answer:

- Add `.dockerignore`.
- Copy `package*.json` first, run `npm ci`, then copy source.
- Use a slimmer trusted runtime image where appropriate.
- Consider multi-stage build.
- Avoid running as root if possible.
- Use lockfile-based install.
- Do not copy secrets or local artifacts.

Improved sketch:

```dockerfile
FROM node:22 AS build
WORKDIR /app
COPY package*.json .
RUN npm ci
COPY . .
RUN npm run build

FROM node:22-slim
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json .
RUN npm ci --omit=dev
COPY --from=build /app/dist ./dist
USER node
CMD ["node", "dist/server.js"]
```

Exact final shape depends on the app.

### 22. What is wrong with this Dockerfile?

```dockerfile
FROM python:3.12-slim
ENV API_KEY=real-secret
COPY . /app
CMD ["python", "/app/app.py"]
```

Answer:

It bakes a real secret into the image. Secrets can persist in layers and registry history. Use runtime secret injection instead and rotate the exposed secret.

### 23. Why prefer `COPY` over `ADD` for ordinary file copy?

Answer:

`COPY` does basic local copying and is clearer. `ADD` has extra behavior such as archive extraction and remote URL handling, which can surprise readers. Use `ADD` only when those features are intentionally needed.

### 24. Why is `WORKDIR` useful?

Answer:

It avoids accidental commands running in unexpected directories, makes relative paths clearer, and creates the directory if needed.

### 25. When should you use `ENTRYPOINT`?

Answer:

Use `ENTRYPOINT` when the image should behave like a specific executable, with `CMD` supplying default arguments. Use plain `CMD` for simpler application images where users commonly override the command.

## Compose Review Questions

### 26. Review this Compose snippet.

```yaml
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      DB_HOST: localhost
  db:
    image: postgres:16
```

What is wrong?

Answer:

Inside `app`, `localhost` means the app container, not the database container. Use `DB_HOST=db` if both services are on the same Compose network. Also add a named volume for Postgres data and avoid hard-coded real secrets.

### 27. Why might `docker compose down -v` be destructive?

Answer:

It removes volumes defined by the Compose project. If a database stores data there, local data is deleted.

### 28. What does `docker compose config` show?

Answer:

It renders the effective Compose configuration after interpolation and merge behavior. It helps catch wrong env values, ports, volumes, profiles, and service definitions.

### 29. How do Compose service names work?

Answer:

Compose creates a project network by default. Services on that network can resolve each other by service name, such as `db` or `redis`.

### 30. Should a production app rely only on Compose startup order?

Answer:

No. Real apps need retries, health checks, and clear readiness behavior.

## Security Questions

### 31. Why should containers avoid running as root?

Answer:

If the app is compromised, non-root execution reduces what the attacker can do inside the container and through mounted paths. It also aligns better with stricter Kubernetes security contexts. It is not the only security control.

### 32. Why is mounting `/var/run/docker.sock` risky?

Answer:

It gives the container access to the Docker daemon API. A compromised process may create privileged containers, mount host paths, or manipulate other containers, which can become host-level control.

### 33. What is rootless Docker?

Answer:

Rootless mode runs the Docker daemon and containers as a non-root user using user namespaces, reducing daemon/runtime privilege risk. It is different from simply running a process as non-root inside a rootful daemon.

### 34. Does image scanning prove an image is safe?

Answer:

No. Scanning finds known vulnerabilities and sometimes secrets/misconfigurations. It does not prove application logic, runtime privileges, secrets, or deployment policy are safe.

### 35. Why are bind mounts security-sensitive?

Answer:

Writable bind mounts let container processes modify host files. They can also expose sensitive host paths to the container.

## Kubernetes Connection Questions

### 36. Can Kubernetes run images built with Docker?

Answer:

Yes, if they are valid container images and available from a registry the cluster can pull. Kubernetes does not need Docker CLI commands in the Pod spec.

### 37. What is the Kubernetes equivalent of `docker run -p`?

Answer:

There is no exact one-line equivalent. Pods define container ports, and Services/Ingress/Gateway expose network access. `kubectl port-forward` can be used for local debugging but is not a production exposure model.

### 38. What replaces Compose `depends_on` in Kubernetes?

Answer:

Usually app retry logic, readiness probes, init containers for specific initialization gates, and controllers. Kubernetes does not make distributed dependency readiness vanish.

### 39. What Kubernetes object stores environment-like non-secret config?

Answer:

ConfigMap.

### 40. What Kubernetes object stores sensitive data, and what caveat matters?

Answer:

Secret. Kubernetes Secrets need proper RBAC, encryption at rest where required, and external secret management in many production setups. They are not magic security by name alone.

## Interview Explanation Prompts

### 41. Explain Docker to a beginner without saying "lightweight VM."

Answer:

Docker packages an application and its dependencies into an image. When that image runs, it becomes a container, which is an isolated process using the host kernel. The isolation comes from kernel features around process, filesystem, network, users, and resources. This makes the app more repeatable across machines without booting a full guest OS for each app.

### 42. Explain image layers.

Answer:

An image is built from immutable filesystem changes called layers. Each Dockerfile instruction can create a layer. Docker reuses unchanged layers during builds and pulls, which improves speed and bandwidth. Layering also means Dockerfile order affects cache efficiency, and secrets copied in an earlier layer may remain even if deleted later.

### 43. Explain Docker Compose.

Answer:

Compose defines a local multi-container application in YAML. A service describes how to run one container type. Compose creates containers, networks, and volumes for the project and gives services DNS names. It is excellent for local development and simple stacks, but it is not the same control model as Kubernetes.

### 44. Explain Docker volumes.

Answer:

A volume is Docker-managed storage mounted into a container. It persists beyond the container lifecycle and is suited for data that should survive container replacement, such as database data. It differs from a bind mount because Docker manages the storage location rather than directly using a user-chosen host path.

### 45. Explain how you would make a Docker image production-ready.

Answer:

Use a trusted minimal base, add `.dockerignore`, structure layers for cache, use multi-stage builds, avoid secrets in images, run as non-root where practical, scan dependencies, pin important versions, emit logs to stdout/stderr, define health behavior, test graceful shutdown, and promote the same image through environments using tags/digests.

## Small Details That Matter Later

- Interview questions often hide a build-time vs runtime distinction.
- A host port conflict is not a container port conflict.
- `docker run` creates; `docker start` restarts existing.
- `docker exec` is investigation, not durable configuration.
- A health check command must exist inside the image.
- Bind mounts are tied to host paths and Docker daemon location.
- `--platform` can matter on Apple Silicon, ARM servers, and mixed clusters.
- `USER` in Dockerfile can be overridden at runtime.
- Compose file version fields are less central in modern Compose Specification than old v2/v3 memorization.
- Kubernetes `imagePullPolicy` and tag choice can change pull behavior; verify actual manifest and cluster defaults.

## Common Misunderstandings

| Misunderstanding | Correction |
| --- | --- |
| Docker is only commands. | Docker is an artifact, runtime, network, storage, and security model. |
| Bigger images are only a disk problem. | Bigger images also affect pull time, attack surface, and CVE volume. |
| If Compose works, Kubernetes will work. | Kubernetes has different networking, storage, health, and lifecycle behavior. |
| A passed vulnerability scan means production-safe. | Security requires build, runtime, secrets, host, policy, and app controls. |

## Chapter Summary

The best Docker answers explain the mechanism behind the command. Whenever you answer, identify the layer: image build, registry, container create, runtime process, network, storage, security, Compose, or Kubernetes.

## Questions to Test Understanding

1. Which three Docker distinctions are most likely to appear in interviews?
2. Why should scenario answers name commands, not only concepts?
3. Why is "the container is running" weak evidence?
4. Why should a Dockerfile review consider both speed and security?
5. Why does Kubernetes connection matter in Docker practice?

## Answers and Reasoning

1. Image vs container, `EXPOSE` vs `-p`, and volume vs bind mount are common because they reveal whether the candidate understands runtime mechanics.
2. Commands show how the claim would be verified. `docker logs`, `docker inspect`, `docker port`, and `docker compose config` turn guesses into evidence.
3. A running process may still be unready, unreachable, misconfigured, unhealthy, or unable to serve real traffic.
4. Dockerfile order affects build cache and speed; base image, `.dockerignore`, secret handling, user, and multi-stage design affect security.
5. Docker images are the artifact Kubernetes consumes. Understanding images, ports, health, config, secrets, and storage prevents wrong translations from local Docker to cluster workloads.

## Source Backbone

- Docker overview: <https://docs.docker.com/get-started/docker-overview/>
- Dockerfile best practices: <https://docs.docker.com/build/building/best-practices/>
- Docker storage: <https://docs.docker.com/engine/storage/>
- Docker networking: <https://docs.docker.com/engine/network/>
- Docker Compose Specification: <https://docs.docker.com/reference/compose-file/>
- Docker Engine security: <https://docs.docker.com/engine/security/>
- Kubernetes images: <https://kubernetes.io/docs/concepts/containers/images/>
