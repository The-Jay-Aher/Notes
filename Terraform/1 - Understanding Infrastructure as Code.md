# 1 - Understanding Infrastructure as Code

## What Is Infrastructure as Code (IaC)?

Infrastructure as Code is the practice of defining and managing infrastructure using versioned code instead of manual console clicks.

You declare resources such as:

- Compute
- Networking
- Storage
- Identity and policy controls

## Why IaC Matters

### 1. Consistency

- Same code creates same infrastructure patterns repeatedly.
- Reduces configuration drift and manual mistakes.

### 2. Speed

- Provision environments quickly.
- Easier to replicate environments (dev/test/stage/prod).

### 3. Collaboration

- Infrastructure lives in Git like application code.
- Supports pull requests, reviews, and audit history.

### 4. Safer Change Management

- Planned changes are reviewed before execution.
- Easier rollback/recovery strategies with version control.

### 5. Cost and Governance Benefits

- Standardized templates reduce overprovisioning.
- Policy checks and tagging standards are easier to enforce.

## Declarative vs Imperative Approaches

- **Declarative:** Describe desired end state; tool calculates required actions.
- **Imperative:** Define step-by-step commands.

Terraform primarily follows a declarative model.

## Why Terraform for IaC

Terraform helps you:

- Manage infrastructure across many providers.
- Reuse patterns via modules.
- Track real infrastructure using state.
- Plan changes before applying them.

## Quick Summary

1. IaC replaces manual infrastructure workflows with reproducible code.
2. Terraform is a declarative IaC tool with strong ecosystem support.
3. Version control and review processes are foundational to reliable IaC.
