# 11 - Jenkins Glossary

## Purpose

This glossary explains Jenkins terms in the practical sense needed for CI/CD work, interviews, and production troubleshooting.

Source snapshot: 2026-05-27. Some terms are plugin-sensitive.

## Core Terms

### Agent

A machine, VM, container, or Kubernetes Pod that runs build steps. Agents are where compilation, tests, packaging, and most shell commands should run.

Why it matters: agents isolate build work from the controller and allow different toolchains for different jobs.

### Artifact

A file produced by a build, such as a JAR, binary, test report, coverage report, image digest file, or zipped package.

Small detail: Jenkins artifacts are attached to build history. Important release artifacts usually belong in an external artifact repository, package registry, container registry, or object storage.

### Blue Ocean

A Jenkins user interface focused on Pipeline visualization. It is not the same thing as Pipeline itself.

### Build

One execution of a Jenkins job or Pipeline.

Small detail: a "successful" build means Jenkins marked the run successful. It does not automatically mean the release is safe if tests were skipped or gates were weak.

### Build Discarder

Retention policy that removes old builds and artifacts.

Why it matters: Jenkins controllers often fail from disk pressure when retention is ignored.

### Controller

The Jenkins server that stores configuration, schedules builds, manages plugins, serves UI/API, and coordinates agents.

Small detail: the controller is stateful and security-critical. Protect it like a control plane.

### Credential

A stored secret or identity material used by jobs, Pipelines, or integrations.

Examples: username/password, token, SSH key, certificate, secret file.

Small detail: Jenkinsfiles should reference credential IDs, not secret values.

### Credential Scope

The visibility boundary of a credential, such as global scope or folder/item scope.

Why it matters: credential scope controls which jobs can use a secret. Folder moves or copies can change visibility.

### Declarative Pipeline

Structured Jenkins Pipeline syntax using `pipeline {}` with blocks such as `agent`, `stages`, `steps`, `post`, and `options`.

Why it matters: it is easier to standardize and review than heavily custom Scripted Pipeline for most CI/CD workflows.

### Executor

A slot on a Jenkins node that can run one build at a time.

Small detail: an online agent with zero free executors cannot start another build.

### Fingerprint

Jenkins feature used to track file usage across builds.

Why it matters: useful for traceability, but not a complete artifact management strategy.

### Folder

A Jenkins organizational container for jobs. Folders can also help scope permissions and credentials.

Small detail: folder-level credentials are not visible everywhere.

### Freestyle Job

Older Jenkins job type configured mostly through the UI.

Why it matters: useful historically and for simple tasks, but modern CI/CD usually prefers Pipeline as code.

### Groovy

Language used by Jenkins Pipeline and Jenkins administrative scripting.

Small detail: Pipeline Groovy and Script Console Groovy have very different risk levels.

### In-Process Script Approval

Jenkins security mechanism that controls certain Groovy method calls in sandboxed scripts.

Why it matters: a Pipeline may fail because a script needs approval, but approving unsafe signatures can weaken Jenkins security.

### Jenkinsfile

A text file containing Pipeline definition, usually stored in the source repository.

Why it matters: it makes build logic reviewable, versioned, and branch-aware.

### JENKINS_HOME

The directory where Jenkins stores jobs, build records, plugins, users, credentials metadata, secrets/key material, and configuration.

Small detail: backing up only job XML is not enough for real disaster recovery.

### Job

A configured Jenkins task. It may be a Pipeline, Freestyle project, multibranch Pipeline, folder child, or other plugin-defined type.

### Label

Metadata assigned to nodes/agents and used by Pipelines to request a suitable execution environment.

Example:

```groovy
agent { label 'linux && docker' }
```

Why it matters: labels are scheduling contracts.

### Multibranch Pipeline

Pipeline job type that discovers branches and pull requests and runs the Jenkinsfile found in each branch.

Why it matters: it aligns CI with repository branches and PRs.

### Node

Any Jenkins execution machine known to the controller. A node may be the built-in node/controller or an external agent.

Small detail: avoid running normal build workloads on the controller node.

### Pipeline

Jenkins workflow defined as code. Pipelines usually include checkout, build, test, scan, package, publish, and deploy stages.

### Pipeline Syntax Generator

Jenkins UI tool that generates snippets for installed Pipeline steps.

Why it matters: it prevents guessing plugin-specific syntax, especially for credentials.

### Plugin

An extension that adds Jenkins functionality, UI, steps, integrations, or security features.

Small detail: plugins run inside Jenkins and can affect security and stability.

### Post Condition

Declarative Pipeline block that runs after a stage or Pipeline based on result.

Examples: `always`, `success`, `failure`, `unstable`, `aborted`, `cleanup`.

### Queue

Where Jenkins holds builds waiting for an executor.

Small detail: a queue problem often means labels, agents, executors, or locks are wrong.

### Script Console

Administrative Groovy console that runs in the Jenkins controller JVM.

Why it matters: it can inspect or modify Jenkins internals. Restrict access tightly.

### Scripted Pipeline

More flexible Pipeline syntax written as Groovy script.

Tradeoff: powerful, but can become harder to standardize and review than Declarative Pipeline.

### Shared Library

Reusable Pipeline code stored outside individual Jenkinsfiles and imported into Pipelines.

Why it matters: reduces copy-paste Pipeline logic, but the shared library becomes part of the delivery platform and needs review/versioning.

### Stash

Pipeline step that temporarily stores files for use by later stages in the same run.

Small detail: `stash` is not for long-term artifacts.

### Step

An individual Pipeline operation, such as `sh`, `junit`, `checkout`, `archiveArtifacts`, or `withCredentials`.

### Unstable

Build status commonly used when the build ran but quality checks, tests, or reports indicate problems.

Small detail: unstable is not the same as failed, but release gates often treat it as non-promotable.

### Webhook

HTTP callback from source control or another system that triggers Jenkins activity.

Why it matters: broken webhooks create delayed or missing CI feedback.

### Workspace

Filesystem directory where Jenkins checks out and builds code for a job on a node.

Small detail: workspace reuse is a common source of stale-file bugs.

## Small Details That Matter Later

- Job name, branch name, workspace path, and folder path can affect scripts that assume fixed paths.
- Credential ID stability matters because Jenkinsfiles hard-code IDs.
- Plugin versions are part of the Jenkins runtime, just like library versions are part of application runtime.
- A node can be online but still unsuitable because labels or tools do not match.
- A build can be stuck because of a lock or concurrency rule even when executors are available.
- A Jenkins restore without secret keys can break credential decryption.
- Script Console scripts may be outdated because Jenkins APIs and plugins change.
- Multibranch jobs can run different Jenkinsfiles on different branches.
- Logs prove what Jenkins saw, not necessarily what an external deployment target actually applied.
