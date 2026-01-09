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