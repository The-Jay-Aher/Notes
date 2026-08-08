# 3 - Using and Managing Jenkins

## Quick Summary

Managing Jenkins means keeping the automation platform reliable, secure, and maintainable. The important parts are controllers, agents, executors, plugins, credentials, jobs, Pipelines, backups, permissions, and upgrade discipline.

## Jenkins Architecture

```text
users -> Jenkins controller -> agents/executors -> build workspaces
```

| Component | Purpose |
| --- | --- |
| Controller | Web UI, scheduling, configuration, plugin management, job orchestration. |
| Agent | Machine/container that runs build steps. |
| Executor | Slot on a node that can run one build at a time. |
| Workspace | Directory where job files are checked out and built. |
| Plugin | Extension that adds functionality. |

Best practice: do not run heavy builds on the controller. Use agents.

## Jobs And Pipelines

Common job types:

| Type | Use |
| --- | --- |
| Freestyle project | Simple legacy jobs. |
| Pipeline | Jenkinsfile-based automation. |
| Multibranch Pipeline | Automatically discovers branches/PRs with Jenkinsfiles. |
| Folder | Organizes jobs and applies scoped permissions/credentials. |

Prefer Pipeline and Multibranch Pipeline for modern CI/CD.

## Jenkins Plugin Model

Jenkins functionality is plugin-driven.

Plugins can add:

- SCM integration.
- Pipeline steps.
- Credentials providers.
- Cloud agents.
- UI features.
- Build tools.
- Security integrations.

## Plugin Management

Best practices:

- Install plugins from the official update center.
- Keep a minimal plugin set.
- Review plugin health and security advisories.
- Test plugin upgrades before production.
- Back up Jenkins before major upgrades.
- Keep a plugin baseline list with versions.

Plugin risk:

- Plugins run inside Jenkins and can affect security/stability.
- Old plugins can block Jenkins core upgrades.
- Too many plugins increase maintenance load.

## Credentials

Jenkins credentials store secrets for jobs and Pipelines.

Common credential types:

- Username/password.
- Secret text.
- SSH username with private key.
- Certificate.
- Cloud-provider credentials through plugins.

Use credentials by ID. Do not hard-code secrets in Jenkinsfiles or shell scripts.

Example Pipeline pattern:

```groovy
withCredentials([string(credentialsId: 'deploy-token', variable: 'DEPLOY_TOKEN')]) {
    sh './deploy.sh'
}
```

## Security Basics

Configure:

- Security realm: how users authenticate.
- Authorization strategy: what authenticated users can do.
- CSRF protection.
- Agent security.
- Credential scopes.
- Admin user/group ownership.

Least privilege examples:

- Developers can run/read their project jobs.
- Release managers can deploy production.
- Only Jenkins admins can install plugins or edit global config.

## Agents And Labels

Agents can be static machines, Docker containers, cloud instances, or Kubernetes Pods.

Labels route builds:

```groovy
agent { label 'linux && docker' }
```

Common problems:

- Job label does not match any online agent.
- Agent has no required tools.
- Workspace permissions are broken.
- Agent disconnected.

## Build History And Artifacts

Set retention policies:

- Number of builds to keep.
- Days to keep builds.
- Artifact retention.

Avoid storing large artifacts forever in Jenkins. Use an artifact repository, container registry, package registry, or object storage for long-term storage.

## Backups

Back up:

- `JENKINS_HOME`.
- Jobs.
- Credentials and secret keys.
- Plugin list/versions.
- Global configuration.
- User/security config.

Test restore. A backup that was never restored is only a hope, not a recovery plan.

## Monitoring

Watch:

- Queue length.
- Executor usage.
- Agent availability.
- Disk usage.
- JVM memory.
- Plugin/security warnings.
- Build duration trends.
- Failed login attempts.

## Benefits

- Jenkins is flexible and extensible.
- Pipelines are version-controlled.
- Agents support many build environments.
- Credentials and permissions can be centralized.
- Large plugin ecosystem supports many tools.

## Drawbacks / Limitations

- Plugin maintenance is real operational work.
- Stateful controller requires backup and upgrade planning.
- Misconfigured credentials can leak secrets.
- Too many jobs/plugins can make Jenkins difficult to manage.
- Build environments can drift if agents are not standardized.

## Hidden Details / Caveats

- Jenkinsfile changes are code changes and should be reviewed.
- Credentials can still leak if scripts print them or write them to artifacts.
- Workspace reuse can hide stale files unless cleaned.
- Agents need tool/version consistency.
- Plugin updates can change Pipeline step behavior.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Everyone is admin | Use role-based permissions. |
| Builds run on controller | Move builds to agents. |
| No plugin governance | Maintain a tested plugin baseline. |
| Artifacts stored only in Jenkins | Publish important artifacts externally. |
| No restore test | Practice restoring Jenkins. |
| Secrets in logs | Use credentials binding and avoid echoing secrets. |

## Troubleshooting

| Problem | Checks |
| --- | --- |
| Job stuck in queue | Agent online, label match, executor availability. |
| Pipeline step unknown | Missing/outdated plugin. |
| Credential not found | Credential scope, ID, folder/global location. |
| Build fails on agent only | Tool versions, environment variables, permissions, workspace. |
| Jenkins UI slow | Controller CPU/memory, plugin issues, job count, disk I/O. |
| Cannot update plugins | Update center access, proxy, Jenkins core compatibility. |

## Interview Notes

- Controller schedules and manages Jenkins; agents execute builds.
- Executors are build slots.
- Plugins add functionality but also add maintenance/security risk.
- Jenkins credentials should be referenced by ID.
- Modern Jenkins uses Pipeline and Jenkinsfile.
- Backups must include Jenkins secrets/keys, not only job XML.

## Related Topics

- [Jenkins Installation](2%20-%20Jenkins%20Installation.md)
- [Using Declarative Jenkins Pipeline](5%20-%20Using%20Declarative%20Jenkins%20Pipeline.md)

