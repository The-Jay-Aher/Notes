# 2 - Jenkins Installation

## Quick Summary

Jenkins can run from native packages, a WAR file, or Docker. For learning, Docker or WAR is quick. For production, prefer a managed, repeatable installation with persistent `JENKINS_HOME`, backups, TLS, access control, and controlled plugin updates.

## Installation Options

| Method | Best For | Notes |
| --- | --- | --- |
| Native package | Long-running VM/server install. | Integrates with systemd and OS package management. |
| WAR file | Lab, testing, custom runtime. | Requires supported Java. |
| Docker | Local learning and reproducible controller setup. | Must persist `/var/jenkins_home`. |
| Kubernetes | Scalable/cloud-native setup. | Usually installed with Helm/operator and persistent storage. |

## Prerequisites

Before installing:

- Use a supported Java version for your Jenkins release.
- Decide where `JENKINS_HOME` will live.
- Plan backups.
- Plan administrator access.
- Plan plugins intentionally.
- Decide whether this is a controller only or controller plus agents.

## Running Jenkins WAR File

Example:

```bash
sudo apt update
sudo apt install -y openjdk-17-jre wget
wget https://get.jenkins.io/war-stable/latest/jenkins.war
java -jar jenkins.war --httpPort=8080
```

Optional custom prefix:

```bash
java -jar jenkins.war --httpPort=8080 --prefix=/jenkins
```

Use WAR mode for learning or troubleshooting, not as the default production pattern unless you have a controlled service wrapper and operational process.

## Package-Based Install

Package installations usually create:

- Jenkins service user.
- systemd service.
- Default Jenkins home.
- Log locations.

Common commands:

```bash
sudo systemctl status jenkins
sudo systemctl enable jenkins
sudo systemctl restart jenkins
sudo journalctl -u jenkins -f
```

## Docker Install

Basic learning command:

```bash
docker run --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts-jdk17
```

Get initial admin password:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Important: the volume is not optional. Without persistence, Jenkins state is lost when the container is removed.

## Initial Admin Password

Common locations:

Native/package install:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

Docker:

```bash
docker exec <container> cat /var/jenkins_home/secrets/initialAdminPassword
```

## First Login Checklist

After first login:

- Install only required plugins.
- Create a real admin user.
- Disable anonymous access unless intentionally needed.
- Configure security realm.
- Configure authorization strategy.
- Configure Jenkins URL.
- Configure agents or clouds.
- Configure credentials.
- Set up backups.
- Add controller resource monitoring.

## Production Hardening

| Area | Recommendation |
| --- | --- |
| TLS | Terminate HTTPS at reverse proxy or load balancer. |
| Access | Require authentication and least-privilege authorization. |
| Plugins | Install only needed plugins and keep them updated. |
| Credentials | Store secrets in Jenkins credentials, not in job scripts. |
| Backups | Back up `JENKINS_HOME`, job config, credentials, and plugin list. |
| Agents | Run builds on agents, not the controller, where possible. |
| Updates | Test Jenkins/plugin updates before production. |
| Logs | Centralize and monitor logs. |

## Reverse Proxy Pattern

Common production flow:

```text
users -> HTTPS reverse proxy/load balancer -> Jenkins controller HTTP port
```

Benefits:

- TLS management.
- Standard access logging.
- IP allow-listing.
- SSO/proxy integration if needed.

## Backup Scope

Back up:

- Jobs and Pipeline config.
- Credentials.
- Users/security config.
- Plugin list and versions.
- Global configuration.
- Secrets/master keys.
- Build history only if required.

Avoid backing up:

- Temporary workspace files unless needed.
- Large build artifacts if they are stored in an artifact repository.

## Benefits

- Multiple installation options.
- Easy local startup for learning.
- Mature plugin ecosystem.
- Can run on VM, container, or Kubernetes.

## Drawbacks / Limitations

- Jenkins requires ongoing plugin/security maintenance.
- Controller state must be protected and backed up.
- Plugin compatibility can make upgrades risky.
- Uncontrolled builds on the controller can affect Jenkins stability.

## Hidden Details / Caveats

- `JENKINS_HOME` is the critical state directory.
- Installing suggested plugins blindly can add more plugins than needed.
- Docker-in-Docker or Docker socket mounting can create high security risk.
- Jenkins upgrades should be tested with your plugin set.
- The initial admin password is only for first setup.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| No persistent Jenkins home | Mount a volume or persistent disk. |
| Running builds on controller | Use agents for workload execution. |
| Installing too many plugins | Keep a minimal plugin baseline. |
| No backup before upgrade | Back up and test restore. |
| Jenkins exposed over plain HTTP publicly | Put behind TLS and access controls. |
| Secrets in shell scripts | Use Jenkins credentials binding. |

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Jenkins does not start | Java version, logs, port conflict, permissions. |
| Cannot unlock Jenkins | Correct initial admin password path and `JENKINS_HOME`. |
| Plugins fail | Jenkins core compatibility, update center access, proxy settings. |
| Jobs stuck in queue | Agents offline, labels mismatch, no executors. |
| Data disappeared in Docker | Missing persistent volume. |

## Interview Notes

- Jenkins needs a controller and usually agents for build execution.
- `JENKINS_HOME` stores critical state.
- First unlock uses `initialAdminPassword`.
- Production Jenkins needs backups, TLS, access control, and plugin governance.
- Docker installation must persist `/var/jenkins_home`.

## Related Topics

- [Running Jenkins in Docker](4%20-%20Running%20Jenkins%20in%20Docker.md)
- [Using and Managing Jenkins](3%20-%20Using%20and%20Managing%20Jenkins.md)

