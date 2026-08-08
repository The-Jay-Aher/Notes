# 10 - Jenkins Cheatsheet

## Purpose

This cheatsheet is a fast revision sheet for Jenkins architecture, Pipeline syntax, credentials, operations, and troubleshooting. Use the deeper chapters when you need explanations; use this file when you need recall.

Source snapshot: 2026-05-27. Jenkins details can vary by Jenkins core version and installed plugins.

## Core Mental Model

```text
source change -> Jenkins job -> controller schedules -> agent executes -> logs/reports/artifacts -> gate/deploy
```

| Concept | One-line meaning |
| --- | --- |
| Controller | Jenkins server that stores configuration, schedules builds, manages plugins, and serves UI/API. |
| Agent | Machine/container/pod that executes build steps. |
| Executor | One concurrent build slot on a node. |
| Workspace | Directory where a job checks out and builds code. |
| Jenkinsfile | Pipeline-as-code definition, ideally stored in source control. |
| Plugin | Extension that adds features, UI, steps, or integrations. |
| Credential | Stored secret referenced by ID from jobs or Pipelines. |

## Pipeline Skeleton

```groovy
pipeline {
    agent none

    options {
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '30'))
        disableConcurrentBuilds()
    }

    stages {
        stage('Build') {
            agent { label 'linux && builder' }
            steps {
                checkout scm
                sh 'make build'
            }
        }

        stage('Test') {
            agent { label 'linux && test' }
            steps {
                sh 'make test'
            }
            post {
                always {
                    junit 'reports/**/*.xml'
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'dist/**', allowEmptyArchive: true
        }
    }
}
```

## Declarative Blocks

| Block | Use |
| --- | --- |
| `pipeline` | Top-level Declarative Pipeline block. |
| `agent` | Select where the Pipeline or stage runs. |
| `stages` | Contains ordered stages. |
| `stage` | Human-readable phase. |
| `steps` | Actual work. |
| `environment` | Environment variables or credentials helper. |
| `parameters` | User inputs for manual or parameterized builds. |
| `when` | Conditional execution. |
| `post` | Always/success/failure/cleanup behavior. |
| `options` | Timeouts, retention, concurrency, timestamps. |

## Common Steps

| Step | Purpose | Watch for |
| --- | --- | --- |
| `checkout scm` | Check out repository configured for the job. | Branch source credentials and workspace permissions. |
| `sh 'cmd'` | Run shell command on Unix-like agents. | Exit code fails the step unless handled. |
| `bat 'cmd'` | Run batch command on Windows agents. | Windows path and quoting differences. |
| `powershell 'cmd'` | Run PowerShell command. | Execution policy and quoting. |
| `junit 'path'` | Publish test reports. | Path relative to workspace; plugin availability. |
| `archiveArtifacts` | Attach files to build record. | Retention and missing paths. |
| `stash` / `unstash` | Move short-lived files between stages/agents. | Not a release repository. |
| `withCredentials` | Bind secrets for a limited block. | Avoid Groovy interpolation and env dumps. |
| `cleanWs` | Clean workspace. | Requires Workspace Cleanup plugin. |
| `input` | Manual approval gate. | Use sparingly and with permissions. |

## Credential Patterns

Safer:

```groovy
withCredentials([string(credentialsId: 'api-token', variable: 'API_TOKEN')]) {
    sh 'curl -H "Authorization: Bearer $API_TOKEN" https://example.com'
}
```

Risky:

```groovy
withCredentials([string(credentialsId: 'api-token', variable: 'API_TOKEN')]) {
    sh "curl -H 'Authorization: Bearer ${API_TOKEN}' https://example.com"
}
```

Rules:

- Use credential IDs, not literal secrets.
- Scope credentials narrowly.
- Do not print environment variables in secret-heavy jobs.
- Do not store generated secret files as artifacts.
- Do not rely on masking as the only security control.

## Agent Selection

| Pattern | Meaning |
| --- | --- |
| `agent any` | Run on any available eligible agent. Convenient but imprecise. |
| `agent none` | No global agent; each stage chooses one. Good for multi-environment Pipelines. |
| `agent { label 'linux && docker' }` | Requires an online node matching both labels. |
| `agent { docker { image 'node:20' } }` | Run stage inside a Docker image when the Docker Pipeline setup supports it. |

Label debugging:

```text
queued build -> read queue reason -> check requested label -> check online nodes -> check executor capacity
```

## Jenkins Operations Checklist

| Area | Healthy state |
| --- | --- |
| Controller | Not running heavy builds; CPU/memory/disk monitored. |
| Agents | Online, labeled correctly, tool versions known. |
| Plugins | Minimal, updated through tested baseline, advisories watched. |
| Credentials | Scoped, named by stable IDs, rotated, least privilege. |
| Jobs | Jenkinsfiles in SCM, retention configured, artifacts controlled. |
| Backups | `JENKINS_HOME`, credentials/key material, plugin versions, config, restore tested. |
| Security | Authentication, authorization, CSRF, admin boundaries, Script Console locked down. |

## Troubleshooting Fast Map

| Symptom | First checks |
| --- | --- |
| Build stuck in queue | Label, agent online, executor capacity, concurrency lock. |
| Unknown Pipeline step | Missing/disabled/incompatible plugin; Pipeline Syntax page. |
| Credential not found | Credential ID, scope, folder, permissions. |
| Checkout fails | SCM credentials, branch, webhook, workspace permissions. |
| Tests fail only on Jenkins | Tool versions, env vars, filesystem, time zone, dependency cache. |
| Artifact missing | Path relative to workspace, stage/agent boundary, `stash`, `allowEmptyArchive`. |
| UI slow | Controller resources, disk I/O, job count, plugins, logs. |
| Agent disconnected | Network, agent service, remoting/WebSocket config, credentials. |
| Build unstable | JUnit/test report results, quality gates, warnings parser. |
| Deploy wrong version | Mutable artifact/tag, rebuild during deploy, no promotion model. |

## Security Reminders

- Controller is the control plane. Protect it.
- Script Console has admin-level power.
- Plugins are code running in Jenkins.
- Builds that run untrusted PR code must not receive production credentials.
- Docker socket access is high privilege.
- Folder-level permissions and credentials reduce blast radius.
- Job configure permission is powerful because changing a Jenkinsfile or job script can change what executes.
- Use external secret managers where policy requires stronger audit/rotation than Jenkins credentials alone.

## Small Details That Matter Later

- `allowEmptyArchive: true` can hide missing artifacts.
- `stash` files are temporary to a Pipeline run.
- `junit` can mark a build unstable even if the shell command exited successfully.
- A step can disappear after a plugin is disabled or upgraded.
- Workspace cleanup can break jobs that secretly depend on stale files, which is a good bug to expose.
- `agent any` can choose an agent without the tools you expected.
- Environment variables set at top level may be visible to all stages.
- Credentials in `environment {}` live for a wider scope than credentials inside `withCredentials`.
- `disableConcurrentBuilds()` is important for deployments and shared mutable state.
- Build retention protects disk but can remove logs you wanted during incident review.
- Restarting Jenkins may clear a symptom but does not explain the failed layer.

## Interview Answer Frames

Controller vs agent:

```text
Controller schedules and stores Jenkins state. Agents execute build work. Heavy or untrusted builds should run on agents so the controller remains stable and protected.
```

Job stuck in queue:

```text
I would inspect the queue reason, requested label, online nodes, executor capacity, and any concurrency locks. This is a scheduling problem before it is a build problem.
```

Secret handling:

```text
I would store secrets in Jenkins credentials or an approved external secrets system, reference them by ID, bind them only around required steps, avoid Groovy interpolation, and prevent untrusted code from receiving production credentials.
```

Plugin upgrade:

```text
I would maintain a tested plugin baseline, check security advisories and compatibility, back up Jenkins, test upgrades in a staging controller, and verify critical Pipelines before production rollout.
```

## Revision Questions

1. Why should builds normally run on agents instead of the controller?
2. What does a Jenkins agent label actually control?
3. Why is a Jenkinsfile in source control safer than UI-only Pipeline text?
4. Why is the Script Console dangerous?
5. What evidence separates an agent problem from an application test failure?
