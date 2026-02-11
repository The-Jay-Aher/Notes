# 2 - IAM and AWS CLI

## IAM Overview

**IAM (Identity and Access Management)** is a global AWS service used to control authentication (who signs in) and authorization (what they can do).

Core IAM entities:

- **User:** Identity for a person or workload needing long-term credentials.
- **Group:** Collection of users with shared permissions.
- **Role:** Identity with permissions that is assumed temporarily.
- **Policy:** JSON document defining allowed/denied actions.

## IAM Users and Groups

- Users can belong to multiple groups.
- Groups can contain users only (not other groups).
- Users do not have to belong to a group.
- Common pattern: assign permissions to groups, then place users in groups.

## IAM Policies

Policies define permissions via JSON statements.

### Policy Structure

Top-level fields:

- `Version` (commonly `2012-10-17`)
- `Id` (optional)
- `Statement` (required; one or more statements)

Statement fields:

- `Sid` (optional)
- `Effect` (`Allow` or `Deny`)
- `Principal` (who is allowed/denied; mainly in resource-based/trust policies)
- `Action` (API actions such as `s3:GetObject`)
- `Resource` (ARNs the action applies to)
- `Condition` (optional context-based controls)

### Least Privilege Principle

Grant only the minimum permissions required for a task, then refine further as usage becomes clear.

### IAM Policy Evaluation Basics

- By default, all requests are implicitly denied.
- An explicit `Allow` is required to grant access.
- Any explicit `Deny` overrides an `Allow`.

## Password Policy and MFA

### IAM Password Policy

AWS account password policies can enforce:

- Minimum length
- Uppercase/lowercase/number/symbol requirements
- Password expiration and rotation settings
- Prevention of password reuse
- User ability to change own password

### Multi-Factor Authentication (MFA)

MFA adds a second factor beyond password (something you know + something you have).

Why it matters:

- Protects against compromised passwords
- Strongly recommended for all users
- Critical for the root account

## Accessing AWS

Users commonly access AWS through:

1. **AWS Management Console**
2. **AWS CLI (Command Line Interface)**
3. **AWS SDKs** (programmatic access from code)

## Access Keys, CLI, and SDK

### Access Keys

- Created for IAM users (or avoided in favor of temporary credentials when possible).
- Consist of:
  - **Access Key ID**
  - **Secret Access Key**

Security guidance:

- Treat secret keys like passwords.
- Never hardcode keys in source code or notes.
- Rotate keys and disable unused keys.
- Prefer IAM roles + temporary credentials over long-lived keys.

### AWS CLI Basics

AWS CLI lets you call AWS APIs from a terminal and automate operations.

Typical setup:

- Install CLI
- Run `aws configure`
- Provide access key, secret key, default region, and output format

Useful for:

- Operational scripting
- Repeatable infrastructure workflows
- Faster troubleshooting and resource inspection

## IAM Roles for AWS Services

Use IAM roles so AWS services can act on your behalf without static credentials.

Common examples:

- EC2 instance role
- Lambda execution role
- CloudFormation service role

Benefits:

- Temporary credentials
- Easier credential rotation and reduced secret management risk

## IAM Security and Audit Tools

### IAM Credentials Report (Account Level)

Provides credential status details for users, including:

- Password enabled/last used
- Access key age/last used
- MFA enabled status

### IAM Access Advisor (Principal Level)

Shows:

- Which services a user/role can access
- When those services were last accessed

Useful for identifying and removing unnecessary permissions.

## IAM Best Practices

- Use root account only for tasks that require root.
- Enable MFA for root and IAM users.
- Create users for people; avoid shared identities.
- Assign permissions to groups and roles, not directly to every user when avoidable.
- Prefer roles and temporary credentials over long-lived access keys.
- Apply least privilege and review permissions regularly.
- Use credential reports and access advisor for audits.
- Never share IAM credentials.

## Quick Summary

1. IAM is global and controls access to AWS.
2. Users, groups, roles, and policies are the IAM building blocks.
3. Policies use JSON and follow implicit deny + explicit allow + explicit deny precedence.
4. MFA and strong password policy significantly improve account security.
5. CLI and SDK access should use secure credential practices.
6. IAM roles are the preferred way for AWS services/workloads to obtain permissions.
