# 2 - Storage, Networking and Database

## 1) Storage Technology and Services

### EC2 Storage Options

### Amazon EBS (Elastic Block Store)

Amazon EBS provides persistent block storage for EC2 instances.

Key points:

- Data persists independently of instance lifecycle (stop/start).
- Volumes are created in a specific Availability Zone.
- Supports snapshots for backup and restore workflows.
- Can be resized with minimal operational disruption.

Common use cases:

- Boot volumes for EC2
- Transactional databases
- Enterprise applications requiring persistent block storage

### Amazon EFS (Elastic File System)

Amazon EFS is a fully managed, shared file system for Linux workloads.

Key points:

- Multiple EC2 instances can mount the same file system.
- Automatically scales as files are added/removed.
- Regional service with high durability and multi-AZ design options.

Common use cases:

- Shared web content
- CMS and application data sharing
- Dev/test environments needing shared storage

### EC2 Instance Store

Instance store is temporary block storage physically attached to the host machine.

Key points:

- Very high I/O performance.
- Data is ephemeral (lost on stop/terminate or host failure events).
- Good for scratch data, caches, and buffers.

Common use cases:

- Temporary processing data
- Cache layers
- Workloads that replicate data externally

### Amazon S3 (Simple Storage Service)

S3 is an object storage service designed for scalability, durability, and security.

Important concepts:

- **Bucket:** Container for objects; bucket names are globally unique.
- **Object:** Data + key + metadata.
- **Region-scoped buckets:** Buckets are created in a Region, even though S3 is globally accessible via API endpoints.

Core benefits:

- High durability
- Virtually unlimited scale
- Fine-grained access control
- Encryption and lifecycle management capabilities

Common use cases:

- Backups and archives
- Static website content
- Data lakes and analytics storage
- Media and document repositories

### S3 Storage Classes

### S3 Standard

- For frequently accessed data.
- Low latency and high throughput.

### S3 Intelligent-Tiering

- For unpredictable access patterns.
- Automatically moves objects across access tiers to optimize cost.

### S3 Standard-IA (Infrequent Access)

- For data accessed less frequently but requiring rapid retrieval.
- Lower storage cost with retrieval charges.

### S3 One Zone-IA

- Lower-cost IA class stored in a single AZ.
- Suitable for reproducible or secondary backup data.

### S3 Glacier Instant Retrieval

- Archive data requiring millisecond retrieval.

### S3 Glacier Flexible Retrieval

- Low-cost archive with retrieval in minutes to hours.

### S3 Glacier Deep Archive

- Lowest-cost archival class.
- Retrieval typically in hours, designed for long-term retention.

### Additional AWS Storage Services

### Amazon FSx

Managed file systems for specialized workloads, including:

- FSx for Windows File Server
- FSx for Lustre
- FSx for NetApp ONTAP
- FSx for OpenZFS

### AWS Elastic Disaster Recovery (DRS)

Service for disaster recovery by continuously replicating source servers to AWS.

Benefits:

- Reduced recovery time objectives (RTO)
- Reduced recovery point objectives (RPO)
- Pay-for-use recovery architecture patterns

### AWS Storage Gateway

Hybrid storage service connecting on-premises environments to AWS storage.

Gateway types:

- S3 File Gateway
- FSx File Gateway
- Volume Gateway
- Tape Gateway

Common use cases:

- Backup modernization
- Hybrid cloud file access
- Archival with virtual tape workflows

### AWS Backup

Centralized backup service for defining backup plans and retention across AWS services.

Supported examples include:

- EBS volumes
- EFS file systems
- RDS databases
- DynamoDB tables
- FSx file systems
- Storage Gateway volumes

Core capabilities:

- Policy-based scheduling
- Encryption and compliance support
- Cross-account/cross-Region backup options

---

## 2) Content Delivery and Networking Technology and Services

### Content Delivery (CDN) Basics

A CDN caches content close to end users to reduce latency and improve delivery speed.

### Amazon CloudFront

CloudFront is AWS's global CDN service.

Key benefits:

- Lower latency through edge caching
- Better performance for static and dynamic content
- Integrates with AWS Shield and AWS WAF for protection
- Works well with S3, EC2, Elastic Load Balancing, and Route 53

Common use cases:

- Video/content streaming
- Static website acceleration
- API delivery and edge security
- Handling traffic spikes

### AWS Global Accelerator

Global Accelerator improves performance and availability for global applications using the AWS global network and static anycast IPs.

Key benefits:

- Improved path selection to healthy regional endpoints
- Faster failover across Regions/endpoints
- Static entry points for simplified client configuration

Common use cases:

- Multi-Region applications
- Latency-sensitive global services
- High-availability internet-facing applications

### VPC Networking Fundamentals

### Public and Private Subnets

- **Public subnet:** Can route to internet through an Internet Gateway (IGW).
- **Private subnet:** No direct inbound internet route.

### Route Tables and Gateways

- Every subnet is associated with a route table.
- **Internet Gateway (IGW):** Enables internet access for public subnet resources.
- **NAT Gateway:** Enables outbound internet access for private subnet resources.

### Security in a VPC

#### Security Groups

- Instance/ENI-level, stateful virtual firewall.
- Allow rules only (no explicit deny).

#### Network ACLs (NACLs)

- Subnet-level, stateless filtering.
- Supports allow and deny rules.

### Reserved IP Addresses in Each VPC Subnet

AWS reserves 5 IP addresses in every subnet:

1. Network address
2. VPC router
3. DNS
4. Reserved for future use
5. Broadcast address (broadcast not supported in VPC)

### DNS with Amazon Route 53

Route 53 is AWS DNS and domain management service.

Capabilities:

- Domain registration
- Public and private hosted zones
- Routing policies (latency, weighted, failover, geolocation, etc.)
- Health checks and DNS failover

Common use cases:

- Web app routing
- Multi-Region failover
- Internal DNS for private VPC workloads

### Hybrid Connectivity

### AWS Direct Connect

Dedicated private network connection from on-premises to AWS.

Benefits:

- Consistent network performance
- Potentially lower data transfer cost at scale
- Private connectivity model

### AWS Site-to-Site VPN and Client VPN

- **Site-to-Site VPN:** Secure connection between on-prem network and AWS VPC.
- **Client VPN:** Secure remote user access to AWS/private networks.

High-level comparison:

- VPN: faster setup, internet-based, encrypted by default.
- Direct Connect: private dedicated link, higher consistency for enterprise traffic patterns.

---

## 3) Database Technology and Services

### Database Categories on AWS

- **Relational:** Amazon RDS, Amazon Aurora
- **Key-value / NoSQL:** Amazon DynamoDB
- **In-memory:** Amazon ElastiCache, Amazon MemoryDB for Redis
- **Graph:** Amazon Neptune

### Amazon RDS

Managed relational database service supporting engines such as MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and others.

Benefits:

- Automated backups/patching options
- Multi-AZ high availability options
- Read replicas (engine-dependent)

Common use cases:

- E-commerce applications
- Line-of-business applications
- Web/mobile backends with relational models

### Amazon DynamoDB

Fully managed NoSQL key-value/document database.

Benefits:

- Single-digit millisecond performance at scale
- Serverless operational model
- Built-in security and backup capabilities

Common use cases:

- Web/mobile backends
- Gaming leaderboards and sessions
- IoT event/state storage

### Amazon Neptune

Managed graph database service.

Common use cases:

- Fraud detection graphs
- Recommendation engines
- Knowledge graphs and relationship-heavy datasets

### Database Migration Services

### AWS Database Migration Service (DMS)

Helps migrate databases to AWS with minimal downtime.

Capabilities:

- Homogeneous and heterogeneous migrations
- Continuous replication for cutover planning
- Migration for analytics modernization and data center exits

### AWS Schema Conversion Tool (SCT)

Converts database schema and code objects when moving between different database engines.

Useful when:

- Source and target engines differ
- Schema transformation is required before/alongside DMS

### In-Memory Databases

In-memory databases store data in RAM for very fast response times.

AWS options:

- Amazon ElastiCache (Redis/Memcached)
- Amazon MemoryDB for Redis

Common use cases:

- Caching hot data
- Session stores
- Real-time analytics patterns
- Gaming leaderboards
