# 6 - Automating Jenkins with Groovy

## Quick Summary

Jenkins uses Groovy in Pipelines, the Script Console, init hooks, shared libraries, and some automation plugins. Groovy automation is powerful, but it can also change Jenkins globally, expose secrets, or break jobs if used carelessly.

Use Groovy carefully and prefer reviewed, version-controlled automation over one-off manual scripts.

## Where Groovy Appears In Jenkins

| Location | Use |
| --- | --- |
| Jenkinsfile | Pipeline logic. |
| Script Console | Admin scripts executed inside Jenkins runtime. |
| `init.groovy.d` | Startup automation. |
| Shared Libraries | Reusable Pipeline code. |
| Job DSL plugin | Define jobs as code. |

## Pipeline Groovy vs System Groovy

| Type | Scope | Risk |
| --- | --- | --- |
| Pipeline Groovy | Runs as part of a job, often sandboxed. | Can affect build behavior and leak credentials if careless. |
| Script Console/System Groovy | Runs inside Jenkins controller runtime with admin power. | Can modify/delete jobs, credentials, users, and Jenkins config. |

Treat Script Console like root access to Jenkins.

## Script Console

The Script Console lets admins run Groovy directly in Jenkins.

Use cases:

- Inspect Jenkins state.
- Bulk-update job configuration.
- Diagnose plugin/config issues.
- Run controlled admin maintenance.

Avoid:

- Running copied scripts without understanding them.
- Printing secrets.
- Making untested bulk changes.
- Using it as a permanent automation strategy.

Example read-only script:

```groovy
Jenkins.instance.items.each { item ->
    println(item.fullName)
}
```

## init.groovy.d Startup Hooks

Jenkins can run Groovy scripts at startup from:

```text
$JENKINS_HOME/init.groovy.d/
```

In the official Docker image, seed scripts are commonly placed in:

```text
/usr/share/jenkins/ref/init.groovy.d/
```

Use startup hooks for:

- Initial admin setup in controlled environments.
- Default configuration.
- Bootstrapping seed jobs.

Be careful:

- Scripts run with high privilege.
- Bad scripts can break startup.
- Keep scripts version-controlled.

## Shared Libraries

Shared libraries move repeated Pipeline logic out of Jenkinsfiles.

Typical structure:

```text
(shared-library repo)
vars/
  buildJava.groovy
src/
  org/example/Deploy.groovy
resources/
```

Example `vars/buildJava.groovy`:

```groovy
def call() {
    sh 'mvn test'
}
```

Use in Jenkinsfile:

```groovy
@Library('company-shared') _

pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                buildJava()
            }
        }
    }
}
```

Use shared libraries when many repositories repeat the same pipeline logic.

## Job DSL

Job DSL lets you define Jenkins jobs using Groovy.

Example concept:

```groovy
pipelineJob('example-app') {
    definition {
        cpsScm {
            scm {
                git('https://github.com/example/app.git')
            }
            scriptPath('Jenkinsfile')
        }
    }
}
```

Use cases:

- Seed jobs.
- Reproducible job creation.
- Managing many similar jobs.

## Exception Handling

Pipeline example:

```groovy
try {
    sh './deploy.sh'
} catch (err) {
    currentBuild.result = 'FAILURE'
    echo "Deployment failed: ${err}"
    throw err
}
```

Prefer clear stage/post behavior over hiding failures.

## Security Best Practices

- Restrict Script Console access to trusted admins only.
- Keep Groovy automation in version control.
- Review scripts before running.
- Test in non-production Jenkins first.
- Avoid printing credentials or environment dumps.
- Prefer Configuration as Code or declarative config where possible.
- Use shared libraries for repeated Pipeline logic instead of copy-paste Jenkinsfiles.

## Benefits

- Can automate repetitive admin tasks.
- Reduces duplicate Pipeline logic.
- Supports jobs/configuration as code.
- Enables powerful Jenkins customization.

## Drawbacks / Limitations

- High risk when run with admin privileges.
- Plugin/internal APIs may change.
- Groovy errors can break startup or jobs.
- Hard-to-review one-off scripts can create hidden state.
- Pipeline Groovy can become too complex for normal CI/CD logic.

## Hidden Details / Caveats

- Script Console scripts execute on the controller.
- Pipeline code may be CPS-transformed, which affects some Groovy patterns.
- Sandbox approval may be required for some Pipeline scripts.
- Shared library changes can affect many repositories at once.
- Startup scripts in Docker seed path are copied only when initializing a new Jenkins home.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Running random Script Console snippets | Read, test, and version-control scripts. |
| Putting too much logic in Jenkinsfile | Move reusable logic to shared libraries. |
| Printing all environment variables | Avoid exposing credentials. |
| Editing global config manually only | Use documented automation where possible. |
| No rollback for bulk change | Back up and test before running. |

## Troubleshooting

| Problem | Check |
| --- | --- |
| Script Console fails | Imports, Jenkins API changes, permissions, plugin availability. |
| Startup script breaks Jenkins | Move script out, restart, test in lower environment. |
| Shared library not found | Library config, branch, SCM credentials, annotation name. |
| Pipeline sandbox rejection | Admin script approval or safer Pipeline pattern. |
| Job DSL missing method | Plugin version or DSL syntax support. |

## Interview Notes

- Jenkinsfile uses Groovy-based Pipeline syntax.
- Script Console is powerful admin-level Groovy execution.
- `init.groovy.d` runs startup Groovy scripts.
- Shared libraries reuse Pipeline logic.
- Job DSL can define jobs as code.
- Groovy automation should be reviewed, tested, and version-controlled.

## Related Topics

- [Using Declarative Jenkins Pipeline](5%20-%20Using%20Declarative%20Jenkins%20Pipeline.md)
- [Using and Managing Jenkins](3%20-%20Using%20and%20Managing%20Jenkins.md)

