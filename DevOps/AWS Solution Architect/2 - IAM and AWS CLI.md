# IAM Introduction

## IAM: Users & Groups

- IAM = Identity and Access Management, Global Service
- Users are people within your organization, and can be grouped
- Groups only contain users, not other groups
- users don't have to belong to a group, and a user can belong to multiple groups

## IAM: Permissions

- Users or groups can be assigned JSON documents called policies
- These policies define the permission of the users
- In AWS, you apply the **least privilege principle**: don't give more permissions that a user needs

# IAM Policies

## IAM Policies Structure

Consists of
	- Version: policy language version, always include `"2012-10-17"`
	- Id: an identifier for a policy (optional)
	- Statement: one or more individual statements (required)
Statements consists of
	- Sid: an identifier for the statement (optional)
	- Effect: Whether the statement allows or denies access (Allow, Deny)
	- Principal: Account/user/role to which this policy is applied to
	- Action: list of actions this policy allows or denies
	- Resource: list of resources to which the action is applied to
	- Condition: condition for when this policy is in effect (optional)

# IAM MFA

## IAM - Password Policy

Strong passwords = higher security for your accounts
In AWS, you can setup a password policy:
	- Set a minimum password length
	- Require specific character types:
		- including uppercase letters
		- lowercase numbers
		- numbers
		- non-alphanumeric characters
	- Allow all IAM user to change their own passwords
	- require users to change their password after some time (password expiration)
	- Prevent password re-use

## Multi Factor Authentication - MFA

Users have access to your account and can possibly change configurations or delete resources in you AWS account
You want to protect your root accounts and IAM users
MFA - Passwords you know + security device you own

Main benefit of MFA:
	If a password is stolen or hacked, the account is not compromised 

# AWS Access Key, CLI and SDK

## How can users access AWS?

TO access AWS users have 3 option:
1. AWS Management Console
2. AWS Command Line Interface (CLI)
3. AWS Software Development Kit (SDK)

Access keys are generated through AWS console
users manage their own access keys

***Access Keys are secret, just like password. Don't share them***

Access Key ID ~= Username
Secret Access Key ~= password

## What's the AWS CLI?

- A tool that enables you to interact with AWS services, using commands in your command-line shell
- Direct access to the public APIs of AWS services
- You can develop scripts to manage your resources

# IAM Roles for AWS Services

Some AWS services will perform actions on your behalf
To do so, we will assign permissions to AWS Services with IAM Roles
Common Roles:
	- EC2 Instance roles
	- Lambda Function Roles
	- Roles for CloudFormation

# IAM Security Tools

- IAM Credentials Report (account-level)
	- A report that lists all your account user's and the status of their various credentials
- IAM Access Advisor (user-level)
	- Access advisor shows the service permissions granted to a user and when those services were last accessed
	- You can use this information to revise your policies

# IAM Guidelines & Best Practices

- Don't use the root account except for AWS account setup
- One physical server = One AWS Server
- Assign users to groups and assign permissions to groups 
- Create a strong password policy
- Use and enforce the use of Multi Factor Authentication (MFA)
- Create and use **Roles** for giving permissions to AWS services
- Use access keys for programmatic access (cli/sdk)
- Audit the permissions to your account, using IAM Credentials Report & IAM Access Advisor
- **Never share your IAM users and Access Keys**

# IAM Summary
1. Users: mapped to physical users, has a password for physical console
2. Groups: contains users only
3. Policies: JSON document that outlines permissions for users and groups
4. Roles: for EC2 Instances or AWS Services
5. Security: MFA + Password Policy
6. AWS CLI: manage your AWS services using command line
7. AWS SDK: manage your AWS services using a programming language
8. Access Keys: access AWS using CLI or SDK
9. Audit: IAM Credentials Report & IAM Access Advisor