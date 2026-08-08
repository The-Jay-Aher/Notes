# AWS Monitoring and Audit: CloudWatch, CloudTrail and Config

## Quick Summary
- CloudWatch observes operational health: metrics, logs, alarms, dashboards, and events.
- CloudTrail records AWS API activity: who did what, when, from where.
- AWS Config records resource configuration history and evaluates compliance rules.
- Use CloudWatch to answer "is it healthy?", CloudTrail to answer "who changed it?", and Config to answer "is it configured correctly?"
- A good architecture uses all three because they solve different problems.

## Three Different Questions
| Question | Service |
|---|---|
| Is my application healthy? | CloudWatch |
| Who called this AWS API? | CloudTrail |
| Did a resource configuration drift from policy? | AWS Config |

## Amazon CloudWatch
CloudWatch is AWS's main monitoring and observability service.

It provides:
- Metrics.
- Logs.
- Alarms.
- Dashboards.
- Events/EventBridge integration.
- Synthetics canaries.
- Application monitoring features.

## CloudWatch Metrics
Metrics are numeric time-series data.

Examples:
- EC2 CPUUtilization.
- ALB TargetResponseTime.
- Lambda Errors.
- DynamoDB ThrottledRequests.
- SQS ApproximateAgeOfOldestMessage.

Metric dimensions identify what the metric belongs to.

Example:
- EC2 CPUUtilization by InstanceId.
- ALB metrics by LoadBalancer and TargetGroup.

## CloudWatch Alarms
Alarms watch metrics and change state.

States:
- OK.
- ALARM.
- INSUFFICIENT_DATA.

Alarms can trigger actions:
- SNS notification.
- Auto Scaling policy.
- EC2 action.
- Systems Manager action in supported workflows.

Example:

```text
If SQS oldest message age > 5 minutes for 3 datapoints -> send SNS alert
```

## CloudWatch Logs
CloudWatch Logs stores log events.

Common sources:
- Lambda logs.
- ECS container logs.
- EC2 application logs via agent.
- API Gateway logs.
- VPC Flow Logs.
- Route 53 Resolver logs.

Core concepts:
- Log group.
- Log stream.
- Log event.
- Retention setting.

Important beginner point:
- Set log retention. Otherwise logs may be kept indefinitely and cost can grow.

## CloudWatch Logs Insights
Logs Insights lets you query logs.

Example query:

```text
fields @timestamp, @message
| sort @timestamp desc
| limit 20
```

Use it for:
- Finding errors.
- Filtering by request ID.
- Investigating latency.
- Counting events.

## CloudWatch Dashboards
Dashboards show metrics and logs widgets.

Use dashboards for:
- Service health views.
- Executive status.
- Operations screens.
- Deployment monitoring.

Do not rely only on dashboards. Use alarms for active notification.

## CloudTrail
CloudTrail records AWS account activity and API calls.

CloudTrail answers:
- Who made this change?
- Which API was called?
- From which IP?
- At what time?
- Was it successful?

Examples:
- A user deleted a security group rule.
- A role created an S3 bucket.
- An access key called `RunInstances`.
- A root user action occurred.

## CloudTrail Events
Types include:
- Management events: control plane actions such as creating buckets or changing IAM.
- Data events: data plane actions such as S3 object-level access or Lambda function invocation.
- Insights events: unusual API activity patterns.

Management events are broadly important. Data events are high volume and must be enabled selectively.

## CloudTrail Trails
A trail delivers events to S3 and optionally CloudWatch Logs.

Good practice:
- Create an organization trail across accounts.
- Store logs in a central security account.
- Enable log file validation.
- Encrypt logs with KMS where required.
- Restrict deletion access.

## CloudTrail vs CloudWatch Logs
CloudTrail logs AWS API activity.

CloudWatch Logs stores application, service, and operational logs.

Example:
- Lambda application error goes to CloudWatch Logs.
- The API call that changed Lambda memory size appears in CloudTrail.

## AWS Config
AWS Config records resource configurations and evaluates them against rules.

It answers:
- What did this resource configuration look like yesterday?
- Which resources are non-compliant?
- Who changed a resource and when, combined with CloudTrail?
- Did a security group become open to the world?

## Config Rules
Rules evaluate compliance.

Examples:
- S3 buckets should not be public.
- EBS volumes should be encrypted.
- IAM users should not have inline policies.
- Security groups should not allow unrestricted SSH.

Rules can be:
- AWS managed rules.
- Custom rules using Lambda.

## Config Remediation
Config can trigger remediation actions.

Example:

```text
Rule detects unencrypted S3 bucket -> Systems Manager automation remediates or alerts
```

Use caution with automatic remediation. Test it carefully to avoid breaking production.

## Common Combined Investigation
Scenario:
- A security group now allows SSH from `0.0.0.0/0`.

Use:
- AWS Config to see when the resource became non-compliant.
- CloudTrail to see who called the security group API.
- CloudWatch alarms/logs if the change caused operational impact.

## VPC Flow Logs
VPC Flow Logs capture network flow metadata.

They can help answer:
- Is traffic accepted or rejected?
- Which IPs are communicating?
- Which ports are used?

They do not capture packet payloads.

Destinations include:
- CloudWatch Logs.
- S3.
- Kinesis Data Firehose.

## Monitoring Design Checklist
- Define service-level indicators: latency, errors, availability, saturation.
- Add CloudWatch alarms for user-impacting symptoms.
- Add alarms for queue backlog and DLQs.
- Send important logs to CloudWatch Logs or a log analytics system.
- Set log retention.
- Enable CloudTrail organization trail.
- Enable AWS Config for important accounts/Regions.
- Protect audit logs from deletion.
- Test alerts so they reach the right people.

## Common Mistakes
- Using CloudTrail as an application log system.
- Using CloudWatch metrics to find who changed IAM policies.
- Enabling CloudTrail data events everywhere without understanding cost.
- Creating dashboards but no alarms.
- Leaving CloudWatch Logs retention unlimited by accident.
- Enabling Config in only one Region when resources exist in many Regions.
- Not centralizing logs across accounts.

## Official References
- [Amazon CloudWatch documentation](https://docs.aws.amazon.com/cloudwatch/)
- [CloudWatch Logs documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [AWS CloudTrail documentation](https://docs.aws.amazon.com/cloudtrail/)
- [AWS Config documentation](https://docs.aws.amazon.com/config/)
- [VPC Flow Logs documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
