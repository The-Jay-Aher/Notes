# 5 - Using Declarative Jenkins Pipeline

## Quick Summary

Declarative Pipeline is a structured Jenkinsfile syntax for defining CI/CD workflows as code. It is easier to read and standardize than fully scripted Pipeline for most common CI/CD use cases.

Basic shape:

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }
    }
}
```

## Why It Matters

Declarative Pipeline lets teams:

- Store CI/CD logic in version control.
- Review pipeline changes through pull requests.
- Standardize stages and post-actions.
- Reuse credentials safely.
- Run automation on selected agents.
- Archive artifacts and reports.

## Core Blocks

| Block | Purpose |
| --- | --- |
| `pipeline` | Top-level block. |
| `agent` | Where the Pipeline or stage runs. |
| `stages` | Collection of stages. |
| `stage` | Named pipeline phase. |
| `steps` | Commands/actions inside a stage. |
| `environment` | Environment variables. |
| `parameters` | User inputs for manual runs. |
| `post` | Actions after build/stage result. |
| `options` | Pipeline options such as timeout or build discard. |
| `when` | Conditional stage execution. |

## Basic Jenkinsfile

```groovy
pipeline {
    agent any

    options {
        timeout(time: 20, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'pytest -q'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
```

## Agent

Run anywhere:

```groovy
agent any
```

Run on a labeled agent:

```groovy
agent { label 'linux && docker' }
```

No global agent, choose per stage:

```groovy
pipeline {
    agent none
    stages {
        stage('Build') {
            agent { label 'builder' }
            steps {
                sh 'make build'
            }
        }
    }
}
```

## Environment

```groovy
environment {
    APP_ENV = 'test'
}
```

Use credentials:

```groovy
environment {
    DEPLOY_TOKEN = credentials('deploy-token')
}
```

For finer control, use `withCredentials` in steps.

## Parameters

```groovy
parameters {
    choice(name: 'ENVIRONMENT', choices: ['dev', 'staging', 'prod'], description: 'Target environment')
    booleanParam(name: 'RUN_MIGRATIONS', defaultValue: false, description: 'Run DB migrations')
}
```

Use:

```groovy
sh "echo Deploying to ${params.ENVIRONMENT}"
```

## Stages And Steps

```groovy
stage('Build') {
    steps {
        sh 'npm ci'
        sh 'npm run build'
    }
}
```

Windows:

```groovy
bat 'mvn test'
```

PowerShell:

```groovy
powershell 'Get-ChildItem'
```

## Post Actions

```groovy
post {
    always {
        archiveArtifacts artifacts: 'dist/**', allowEmptyArchive: true
    }
    success {
        echo 'Success'
    }
    failure {
        echo 'Failure'
    }
    cleanup {
        cleanWs()
    }
}
```

Common post conditions:

- `always`
- `success`
- `failure`
- `unstable`
- `aborted`
- `changed`
- `cleanup`

## When Conditions

```groovy
stage('Deploy') {
    when {
        branch 'main'
    }
    steps {
        sh './deploy.sh'
    }
}
```

Expression:

```groovy
when {
    expression { return params.ENVIRONMENT == 'prod' }
}
```

## Parallel Stages

```groovy
stage('Test') {
    parallel {
        stage('Unit') {
            steps {
                sh 'make unit'
            }
        }
        stage('Lint') {
            steps {
                sh 'make lint'
            }
        }
    }
}
```

Use parallelism to reduce feedback time when stages are independent.

## Artifacts And Test Reports

```groovy
post {
    always {
        junit 'reports/**/*.xml'
        archiveArtifacts artifacts: 'dist/**', fingerprint: true
    }
}
```

Use:

- `junit` for test reports.
- `archiveArtifacts` for build outputs/logs.
- External artifact repository for long-lived release artifacts.

## Credentials

Safe pattern:

```groovy
withCredentials([string(credentialsId: 'api-token', variable: 'API_TOKEN')]) {
    sh './run-secure-task.sh'
}
```

Avoid:

```groovy
sh 'echo my-secret-password'
```

Jenkins masks many secrets in logs, but scripts can still leak secrets through files, command-line arguments, debug logs, or artifacts.

## Jenkinsfile In Version Control

Best practice:

- Store `Jenkinsfile` in the application repository.
- Review it like application code.
- Keep stages understandable.
- Avoid excessive Groovy complexity in Declarative Pipeline.

## Benefits

- Version-controlled CI/CD.
- Clear structure.
- Built-in stage visualization.
- Post-condition handling.
- Supports agents, parameters, environment variables, and credentials.

## Drawbacks / Limitations

- Very complex logic can become awkward.
- Plugin behavior affects available steps.
- Groovy/string interpolation can create quoting and secret-handling issues.
- Long Jenkinsfiles become hard to maintain without shared libraries.

## Hidden Details / Caveats

- `agent none` means stages must define their own agents.
- Environment variables are strings.
- Stages fail fast unless errors are caught or marked unstable.
- `post` can run even when earlier stages fail depending on condition.
- Shell commands run on the agent, not the controller.
- Workspace contents persist during a build but may be cleaned before/after depending on configuration.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| No timeout | Add `timeout` option. |
| No artifact/test report publishing | Add `junit` and `archiveArtifacts`. |
| Secrets in plain text | Use credentials binding. |
| Running deployment on every branch | Use `when` and approvals. |
| One huge stage | Split into Build/Test/Package/Deploy. |
| Overusing scripted Groovy | Use shared libraries or simpler steps. |

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Jenkinsfile syntax error | Use Pipeline syntax docs or declarative linter where available. |
| No matching agent | Labels and agent availability. |
| Step not found | Missing plugin. |
| Credential missing | Credential ID and scope. |
| Shell works locally but fails | Agent OS, tools, PATH, permissions. |
| Post action fails | Artifact path, report path, plugin availability. |

## Interview Notes

- Declarative Pipeline starts with `pipeline {}`.
- `agent` decides where work runs.
- `stages` contain `stage` blocks; each stage contains `steps`.
- `post` handles actions after success/failure/always.
- Jenkinsfile should be stored in version control.
- Credentials should be referenced by ID, not hard-coded.

## Related Topics

- [CI-CD Pipelines and Testing Practices](1%20-%20CI-CD%20Pipelines%20and%20Testing%20Practices.md)
- [Automating Jenkins with Groovy](6%20-%20Automating%20Jenkins%20with%20Groovy.md)

