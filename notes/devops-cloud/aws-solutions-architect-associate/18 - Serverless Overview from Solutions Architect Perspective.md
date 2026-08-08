# Serverless Overview from Solutions Architect Perspective

## Quick Summary
- Serverless means you focus on application logic while AWS manages most server operations.
- The most common serverless building blocks are Lambda, API Gateway, DynamoDB, S3 events, EventBridge, SQS, SNS, and Step Functions.
- Serverless is event-driven: something happens, and a service reacts.
- It can reduce operational work, but you must design carefully for timeouts, retries, idempotency, limits, observability, and cost.
- Serverless does not mean "no servers"; it means server management is abstracted away.

## What Serverless Means
In a traditional architecture, you manage servers:

```text
EC2 instance -> OS patches -> runtime installation -> scaling -> app deployment
```

In a serverless architecture, you define behavior and configuration:

```text
Event -> managed service -> function/workflow/database -> response
```

AWS handles much of:
- Provisioning.
- Scaling.
- High availability.
- Runtime infrastructure.
- Some patching responsibility.

You still own:
- Code.
- IAM permissions.
- Data design.
- Error handling.
- Security configuration.
- Monitoring.
- Cost control.

## Common Serverless Services
| Service | Role |
|---|---|
| AWS Lambda | Run code in response to events |
| Amazon API Gateway | Build HTTP, REST, and WebSocket APIs |
| Amazon DynamoDB | Serverless NoSQL key-value/document database |
| Amazon S3 | Object storage and event source |
| Amazon EventBridge | Event bus and scheduler |
| Amazon SQS | Queue for asynchronous work |
| Amazon SNS | Pub/sub fanout |
| AWS Step Functions | Workflow orchestration |
| Amazon Cognito | User sign-up, sign-in, and identity features |

## AWS Lambda
Lambda runs code without you managing servers.

You provide:
- Function code.
- Runtime.
- Handler.
- Memory.
- Timeout.
- IAM role.
- Trigger configuration.

Lambda is invoked by events such as:
- API Gateway requests.
- S3 object uploads.
- SQS messages.
- EventBridge schedules.
- DynamoDB Streams.
- SNS messages.

### Lambda Handler
The handler is the entry point.

Example in Python:

```python
def handler(event, context):
    return {
        "statusCode": 200,
        "body": "hello"
    }
```

`event` contains the input. `context` contains runtime information.

### Lambda Limits to Remember
Important design constraints:
- Maximum execution time is limited.
- Memory and CPU are configured together.
- Deployment package size has limits.
- Functions are stateless between invocations from an architecture perspective.
- Temporary storage is available but should not be treated as durable state.

Exam idea:
- If work can run longer than Lambda's maximum timeout, use Step Functions, ECS/Fargate, Batch, or another service.

### Cold Starts
A cold start happens when AWS prepares a new execution environment before running the function.

Cold starts can be affected by:
- Runtime.
- Package size.
- VPC networking.
- Initialization code.
- Provisioned Concurrency configuration.

Design tips:
- Keep initialization light.
- Reuse clients outside the handler where appropriate.
- Use Provisioned Concurrency for latency-sensitive workloads.

## API Gateway
API Gateway receives API requests and routes them to backend integrations.

Common integrations:
- Lambda.
- HTTP endpoints.
- AWS services.
- Mock integrations.

API Gateway can provide:
- Authentication and authorization integration.
- Throttling.
- Request validation.
- Usage plans and API keys.
- Caching for REST APIs.
- Custom domains.
- WebSocket APIs.

### REST API vs HTTP API
Beginner mental model:
- REST APIs provide more features and older advanced controls.
- HTTP APIs are simpler and often lower cost for common HTTP API needs.

Check current AWS docs for exact feature differences because AWS evolves these services over time.

## DynamoDB
DynamoDB is a managed NoSQL database.

Serverless-friendly properties:
- No servers to manage.
- Scales to high request rates.
- Single-digit millisecond performance for many access patterns.
- Supports on-demand capacity.
- Supports streams for event-driven designs.

Main design rule:
- Model DynamoDB around access patterns, not around normalized relational tables.

Example access pattern:
- Get order by `orderId`.
- List orders for `customerId`.
- Find open orders by status.

Design keys and indexes around those queries.

## Step Functions
Step Functions orchestrates workflows.

Use it when:
- Multiple steps must run in order.
- You need retries and error branches.
- You need human approval or long-running workflows.
- You need to coordinate Lambda, ECS, Batch, Glue, SNS, SQS, and other services.

Example:

```text
Receive order -> validate payment -> reserve inventory -> ship order -> send notification
```

Without Step Functions, this logic often becomes tangled inside Lambda code.

## EventBridge
EventBridge routes events.

Use it for:
- Event-driven integration.
- Scheduled jobs.
- SaaS event sources.
- Filtering events by pattern.

Example:

```text
OrderCreated event -> EventBridge bus -> billing Lambda
                                  -> analytics Firehose
                                  -> notification workflow
```

## S3 Event-Driven Processing
S3 can publish events when objects are created or changed.

Examples:
- Image uploaded -> Lambda creates thumbnail.
- Log file uploaded -> Lambda starts parsing.
- Data file uploaded -> Step Functions starts ETL workflow.

Be careful:
- Events can be delivered more than once.
- Design processing to be idempotent.
- For robust buffering, route events to SQS where appropriate.

## Serverless Security
Key practices:
- Use least-privilege IAM roles.
- Give each Lambda function its own role when practical.
- Store secrets in Secrets Manager or SSM Parameter Store.
- Do not hardcode credentials.
- Validate API inputs.
- Use WAF for public APIs when needed.
- Encrypt data at rest and in transit.
- Monitor CloudTrail and CloudWatch logs.

## Serverless Observability
You need visibility into:
- Function errors.
- Function duration.
- Throttles.
- Iterator age for stream sources.
- DLQ depth.
- API Gateway 4xx/5xx errors.
- DynamoDB throttles.
- Step Functions failed executions.

Common tools:
- CloudWatch Metrics.
- CloudWatch Logs.
- AWS X-Ray.
- CloudTrail.
- Service-specific dashboards.

## Serverless Cost Model
Serverless often charges by usage.

Examples:
- Lambda: requests and duration.
- API Gateway: requests and data transfer.
- DynamoDB: read/write capacity or on-demand requests, storage, backups.
- Step Functions: state transitions or duration depending on workflow type.
- SQS/SNS/EventBridge: requests/events.

Good:
- Low idle cost.
- Scales with demand.

Risk:
- Chatty architectures can create many paid events.
- Inefficient code can increase duration.
- Unbounded retries can increase cost.

## Serverless vs Containers vs EC2
| Requirement | Better starting point |
|---|---|
| Short event-driven code | Lambda |
| Long-running service | ECS/EKS/EC2 |
| Existing container app | ECS/Fargate or EKS |
| Full OS control | EC2 |
| Workflow with retries and branches | Step Functions |
| Very predictable always-on workload | Compare EC2/ECS reserved capacity vs serverless cost |

## Common Mistakes
- Treating Lambda local storage as durable.
- Ignoring retries and duplicate events.
- Putting too much business workflow logic into one large Lambda.
- Giving all functions broad admin IAM permissions.
- Forgetting concurrency limits and downstream database capacity.
- Using Lambda for jobs that exceed the timeout.
- Not setting alarms on errors, throttles, and DLQs.

## Official References
- [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/)
- [Amazon API Gateway documentation](https://docs.aws.amazon.com/apigateway/)
- [Amazon DynamoDB documentation](https://docs.aws.amazon.com/dynamodb/)
- [AWS Step Functions documentation](https://docs.aws.amazon.com/step-functions/)
- [Amazon EventBridge documentation](https://docs.aws.amazon.com/eventbridge/)
- [Serverless on AWS](https://aws.amazon.com/serverless/)
