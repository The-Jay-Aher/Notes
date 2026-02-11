# 1 - CI/CD Pipelines and Testing Practices

## CI/CD Overview

CI/CD helps teams build, test, and release software faster and more reliably.

- **Continuous Integration (CI):** Frequently merge changes and validate with automated builds/tests.
- **Continuous Delivery/Deployment (CD):** Automate release steps so software can be delivered consistently.

## Common Test Types in a CI/CD Pipeline

### Smoke Test

- Fast, shallow checks to confirm core functionality works.
- Usually run early after build/deploy.

### Unit Test

- Tests the smallest parts of code in isolation.
- Helps catch regressions early in development.

### Functional Test

- Validates behavior against functional requirements.
- Focuses on whether features do what they are expected to do.

### Acceptance Test

- Validates software against business/user requirements.
- Confirms solution is acceptable for end users.

## Practical Pipeline Testing Order

A common flow:

1. Build
2. Unit tests
3. Smoke tests
4. Functional/integration tests
5. Acceptance tests
6. Deployment and post-deployment checks

## Quick Summary

1. CI/CD improves release velocity and quality.
2. Different test levels provide layered confidence.
3. Fast feedback loops reduce deployment risk.
