# Jenkins

## Quick Summary

Jenkins is an automation server most commonly used for CI/CD. It can build, test, scan, package, deploy, and schedule automation through jobs and Pipelines.

This folder is ordered from CI/CD basics to installation, administration, Docker usage, Declarative Pipeline, Groovy automation, and production operations.

Source snapshot: 2026-05-27. Jenkins behavior is version-sensitive because Jenkins core, Java baseline, plugins, agents, credentials bindings, Docker integrations, Kubernetes clouds, and script-security settings can change behavior. Verify plugin-specific steps against the current controller before using them in production.

## Learning Order

| Order | Note | Focus |
| --- | --- | --- |
| 1 | [CI-CD Pipelines and Testing Practices](1%20-%20CI-CD%20Pipelines%20and%20Testing%20Practices.md) | CI/CD flow, test stages, artifacts, gates, and pipeline quality. |
| 2 | [Jenkins Installation](2%20-%20Jenkins%20Installation.md) | Installation methods, Java, WAR, packages, Docker, first login, and hardening. |
| 3 | [Using and Managing Jenkins](3%20-%20Using%20and%20Managing%20Jenkins.md) | Controllers, agents, plugins, credentials, jobs, backups, and operations. |
| 4 | [Running Jenkins in Docker](4%20-%20Running%20Jenkins%20in%20Docker.md) | Local Docker setup, persistence, agents, Docker socket risks, and upgrades. |
| 5 | [Using Declarative Jenkins Pipeline](5%20-%20Using%20Declarative%20Jenkins%20Pipeline.md) | Jenkinsfile syntax, agents, stages, environment, post actions, credentials, and validation. |
| 6 | [Automating Jenkins with Groovy](6%20-%20Automating%20Jenkins%20with%20Groovy.md) | Script Console, init hooks, Job DSL, shared libraries, and automation safety. |
| 7 | [Pipeline Operations, Security, and Troubleshooting Runbooks](7%20-%20Pipeline%20Operations%20Security%20and%20Troubleshooting%20Runbooks.md) | Controller/agent boundaries, credential safety, queue diagnosis, plugin failures, artifacts, backups, and production runbooks. |
| 10 | [Cheatsheet](10%20-%20Cheatsheet.md) | Fast revision for Pipeline syntax, operations, security, and troubleshooting. |
| 11 | [Glossary](11%20-%20Glossary.md) | Practical Jenkins terms with production details and traps. |
| Changelog | [CHANGELOG](CHANGELOG.md) | Tracks upgrades, preservation notes, and verification reminders. |

## Revision Path

1. Understand what CI/CD is trying to protect: fast feedback, repeatability, quality gates, traceability.
2. Learn Jenkins architecture: controller, agents, executors, workspaces, plugins, credentials.
3. Practice a basic Jenkinsfile.
4. Add test, artifact, and post-failure behavior.
5. Learn safe credential usage.
6. Learn Docker and agent execution models.
7. Automate common admin tasks carefully with Groovy or Configuration as Code.
8. Practice layered troubleshooting: queue, controller, agent, workspace, plugin, credentials, tests, artifacts, deploy.
9. Revise with the cheatsheet and glossary before interviews or production work.

## Official References

- Jenkins documentation: <https://www.jenkins.io/doc/>
- Installing Jenkins: <https://www.jenkins.io/doc/book/installing/>
- Jenkins Docker install guide: <https://www.jenkins.io/doc/book/installing/docker/>
- Jenkins Pipeline: <https://www.jenkins.io/doc/book/pipeline/>
- Pipeline syntax: <https://www.jenkins.io/doc/book/pipeline/syntax/>
- Jenkins credentials: <https://www.jenkins.io/doc/book/using/using-credentials/>
- Jenkins Script Console: <https://www.jenkins.io/doc/book/managing/script-console/>
- Groovy hook scripts: <https://www.jenkins.io/doc/book/managing/groovy-hook-scripts/>

## Upgrade Notes

The 2026-05-27 upgrade preserved the original six chapters and added operational depth instead of duplicating introductory material. The new runbook chapter covers the failure paths that matter in real Jenkins systems: stuck queues, missing plugins, credential scope, unsafe secret interpolation, missing artifacts, Script Console risk, controller backups, agent labels, and Docker socket exposure.
