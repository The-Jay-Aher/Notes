# 10 - Hands-on Labs

## Why This Chapter Matters

Docker becomes clear when you make it fail in small, controlled ways. These labs are designed to teach not only the happy path, but also the interpretation habit: what command to run, what good output means, what bad output means, and what small detail matters later.

Run these labs on a local machine with Docker Engine or Docker Desktop. Commands assume a shell with Docker CLI access.

## The Big Picture

Lab sequence:

```text
run a container -> inspect lifecycle -> build an image -> understand layers -> persist data -> connect services -> use Compose -> debug failures -> harden runtime -> map to Kubernetes
```

## First-Principles Explanation

Hands-on Docker practice should move from artifact to runtime:

Cause: Docker concepts are easy to memorize incorrectly.

Mechanism: run commands, observe state, break assumptions, inspect evidence.

Immediate result: command output becomes meaningful.

Long-term impact: production debugging and interview answers become grounded in real behavior.

Next connected topic: Kubernetes labs, CI image builds, and platform operations.

## Lab Safety Rules

- Do not run cleanup commands blindly on a machine with important Docker volumes.
- Avoid using `docker system prune --volumes` unless you intentionally want to remove unused volumes.
- These labs use public images. In restricted corporate environments, registry access may need proxy/auth configuration.
- If using Docker Desktop, remember that filesystem paths and networking pass through a VM.
- If a command differs by platform, verify against current Docker documentation.

## Lab 1 - Run and Inspect a Short-Lived Container

### Objective

Understand that `docker run` creates a container from an image and that short-lived commands exit immediately.

### Commands

```bash
docker run --name hello-lab alpine:3.20 echo "hello from a container"
docker ps
docker ps -a --filter name=hello-lab
docker logs hello-lab
docker inspect --format '{{.State.Status}} {{.State.ExitCode}}' hello-lab
docker rm hello-lab
```

### Expected Output Meaning

- `docker ps` will not show it because it exited.
- `docker ps -a` will show it because the container object still exists.
- Logs show the printed message.
- Exit code `0` means the command completed successfully.

### Bad Output Clues

- Image pull fails: check internet, registry access, tag spelling.
- Docker daemon error: check Docker service/Desktop is running.

### Small Detail

Use `--rm` for temporary containers when you do not need post-exit inspection:

```bash
docker run --rm alpine:3.20 echo "clean exit"
```

## Lab 2 - Run a Web Server and Publish a Port

### Objective

Separate container port from host port.

### Commands

```bash
docker run -d --name web-lab -p 8080:80 nginx:1.27
docker ps --filter name=web-lab
docker port web-lab
curl http://localhost:8080
docker logs --tail 20 web-lab
docker rm -f web-lab
```

### Expected Output Meaning

- `0.0.0.0:8080->80/tcp` means host port 8080 forwards to container port 80.
- `curl` should return an Nginx page.

### Bad Output Clues

- `port is already allocated`: another process/container uses host port 8080.
- Browser fails but container runs: check port mapping and local firewall.

### Small Detail

Publishing a port can expose the service beyond localhost depending on host/network configuration. Bind to a specific host address if needed:

```bash
docker run -d --name web-lab -p 127.0.0.1:8080:80 nginx:1.27
```

## Lab 3 - Build a Simple Python Image

### Objective

Understand Dockerfile, build context, image tag, and runtime command.

### Files

Create a temporary lab directory manually, then place these files in it.

`app.py`:

```python
print("hello from image")
```

`Dockerfile`:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
```

### Commands

```bash
docker build -t python-lab:1 .
docker image ls python-lab
docker run --rm python-lab:1
```

### Expected Output Meaning

- Build creates an image tagged `python-lab:1`.
- Running the image prints from `app.py`.

### Bad Output Clues

- `COPY failed`: file is not in build context or path is wrong.
- `python:3.12-slim` pull fails: registry/network/auth problem.

### Small Detail

The final `.` in `docker build -t python-lab:1 .` is the build context. Docker cannot copy files outside the context unless they are provided through supported build features.

## Lab 4 - Observe Layer Cache

### Objective

See why Dockerfile order matters.

### Files

`requirements.txt`:

```text
flask==3.0.3
```

`app.py`:

```python
print("cache lab")
```

`Dockerfile`:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
CMD ["python", "app.py"]
```

### Commands

```bash
docker build -t cache-lab:1 .
docker build -t cache-lab:2 .
```

Now edit only `app.py` and rebuild:

```bash
docker build -t cache-lab:3 .
```

### Expected Output Meaning

The dependency installation layer should be reused when only app source changes.

### Bad Output Clues

If dependencies reinstall every time, Dockerfile ordering or build cache settings are wrong.

### Small Detail

For Node, copy `package*.json` before copying source. For Python, copy dependency lock/requirements files before source. The exact files vary by ecosystem.

## Lab 5 - Use `.dockerignore`

### Objective

Prevent unnecessary and sensitive files from entering the build context.

### File

`.dockerignore`:

```text
.git
.venv
__pycache__
node_modules
dist
*.log
.env
```

### Commands

```bash
docker build --progress=plain -t ignore-lab:1 .
```

### Expected Output Meaning

The build should send less context and avoid copying ignored files.

### Bad Output Clues

- Slow "load build context" step: context is too large.
- Secret appears in image: `.dockerignore` and Dockerfile copy rules are wrong.

### Small Detail

`.dockerignore` is not the same as `.gitignore`. Maintain it deliberately.

## Lab 6 - Multi-Stage Build

### Objective

Separate build tools from runtime image.

### Dockerfile

```dockerfile
FROM golang:1.23 AS build
WORKDIR /src
COPY main.go .
RUN go build -o /out/hello main.go

FROM scratch
COPY --from=build /out/hello /hello
CMD ["/hello"]
```

`main.go`:

```go
package main

import "fmt"

func main() {
	fmt.Println("hello from multi-stage")
}
```

### Commands

```bash
docker build -t multistage-lab:1 .
docker run --rm multistage-lab:1
docker image inspect multistage-lab:1
```

### Expected Output Meaning

Final image contains the compiled binary, not the Go toolchain.

### Bad Output Clues

- Binary fails in `scratch`: may need static build depending on language/runtime.
- Build stage name typo: `COPY --from=build` fails.

### Small Detail

Name stages with `AS build` instead of relying on numeric stage indexes. It survives Dockerfile reordering better.

## Lab 7 - Named Volume Persistence

### Objective

See data persist after container replacement.

### Commands

```bash
docker volume create volume-lab
docker run --rm -v volume-lab:/data alpine:3.20 sh -c 'date > /data/created.txt'
docker run --rm -v volume-lab:/data alpine:3.20 cat /data/created.txt
docker volume inspect volume-lab
docker volume rm volume-lab
```

### Expected Output Meaning

The second container reads data written by the first container because both mounted the same volume.

### Bad Output Clues

- File missing: wrong mount target or different volume name.
- Volume removal fails: another container still uses it.

### Small Detail

Volumes are managed by Docker. Do not casually edit volume internals from the host path shown by inspect.

## Lab 8 - Bind Mount and Read-Only Mount

### Objective

Understand host path mounts and write protection.

### Commands

```bash
mkdir -p bind-lab
printf 'hello\n' > bind-lab/message.txt
docker run --rm --mount type=bind,src="$PWD/bind-lab",dst=/data,ro alpine:3.20 cat /data/message.txt
docker run --rm --mount type=bind,src="$PWD/bind-lab",dst=/data,ro alpine:3.20 sh -c 'echo fail > /data/new.txt'
```

### Expected Output Meaning

The first command reads the host file. The second should fail because the mount is read-only.

### Bad Output Clues

- Source path error: with `--mount`, missing paths fail instead of being silently created.
- Permission denied: check host permissions and container user.

### Small Detail

Prefer `--mount` for clarity. The shorter `-v` syntax can create missing host directories in ways that hide mistakes.

## Lab 9 - User-Defined Bridge Network

### Objective

Learn container DNS on user-defined networks.

### Commands

```bash
docker network create net-lab
docker run -d --name web-lab --network net-lab nginx:1.27
docker run --rm --network net-lab curlimages/curl:8.8.0 curl -s http://web-lab:80
docker rm -f web-lab
docker network rm net-lab
```

### Expected Output Meaning

The curl container resolves `web-lab` by container name on the same user-defined bridge network.

### Bad Output Clues

- DNS fails: not on same user-defined network or wrong name.
- HTTP fails: service not listening or container not running.

### Small Detail

Container-to-container access on the same Docker network does not require publishing a host port.

## Lab 10 - Compose Local Stack

### Objective

Replace multiple `docker run` commands with a Compose file.

### compose.yml

```yaml
services:
  web:
    image: nginx:1.27
    ports:
      - "8080:80"

  redis:
    image: redis:7
```

### Commands

```bash
docker compose up -d
docker compose ps
docker compose logs --tail 20 web
curl http://localhost:8080
docker compose down
```

### Expected Output Meaning

Compose creates project-scoped containers and a default network. Services can resolve each other by service name inside that network.

### Bad Output Clues

- Port conflict: host port 8080 already used.
- Wrong directory: Compose project name and file path may not be what you think.

### Small Detail

Use this command before debugging a complex Compose stack:

```bash
docker compose config
```

It shows the resolved configuration.

## Lab 11 - Compose Health Check and Dependency Race

### Objective

Understand that startup order is not the same as readiness.

### compose.yml

```yaml
services:
  api:
    image: curlimages/curl:8.8.0
    command: ["sh", "-c", "while true; do curl -fsS http://web || true; sleep 5; done"]
    depends_on:
      - web

  web:
    image: nginx:1.27
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 10s
      timeout: 3s
      retries: 3
```

### Commands

```bash
docker compose up
```

### Expected Output Meaning

`api` can start before `web` is truly ready. Real applications need retry logic and meaningful health checks.

### Bad Output Clues

If `curl` is missing inside `nginx`, the health check fails because the image lacks the tool. Health check commands must exist inside the container.

### Small Detail

Health check commands run inside the container, with that container's filesystem and tools.

## Lab 12 - Debug an Exiting Container

### Objective

Practice exit-code and log-based diagnosis.

### Command

```bash
docker run --name broken-lab alpine:3.20 sh -c 'echo starting; exit 42'
docker ps -a --filter name=broken-lab
docker logs broken-lab
docker inspect --format '{{.State.Status}} {{.State.ExitCode}}' broken-lab
docker rm broken-lab
```

### Expected Output Meaning

The container exits with code `42`. Docker is not broken; the process did exactly what it was told.

### Small Detail

An exited container can still be inspected until removed. Avoid `--rm` while investigating failures.

## Lab 13 - Run as Non-Root

### Objective

Experience file permission assumptions.

### Command

```bash
docker run --rm --user 1000:1000 alpine:3.20 id
docker run --rm --user 1000:1000 alpine:3.20 sh -c 'touch /root/test'
```

### Expected Output Meaning

The first command shows non-root identity. The second should fail because the user cannot write in `/root`.

### Small Detail

Non-root containers require writable paths to be owned or permitted correctly. Production hardening is design work, not just adding `USER`.

## Lab 14 - Read-Only Filesystem

### Objective

See how strict runtime settings reveal app write paths.

### Commands

```bash
docker run --rm --read-only alpine:3.20 sh -c 'touch /tmp/test'
docker run --rm --read-only --tmpfs /tmp alpine:3.20 sh -c 'touch /tmp/test && echo ok'
```

### Expected Output Meaning

The first command may fail because the root filesystem is read-only. The second gives `/tmp` a writable tmpfs mount.

### Small Detail

Read-only root filesystems are safer, but apps often need explicit writable temp/cache directories.

## Lab 15 - Translate Docker Thinking to Kubernetes

### Objective

Map image, port, env, and health concepts into a Kubernetes Pod/Deployment mindset.

### Docker Command

```bash
docker run -d --name api -p 8080:8080 -e APP_ENV=prod myregistry.example.com/api:1.2.3
```

### Kubernetes Sketch

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: myregistry.example.com/api:1.2.3
          env:
            - name: APP_ENV
              value: prod
          ports:
            - containerPort: 8080
```

### Interpretation

- Docker publishes host ports with `-p`.
- Kubernetes usually exposes Pods through a Service, not by publishing a node port for every Pod directly.
- The image is the shared concept.
- Runtime config becomes Pod spec fields.

### Small Detail

Kubernetes desired state means a manually modified container is disposable. Put changes in image/config manifests.

## Common Misunderstandings

| Misunderstanding | Correction |
| --- | --- |
| Labs should only show successful commands. | Controlled failure teaches the debugging map. |
| If a lab fails, Docker is broken. | Read the failure layer: pull, daemon, build, mount, network, app. |
| Local Compose success proves production readiness. | Compose is local wiring. Production needs durability, security, monitoring, rollout, and orchestration. |

## Failure Modes / Mistakes / Traps

- Running labs in a directory with real secrets and no `.dockerignore`.
- Running volume prune on a machine with important databases.
- Using `latest` and then not knowing which image ran.
- Forgetting that Docker Desktop uses a VM boundary.
- Copying lab `depends_on` patterns into production without retries/readiness.
- Treating temporary `docker exec` modifications as durable fixes.

## Debugging / Analysis Method

After each lab, answer:

1. What object did I create: image, container, volume, network, or Compose project?
2. What state does Docker report?
3. What logs exist?
4. What would be lost if I removed the container?
5. What would remain if I removed the container?
6. What would break on another machine?
7. What command proves my interpretation?

## Real-World or Exam Relevance

Hands-on labs prepare you for:

- debugging CI Docker builds
- answering Docker interview prompts
- writing production Dockerfiles
- designing Compose dev stacks
- recognizing Kubernetes mappings
- avoiding destructive cleanup
- explaining image layers and runtime state under pressure

## Connected Topics

- [Docker CLI and Container Lifecycle](2%20-%20Docker%20CLI%20and%20Container%20Lifecycle.md)
- [Dockerfiles and Image Builds](3%20-%20Dockerfiles%20and%20Image%20Builds.md)
- [Volumes and Networking](4%20-%20Volumes%20and%20Networking.md)
- [Docker Compose](5%20-%20Docker%20Compose.md)
- [Debugging and Operations Playbook](8%20-%20Debugging%20and%20Operations%20Playbook.md)

## Chapter Summary

The goal of these labs is not to finish commands. The goal is to build operational instinct: create the Docker object, inspect the Docker object, understand its lifecycle, identify the boundary, and move the fix into source-controlled configuration.

## Questions to Test Understanding

1. Why should you avoid `--rm` while investigating a failing container?
2. Why does a user-defined network help service discovery?
3. Why is `.dockerignore` part of build security?
4. Why does a read-only root filesystem break some apps?
5. Why is `docker compose config` useful before debugging?

## Answers and Reasoning

1. `--rm` removes the container after exit, so you lose inspectable state.
2. User-defined bridge networks provide container-name DNS and isolation from unrelated stacks.
3. It prevents unnecessary or sensitive files from entering the build context.
4. Apps often write temp files, caches, logs, or sockets unless writable paths are mounted.
5. It shows the resolved Compose configuration after interpolation, defaults, and merges.

## Source Backbone

- Docker CLI reference: <https://docs.docker.com/reference/cli/docker/>
- Dockerfile best practices: <https://docs.docker.com/build/building/best-practices/>
- Docker storage: <https://docs.docker.com/engine/storage/>
- Docker networking: <https://docs.docker.com/engine/network/>
- Docker Compose CLI reference: <https://docs.docker.com/reference/cli/docker/compose/>
