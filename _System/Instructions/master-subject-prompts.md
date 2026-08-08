3. Topic-Specific Prompts You Can Directly Use
For CKA
Create or upgrade legendary-teacher-level notes for:

CKA - Certified Kubernetes Administrator

Follow AGENTS.md completely.

Focus heavily on:
- Kubernetes architecture
- control plane
- worker nodes
- API server
- etcd
- scheduler
- controllers
- kubelet
- kube-proxy
- container runtime
- CNI
- CSI
- Pods
- Deployments
- Services
- networking
- DNS
- storage
- RBAC
- security
- scheduling
- troubleshooting
- cluster maintenance
- upgrades
- etcd backup and restore
- kubeadm
- kubectl command mastery
- CKA exam tasks

Every command must include:
- purpose
- flags
- expected output
- bad output
- troubleshooting interpretation
- exam shortcut if useful

Add architecture diagrams and troubleshooting flowcharts.

If CKA notes already exist, upgrade them instead of duplicating them.
For CKAD
Create or upgrade legendary-teacher-level notes for:

CKAD - Certified Kubernetes Application Developer

Follow AGENTS.md completely.

Focus heavily on:
- Pods
- Deployments
- ReplicaSets
- Jobs
- CronJobs
- ConfigMaps
- Secrets
- Services
- probes
- init containers
- sidecars
- volumes
- service accounts
- security context
- resource requests and limits
- labels and selectors
- annotations
- namespaces
- Helm basics if relevant
- debugging application workloads
- kubectl command speed
- YAML writing
- CKAD exam traps

Explain every Kubernetes object from:
what it is → why it exists → how it behaves → common YAML mistakes → debugging → exam relevance.

If CKAD notes already exist, upgrade them instead of duplicating them.
For Kubernetes Architecture
Create or upgrade legendary-teacher-level notes for:

Kubernetes Architecture

Follow AGENTS.md completely.

This should not be shallow certification notes.
This should explain Kubernetes as a distributed system.

Focus on:
- why Kubernetes exists
- desired state vs actual state
- reconciliation loop
- declarative APIs
- API server
- etcd
- controllers
- scheduler
- kubelet
- kube-proxy
- CRI
- CNI
- CSI
- admission controllers
- watch mechanism
- object lifecycle
- Pod creation lifecycle
- Service networking
- DNS flow
- storage provisioning
- RBAC authorization flow
- failure boundaries
- scaling boundaries
- production design tradeoffs

Use Mermaid diagrams extensively.

If Kubernetes architecture notes already exist, upgrade them instead of duplicating them.
For AWS Solutions Architect Associate
Create or upgrade legendary-teacher-level notes for:

AWS Solutions Architect Associate

Follow AGENTS.md completely.

Focus on:
- cloud fundamentals
- AWS global infrastructure
- IAM
- VPC
- EC2
- EBS
- EFS
- S3
- RDS
- Aurora
- DynamoDB
- ELB
- Auto Scaling
- Route 53
- CloudFront
- SQS
- SNS
- EventBridge
- Lambda
- ECS
- EKS basics
- CloudWatch
- CloudTrail
- KMS
- Secrets Manager
- high availability
- fault tolerance
- security
- cost optimization
- disaster recovery
- Well-Architected Framework
- scenario-based exam questions

For every service:
explain what it is, why it exists, when to use it, when not to use it, limits, security, pricing traps, architecture patterns, and exam traps.

If notes already exist, upgrade them instead of duplicating them.
For AWS Solutions Architect Professional
Create or upgrade legendary-teacher-level notes for:

AWS Solutions Architect Professional

Follow AGENTS.md completely.

Focus on advanced architecture and scenario judgment.

Include:
- multi-account strategy
- AWS Organizations
- SCPs
- IAM boundaries
- advanced VPC design
- Transit Gateway
- Direct Connect
- VPN
- hybrid networking
- multi-region architecture
- disaster recovery strategies
- migration planning
- cost optimization at scale
- advanced security architecture
- logging and governance
- workload modernization
- event-driven architecture
- serverless architecture
- container architecture
- professional-level tradeoff questions

Every chapter must include:
- design decisions
- tradeoffs
- why wrong answers are wrong
- scenario patterns
- exam traps
- architecture diagrams

If notes already exist, upgrade them instead of duplicating them.
For Docker
Create or upgrade legendary-teacher-level notes for:

Docker

Follow AGENTS.md completely.

Focus on:
- why containers exist
- containers vs virtual machines
- images
- layers
- Dockerfile
- build cache
- registries
- volumes
- bind mounts
- Docker networking
- container lifecycle
- environment variables
- Docker Compose
- multi-stage builds
- image optimization
- image security
- logs
- debugging
- Docker in CI/CD
- Docker with Kubernetes

Explain Docker through:
problem → old deployment pain → container model → image layering → runtime behavior → production limitations.

If notes already exist, upgrade them instead of duplicating them.
For Ansible
Create or upgrade legendary-teacher-level notes for:

Ansible

Follow AGENTS.md completely.

Focus on:
- configuration management
- agentless architecture
- SSH-based automation
- inventory
- playbooks
- tasks
- modules
- handlers
- variables
- facts
- templates
- roles
- collections
- vault
- idempotency
- conditionals
- loops
- privilege escalation
- error handling
- dynamic inventory
- real infrastructure automation

Explain idempotency deeply with examples.

If notes already exist, upgrade them instead of duplicating them.
For Jenkins
Create or upgrade legendary-teacher-level notes for:

Jenkins

Follow AGENTS.md completely.

Focus on:
- CI/CD fundamentals
- Jenkins architecture
- controller-agent model
- jobs
- pipelines
- Jenkinsfile
- declarative pipeline
- scripted pipeline
- stages
- steps
- credentials
- plugins
- webhooks
- distributed builds
- artifacts
- Docker integration
- Kubernetes agents
- security
- backup
- scaling
- pipeline debugging
- real CI/CD design

If notes already exist, upgrade them instead of duplicating them.
For ArgoCD
Create or upgrade legendary-teacher-level notes for:

ArgoCD

Follow AGENTS.md completely.

Focus on:
- GitOps from first principles
- desired state vs live state
- pull-based deployment
- ArgoCD architecture
- applications
- app projects
- repositories
- sync
- auto-sync
- manual sync
- pruning
- self-healing
- drift detection
- rollback
- Helm integration
- Kustomize integration
- RBAC
- secrets
- sync waves
- hooks
- app-of-apps pattern
- multi-cluster deployment
- troubleshooting

Explain the causal chain:
manual deployment pain → CI/CD drift → Git as source of truth → GitOps → ArgoCD reconciliation.

If notes already exist, upgrade them instead of duplicating them.
For Competitive Programming
Create or upgrade legendary-teacher-level notes for:

Competitive Programming

Follow AGENTS.md completely.

Focus on:
- problem-solving mindset
- complexity analysis
- Big O
- input/output optimization
- arrays
- strings
- hashing
- sorting
- binary search
- two pointers
- sliding window
- prefix sums
- recursion
- backtracking
- bit manipulation
- greedy
- dynamic programming
- graphs
- BFS
- DFS
- shortest paths
- DSU
- trees
- segment trees
- Fenwick trees
- tries
- heaps
- priority queues
- number theory
- modular arithmetic
- combinatorics
- common patterns
- debugging wrong answers
- avoiding TLE
- avoiding MLE

For every algorithm:
- start with the naive approach
- explain why it fails
- derive the optimized approach
- prove or intuitively justify it
- show dry run
- show code
- explain edge cases
- show common bugs
- provide practice problems with answers

If notes already exist, upgrade them instead of duplicating them.
For Java
Create or upgrade legendary-teacher-level notes for:

Java

Follow AGENTS.md completely.

Focus on:
- Java history and why it exists
- JVM
- JDK vs JRE
- compilation
- bytecode
- class loading
- memory model
- stack vs heap
- garbage collection
- OOP
- classes and objects
- inheritance
- polymorphism
- abstraction
- encapsulation
- interfaces
- generics
- collections
- exceptions
- streams
- lambdas
- concurrency
- threads
- synchronization
- executors
- file handling
- interview questions
- coding examples

Explain Java through:
C/C++ portability pain → JVM design → bytecode → managed runtime → enterprise adoption → modern Java.

If notes already exist, upgrade them instead of duplicating them.
For Python
Create or upgrade legendary-teacher-level notes for:

Python

Follow AGENTS.md completely.

Focus on:
- why Python exists
- interpreter model
- variables and references
- data types
- lists
- tuples
- dictionaries
- sets
- functions
- decorators
- generators
- iterators
- comprehensions
- modules
- packages
- virtual environments
- error handling
- file handling
- OOP
- typing
- async basics
- memory model
- GIL
- standard library
- scripting
- DevOps automation
- interview and coding examples

Explain Python through:
developer productivity problem → readable syntax → interpreted execution → dynamic typing → automation and data ecosystem.

If notes already exist, upgrade them instead of duplicating them.
For C++
Create or upgrade legendary-teacher-level notes for:

C++

Follow AGENTS.md completely.

Focus on:
- C++ history and why it exists
- compilation model
- headers
- linking
- memory layout
- stack vs heap
- pointers
- references
- RAII
- constructors
- destructors
- copy semantics
- move semantics
- classes
- inheritance
- polymorphism
- templates
- STL
- vectors
- maps
- sets
- unordered containers
- iterators
- algorithms
- lambdas
- smart pointers
- undefined behavior
- performance
- competitive programming patterns

Explain dangerous details carefully:
what can go wrong, why it goes wrong, how to avoid it, and how to debug it.

If notes already exist, upgrade them instead of duplicating them.
For UPSC
Create or upgrade legendary-teacher-level notes for:

UPSC Civil Services Examination

Follow AGENTS.md completely.

Focus on:
- syllabus mapping
- prelims
- mains
- essay
- ethics
- answer writing
- history
- geography
- polity
- governance
- economy
- environment
- science and technology
- society
- international relations
- internal security
- disaster management
- current affairs integration
- PYQ linkage

Every historical, political, economic, and social topic must include causal chains:
what happened → why it happened → what changed → what came next → why it matters for UPSC.

For mains topics, include:
- answer frameworks
- examples
- committees
- constitutional articles where relevant
- case studies
- diagrams
- balanced arguments
- conclusion templates

If notes already exist, upgrade them instead of duplicating them.
For MPSC
Create or upgrade legendary-teacher-level notes for:

MPSC

Follow AGENTS.md completely.

Focus on:
- syllabus mapping
- Maharashtra-specific history
- Maharashtra geography
- Maharashtra polity and administration
- Maharashtra economy
- social reform movements
- Indian polity
- Indian economy
- environment
- science and technology
- current affairs
- answer writing
- MCQ traps
- state-specific examples

Use causal chains especially for:
- Maratha history
- social reform movements
- British period
- Maharashtra formation
- cooperative movement
- regional development
- state policy issues

If notes already exist, upgrade them instead of duplicating them.
For RBI Grade B
Create or upgrade legendary-teacher-level notes for:

RBI Grade B

Follow AGENTS.md completely.

Focus on:
- latest official syllabus verification
- exam pattern
- Quantitative Aptitude
- Reasoning
- English
- General Awareness
- Economic and Social Issues
- Finance and Management
- Descriptive English
- RBI functions
- monetary policy
- inflation
- banking system
- financial markets
- government schemes
- budget
- economic survey
- reports and indices
- current affairs
- answer writing

For economics and finance topics, explain:
problem → institution involved → policy tool → transmission mechanism → impact → limitations → exam relevance.

If notes already exist, upgrade them instead of duplicating them.
For RBI Assistant
Create or upgrade legendary-teacher-level notes for:

RBI Assistant

Follow AGENTS.md completely.

Focus on:
- latest official syllabus verification
- exam pattern
- Reasoning
- Numerical Ability
- English
- General Awareness
- Computer Knowledge if relevant
- banking awareness
- RBI basics
- financial awareness
- current affairs
- speed-based practice
- MCQ traps
- revision sheets

If notes already exist, upgrade them instead of duplicating them.
For SEBI Grade A
Create or upgrade legendary-teacher-level notes for:

SEBI Grade A

Follow AGENTS.md completely.

Focus on:
- latest official syllabus verification
- exam pattern
- securities market
- capital markets
- SEBI Act
- Companies Act basics
- securities regulation
- mutual funds
- derivatives
- bonds
- primary market
- secondary market
- financial institutions
- economics
- finance
- management
- cost accounting basics if relevant
- current affairs
- descriptive answer writing if applicable

Explain every regulation or institution through:
market problem → regulatory need → SEBI mechanism → impact on investors/companies/markets → exam relevance.

If notes already exist, upgrade them instead of duplicating them.
