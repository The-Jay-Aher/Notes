# 3 - Deployment, Migration, and AI

## 1) Development, Messaging, and Deployment Services

### CI/CD Basics

- **Continuous Integration (CI):** Merge code changes frequently and validate with automated builds/tests.
- **Continuous Delivery/Deployment (CD):** Automate release steps so changes are shipped safely and consistently.

Benefits:

- Faster releases
- Fewer manual errors
- Smaller, lower-risk changes
- Better rollback and auditability

### AWS Developer and Deployment Services

### AWS CodeBuild

- Fully managed build service.
- Compiles code, runs tests, and produces artifacts.

### AWS CodeDeploy

- Automates application deployments to EC2, on-premises servers, Lambda, and ECS.
- Supports deployment strategies to reduce downtime.

### AWS CodePipeline

- Orchestrates CI/CD stages end-to-end.
- Integrates with build, test, approval, and deploy actions.

### AWS CodeArtifact

- Managed artifact/package repository.
- Stores and shares packages (for example npm, Maven, PyPI).

### AWS CloudFormation

- Infrastructure as Code service for declarative AWS provisioning.
- Improves consistency, repeatability, and change control.

### AWS Elastic Beanstalk

- PaaS-style service to deploy web apps quickly.
- AWS handles provisioning, scaling, monitoring, and patching for the environment.

### AWS X-Ray

- Distributed tracing service.
- Helps troubleshoot latency and errors across microservices.

### Decoupling with Messaging Services

Monolithic systems often have tightly coupled components. Messaging services enable loose coupling and better resilience.

### Amazon SNS (Simple Notification Service)

- Pub/sub messaging service.
- One message can fan out to multiple subscribers.
- Common endpoints: email, SMS, HTTP/S, Lambda, SQS.

### Amazon SQS (Simple Queue Service)

- Fully managed message queue.
- Pull-based consumption model.
- Decouples producers and consumers.

Queue types:

- **Standard queue:** At-least-once delivery, best-effort ordering, very high throughput.
- **FIFO queue:** Ordered processing with deduplication support for exactly-once processing behavior in many scenarios.

Polling:

- **Short polling:** Returns immediately.
- **Long polling:** Waits for messages, reducing empty responses and API cost.

### Amazon EventBridge

- Event bus service for event-driven architectures.
- Routes events from AWS services, SaaS apps, and custom apps to targets.
- Supports scheduled rules.

### AWS Step Functions

- Orchestrates workflows as state machines.
- Coordinates retries, branching, error handling, and service integrations.

### Amazon SES (Simple Email Service)

- Service for transactional and marketing email.
- Supports bulk email and delivery metrics.

---

## 2) Migration and Transfer Services

### AWS Snow Family

Used for moving large datasets when network transfer is too slow/expensive.

- **Snowcone:** Small portable edge device.
- **Snowball Edge:** Data transfer and edge compute.
- **Snowmobile:** Exabyte-scale transfer via physical transport for very large migrations.

### Database and Application Migration

### AWS Database Migration Service (DMS)

- Migrates databases to AWS with minimal downtime.
- Supports homogeneous and heterogeneous migrations.

### AWS Schema Conversion Tool (SCT)

- Converts schema/code when source and target database engines differ.

### AWS Application Migration Service (MGN)

- Lift-and-shift server migration service.
- Continuously replicates source servers and simplifies cutover.

### AWS Application Discovery Service

- Collects on-prem inventory and utilization data.
- Helps build migration plans and dependency mapping.

### AWS Migration Hub

- Central place to track migrations across AWS migration tools.
- Helps coordinate and monitor progress.

### Data Transfer Services

### AWS DataSync

- Accelerated online data transfer service.
- Moves data between on-premises storage and AWS storage/services.
- Supports NFS, SMB, object stores, and more.

### AWS Transfer Family

Managed file transfer into/out of AWS storage.

Supported protocols:

- SFTP
- FTPS
- FTP
- AS2

---

## 3) AI, ML, and Analytics Services

### Amazon Redshift / Redshift Serverless

- Managed data warehouse for analytics and reporting (OLAP workloads).
- Redshift Serverless removes infrastructure management overhead.

### Amazon Kinesis

Family of real-time streaming services.

- **Kinesis Data Streams:** Ingest/process streaming data.
- **Kinesis Data Firehose:** Load streaming data into destinations like S3, Redshift, OpenSearch with optional transforms.
- **Kinesis Video Streams:** Ingest/manage video streams.

Use cases:

- Clickstream analytics
- IoT telemetry processing
- Log ingestion pipelines

### Amazon Athena

- Serverless SQL query service for data stored in S3.
- Useful for ad-hoc analytics without managing database servers.

### AI/ML Service Awareness (Cloud Practitioner level)

- **Amazon SageMaker:** Build, train, and deploy ML models.
- **Amazon Bedrock:** Build generative AI apps using foundation models.
- **Amazon Rekognition / Comprehend / Lex / Polly / Transcribe:** Prebuilt AI APIs for vision, NLP, chat, speech, and transcription use cases.

### Quick Summary

1. CI/CD services automate reliable software delivery.
2. Messaging/event services improve decoupling and resilience.
3. Migration services reduce risk and downtime during cloud adoption.
4. Analytics and AI services support data-driven and intelligent applications.
