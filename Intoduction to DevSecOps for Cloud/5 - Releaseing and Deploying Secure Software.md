# 5 - Releasing and Deploying Secure Software

## Releasing Secure Software

## Release Stage Focus Areas

- Configuration management
- Access management
- Data protection controls

## Configuration Management

Core practices:

- Baselines and standards
- Controlled change process
- Auditability and documentation
- Verification of desired state

## Access Management

- Strong authentication and authorization
- Role-based access and least privilege
- Privileged access controls

## Container and Runtime Security

- Use trusted/minimal images
- Remove unnecessary components
- Apply runtime restrictions and policy controls

## Network Security Controls

Examples:

- VPC segmentation
- Security groups/firewalls
- Network-level inspection where needed

## Data Security Controls

Examples of cloud-native services:

- AWS KMS
- Azure information protection/security services
- GCP Secret Manager

## Deploying Secure Software

## Environment Strategy

Maintain clear separation of:

- Development
- Staging
- Production

## Infrastructure as Code (IaC)

IaC benefits:

- Automation and consistency
- Versioned secure templates
- Repeatable deployments and policy enforcement

Cloud examples:

- AWS CloudFormation
- Azure Resource Manager / Bicep ecosystems
- GCP deployment tooling

## Penetration Testing

Purpose:

- Simulate attacker behavior to validate defenses.

Typical phases:

1. Reconnaissance
2. Enumeration
3. Exploitation (authorized scope only)
4. Reporting and remediation guidance

## Quick Summary

1. Secure release requires strong config, access, and data controls.
2. Deployment should use environment isolation and IaC.
3. Pen testing validates real-world defensive readiness.
