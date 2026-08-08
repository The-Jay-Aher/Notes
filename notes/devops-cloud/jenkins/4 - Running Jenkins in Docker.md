# 4 - Running Jenkins in Docker

## Quick Summary

Running Jenkins in Docker is useful for local learning and reproducible controller setup. The most important rule is to persist Jenkins state by mounting `/var/jenkins_home`.

Docker makes startup easy, but production still requires backups, upgrades, security controls, and an agent strategy.

## Containers vs Virtual Machines

| Topic | Container | Virtual Machine |
| --- | --- | --- |
| Isolation | Process-level isolation using host kernel. | Full guest OS isolation. |
| Startup | Usually fast. | Usually slower. |
| Image | Application/runtime image. | Full OS image. |
| Persistence | Needs explicit volumes. | Disk usually persists with VM. |
| Best use | Reproducible app runtime. | Stronger OS-level boundary and long-running server patterns. |

## Basic Jenkins Docker Run

```bash
docker run --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts-jdk17
```

Ports:

| Port | Purpose |
| --- | --- |
| 8080 | Jenkins web UI. |
| 50000 | Inbound agent communication, if used. |

## Initial Admin Password

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

## Persistent Data

Jenkins stores important state in:

```text
/var/jenkins_home
```

Use a named volume:

```bash
docker volume create jenkins_home
```

Or a bind mount:

```bash
docker run --name jenkins \
  -p 8080:8080 \
  -v /srv/jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts-jdk17
```

Named volumes are convenient for local learning. Bind mounts are easier to inspect and back up explicitly.

## Docker Compose Example

```yaml
services:
  jenkins:
    image: jenkins/jenkins:lts-jdk17
    container_name: jenkins
    ports:
      - "8080:8080"
      - "50000:50000"
    volumes:
      - jenkins_home:/var/jenkins_home
    restart: unless-stopped

volumes:
  jenkins_home:
```

Start:

```bash
docker compose up -d
```

Logs:

```bash
docker logs -f jenkins
```

## Accessing Container Shell

```bash
docker exec -it jenkins bash
```

Use this for inspection, not routine manual configuration. Prefer Jenkins UI, Configuration as Code, or documented setup files.

## Controller And Agent Best Practice

Avoid running heavy builds on the Jenkins controller container.

Better pattern:

```text
Jenkins controller container -> separate agents -> build/test work
```

Agents may be:

- Static VMs.
- Docker containers.
- Kubernetes Pods.
- Cloud instances.

## Docker Socket Warning

A common shortcut is mounting Docker socket:

```bash
-v /var/run/docker.sock:/var/run/docker.sock
```

This allows jobs to control the host Docker daemon. That is powerful and risky. A job with Docker socket access can often gain host-level control.

Safer alternatives:

- Use dedicated isolated build agents.
- Use rootless builders where suitable.
- Use remote build services.
- Use container build tools designed for CI.
- Restrict who can modify jobs that access Docker.

## Upgrading Jenkins In Docker

Basic flow:

1. Back up `jenkins_home`.
2. Check plugin compatibility.
3. Pull newer image.
4. Stop old container.
5. Start new container with same volume.
6. Validate jobs and plugins.

Example:

```bash
docker pull jenkins/jenkins:lts-jdk17
docker stop jenkins
docker rm jenkins
docker run --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts-jdk17
```

Do not upgrade without a backup.

## Benefits

- Quick setup.
- Reproducible runtime image.
- Easy local cleanup.
- Works well with Docker Compose.
- Good for labs and small internal setups.

## Drawbacks / Limitations

- State persistence must be handled explicitly.
- Docker socket access can be dangerous.
- Containerized controller still needs backup and upgrade discipline.
- Jenkins agents/tooling need a separate design.
- File permissions on bind mounts can be confusing.

## Hidden Details / Caveats

- Removing a container does not remove named volumes unless explicitly removed.
- Removing an anonymous volume may lose state.
- Jenkins plugins and jobs live in the volume, not the image.
- The official image is a controller image, not automatically a complete CI platform.
- If you need preinstalled plugins/config, build a custom image or use Configuration as Code.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Running without a volume | Mount `/var/jenkins_home`. |
| Removing the volume accidentally | Back up before cleanup. |
| Building everything on controller | Use agents. |
| Mounting Docker socket casually | Treat as high privilege. |
| Upgrading image without backup | Back up and test. |
| Forgetting port 50000 for inbound agents | Publish it only if needed. |

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Jenkins state disappeared | Container/volume mapping. |
| Cannot open UI | Port mapping, container logs, firewall. |
| Permission denied in Jenkins home | Volume ownership and container user. |
| Plugins fail after restart | Plugin compatibility and update logs. |
| Docker commands fail in job | Docker CLI availability, socket/daemon access, permissions. |

## Interview Notes

- Persist `/var/jenkins_home`.
- Dockerizing Jenkins does not remove the need for backups.
- Controller should orchestrate; agents should run builds.
- Docker socket mounting is powerful and risky.
- Use Docker Compose for repeatable local setup.

## Related Topics

- [Jenkins Installation](2%20-%20Jenkins%20Installation.md)
- [Using and Managing Jenkins](3%20-%20Using%20and%20Managing%20Jenkins.md)

