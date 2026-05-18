# Jenkins

## Quick Summary

Jenkins is an automation server most commonly used for CI/CD. It can build, test, scan, package, deploy, and schedule automation through jobs and Pipelines.

This folder is ordered from CI/CD basics to installation, administration, Docker usage, Declarative Pipeline, and Groovy automation.

## Learning Order

| Order | Note | Focus |
| --- | --- | --- |
| 1 | [CI-CD Pipelines and Testing Practices](1%20-%20CI-CD%20Pipelines%20and%20Testing%20Practices.md) | CI/CD flow, test stages, artifacts, gates, and pipeline quality. |
| 2 | [Jenkins Installation](2%20-%20Jenkins%20Installation.md) | Installation methods, Java, WAR, packages, Docker, first login, and hardening. |
| 3 | [Using and Managing Jenkins](3%20-%20Using%20and%20Managing%20Jenkins.md) | Controllers, agents, plugins, credentials, jobs, backups, and operations. |
| 4 | [Running Jenkins in Docker](4%20-%20Running%20Jenkins%20in%20Docker.md) | Local Docker setup, persistence, agents, Docker socket risks, and upgrades. |
| 5 | [Using Declarative Jenkins Pipeline](5%20-%20Using%20Declarative%20Jenkins%20Pipeline.md) | Jenkinsfile syntax, agents, stages, environment, post actions, credentials, and validation. |
| 6 | [Automating Jenkins with Groovy](6%20-%20Automating%20Jenkins%20with%20Groovy.md) | Script Console, init hooks, Job DSL, shared libraries, and automation safety. |

## Revision Path

1. Understand what CI/CD is trying to protect: fast feedback, repeatability, quality gates, traceability.
2. Learn Jenkins architecture: controller, agents, executors, workspaces, plugins, credentials.
3. Practice a basic Jenkinsfile.
4. Add test, artifact, and post-failure behavior.
5. Learn safe credential usage.
6. Learn Docker and agent execution models.
7. Automate common admin tasks carefully with Groovy or Configuration as Code.

## Official References

- Jenkins documentation: <https://www.jenkins.io/doc/>
- Installing Jenkins: <https://www.jenkins.io/doc/book/installing/>
- Jenkins Docker install guide: <https://www.jenkins.io/doc/book/installing/docker/>
- Jenkins Pipeline: <https://www.jenkins.io/doc/book/pipeline/>
- Pipeline syntax: <https://www.jenkins.io/doc/book/pipeline/syntax/>
- Jenkins credentials: <https://www.jenkins.io/doc/book/using/using-credentials/>
- Jenkins Script Console: <https://www.jenkins.io/doc/book/managing/script-console/>
- Groovy hook scripts: <https://www.jenkins.io/doc/book/managing/groovy-hook-scripts/>

