# 13 - Glossary

## Why This Chapter Matters

Docker vocabulary is compact but easy to misuse. A student who confuses image, container, layer, registry, tag, digest, volume, and bind mount will misread documentation, fail interviews, and debug the wrong layer in production.

This glossary explains terms with practical significance instead of one-line dictionary definitions.

## The Big Picture

Docker terms belong to families:

- Build terms: Dockerfile, context, layer, cache, BuildKit.
- Artifact terms: image, tag, digest, registry, repository.
- Runtime terms: container, entrypoint, command, env, user, signal.
- Storage terms: writable layer, volume, bind mount, tmpfs.
- Network terms: bridge, host network, DNS, published port.
- Security terms: rootless, capabilities, seccomp, privileged, socket.
- Orchestration terms: Compose, service, Kubernetes Pod, probe.

## First-Principles Explanation

Technical vocabulary is useful only when it points to the correct mechanism.

Cause: Docker compresses many operating-system and delivery concepts into short words.

Mechanism: define each term by what it controls and what failure it explains.

Immediate result: commands and errors become easier to interpret.

Long-term impact: you can move from local Docker to CI/CD and Kubernetes without relearning the artifact model from scratch.

## Core Vocabulary

### `.dockerignore`

A file that excludes paths from the Docker build context. It reduces build time and helps prevent secrets, logs, dependency directories, and local artifacts from entering the build.

Small detail: `.dockerignore` is independent of `.gitignore`.

### `ADD`

Dockerfile instruction that copies files like `COPY` but also has extra behavior such as archive extraction and remote URL handling. Prefer `COPY` for ordinary file copying because it is more explicit.

### AppArmor

Linux security module that can restrict process behavior. Docker can use security profiles depending on host setup.

### ARG

Dockerfile build-time variable. It can parameterize builds but should not be treated as secret storage.

### Base Image

The image named in `FROM`. It provides the starting filesystem and metadata for later image layers.

Small detail: base image choice affects size, CVEs, package manager behavior, libc compatibility, and architecture support.

### Bind Mount

A host file or directory mounted into a container. Good for local development and host-config sharing. Risky if writable or if it exposes sensitive host paths.

Small detail: bind mounting over a non-empty container directory hides the image's files at that path while the mount exists.

### Bridge Network

Docker network driver that provides isolated networking on a single host. User-defined bridge networks support container-name DNS.

### Build Cache

Reused output from previous build steps. Good Dockerfile ordering lets dependency layers remain cached when app source changes.

### Build Context

The directory or source set sent to Docker build. Dockerfile `COPY` usually reads from this context.

Small detail: the final `.` in `docker build -t app .` is the build context.

### BuildKit

Modern Docker build engine. It improves build performance and enables advanced build features.

### Capability

Fine-grained Linux privilege. Docker can drop or add capabilities so a container does not need full root-style power.

### Cgroup

Linux kernel feature for resource accounting and limits. Docker uses cgroups for CPU, memory, and other resource controls.

### CMD

Dockerfile instruction defining the default command or default arguments for the container.

Small detail: `CMD` can be overridden at runtime.

### Compose

Docker tool for defining and running multi-container applications from a Compose YAML file.

Small detail: Compose is excellent for local development but is not the same as Kubernetes.

### Compose Project

The logical project Compose creates from a directory/name. Project name affects container, network, and volume names.

### Compose Service

A container configuration in a Compose file. A service can be scaled to multiple containers, but published ports must be designed carefully.

### Container

A runnable instance of an image plus runtime configuration. It has process state, network attachments, mounts, environment, and a writable layer.

Small detail: a stopped container still exists until removed.

### containerd

Container lifecycle manager used underneath Docker and commonly used by Kubernetes nodes through CRI.

### Copy-on-Write

Filesystem behavior where shared read-only image layers stay unchanged, and container modifications go into the container's own writable layer.

### CRI

Container Runtime Interface used by Kubernetes to talk to container runtimes. It is part of why Kubernetes does not depend on Docker CLI commands.

### Digest

Content hash identifying exact image content, often shown as `sha256:...`.

Small detail: digests are stronger than tags for reproducibility because tags can move.

### Docker Client

The `docker` CLI or another API client. It sends requests to the Docker daemon.

### Docker Daemon

Background service that manages Docker objects: images, containers, networks, volumes, and builds.

Small detail: access to the daemon is powerful. Protect the Docker socket.

### Docker Desktop

Docker's desktop distribution for macOS, Windows, and Linux. On macOS/Windows, Linux containers run through a Linux VM.

### Docker Engine

Core Docker runtime platform, including daemon/API components that manage Docker objects.

### Docker Hub

Public Docker registry service. Docker commonly pulls from Docker Hub by default when no registry hostname is specified.

### Docker Socket

Usually `/var/run/docker.sock`. It exposes Docker daemon API access.

Small detail: mounting it into a container can effectively give that container control over the Docker host's container environment.

### Dockerfile

Text file containing image build instructions.

### ENTRYPOINT

Dockerfile instruction that configures the container like an executable. Commonly paired with `CMD` for default arguments.

### Environment Variable

Key-value setting passed to the container process. Useful for runtime configuration, but not sufficient as a secure secret strategy by itself.

### EXPOSE

Dockerfile instruction documenting intended container ports.

Small detail: `EXPOSE` does not publish a host port.

### Health Check

Command that determines whether a container is healthy. In Compose and Docker, it marks health status. In Kubernetes, health semantics are split into liveness, readiness, and startup probes.

### Host Network

Network mode where a container uses the host network stack on Linux.

Small detail: this removes network namespace isolation for that container.

### Image

Read-only package/template used to create containers. It includes filesystem layers and metadata.

### Image Layer

Immutable filesystem change in an image. Layers explain cache reuse, image size, and some secret leakage risks.

### Image Repository

Named collection of image tags in a registry, such as `library/nginx` or `team/api`.

### Init Container

Kubernetes concept: a container that runs before app containers in a Pod. Useful for setup gates. Not a Docker Compose `depends_on` replacement in direct syntax, but conceptually related to startup sequencing.

### Kubernetes Pod

Smallest deployable Kubernetes workload unit. A Pod can contain one or more containers that share network namespace and certain volumes.

### Label

Metadata attached to Docker objects or Kubernetes objects. Useful for organization, selection, automation, and policy.

### Layer Cache

Build cache based on unchanged Dockerfile instructions and inputs. Good cache design speeds CI and local builds.

### Liveness Probe

Kubernetes check that decides whether a container should be restarted.

### Multi-Stage Build

Dockerfile pattern using multiple `FROM` stages. It lets you compile/build in one stage and copy only required artifacts into a smaller final stage.

### Namespace

Linux kernel feature that gives a process an isolated view of system resources such as process IDs, network, mounts, hostname, IPC, users, or cgroups.

### Named Volume

Docker-managed persistent storage object with a name. It survives container removal until explicitly removed.

### OCI

Open Container Initiative. Standards around container images and runtimes that support portability across tools and platforms.

### Orchestrator

System that manages containers across machines. Kubernetes is the dominant orchestrator.

### Overlay Filesystem

Layered filesystem approach that lets Docker present image layers plus a writable container layer as one filesystem.

### PID 1

The first process inside a container's PID namespace. It has special signal and child-process responsibilities.

Small detail: poor PID 1 behavior can cause bad shutdown handling.

### Port Publishing

Mapping a host port to a container port, usually with `-p HOST_PORT:CONTAINER_PORT`.

### Privileged Container

Container started with broad elevated privileges.

Small detail: `--privileged` is a major security boundary change, not a harmless troubleshooting flag.

### Readiness Probe

Kubernetes check that decides whether a Pod should receive traffic.

### Registry

Service that stores and distributes container images.

### Restart Policy

Docker/Compose setting controlling whether a container restarts after exit. Kubernetes has its own Pod/controller restart behavior.

### Rootless Docker

Mode where the Docker daemon and containers run as a non-root user using user namespaces, reducing some daemon/runtime risks.

### runc

OCI runtime used to create containers with Linux kernel primitives.

### SBOM

Software bill of materials: inventory of components in an artifact. Useful for vulnerability management and supply-chain review.

### Seccomp

Linux system call filtering. Docker can use seccomp profiles to restrict kernel calls.

### Secret

Sensitive value such as password, token, or key. Do not bake secrets into images or commit them in Compose env files.

### Service Discovery

How one service finds another. In Compose, service names resolve on the project network. In Kubernetes, Services and DNS provide discovery.

### Startup Probe

Kubernetes probe for slow-starting containers. It prevents liveness checks from killing an app before startup completes.

### Tag

Human-readable image reference label, such as `1.27` or `prod`.

Small detail: tags are mutable.

### tmpfs Mount

Memory-backed temporary filesystem mounted into a container. Data does not persist after container stop/restart/host reboot.

### User Namespace

Namespace that can map container users to different host users. Important for rootless and user-remapping security models.

### Volume Driver

Plugin/driver mechanism for Docker volumes. Can support storage beyond the default local driver.

### Writable Layer

Per-container filesystem layer where changes are written unless paths are mounted elsewhere.

Small detail: it is not durable storage for important data.

## Mental Model

Use this grouping:

```text
Build words explain how the image is made.
Artifact words explain how the image is named and distributed.
Runtime words explain how the process starts and behaves.
Storage/network words explain boundaries outside the process.
Security words explain how damage is limited.
Orchestration words explain what happens after one host is not enough.
```

## Small Details That Matter Later

- The same word "service" means different things in Compose and Kubernetes.
- A repository in a registry is not the same as a Git repository.
- A tag is not immutable evidence.
- Rootless Docker is different from a non-root container user.
- A volume is not automatically backed up.
- A bind mount is not portable unless every host has the same path and permissions.
- A health check can pass while a real dependency path fails.
- A container can be healthy locally and fail in Kubernetes due to probes, resources, security context, DNS, or storage class differences.
- Docker Desktop hides Linux VM details behind a friendly interface, but those details matter during path and network debugging.

## Common Misunderstandings

| Term confused | Better distinction |
| --- | --- |
| image vs container | package vs runtime instance |
| repository vs registry | named image collection vs storage service |
| tag vs digest | pointer vs content identity |
| volume vs bind mount | Docker-managed path vs host path |
| expose vs publish | document port vs forward host traffic |
| rootless vs non-root | daemon mode vs container process user |
| Compose service vs Kubernetes Service | container config vs stable network abstraction |

## Failure Modes / Mistakes / Traps

- Using the word "container" when you mean "image" during incident reports.
- Saying "Docker exposes port 8080" when only `EXPOSE` exists.
- Treating a tag as proof of exact content.
- Calling a bind mount a volume and then deleting the wrong thing.
- Assuming rootless Docker fixes all container security issues.
- Confusing Compose health checks with Kubernetes readiness/liveness semantics.

## Debugging / Analysis / Answer-Writing Method

When explaining a Docker term, answer five questions:

1. Which Docker object or lifecycle stage does it belong to?
2. What problem does it solve?
3. What command or YAML field exposes it?
4. What can go wrong with it?
5. What is the Kubernetes or production connection, if any?

Example:

```text
A volume belongs to runtime storage. It solves data persistence outside the container writable layer. Docker exposes it with docker volume commands, docker run mounts, or Compose volumes. It can go wrong when deleted accidentally, mounted at the wrong path, or assumed to be backed up. In Kubernetes, the related idea is usually a volume plus PersistentVolumeClaim, depending on the storage requirement.
```

## Real-World or Exam Relevance

Glossary precision helps in:

- writing incident reports
- explaining architecture diagrams
- reviewing Dockerfiles and Compose files
- answering interviews
- reading Docker and Kubernetes docs
- avoiding dangerous cleanup commands
- separating local development behavior from production behavior

## Connected Topics

- [Docker Roadmap and Source Backbone](00%20-%20Docker%20Roadmap%20and%20Source%20Backbone.md)
- [Container Architecture Deep Dive](7%20-%20Container%20Architecture%20Deep%20Dive.md)
- [Debugging and Operations Playbook](8%20-%20Debugging%20and%20Operations%20Playbook.md)
- [Production Gotchas and Kubernetes Connection](9%20-%20Production%20Gotchas%20and%20Kubernetes%20Connection.md)

## Chapter Summary

Docker vocabulary is operational vocabulary. Every term should help you predict behavior, diagnose failure, or design safer systems. If a term does not change what you would inspect or configure, you probably have not learned it deeply enough yet.

## Questions to Test Understanding

1. What is the difference between a registry and a repository?
2. Why is a digest stronger than a tag?
3. Why is a rootless daemon different from a non-root container process?
4. Why is a bind mount less portable than a named volume?
5. Why is a Kubernetes Service not the same as a Compose service?

## Answers and Reasoning

1. A registry stores and distributes images. A repository is a named collection of image tags inside a registry.
2. A digest identifies exact image content; a tag can be moved.
3. Rootless mode changes daemon/runtime privilege on the host. A non-root container process changes the user inside a container run by a daemon.
4. A bind mount depends on a specific host path and permissions. A named volume is managed by Docker.
5. A Compose service is a container configuration. A Kubernetes Service is a stable network abstraction selecting Pods.

## Source Backbone

- Docker overview: <https://docs.docker.com/get-started/docker-overview/>
- Dockerfile reference: <https://docs.docker.com/reference/builder/>
- Docker storage: <https://docs.docker.com/engine/storage/>
- Docker networking: <https://docs.docker.com/engine/network/>
- Docker Compose Specification: <https://docs.docker.com/reference/compose-file/>
- Docker Engine security: <https://docs.docker.com/engine/security/>
- Kubernetes images: <https://kubernetes.io/docs/concepts/containers/images/>
