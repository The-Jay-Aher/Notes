# 4 - Monitoring, Security, and Pricing

## 1) Monitoring, Logging, and Auditing Services

### Observability Basics

Three common telemetry types:

- **Metrics:** Numeric time-series values (for example CPU utilization).
- **Logs:** Event records from systems/apps.
- **Traces:** End-to-end request flow across distributed services.

Good observability supports reliability, security, performance, and cost optimization.

### Amazon CloudWatch

CloudWatch is AWS's primary monitoring and observability service.

Capabilities:

- Metrics collection and dashboards
- Log ingestion and analysis (CloudWatch Logs)
- Alarms and notifications
- Event integration and automation hooks

Examples:

- EC2 CPU utilization alarm
- Lambda error/latency dashboards
- Application logs centralization

### AWS CloudTrail

CloudTrail records API activity and account events.

Why it matters:

- Security forensics
- Compliance evidence
- Change/audit history

Typical pattern:

- Send trails to S3 for retention.
- Analyze with Athena/CloudWatch/third-party SIEM tools.

### AWS Config

Tracks resource configuration changes and evaluates compliance.

- Continuous configuration recording
- Managed and custom rules
- Useful for governance and drift detection

### AWS Audit Manager

Helps collect evidence for compliance audits using prebuilt frameworks.

### AWS Systems Manager (Operations)

Helps operate resources at scale across AWS and hybrid environments.

Examples:

- Parameter Store for configuration/secrets (non-rotating)
- Patch management and automation runbooks
- Fleet operations visibility

### Service Health and Recommendations

### AWS Health Dashboard

- Shows AWS service events that may affect your resources/accounts.

### AWS Trusted Advisor

- Recommendations across cost, security, performance, service limits, and operational excellence.

---

## 2) Security, Compliance, and Governance

### Shared Responsibility Model

- **AWS:** Security *of* the cloud (hardware, facilities, foundational services).
- **Customer:** Security *in* the cloud (identity, data, network config, workloads).

Responsibility varies by service model (IaaS vs managed services).

### IAM and Least Privilege

- Grant minimum permissions required for a task.
- Prefer roles and temporary credentials over long-lived keys.
- Enforce MFA for privileged identities.

Useful IAM tools:

- IAM Access Analyzer
- IAM Policy Simulator

### Identity Federation Services

### AWS IAM Identity Center

- Centralized SSO access to multiple AWS accounts/apps.

### Amazon Cognito

- User authentication/authorization for web/mobile applications.

### AWS Directory Service

- Integrates AWS with Microsoft Active Directory patterns.

### AWS STS (Security Token Service)

- Issues temporary credentials for role-based access.

### Data Protection

### Encryption at Rest and In Transit

- Use service-integrated encryption and AWS KMS where appropriate.
- Use TLS/HTTPS for data in transit.

### AWS Secrets Manager

- Secure secret storage with rotation support.

### Systems Manager Parameter Store

- Secure parameter storage (configuration/secrets) with optional KMS encryption.

### Amazon Macie

- Discovers and helps protect sensitive data in S3 (for example PII).

### Network and Application Protection Services

### Security Groups and NACLs

- Security Groups: stateful, resource-level firewall.
- NACLs: stateless, subnet-level filtering.

### AWS WAF

- Protects web apps from common web exploits.

### AWS Shield

- DDoS protection.
- Shield Standard is included for many AWS services.

### AWS Network Firewall

- Managed network firewall for advanced VPC traffic filtering.

### AWS Firewall Manager

- Centralized policy management across accounts.

### Threat Detection and Security Posture

### Amazon GuardDuty

- Threat detection service using account/network/activity signals.

### Amazon Inspector

- Automated vulnerability management for supported workloads.

### AWS Security Hub

- Aggregates and prioritizes security findings from integrated services.

### Amazon Detective

- Investigates and analyzes security events.

---

## 3) AWS Pricing and Cost Management

### Pricing Fundamentals

Typical cost dimensions:

- Compute time
- Storage usage
- Data transfer
- Requests/operations

General cloud economics:

- Pay-as-you-go
- Save with commitment models where usage is predictable
- Optimize continuously

### Core Cost Management Services

### AWS Pricing Calculator

- Estimates workload cost before deployment.

### AWS Billing and Cost Management

- Billing dashboard, invoices, and account-level cost views.

### AWS Cost Explorer

- Visualize and analyze historical spend and usage trends.

### AWS Budgets

- Alerts for cost/usage thresholds.

### Cost and Usage Report (CUR)

- Most detailed billing dataset for advanced analysis.

### Savings Plans and Reserved Capacity Concepts

- Commitment-based pricing can reduce cost for predictable usage.

### Cost Optimization Practices

- Right-size resources.
- Turn off idle non-production environments.
- Use auto scaling.
- Choose appropriate storage classes/lifecycle policies.
- Use tagging (`Environment`, `Owner`, `Application`, `CostCenter`) for allocation and governance.

### Quick Summary

1. CloudWatch + CloudTrail + Config form a strong monitoring/auditing core.
2. Security is shared between AWS and the customer.
3. Cost visibility and optimization require continuous tracking and governance.
