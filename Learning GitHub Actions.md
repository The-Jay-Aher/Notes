# Learning GitHub Actions

## Quick Summary

GitHub Actions is GitHub's built-in automation platform. It runs workflows from YAML files stored in `.github/workflows/` and is commonly used for CI, CD, release automation, scheduled jobs, security scans, issue automation, and repository maintenance.

The mental model is simple:

```text
event happens -> workflow starts -> jobs run on runners -> steps execute commands or actions
```

Official reference links:

- GitHub Actions documentation: <https://docs.github.com/en/actions>
- Workflow syntax: <https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions>
- Contexts: <https://docs.github.com/en/actions/learn-github-actions/contexts>
- Expressions: <https://docs.github.com/en/actions/learn-github-actions/expressions>

## Why It Matters

GitHub Actions is useful because it keeps automation close to the repository:

- Every pull request can run tests before merge.
- Deployments can require approvals through environments.
- Releases can be built consistently from tags.
- Security checks can run automatically.
- Repetitive repository tasks can be automated without a separate CI server.

In real teams, a good workflow prevents broken code from reaching `main`, makes deployment repeatable, and creates an audit trail for what ran, when it ran, and which commit triggered it.

## Core Concepts

| Concept | Meaning |
| --- | --- |
| Workflow | A YAML automation file under `.github/workflows/`. |
| Event | The trigger, such as `push`, `pull_request`, `workflow_dispatch`, or `schedule`. |
| Job | A group of steps that runs on the same runner by default. |
| Step | A single command or action inside a job. |
| Runner | The machine that executes the job. It can be GitHub-hosted or self-hosted. |
| Action | A reusable automation unit, often referenced as `owner/repo@version`. |
| Context | Runtime data available to expressions, such as `github`, `env`, `secrets`, `inputs`, and `matrix`. |
| Artifact | A file produced by a workflow and stored for later download. |
| Cache | Reused dependency or build data that speeds up future runs. |
| Environment | A deployment target such as `staging` or `production`, often with protection rules. |

## Workflow File Location

Workflow files live here:

```text
.github/workflows/<workflow-name>.yml
.github/workflows/<workflow-name>.yaml
```

Example:

```text
.github/workflows/ci.yml
```

## Basic Workflow Example

```yaml
name: CI

on:
  pull_request:
  push:
    branches:
      - main

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest -q
```

## How It Works

1. A developer opens a pull request or pushes to `main`.
2. GitHub checks `.github/workflows/`.
3. Any workflow whose `on:` trigger matches the event is queued.
4. GitHub assigns each job to a runner.
5. The runner checks out code if the workflow asks it to.
6. Steps run in order inside each job.
7. The workflow reports success, failure, skipped, or cancelled.
8. Branch protection can require specific workflow checks before merge.

## Events

Common events:

| Event | Use Case |
| --- | --- |
| `push` | Run after code is pushed to selected branches or tags. |
| `pull_request` | Validate proposed changes before merge. |
| `workflow_dispatch` | Manual button-triggered workflow. |
| `schedule` | Cron-based automation. |
| `release` | Build or publish after release events. |
| `issues` | Automate issue triage. |
| `pull_request_target` | Runs in the context of the base repo; powerful but dangerous for untrusted PRs. |

Example manual trigger with inputs:

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: Deployment environment
        required: true
        type: choice
        options:
          - staging
          - production
```

Example schedule:

```yaml
on:
  schedule:
    - cron: "0 2 * * 1"
```

GitHub cron schedules use UTC.

## Jobs

Jobs run in parallel by default. Use `needs:` when one job depends on another.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm test

  build:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4
      - run: npm run build
```

Important job settings:

| Setting | Purpose |
| --- | --- |
| `runs-on` | Selects runner type. |
| `needs` | Creates job dependency order. |
| `if` | Conditionally runs or skips a job. |
| `permissions` | Controls `GITHUB_TOKEN` permissions. |
| `timeout-minutes` | Prevents hung jobs. |
| `strategy.matrix` | Runs job variations. |
| `environment` | Connects a job to deployment approvals/secrets. |

## Steps

Steps can either run shell commands or use actions.

```yaml
steps:
  - name: Run shell command
    run: echo "Hello from GitHub Actions"

  - name: Use a reusable action
    uses: actions/checkout@v4
```

Multiple commands:

```yaml
- name: Build
  run: |
    npm ci
    npm run lint
    npm test
```

## Runners

### GitHub-Hosted Runners

GitHub-hosted runners are managed by GitHub. Common labels include:

- `ubuntu-latest`
- `windows-latest`
- `macos-latest`

Use them when you want low-maintenance CI.

### Self-Hosted Runners

Self-hosted runners are machines you manage.

Use them when you need:

- Private network access.
- Custom hardware.
- GPU or large machines.
- Special software that is expensive to install every run.

Be careful: a self-hosted runner executes code from workflows. Do not let untrusted pull requests run on sensitive self-hosted runners without strong controls.

## Actions

Actions are reusable units.

Common official actions:

| Action | Purpose |
| --- | --- |
| `actions/checkout` | Checks out repository code. |
| `actions/setup-node` | Installs/selects Node.js. |
| `actions/setup-python` | Installs/selects Python. |
| `actions/cache` | Caches dependencies or build outputs. |
| `actions/upload-artifact` | Uploads workflow artifacts. |
| `actions/download-artifact` | Downloads artifacts from the workflow run. |

Pin actions by version tag at minimum:

```yaml
uses: actions/checkout@v4
```

For high-security workflows, pin third-party actions to a full commit SHA so the referenced code cannot change unexpectedly.

## Permissions

Every workflow gets a `GITHUB_TOKEN`. Its permissions should be minimized.

Good default:

```yaml
permissions:
  contents: read
```

Example for a workflow that writes pull request comments:

```yaml
permissions:
  contents: read
  pull-requests: write
```

Avoid using broad permissions such as `write-all` unless there is a clear reason.

## Secrets And Variables

Use secrets for sensitive data:

- API tokens.
- Cloud credentials.
- Passwords.
- Signing keys.

Use variables for non-secret configuration:

- Environment names.
- Region names.
- Feature flags that are not sensitive.

Example:

```yaml
env:
  AWS_REGION: ${{ vars.AWS_REGION }}

steps:
  - name: Use secret
    run: ./deploy.sh
    env:
      DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

Do not print secrets. GitHub masks many secret values, but masking is not a replacement for careful logging.

## Expressions And Contexts

Expressions use `${{ ... }}`.

```yaml
if: ${{ github.event_name == 'pull_request' }}
```

Common contexts:

| Context | Example |
| --- | --- |
| `github` | Commit SHA, branch, event data. |
| `env` | Environment variables defined in workflow/job/step. |
| `secrets` | Repository, organization, or environment secrets. |
| `vars` | Repository, organization, or environment variables. |
| `matrix` | Matrix values for the current job. |
| `steps` | Outputs from earlier steps. |
| `needs` | Outputs/results from dependency jobs. |

## Matrix Builds

Matrix builds run the same job with different inputs.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.10", "3.11", "3.12"]

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pytest -q
```

Use matrix builds for:

- Multiple language versions.
- Multiple operating systems.
- Multiple dependency versions.
- Multiple deployment regions.

## Caching

Caching reduces repeated dependency downloads.

Example npm cache:

```yaml
- uses: actions/setup-node@v4
  with:
    node-version: "20"
    cache: npm

- run: npm ci
```

Example direct cache:

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: pip-${{ runner.os }}-${{ hashFiles('requirements.txt') }}
    restore-keys: |
      pip-${{ runner.os }}-
```

Do not cache secrets or files containing credentials.

## Artifacts

Artifacts are run outputs that should be stored.

```yaml
- name: Upload test report
  uses: actions/upload-artifact@v4
  with:
    name: pytest-report
    path: reports/
```

Use artifacts for:

- Test reports.
- Coverage reports.
- Build outputs.
- Logs from failed jobs.

Do not use artifacts as a long-term package registry. Use a package registry, release asset, container registry, or object storage for long-lived distribution.

## Environments And Deployments

Environments are useful for deployment gates.

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - run: ./deploy.sh
```

Common environment controls:

- Required reviewers.
- Environment-specific secrets.
- Deployment history.
- Branch restrictions.

Use environments when a job changes real infrastructure or production systems.

## Reusable Workflows

Reusable workflows reduce duplication across repositories or workflows.

Caller:

```yaml
jobs:
  call-ci:
    uses: org/shared-workflows/.github/workflows/python-ci.yml@main
    with:
      python-version: "3.12"
```

Reusable workflow:

```yaml
on:
  workflow_call:
    inputs:
      python-version:
        required: true
        type: string
```

Use reusable workflows for standard organization-wide patterns such as test, scan, build, and deploy.

## Composite Actions

Composite actions package repeated step logic.

Directory:

```text
.github/actions/setup-project/action.yml
```

Example:

```yaml
name: Setup project
description: Install dependencies
runs:
  using: composite
  steps:
    - run: npm ci
      shell: bash
```

Use composite actions when you want reusable steps inside one repo or across repos.

## CI Example For A Python Project

```yaml
name: Python CI

on:
  pull_request:
  push:
    branches:
      - main

permissions:
  contents: read

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest -q
```

## Deployment Example With Manual Approval

```yaml
name: Deploy

on:
  workflow_dispatch:
    inputs:
      version:
        description: Version to deploy
        required: true
        type: string

permissions:
  contents: read

jobs:
  deploy-production:
    runs-on: ubuntu-latest
    environment: production
    timeout-minutes: 20

    steps:
      - uses: actions/checkout@v4

      - name: Deploy
        run: ./deploy.sh "${{ inputs.version }}"
```

## Benefits

- Easy to start because it is built into GitHub.
- Workflows live with code and can be reviewed like code.
- Marketplace provides many reusable actions.
- Good fit for PR validation and release automation.
- Environments support approval gates.
- Matrix builds make compatibility testing easier.

## Drawbacks / Limitations

- YAML can become hard to maintain when workflows grow large.
- Third-party actions create supply chain risk.
- Debugging can be slower than local shell execution.
- Self-hosted runners require careful security and patching.
- Hosted runner images change over time, so workflows should avoid relying on undocumented image details.
- Complex deployment orchestration may need a dedicated deployment tool.

## Hidden Details / Caveats

- `pull_request_target` can access base repository secrets and write tokens. Do not run untrusted PR code in that context.
- `secrets` are not passed to workflows triggered from forks in the same way as trusted repository events.
- Jobs run in parallel unless `needs:` creates order.
- Each job gets a fresh runner environment unless you use a self-hosted runner with persistent state.
- A step failing normally fails the job unless `continue-on-error` is used.
- `GITHUB_TOKEN` permissions should be explicitly set.
- `schedule` events are not guaranteed to run exactly at the cron minute.
- `actions/checkout` is required before files from the repository are available.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Forgetting `actions/checkout` | Add checkout before accessing repo files. |
| Giving broad token permissions | Set minimal `permissions:` at workflow or job level. |
| Printing secrets in logs | Pass secrets through environment variables and avoid echoing them. |
| Using unpinned third-party actions | Pin at least to a major version, preferably SHA for sensitive workflows. |
| Running deployment on every push | Restrict branches, tags, or use manual approval. |
| Duplicating workflow logic everywhere | Use reusable workflows or composite actions. |
| Overusing cache | Cache only safe dependency/build directories with stable keys. |

## Best Practices

- Keep workflows small and named by purpose, such as `ci.yml`, `release.yml`, and `deploy.yml`.
- Use `pull_request` checks for validation.
- Use protected environments for production deployments.
- Set job timeouts.
- Minimize `GITHUB_TOKEN` permissions.
- Store secrets in GitHub Secrets or environment secrets, not in YAML.
- Use matrix builds where compatibility matters.
- Upload logs/reports as artifacts for failed or complex jobs.
- Prefer official setup actions for common languages.
- Use branch protection so required checks must pass before merge.

## Troubleshooting

| Problem | Checks |
| --- | --- |
| Workflow does not start | Confirm file is under `.github/workflows/`, YAML is valid, and `on:` matches the event/branch. |
| Command not found | Install the tool, use the right runner OS, or check PATH. |
| Secret is empty | Verify secret name, environment selection, fork restrictions, and repository/organization settings. |
| Cache not restoring | Check key, restore keys, path, and whether the dependency file hash changed. |
| Job waits forever | Check concurrency limits, required environment approvals, or unavailable self-hosted runners. |
| Permission denied from GitHub API | Add the needed `permissions:` entry. |
| Deployment ran on wrong branch | Add branch filters and environment protection rules. |

## Interview Notes

- A workflow is triggered by events and contains jobs.
- Jobs run on runners and contain steps.
- Steps either run commands or use actions.
- Jobs are parallel by default; use `needs:` for ordering.
- `GITHUB_TOKEN` should use least privilege.
- Use secrets for sensitive values and variables for non-sensitive configuration.
- Use artifacts for outputs and caches for dependency speed.
- Use environments for deployment approvals and environment-specific secrets.

## Related Topics

- [Jenkins CI/CD notes](Jenkins/1%20-%20CI-CD%20Pipelines%20and%20Testing%20Practices.md)
- [Terraform CLI](Terraform/7%20-%20Terraform%20CLI.md)
- [Introduction to DevSecOps for Cloud](Introduction%20to%20DevSecOps%20for%20Cloud/1%20-%20Introduction.md)
