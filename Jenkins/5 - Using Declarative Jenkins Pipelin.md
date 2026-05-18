# 5 - Using Declarative Jenkins Pipeline

## Declarative Pipeline Basics

Declarative Pipeline is a structured Jenkinsfile syntax designed for readability and standardization.

Common high-level blocks:

- `pipeline`
- `agent`
- `stages`
- `stage`
- `steps`
- `post`
- `environment`
- `triggers`

## Why Declarative Pipeline

- Easier to read and review
- Strong structure for CI/CD standards
- Built-in post-condition handling (`always`, `success`, `failure`, etc.)

## Limitations and Practical Notes

- Some advanced control logic is easier in Scripted Pipeline.
- Not every plugin feature is equally ergonomic in declarative syntax.
- You can still execute shell commands within `steps`.

## Jenkinsfile in Version Control

Best practice:

- Store `Jenkinsfile` with application source code.
- Use branches/PRs to review pipeline changes.

Alternative pattern:

- Centralized pipeline repo for shared platform governance.

## Pipeline Validation (Linting)

Why lint:

- Detect syntax issues early.
- Reduce failed builds from invalid Jenkinsfile changes.

Note:

- Lint behavior can depend on Jenkins instance/plugins.

## Agent Label Resolution

- Agent labels are resolved at execution time.
- Dynamic/ephemeral agents are commonly provisioned for runs.

## Quick Summary

1. Declarative Pipeline covers most CI/CD needs with cleaner structure.
2. Version-control your Jenkinsfiles.
3. Validate pipeline syntax before full runs.
