# 4 - Running Jenkins in Docker

## Containers vs Virtual Machines

- **VMs:** Include full guest OS + kernel abstraction.
- **Containers:** Share host kernel (on Linux-native container setups).

This generally makes containers lighter and faster to start.

## Basic Jenkins Docker Commands

### Pull image

```bash
docker pull jenkins/jenkins:lts
```

### Run Jenkins (basic)

```bash
docker run -p 8080:8080 --name jenkins-controller jenkins/jenkins:lts
```

### Run with UI + inbound agent port

```bash
docker run -d \
  -p 8080:8080 \
  -p 50000:50000 \
  --name jenkins-controller \
  jenkins/jenkins:lts
```

## Persisting Jenkins Data

Jenkins state should survive container recreation.

Example with volume mount:

```bash
docker run -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  --name jenkins-controller \
  jenkins/jenkins:lts
```

Why this matters:

- Preserves jobs, plugins, credentials metadata, and config.
- Simplifies upgrades/rollback.

## Accessing Container Shell

```bash
docker exec -it jenkins-controller /bin/bash
```

## Controller and Agent Best Practice

- Keep controller focused on orchestration.
- Run builds on dedicated agents.
- Prefer ephemeral agents for scalability and isolation.

## Image and Supply Chain Security

- Use trusted base images.
- Pin image tags intentionally.
- Minimize installed packages.
- Scan images for vulnerabilities.

## Quick Summary

1. Docker makes Jenkins deployment reproducible.
2. Persistent storage for `JENKINS_HOME` is mandatory for real use.
3. Separate controller and build execution for security and performance.
