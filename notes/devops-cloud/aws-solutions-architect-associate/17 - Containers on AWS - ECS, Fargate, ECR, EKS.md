# Containers on AWS: ECS, Fargate, ECR, EKS

## Quick Summary
- Containers package an application with its runtime dependencies so it runs consistently across environments.
- Amazon ECR stores container images.
- Amazon ECS runs containers using AWS-native orchestration.
- AWS Fargate runs containers without managing EC2 worker nodes.
- Amazon EKS runs Kubernetes on AWS.
- Choose ECS for simpler AWS-native container orchestration, EKS for Kubernetes compatibility, and Fargate when you want serverless container compute.

## Containers in Plain English
A container is a packaged application process.

It usually includes:
- Application code.
- Runtime such as Node.js, Python, Java, or Go binary.
- System libraries.
- A startup command.

It does not include a full operating system like a virtual machine. Containers share the host OS kernel.

Basic flow:

```text
Dockerfile -> image -> registry -> container runtime -> running container
```

On AWS:

```text
Build image -> push to ECR -> run with ECS/EKS/App Runner/Fargate
```

## Amazon ECR
Amazon Elastic Container Registry stores container images.

Use ECR for:
- Private image repositories.
- Pulling images into ECS, EKS, Lambda container functions, and other compute.
- Image scanning.
- Lifecycle policies to clean old images.
- Cross-account or cross-Region image sharing when configured.

### ECR Concepts
| Concept | Meaning |
|---|---|
| Registry | Top-level ECR image storage for an AWS account and Region |
| Repository | Collection of related images |
| Image tag | Human-readable label such as `v1.2.0` or `latest` |
| Image digest | Immutable content hash |
| Lifecycle policy | Rule to expire old images |

Best practice:
- Use immutable version tags or digests for production deployments.
- Avoid relying on `latest` for stable production rollouts.

## Amazon ECS
Amazon Elastic Container Service is AWS-native container orchestration.

It schedules containers, keeps desired counts running, integrates with load balancers, and manages service deployments.

### ECS Mental Model
```text
ECS cluster
  -> ECS service
       -> ECS tasks
            -> containers from ECR images
```

### ECS Concepts
| Concept | Meaning |
|---|---|
| Cluster | Logical grouping of compute capacity |
| Task definition | Blueprint for running containers |
| Task | Running copy of a task definition |
| Service | Keeps a desired number of tasks running |
| Container definition | Image, ports, env vars, resources, logs |
| Capacity provider | Defines whether tasks run on Fargate or EC2 capacity |

### Task Definition
A task definition describes:
- Container image.
- CPU and memory.
- Port mappings.
- Environment variables.
- Secrets.
- IAM task role.
- Logging driver.
- Volumes.
- Health check.

Think of it as a recipe. A task is a running meal made from that recipe.

### ECS Service
An ECS service keeps tasks running.

Example:
- Desired count = 4.
- If one task stops, ECS starts another.
- If you deploy a new task definition revision, ECS replaces old tasks with new ones.

Services can integrate with:
- Application Load Balancer.
- Network Load Balancer.
- Service discovery.
- Auto Scaling.

## AWS Fargate
Fargate is serverless compute for containers.

With ECS on EC2:

```text
You manage EC2 instances -> ECS schedules containers on them
```

With ECS on Fargate:

```text
You define task CPU/memory -> AWS runs the container capacity
```

Use Fargate when:
- You do not want to manage EC2 worker nodes.
- Workloads have clear task CPU/memory needs.
- You want isolated task-level compute.
- You prefer simpler operations over fine-grained host control.

Use ECS on EC2 when:
- You need host-level customization.
- You need special instance types or GPUs.
- You want deeper control over bin-packing and cost.
- You already operate EC2 fleets.

## Amazon EKS
Amazon Elastic Kubernetes Service runs Kubernetes control plane components for you.

Use EKS when:
- Your organization standardizes on Kubernetes.
- You need Kubernetes APIs and ecosystem tools.
- You run workloads across multiple environments and want Kubernetes portability.
- You need Kubernetes-native controllers, operators, or CRDs.

### EKS Architecture
```text
AWS-managed Kubernetes control plane
        |
Worker nodes or Fargate profiles
        |
Pods running containers
```

Worker options:
- Managed node groups.
- Self-managed EC2 nodes.
- EKS on Fargate for eligible pod workloads.

### EKS vs ECS
| Topic | ECS | EKS |
|---|---|---|
| Orchestrator | AWS-native | Kubernetes |
| Learning curve | Usually simpler | Usually higher |
| Portability | AWS-focused | Kubernetes ecosystem |
| Control plane | Managed by AWS | Managed Kubernetes control plane |
| Best fit | AWS-native container apps | Kubernetes-standard organizations |

## Load Balancing Containers
Common patterns:
- ECS service behind Application Load Balancer for HTTP/HTTPS.
- ECS service behind Network Load Balancer for TCP/UDP or very high performance.
- EKS Ingress or AWS Load Balancer Controller to create ALB/NLB resources.

Health checks matter:
- Load balancer health check decides if traffic should go to a task/pod.
- Container health check decides if the container itself is healthy.
- Application readiness should not return success until dependencies are ready.

## Container IAM
Do not put AWS access keys inside images.

Use:
- ECS task roles for containers running on ECS.
- IAM Roles for Service Accounts (IRSA) or EKS Pod Identity for EKS workloads.
- Secrets Manager or SSM Parameter Store for secrets.

Separate roles:
- Task execution role: ECS uses it to pull images and write logs.
- Task role: application uses it to call AWS APIs.

## Container Networking
ECS commonly uses `awsvpc` networking mode for Fargate.

Important effects:
- Each task gets its own elastic network interface.
- Security groups can be applied at task level.
- Tasks live in VPC subnets.

For EKS:
- Pods get networking through the Kubernetes CNI plugin.
- Security and network policy depend on the selected setup.

## Logs and Observability
Common container logging design:

```text
Container stdout/stderr -> logging driver/agent -> CloudWatch Logs
```

Watch:
- Task/pod restarts.
- CPU and memory usage.
- Load balancer target health.
- Application errors.
- Deployment events.
- Image pull errors.

## Deployment Strategies
Common patterns:
- Rolling deployment: gradually replace old tasks/pods.
- Blue/green deployment: shift traffic from old environment to new environment.
- Canary deployment: send small traffic percentage to new version first.

AWS services involved:
- ECS service deployment controller.
- CodeDeploy for ECS blue/green.
- EKS with Kubernetes Deployment strategies and optional progressive delivery tools.

## Secrets in Containers
Bad:

```text
Hardcode database password in Docker image
```

Better:
- Store secret in Secrets Manager or SSM Parameter Store.
- Grant container IAM permission to read only needed secret.
- Inject at runtime or fetch at startup.
- Rotate secrets where possible.

## Common Exam Choices
| Requirement | Likely service |
|---|---|
| Store private Docker images | ECR |
| Run containers without managing servers | ECS with Fargate |
| AWS-native container orchestration | ECS |
| Kubernetes-compatible orchestration | EKS |
| Existing Kubernetes manifests | EKS |
| Need host-level customization | ECS on EC2 or EKS nodes |
| Simple web container with minimal orchestration needs | ECS/Fargate or App Runner depending on options |

## Common Mistakes
- Confusing ECR with ECS. ECR stores images; ECS runs containers.
- Confusing task role and task execution role.
- Using `latest` tag in production and not knowing what version is deployed.
- Putting secrets into images or plaintext environment files.
- Forgetting security groups and subnet routing for tasks.
- Under-sizing memory, causing container OOM exits.
- Ignoring image scanning and patching base images.
- Choosing EKS only because it sounds advanced, even when ECS would be simpler.

## Official References
- [Amazon ECS documentation](https://docs.aws.amazon.com/ecs/)
- [AWS Fargate documentation](https://docs.aws.amazon.com/fargate/)
- [Amazon ECR documentation](https://docs.aws.amazon.com/ecr/)
- [Amazon EKS documentation](https://docs.aws.amazon.com/eks/)
- [AWS App Runner documentation](https://docs.aws.amazon.com/apprunner/)
