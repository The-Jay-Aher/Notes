# Serverless Solutions Architect Discussions

## Quick Summary
- Serverless architecture is built by combining managed services, not by using Lambda everywhere.
- A good design separates synchronous request handling from asynchronous background work.
- The most important serverless architecture skills are event design, retries, idempotency, security, observability, and cost control.
- Step Functions should be considered when a workflow has multiple steps, branching, retries, or long waits.
- Queues and dead-letter queues are essential when reliability matters.

## How to Think Like a Solutions Architect
When given a serverless scenario, do not jump directly to Lambda.

Ask:
- What starts the workflow?
- Does the user need an immediate response?
- Which steps can run later?
- What happens if a step fails?
- Does order matter?
- Can the same event arrive twice?
- Where is state stored?
- How will the system be monitored?
- What is the security boundary?

## Pattern 1: Synchronous API with Lambda and DynamoDB
Common architecture:

```text
Client -> API Gateway -> Lambda -> DynamoDB
```

Use it for:
- Simple APIs.
- CRUD operations.
- Lightweight request processing.
- Mobile or web backends.

Design details:
- API Gateway handles HTTP endpoint.
- Lambda validates request and runs business logic.
- DynamoDB stores data.
- IAM role allows Lambda only the required DynamoDB actions.

Good:
- Low operations.
- Scales automatically.
- Low idle cost.

Watch out:
- Lambda timeout.
- DynamoDB key design.
- API throttling.
- Input validation.
- Authentication and authorization.

## Pattern 2: API with Async Background Processing
Common architecture:

```text
Client -> API Gateway -> Lambda -> SQS -> worker Lambda -> database/storage
```

Use it when:
- The request starts slow work.
- The client does not need the final result immediately.
- You need buffering during traffic spikes.
- Workers need retries.

Example:
- User uploads a document.
- API returns "accepted".
- Background worker extracts text, stores results, and sends notification.

Important:
- Return a job ID to the client.
- Store job status in DynamoDB.
- Use DLQ for failed jobs.
- Make worker idempotent.

## Pattern 3: S3 Upload Processing
Common architecture:

```text
Client -> S3 upload -> S3 event -> Lambda -> processed output
```

Use it for:
- Image thumbnails.
- Document conversion.
- Log processing.
- Media metadata extraction.

Better for reliable high-volume processing:

```text
S3 event -> SQS -> Lambda workers
```

Why add SQS?
- It buffers spikes.
- It allows retries.
- It gives backlog visibility.
- It reduces direct pressure on Lambda concurrency.

## Pattern 4: Fanout with SNS and SQS
Common architecture:

```text
Application event -> SNS topic -> SQS queue A -> consumer A
                              -> SQS queue B -> consumer B
                              -> SQS queue C -> consumer C
```

Use it when:
- Multiple systems need the same event.
- Each subscriber should process independently.
- One slow subscriber should not block others.

Example:
- `OrderCreated` event fans out to billing, shipping, analytics, and email.

Best practice:
- Put SQS queues behind SNS subscriptions for durable fanout.
- Use subscription filter policies when subscribers only need some events.

## Pattern 5: Workflow Orchestration with Step Functions
Common architecture:

```text
API/Event -> Step Functions
              -> Lambda validate
              -> Lambda charge payment
              -> Choice: success or failure
              -> Lambda reserve inventory
              -> SNS notification
```

Use Step Functions when:
- Business process has multiple steps.
- You need retries per step.
- You need branching logic.
- Some steps may wait.
- You need visual execution history.

Without Step Functions, teams often build fragile workflow state machines inside Lambda code.

### Standard vs Express Workflows
Beginner view:
- Standard workflows are for durable, longer-running workflows with detailed execution history.
- Express workflows are for high-volume, short-duration event processing.

Check AWS docs for exact limits and pricing because these details can change.

## Pattern 6: EventBridge Event Bus
Common architecture:

```text
Service emits event -> EventBridge bus -> rules -> targets
```

Use it when:
- You want event routing by rules.
- You integrate AWS services, custom apps, or SaaS events.
- You want loosely coupled event-driven services.

Example:
- A payment service emits `PaymentSucceeded`.
- EventBridge routes it to order service, analytics, and notifications.

Good event design:
- Use stable event names.
- Include a unique event ID.
- Include event time.
- Include enough context for consumers.
- Avoid dumping huge payloads into events; store large data in S3 and send a pointer.

## Pattern 7: DynamoDB Streams
DynamoDB Streams capture item-level changes.

Common architecture:

```text
DynamoDB table change -> DynamoDB Stream -> Lambda
```

Use it for:
- Updating search indexes.
- Sending change notifications.
- Replicating derived views.
- Audit/event trails.

Watch out:
- Stream processing can retry.
- A bad record can block progress if not handled.
- Monitor iterator age.

## Idempotency in Serverless
Serverless systems retry. Events can arrive more than once.

Idempotent means repeated processing does not create duplicate side effects.

Examples:
- Do not charge a card twice for the same order ID.
- Do not send duplicate shipment creation requests.
- Do not insert duplicate records.

Techniques:
- Use unique request/event IDs.
- Use conditional writes in DynamoDB.
- Store processing status.
- Use deterministic object keys.
- Treat external API calls carefully.

## Error Handling
Different services retry differently.

Design choices:
- Lambda async destination for success/failure.
- Lambda DLQ for asynchronous invocation failures.
- SQS redrive policy to DLQ.
- Step Functions retry/catch blocks.
- EventBridge DLQs for failed target delivery.

Good failure design:
- Retry transient errors.
- Stop retrying poison messages.
- Alert on DLQ depth.
- Include enough context to reprocess.

## Security Architecture
Serverless does not remove security work.

Security checklist:
- One IAM role per function or workload where practical.
- Least privilege policies.
- Secrets in Secrets Manager or SSM Parameter Store.
- API authentication with Cognito, IAM, Lambda authorizers, or JWT authorizers depending on API type.
- Validate all external input.
- Encrypt S3 buckets, DynamoDB tables, queues, and logs as required.
- Use WAF for public APIs that need web protection.
- Enable CloudTrail.

## Observability Architecture
Minimum useful monitoring:
- Lambda errors, duration, throttles, concurrent executions.
- API Gateway 4xx and 5xx errors.
- SQS oldest message age and visible message count.
- DLQ message count.
- DynamoDB throttled requests.
- Step Functions failed executions.
- EventBridge failed invocations.

Logs should include:
- Request ID.
- Correlation ID.
- Event ID.
- User or tenant identifier when safe.
- Error reason.

## Cost Discussions
Serverless can be cheap when idle, but can become expensive with inefficient event chains.

Cost drivers:
- Number of Lambda invocations.
- Lambda duration and memory.
- API Gateway request count.
- DynamoDB read/write pattern.
- Step Functions state transitions.
- SQS/SNS/EventBridge request volume.
- CloudWatch Logs ingestion and retention.

Cost controls:
- Set log retention.
- Batch SQS processing.
- Avoid unnecessary chatty events.
- Use DynamoDB on-demand or provisioned capacity based on workload predictability.
- Use budgets and alarms.

## Common Exam Discussion Examples
### Image Processing
Requirement:
- Users upload images.
- System generates thumbnails.
- Must handle spikes.

Good answer:

```text
S3 upload -> SQS -> Lambda -> thumbnail bucket
```

Add DLQ and idempotent object key handling.

### Order Workflow
Requirement:
- Validate order, charge payment, reserve inventory, notify user.
- Each step can fail differently.

Good answer:

```text
API Gateway -> Step Functions -> Lambda/service integrations
```

Use retries, catch blocks, and state tracking.

### Partner File Drop
Requirement:
- Partner uploads files using SFTP.
- Files trigger processing.

Good answer:

```text
AWS Transfer Family -> S3 -> SQS/EventBridge -> Lambda/Step Functions
```

### Real-Time Events
Requirement:
- Millions of clickstream events per hour.
- Analytics consumers need replay.

Good answer:

```text
Kinesis Data Streams -> consumers / Firehose -> S3
```

## Common Mistakes
- Making one huge Lambda that does all workflow steps.
- Ignoring duplicate events.
- Forgetting DLQs and alarms.
- Giving every function broad IAM permissions.
- Storing large payloads directly in events instead of S3.
- Using synchronous APIs for work that should be asynchronous.
- Forgetting downstream service limits when Lambda scales quickly.
- Not setting CloudWatch log retention.

## Official References
- [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/)
- [Amazon API Gateway documentation](https://docs.aws.amazon.com/apigateway/)
- [Amazon DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html)
- [AWS Step Functions documentation](https://docs.aws.amazon.com/step-functions/)
- [Amazon EventBridge documentation](https://docs.aws.amazon.com/eventbridge/)
- [Amazon SQS documentation](https://docs.aws.amazon.com/sqs/)
- [Amazon SNS documentation](https://docs.aws.amazon.com/sns/)
