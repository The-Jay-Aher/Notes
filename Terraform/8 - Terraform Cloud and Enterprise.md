# 8 - Terraform Cloud and Enterprise

## Policy as Code with Sentinel

Sentinel is HashiCorp's policy-as-code framework used with Terraform Cloud/Enterprise.

What it enables:

- Enforce governance and security controls before apply
- Standardize compliance checks across teams
- Block non-compliant infrastructure changes automatically

Example policy goals:

- Require mandatory tags
- Restrict instance sizes or regions
- Prevent open security group rules on sensitive ports

## Secrets Best Practice with Vault Provider

### HashiCorp Vault Overview

Vault is a secrets management system that supports:

- Secure secret storage
- Dynamic short-lived credentials
- Access policies and audit trails

## Terraform + Vault Pattern

1. Terraform requests credentials from Vault at runtime.
2. Vault returns temporary credentials.
3. Terraform uses them for provisioning.
4. Secrets are not hardcoded in code or long-lived in pipelines.

Benefits:

- Reduced secret sprawl
- Lower risk than static credentials
- Better operational security controls

## Terraform Registry

Terraform Registry provides reusable modules/providers.

Benefits:

- Faster development with known module patterns
- Standardized building blocks
- Easy sharing of internal/private modules (private registry)

## Terraform Cloud Workspaces

Terraform Cloud workspaces are cloud-hosted execution/state units for Terraform workflows.

Capabilities:

- Remote runs
- State management and history
- Variable and secret management
- Team access controls
- VCS integration and run triggers

## Terraform OSS Workspaces vs Terraform Cloud Workspaces

### Terraform OSS Workspaces

- Alternate state files in one local configuration directory.

### Terraform Cloud Workspaces

- Managed workspace model with remote execution, collaboration, and governance features.

## Terraform Cloud/Enterprise Advantages (Summary)

- Collaboration-oriented workflows
- Remote execution and centralized state
- Policy checks (Sentinel)
- Cost estimation integrations
- Private module registry support
- Role-based access controls

## Quick Summary

1. Sentinel enforces policy guardrails pre-deployment.
2. Vault integration improves secret hygiene using temporary credentials.
3. Terraform Cloud/Enterprise adds collaboration and governance capabilities beyond Terraform OSS alone.
