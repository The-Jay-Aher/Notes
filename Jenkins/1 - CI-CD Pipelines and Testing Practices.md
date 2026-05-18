# 1 - CI/CD Pipelines and Testing Practices

## Quick Summary

CI/CD is the practice of automatically building, testing, packaging, and releasing software changes. Jenkins is one tool that can orchestrate this process.

The goal is not just "run some jobs." The goal is to create fast, repeatable feedback so bad changes are caught early and good changes can move safely toward production.

## Why It Matters

Without a pipeline:

- Builds depend on one person's machine.
- Tests are skipped or run inconsistently.
- Releases become manual and risky.
- Debugging "what changed?" becomes harder.

With a good pipeline:

- Every change follows the same checks.
- Results are visible to the team.
- Artifacts are reproducible.
- Deployments become controlled and auditable.

## Core Concepts

| Concept | Meaning |
| --- | --- |
| CI | Continuous Integration: merge changes frequently and validate automatically. |
| CD | Continuous Delivery or Deployment: automate release steps after validation. |
| Pipeline | Ordered automation flow for build, test, scan, package, and deploy. |
| Stage | A major section of a pipeline, such as Build or Test. |
| Job | A runnable unit in Jenkins. |
| Artifact | Build output, such as jar, image, report, or package. |
| Quality gate | Required check before promotion or deployment. |
| Rollback | Process to return to a known-good version. |

## CI vs Continuous Delivery vs Continuous Deployment

| Practice | Meaning |
| --- | --- |
| Continuous Integration | Every change is integrated and tested frequently. |
| Continuous Delivery | Code is always kept deployable, but production release may require approval. |
| Continuous Deployment | Passing changes automatically deploy to production. |

For many teams, continuous delivery is safer than full continuous deployment because production still has an approval gate.

## Typical Pipeline Flow

```text
checkout -> build -> unit tests -> static checks -> package -> integration tests -> security scans -> publish artifact -> deploy -> smoke test
```

Not every project needs every stage. The pipeline should match risk.

## Common Test Types

| Test Type | Purpose | When To Run |
| --- | --- | --- |
| Lint/static checks | Catch style, syntax, and basic quality issues. | Early. |
| Unit tests | Test small pieces of code in isolation. | Every PR/commit. |
| Smoke tests | Quick check that app starts and core path works. | After build/deploy. |
| Integration tests | Test interaction between components. | PR or pre-merge depending on cost. |
| Functional tests | Verify feature behavior. | PR, nightly, or pre-release. |
| Acceptance tests | Validate business/user requirements. | Pre-release or gated stage. |
| Security scans | Find dependency, code, container, or config risks. | PR and release stages. |
| Performance tests | Measure latency/throughput/capacity. | Scheduled or pre-release. |

## Practical Pipeline Testing Order

Run faster and cheaper checks first:

1. Checkout.
2. Syntax/lint/static validation.
3. Unit tests.
4. Build/package.
5. SCA/dependency scan.
6. Container/IaC scan if relevant.
7. Integration tests.
8. Deploy to test/staging.
9. Smoke tests.
10. Approval gate.
11. Production deployment.
12. Post-deploy verification.

## Quality Gates

Quality gates decide whether a build can move forward.

Examples:

- Tests must pass.
- Code coverage must not drop below a threshold.
- No critical vulnerabilities.
- Build artifact must be produced.
- Manual approval required for production.
- Change ticket must be linked.

Avoid making gates noisy. A gate that blocks for low-value warnings will train people to ignore it.

## Artifact Handling

Good artifact rule:

```text
Build once, promote the same artifact.
```

Bad pattern:

```text
Build separately for dev, staging, and production.
```

Why build once:

- Same code goes through all environments.
- Easier rollback.
- Easier audit.
- Reduces environment-specific build drift.

Common artifacts:

- Java `.jar` or `.war`.
- Docker/OCI image.
- npm package.
- Python wheel.
- Terraform plan file.
- Test reports.

## Branch And Pull Request Strategy

Common model:

```text
feature branch -> pull request -> CI checks -> merge to main -> build release artifact -> deploy
```

Best practices:

- Run CI on pull requests.
- Require status checks before merge.
- Keep branches short-lived.
- Avoid manual changes after artifact creation.
- Tag releases when needed.

## Benefits

- Fast feedback.
- Repeatable builds.
- Safer deployments.
- Better collaboration.
- Auditable release history.
- Easier rollback when artifacts are versioned.

## Drawbacks / Limitations

- Pipelines can become slow and expensive.
- Flaky tests reduce trust.
- Overly strict gates can block useful work.
- Secrets and credentials must be handled carefully.
- Poorly designed deployment automation can break production faster.

## Hidden Details / Caveats

- Passing CI does not prove production readiness if environments differ.
- Test order matters for feedback speed.
- Parallel stages speed up feedback but can make logs harder to follow.
- Deployment should include health checks and rollback planning.
- CI agents need clean, reproducible environments.
- Long-running pipelines should publish intermediate logs and reports.

## Common Mistakes

| Mistake | Better Approach |
| --- | --- |
| One giant pipeline stage | Split into meaningful stages. |
| Running slow tests first | Run fast checks early. |
| Rebuilding artifact per environment | Build once and promote. |
| Ignoring flaky tests | Fix or quarantine with ownership. |
| Storing secrets in Jenkinsfile | Use Jenkins credentials and least privilege. |
| No post-deploy smoke test | Verify the deployed app. |

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Pipeline slow | Stage timing, dependency cache, test parallelism, agent capacity. |
| Build works locally but fails in Jenkins | Environment variables, tool versions, paths, permissions. |
| Flaky tests | Time dependence, shared state, network calls, test order, resource contention. |
| Artifact missing | Archive/publish step, workspace cleanup, failed build step. |
| Deployment failed | Credentials, network access, target environment state, rollback process. |

## Interview Notes

- CI gives fast validation for frequent code integration.
- Continuous delivery keeps code deployable with manual release control.
- Continuous deployment releases automatically after passing gates.
- A good pipeline runs fast checks first.
- Build once, promote the same artifact.
- Quality gates should be meaningful and low-noise.
- Jenkins Pipeline is commonly stored as a `Jenkinsfile` in version control.

## Related Topics

- [Using Declarative Jenkins Pipeline](5%20-%20Using%20Declarative%20Jenkins%20Pipeline.md)
- [Learning GitHub Actions](../Learning%20GitHub%20Actions.md)
- [Introduction to DevSecOps for Cloud](../Introduction%20to%20DevSecOps%20for%20Cloud/1%20-%20Introduction.md)

