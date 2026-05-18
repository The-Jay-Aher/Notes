# 2 - Jenkins Installation

## Installation Approaches

Common ways to run Jenkins:

1. Native package install (systemd service)
2. WAR file execution
3. Docker container (common for reproducibility)

## Running Jenkins WAR File

Example steps (Linux):

```bash
sudo apt update
sudo apt install -y openjdk-17-jre wget
wget https://get.jenkins.io/war-stable/latest/jenkins.war
java -jar jenkins.war --httpPort=8080
```

Optional custom prefix/port:

```bash
java -jar jenkins.war --httpPort=8080 --prefix=/dashboard
```

Notes:

- Avoid port `80` unless you intentionally run with elevated privileges or reverse proxy.
- For production, prefer reverse proxy + TLS.

## Systemd Service Commands (Package-Based Install)

```bash
sudo systemctl status jenkins
sudo systemctl enable jenkins
sudo systemctl restart jenkins
```

## Initial Admin Password

Typical path (package-based installs):

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

If using containers/custom paths, location may differ based on `JENKINS_HOME`.

## Post-Install Checklist

- Install suggested plugins (or curated list)
- Configure admin user and RBAC strategy
- Set up backup strategy for `JENKINS_HOME`
- Configure agents (do not run heavy builds on controller)

## Quick Summary

1. Jenkins can run via WAR, package, or Docker.
2. Secure defaults and backup planning are essential from day one.
3. Controller should orchestrate; agents should execute most builds.
