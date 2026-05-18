# 6 - Docker Security and Best Practices

## Quick Summary

Docker security is about reducing image risk, runtime privilege, secret exposure, host access, and supply-chain problems. Docker makes packaging easier, but a container can still be insecure if the image, Dockerfile, runtime user, mounted paths, or credentials are poorly handled.

## Image Best Practices

- Use trusted base images.
- Use specific tags or digests for production.
- Rebuild images regularly.
- Keep images small.
- Use multi-stage builds.
- Remove build tools from final image.
- Do not copy secrets into images.
- Use `.dockerignore`.

## Runtime Best Practices

- Run as non-root where possible.
- Drop unnecessary Linux capabilities.
- Avoid privileged containers.
- Mount only required paths.
- Keep filesystems read-only when practical.
- Publish only required ports.
- Use resource limits where appropriate.

Example:

```bash
docker run --read-only --cap-drop ALL --user 1000:1000 myapp:1.0.0
```

Not every app works with this strict setup immediately, but it shows the direction.

## Non-Root Containers

Dockerfile example:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
RUN useradd --create-home appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER appuser
CMD ["python", "app.py"]
```

Why:

- Reduces impact if the app is compromised.
- Avoids root-owned output files.
- Better default for Kubernetes security contexts.

## Secrets

Avoid:

```dockerfile
ENV API_KEY=real-secret
COPY secret.txt /app/secret.txt
```

Better:

- Inject secrets at runtime.
- Use CI/CD secret stores.
- Use cloud secret managers.
- Use Docker/Compose secrets where appropriate.
- Rotate secrets if leaked.

## Docker Socket Risk

Mounting Docker socket:

```bash
-v /var/run/docker.sock:/var/run/docker.sock
```

This effectively gives the container control over the host Docker daemon. A compromised container may gain host-level control.

Use only when necessary and with strong isolation/trust boundaries.

## Image Scanning

Scan for:

- OS package vulnerabilities.
- Language dependency vulnerabilities.
- Secrets.
- Malware/suspicious files.
- Misconfiguration.

Common places:

- Docker Desktop/Docker Scout.
- CI pipeline scanner.
- Container registry scanner.
- Cloud provider scanner such as ECR scanning.

## Build Best Practices

Dockerfile pattern:

```dockerfile
FROM node:22 AS build
WORKDIR /app
COPY package*.json .
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1.27-alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

Why this is better:

- Dependencies install before source copy for cache efficiency.
- Final image does not include Node build tooling.
- Smaller attack surface.

## Supply Chain Controls

- Pin base images.
- Use trusted registries.
- Sign images where required.
- Generate SBOM where useful.
- Scan in CI.
- Promote the same tested image to production.
- Restrict who can push production tags.

## Benefits

- Smaller blast radius.
- Fewer vulnerabilities.
- More repeatable builds.
- Safer CI/CD and runtime behavior.

## Drawbacks / Limitations

- Strict security settings can break apps until fixed.
- Image scanning can be noisy.
- Pinning versions requires update discipline.
- Some legacy apps assume root or writable filesystems.

## Hidden Details / Caveats

- Deleting secrets in a later Dockerfile layer may not remove them from image history.
- `USER` affects runtime permissions but not earlier build steps.
- `EXPOSE` is documentation, not firewalling.
- Rootless Docker and non-root containers are different concepts.
- Docker image tags are mutable; digest pinning is stronger.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Running everything as root | Use `USER` and proper file ownership. |
| Putting secrets in Dockerfile | Inject secrets at runtime. |
| Mounting Docker socket in CI casually | Treat as privileged host access. |
| Huge image with build tools | Use multi-stage builds. |
| No scanning | Add image/dependency scanning. |
| Using `latest` in production | Use version tags or digests. |

## Troubleshooting

| Problem | Check |
| --- | --- |
| App fails as non-root | File ownership, privileged ports, write paths. |
| Read-only filesystem breaks app | Identify required writable directories and mount tmp/volume. |
| Scanner reports many CVEs | Update base image, remove packages, assess reachability. |
| Secret leaked in image | Rotate secret and rebuild without it; consider registry cleanup. |
| Permission denied on bind mount | Host UID/GID and container user. |

## Interview Notes

- Containers are not complete security boundaries by themselves.
- Run as non-root where possible.
- Avoid privileged containers and Docker socket mounts.
- Use `.dockerignore`, multi-stage builds, and small trusted base images.
- Do not bake secrets into images.
- Scan images and rebuild regularly.

## Related Topics

- [Dockerfiles and Image Builds](3%20-%20Dockerfiles%20and%20Image%20Builds.md)
- [Docker Compose](5%20-%20Docker%20Compose.md)
- [Introduction to DevSecOps for Cloud](../Introduction%20to%20DevSecOps%20for%20Cloud/INDEX.md)

## Official References

- [Docker security](https://docs.docker.com/engine/security/)
- [Docker rootless mode](https://docs.docker.com/engine/security/rootless/)
- [Dockerfile best practices](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)
