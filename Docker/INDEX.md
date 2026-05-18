# Docker

## Quick Summary

Docker is a platform for packaging applications into container images and running those images as containers. A container is not a full virtual machine; it is an isolated process that uses the host operating system kernel while carrying its own filesystem, dependencies, and startup command.

Use this folder to learn Docker from beginner to practical DevOps usage.

## Learning Order

| Order | Note | Focus |
| --- | --- | --- |
| 1 | [Containers and Images](1%20-%20Containers%20and%20Images.md) | What containers are, what images are, how Docker fits into DevOps. |
| 2 | [Docker CLI and Container Lifecycle](2%20-%20Docker%20CLI%20and%20Container%20Lifecycle.md) | Running, stopping, inspecting, logging, and cleaning containers. |
| 3 | [Dockerfiles and Image Builds](3%20-%20Dockerfiles%20and%20Image%20Builds.md) | Dockerfile instructions, build context, layers, cache, multi-stage builds. |
| 4 | [Volumes and Networking](4%20-%20Volumes%20and%20Networking.md) | Data persistence, bind mounts, named volumes, bridge networks, published ports. |
| 5 | [Docker Compose](5%20-%20Docker%20Compose.md) | Multi-container apps, services, networks, volumes, environment variables. |
| 6 | [Docker Security and Best Practices](6%20-%20Docker%20Security%20and%20Best%20Practices.md) | Smaller images, non-root containers, secrets, scanning, Docker socket risks. |

## Mental Model

```text
Dockerfile -> image -> container
```

- A **Dockerfile** is the recipe.
- An **image** is the packaged application template.
- A **container** is a running instance of the image.

## Official References

- Docker overview: <https://docs.docker.com/engine/docker-overview/>
- Dockerfile reference: <https://docs.docker.com/reference/builder>
- Dockerfile best practices: <https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/>
- Docker Compose: <https://docs.docker.com/compose/>

