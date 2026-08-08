# 12 - Cheatsheet

## Why This Chapter Matters

A cheatsheet is not a replacement for understanding. It is a fast retrieval layer after understanding. Use this file when you need the right command, the right distinction, or the right debugging path quickly.

## The Big Picture

```text
Dockerfile -> image -> registry -> container -> logs/network/storage/security -> Compose -> Kubernetes
```

## First-Principles Explanation

If you forget a command, derive it from the object:

- image commands manage packaged templates
- container commands manage runtime instances
- volume commands manage persistent Docker storage
- network commands manage connectivity scopes
- compose commands manage a local application project
- build commands create images from context and Dockerfile

## Core Vocabulary Fast Table

| Concept | One-line meaning |
| --- | --- |
| Image | Read-only container template. |
| Container | Running or stopped instance of an image. |
| Layer | Immutable filesystem change in an image. |
| Writable layer | Per-container write area. |
| Volume | Docker-managed persistent storage. |
| Bind mount | Host path mounted into container. |
| Registry | Image storage/distribution service. |
| Tag | Human-readable image pointer. |
| Digest | Exact content identity. |
| Compose service | Container configuration in Compose. |

## Daily Commands

### Check Docker

```bash
docker version
docker info
```

Use when:

- Docker CLI cannot connect.
- You need daemon details, storage driver, cgroups, rootless status, or platform context.

### Images

```bash
docker images
docker pull nginx:1.27
docker image inspect nginx:1.27
docker rmi nginx:1.27
```

Interpretation:

- `docker pull` fetches image metadata/layers.
- `docker image inspect` reveals config, architecture, env, entrypoint, labels, and layers.

### Containers

```bash
docker run --rm alpine:3.20 echo hello
docker run -it ubuntu:24.04 bash
docker run -d --name web -p 8080:80 nginx:1.27
docker ps
docker ps -a
docker stop web
docker start web
docker restart web
docker rm web
docker rm -f web
```

Interpretation:

- `run` creates a new container.
- `start` starts an existing stopped container.
- `rm` removes the container object and its writable layer.
- `rm -f` stops and removes.

### Logs and Exec

```bash
docker logs web
docker logs -f --tail 100 web
docker exec -it web sh
docker exec web env
docker exec web ps
```

Interpretation:

- Logs usually come from stdout/stderr.
- `exec` requires the container to be running.

### Inspect

```bash
docker inspect web
docker inspect --format '{{.State.Status}} {{.State.ExitCode}}' web
docker inspect --format '{{json .Mounts}}' web
docker inspect --format '{{json .NetworkSettings.Networks}}' web
```

Use when:

- Runtime config differs from what you expected.
- You need exact mounts, env, networks, ports, user, or state.

## Build Cheatsheet

### Build

```bash
docker build -t myapp:dev .
docker build --no-cache -t myapp:debug .
docker build --pull -t myapp:dev .
docker build --progress=plain -t myapp:dev .
```

Interpretation:

- `.` is the build context.
- `--no-cache` forces rebuild of layers.
- `--pull` checks for a newer base image.
- `--progress=plain` is useful in CI/debugging.

### Dockerfile Pattern: Python

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER 1000:1000
CMD ["python", "app.py"]
```

### Dockerfile Pattern: Node Multi-Stage

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

### `.dockerignore` Starter

```text
.git
.venv
__pycache__
node_modules
dist
build
*.log
.env
coverage
```

## Dockerfile Instruction Quick Meaning

| Instruction | Meaning | Gotcha |
| --- | --- | --- |
| `FROM` | Base image/stage. | Pin meaningful versions. |
| `WORKDIR` | Set working directory. | Avoid accidental root-directory commands. |
| `COPY` | Copy files from context/stage. | Cannot copy arbitrary files outside context. |
| `ADD` | Copy with extra features. | Prefer `COPY` unless extras are needed. |
| `RUN` | Build-time command. | Creates build layer. |
| `CMD` | Default runtime command/args. | Can be overridden. |
| `ENTRYPOINT` | Executable-style runtime entry. | Harder to override if misused. |
| `ENV` | Runtime/build env persisted in image. | Do not store secrets. |
| `ARG` | Build-time variable. | Not secret storage. |
| `EXPOSE` | Document container port. | Does not publish host port. |
| `USER` | Runtime user for later instructions/container. | File ownership must match. |
| `HEALTHCHECK` | Container health command. | Command must exist in image. |

## Storage Cheatsheet

### Named Volumes

```bash
docker volume create db-data
docker run -d --name db -v db-data:/var/lib/postgresql/data postgres:16
docker volume inspect db-data
docker volume ls
docker volume rm db-data
```

Use for:

- database data
- durable app state
- Docker-managed persistence

### Bind Mounts

```bash
docker run --rm --mount type=bind,src="$PWD",dst=/app,ro alpine:3.20 ls /app
docker run --rm -v "$PWD":/app node:22 npm test
```

Use for:

- local source development
- host config files
- generated artifacts you want on host

Gotchas:

- bind mount can hide image files at target path
- writable bind mount can modify host files
- remote daemon path is on daemon host
- Docker Desktop crosses VM boundary

### tmpfs

```bash
docker run --rm --tmpfs /tmp alpine:3.20 sh -c 'touch /tmp/test'
```

Use for:

- temporary sensitive data
- scratch space
- avoiding disk writes

## Network Cheatsheet

### Basic

```bash
docker network ls
docker network create app-net
docker run -d --name api --network app-net myapi:dev
docker run --rm --network app-net curlimages/curl:8.8.0 curl http://api:8080
docker network inspect app-net
docker network rm app-net
```

### Port Publishing

```bash
docker run -d --name web -p 8080:80 nginx:1.27
docker run -d --name web-local -p 127.0.0.1:8080:80 nginx:1.27
docker port web
```

Meaning:

```text
host port 8080 -> container port 80
```

Gotchas:

- container-to-container traffic on same network does not need host port publishing
- `localhost` inside a container is that container
- app must listen on correct interface, often `0.0.0.0`
- published ports may bind broadly if host address is not specified

## Compose Cheatsheet

### Common Commands

```bash
docker compose up
docker compose up -d
docker compose down
docker compose down -v
docker compose ps
docker compose logs -f
docker compose logs -f app
docker compose exec app sh
docker compose build
docker compose pull
docker compose restart
docker compose config
```

### Compose Template

```yaml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8080:8080"
    environment:
      APP_ENV: dev
      DATABASE_URL: postgres://app:app@db:5432/app
    depends_on:
      - db
    volumes:
      - .:/app

  db:
    image: postgres:16
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: app
      POSTGRES_DB: app
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

Gotchas:

- `depends_on` is not full readiness.
- service names become DNS names on Compose network.
- `down -v` removes volumes.
- secrets should not be committed in `.env`.
- relative bind paths are local Compose runtime behavior.

## Security Cheatsheet

### Build Security

- use trusted base images
- pin meaningful versions
- rebuild often
- use `.dockerignore`
- use multi-stage builds
- do not copy secrets
- scan images and dependencies
- keep final image small

### Runtime Security

```bash
docker run --read-only --cap-drop ALL --user 1000:1000 myapp:1.0.0
```

Adjust based on app needs:

- add only required capabilities
- mount only required paths
- use read-only mounts where possible
- avoid privileged mode
- avoid Docker socket mounts
- pass secrets at runtime

### Docker Socket Warning

```bash
-v /var/run/docker.sock:/var/run/docker.sock
```

Treat this as highly privileged. A container with daemon access can often control host-level container behavior.

## Debugging Cheatsheet

### Container Exited

```bash
docker ps -a
docker logs <container>
docker inspect --format '{{.State.ExitCode}} {{.State.Error}}' <container>
```

### Cannot Reach Web App

```bash
docker ps
docker port <container>
docker logs <container>
docker exec <container> sh -c 'ss -lntp || netstat -lntp'
```

Check:

- host port
- container port
- bind address
- app logs
- firewall

### DNS / Network

```bash
docker network inspect <network>
docker exec <container> getent hosts <peer>
docker exec <container> ping <peer>
```

### Mount / Data

```bash
docker inspect --format '{{json .Mounts}}' <container>
docker volume inspect <volume>
docker exec <container> id
ls -ln <host-path>
```

### Disk Cleanup

```bash
docker system df
docker container prune
docker image prune
docker builder prune
docker volume prune
```

Warning: inspect volumes before pruning.

## Docker to Kubernetes Quick Map

| Docker | Kubernetes |
| --- | --- |
| image | container image in Pod spec |
| `docker run` | Pod container spec |
| `-e` | `env` / ConfigMap / Secret |
| `-v named:/path` | PVC or volume |
| bind mount | `hostPath` volume, usually avoid unless necessary |
| `-p` | Service / Ingress / Gateway |
| healthcheck | readiness/liveness/startup probes |
| restart policy | Pod restart policy plus controller behavior |
| Compose service | Deployment plus Service, depending on role |

## Small Details That Matter Later

- `docker run` creates new containers; repeated runs can leave many stopped containers.
- `--rm` is good for temporary commands but bad for post-failure inspection.
- `EXPOSE` is not a firewall rule and not host publishing.
- `docker compose down` keeps named volumes; `docker compose down -v` removes project volumes.
- `--mount` syntax is clearer and stricter than `-v`.
- A health check using `curl` requires `curl` inside the image.
- `USER` can be overridden at runtime.
- Tags can be moved; digests cannot be moved without changing content identity.
- Docker Desktop path behavior differs from native Linux.
- Build args and env vars are not secret storage.

## Common Misunderstandings

| Wrong shortcut | Better memory |
| --- | --- |
| Image equals container. | Image creates container. |
| `latest` means newest. | `latest` is just a tag. |
| `EXPOSE` publishes. | `-p` publishes. |
| Volume and bind mount are same. | Volume is Docker-managed; bind mount is host path. |
| Compose is Kubernetes. | Compose is local stack; Kubernetes is cluster desired state. |

## Failure Modes / Mistakes / Traps

- wrong build context
- missing `.dockerignore`
- dependency install after source copy
- mutable production tags
- storing data in writable layer
- using `localhost` for another container
- publishing database ports unnecessarily
- committing `.env` secrets
- using privileged containers to hide permission issues
- deleting volumes during cleanup

## Chapter Summary

Use this cheatsheet as a command map. For real troubleshooting, pair each command with the deeper chapters so you understand why the output matters.

## Questions to Test Understanding

1. Which command shows all containers, including stopped ones?
2. Which command shows resolved Compose configuration?
3. Which flag publishes host port 8080 to container port 80?
4. Which cleanup command is most dangerous for local database data?
5. Which Dockerfile file reduces build context?

## Answers and Reasoning

1. `docker ps -a`.
2. `docker compose config`.
3. `-p 8080:80`.
4. `docker volume prune` or `docker compose down -v`, depending on context.
5. `.dockerignore`.

## Source Backbone

- Docker CLI reference: <https://docs.docker.com/reference/cli/docker/>
- Dockerfile reference: <https://docs.docker.com/reference/builder/>
- Docker storage: <https://docs.docker.com/engine/storage/>
- Docker networking: <https://docs.docker.com/engine/network/>
- Docker Compose CLI reference: <https://docs.docker.com/reference/cli/docker/compose/>
