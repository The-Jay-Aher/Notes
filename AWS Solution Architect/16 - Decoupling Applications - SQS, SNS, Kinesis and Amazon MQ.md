# Decoupling Applications: SQS, SNS, Kinesis and Amazon MQ

## Quick Summary
- Decoupling means components communicate through a buffer or broker instead of depending directly on each other.
- SQS is a queue for pulling messages and processing them asynchronously.
- SNS is pub/sub fanout for pushing one message to many subscribers.
- Kinesis is for streaming data records at high volume and ordered shard-based processing.
- Amazon MQ is managed ActiveMQ or RabbitMQ for applications that need traditional message broker protocols.
- EventBridge is also important for event-driven AWS architectures, even though this note focuses on SQS, SNS, Kinesis, and Amazon MQ.

## Why Decoupling Matters
Without decoupling:

```text
Web app -> worker
```

If the worker is slow or down, the web app may fail.

With decoupling:

```text
Web app -> queue/topic/stream -> worker
```

The web app can hand off work and continue. The worker processes later.

Benefits:
- Better fault tolerance.
- Better scaling.
- Smoother traffic spikes.
- Retry support.
- Separate deployment of components.
- Easier integration between services.

Tradeoff:
- More moving parts.
- Eventual consistency.
- Need idempotent consumers.
- Need monitoring for backlog and failures.

## Amazon SQS
Amazon Simple Queue Service is a managed message queue.

Producer sends messages. Consumer polls and processes messages.

```text
Producer -> SQS queue -> Consumer workers
```

### SQS Standard Queues
Standard queues provide:
- Very high throughput.
- At-least-once delivery.
- Best-effort ordering.

At-least-once means a message can be delivered more than once. Your consumer must be safe to retry.

### SQS FIFO Queues
FIFO queues provide:
- First-in-first-out ordering within message groups.
- Exactly-once processing behavior from the queue side when deduplication is used.
- Lower throughput than standard queues unless high-throughput FIFO settings are used.

Use FIFO when order matters:
- Bank transaction steps.
- Inventory updates for the same item.
- Workflows where event order is required.

### Visibility Timeout
When a consumer receives a message, SQS hides it for the visibility timeout.

If the consumer finishes, it deletes the message.

If the consumer crashes or does not delete it, the message becomes visible again.

```text
Receive message -> hidden during visibility timeout -> delete or reappear
```

Set visibility timeout longer than normal processing time.

### Dead-Letter Queue
A dead-letter queue stores messages that fail repeatedly.

Use it to:
- Avoid retrying broken messages forever.
- Inspect poison messages.
- Reprocess messages after fixing the bug.

### Long Polling
Long polling lets SQS wait for messages before returning a response.

Benefits:
- Fewer empty responses.
- Lower cost.
- More efficient consumers.

### Delay Queues and Message Timers
Use delay when a message should not be processed immediately.

Examples:
- Send a reminder after 15 minutes.
- Retry a job later.

### SQS with Lambda
Lambda can poll SQS and invoke functions with batches of messages.

Important:
- Configure batch size.
- Configure partial batch response if one failed message should not fail the whole batch.
- Use DLQs or failure destinations.
- Keep Lambda timeout less than SQS visibility timeout.

## Amazon SNS
Amazon Simple Notification Service is a pub/sub service.

Publisher sends a message to a topic. SNS fans out to subscribers.

```text
Publisher -> SNS topic -> SQS queue
                     -> Lambda
                     -> HTTPS endpoint
                     -> email/SMS/mobile push
```

### SNS Use Cases
- Fan out one event to multiple systems.
- Send notifications.
- Trigger Lambda functions.
- Send events to SQS queues for independent consumers.
- Mobile push notifications.

### SNS Topic Types
SNS supports:
- Standard topics: high throughput and best-effort ordering.
- FIFO topics: ordered fanout when paired with compatible FIFO subscribers.

### SNS Plus SQS Pattern
This is a very common architecture.

```text
Order service -> SNS topic -> SQS queue for billing
                           -> SQS queue for shipping
                           -> SQS queue for analytics
```

Why this is useful:
- Each subscriber gets its own queue.
- One slow consumer does not block others.
- Each team can retry independently.
- SNS handles fanout; SQS handles buffering.

### Message Filtering
SNS subscription filter policies let subscribers receive only relevant messages.

Example:
- Billing queue receives events where `eventType = payment`.
- Shipping queue receives events where `eventType = shipment`.

## Amazon Kinesis
Amazon Kinesis is for streaming data.

Think of Kinesis as a continuously flowing log of records.

```text
Producers -> Kinesis stream shards -> Consumers
```

### Kinesis Data Streams
Use Kinesis Data Streams for:
- Clickstream events.
- IoT telemetry.
- Application logs.
- Real-time analytics.
- Fraud detection.
- Ordered processing per partition key.

### Shards
A stream is made of shards.

Shards control:
- Write capacity.
- Read capacity.
- Ordering scope.

Records with the same partition key go to the same shard, preserving order for that key.

### Consumers
Consumers read records from the stream.

Consumer options:
- Custom applications using Kinesis Client Library.
- Lambda event source mapping.
- Kinesis Data Analytics.
- Kinesis Data Firehose for delivery to destinations.

### Retention
Kinesis stores records for a retention period. Consumers can replay records within that period.

This is different from SQS, where messages are usually removed after successful processing.

## Kinesis Data Firehose
Kinesis Data Firehose is for loading streaming data into destinations.

Common destinations:
- S3.
- Redshift.
- OpenSearch Service.
- Third-party observability tools.

Use Firehose when:
- You want managed delivery, buffering, compression, and optional transformation.
- You do not need to manage stream consumers yourself.

Exam clue:
- "Load streaming logs into S3 with minimal administration" often points to Firehose.

## Amazon MQ
Amazon MQ is a managed message broker service for ActiveMQ and RabbitMQ.

Use Amazon MQ when:
- You are migrating existing apps that use JMS, AMQP, MQTT, OpenWire, or STOMP.
- The application depends on broker-specific features.
- Rewriting to SQS/SNS would be too expensive.

Do not choose Amazon MQ just because you need a queue. For cloud-native AWS designs, SQS/SNS/EventBridge are usually simpler and more scalable.

## EventBridge Context
Amazon EventBridge is a serverless event bus.

Use it for:
- Routing events between AWS services, custom apps, and SaaS partners.
- Rule-based event matching.
- Event-driven architecture.
- Scheduled events.

Very simple comparison:
- SNS fans out messages to subscribers.
- SQS buffers work for consumers.
- EventBridge routes events based on rules and schemas.
- Kinesis streams high-volume ordered records.

## Service Comparison
| Service | Pattern | Delivery style | Best for |
|---|---|---|---|
| SQS | Queue | Consumers poll | Async jobs and buffering |
| SNS | Pub/sub topic | Push to subscribers | Fanout and notifications |
| Kinesis Data Streams | Stream | Consumers read stream | Real-time ordered event streams |
| Kinesis Firehose | Delivery stream | Managed delivery | Loading streaming data into S3/Redshift/OpenSearch |
| Amazon MQ | Broker | Traditional broker protocols | Migration of existing broker-based apps |
| EventBridge | Event bus | Rule-based routing | Event-driven integration |

## Idempotency
Idempotency means processing the same message more than once does not cause incorrect results.

Example problem:
- A payment message is delivered twice.
- If the consumer charges the card twice, the system is broken.

Better design:
- Include a unique transaction ID.
- Store processed IDs.
- If the same ID arrives again, skip or return the existing result.

This matters because distributed systems retry.

## Backpressure
Backpressure happens when producers send work faster than consumers process it.

Queues help by absorbing spikes.

Watch:
- SQS ApproximateAgeOfOldestMessage.
- SQS ApproximateNumberOfMessagesVisible.
- Kinesis iterator age.
- Lambda throttles and errors.
- DLQ message count.

## Common Architecture Patterns
### Web Request to Async Worker
```text
API -> SQS -> worker fleet
```

Good for:
- Image processing.
- Sending emails.
- Report generation.
- Slow background jobs.

### Fanout to Many Teams
```text
Order event -> SNS -> billing queue
                  -> shipping queue
                  -> analytics queue
```

Good for:
- Independent downstream processing.

### Real-Time Clickstream
```text
Website -> Kinesis Data Streams -> analytics app
                                  -> Firehose -> S3
```

Good for:
- High-volume streaming events and replay.

### Legacy Broker Migration
```text
Existing JMS app -> Amazon MQ
```

Good for:
- Moving to AWS without rewriting messaging logic immediately.

## Common Mistakes
- Using SNS alone when consumers need durable buffering.
- Forgetting DLQs.
- Setting SQS visibility timeout shorter than processing time.
- Assuming SQS standard queues preserve strict order.
- Choosing Kinesis when a simple queue would work.
- Choosing Amazon MQ for new AWS-native workloads without a protocol requirement.
- Not designing consumers to be idempotent.
- Ignoring backlog metrics.

## Official References
- [Amazon SQS documentation](https://docs.aws.amazon.com/sqs/)
- [Amazon SNS documentation](https://docs.aws.amazon.com/sns/)
- [Amazon Kinesis Data Streams documentation](https://docs.aws.amazon.com/kinesis/)
- [Amazon Kinesis Data Firehose documentation](https://docs.aws.amazon.com/firehose/)
- [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/)
- [Amazon EventBridge documentation](https://docs.aws.amazon.com/eventbridge/)
- [AWS decision guide for SNS, SQS, and EventBridge](https://docs.aws.amazon.com/decision-guides/latest/sns-or-sqs-or-eventbridge/sns-or-sqs-or-eventbridge.html)
