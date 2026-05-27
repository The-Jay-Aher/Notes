# Jenkins Changelog

## 2026-05-27

### Upgraded

- Added [7 - Pipeline Operations, Security, and Troubleshooting Runbooks](7%20-%20Pipeline%20Operations%20Security%20and%20Troubleshooting%20Runbooks.md) to fill production Jenkins gaps that were only lightly covered in the earlier notes.
- Added [10 - Cheatsheet](10%20-%20Cheatsheet.md) for rapid revision of architecture, Pipeline syntax, credentials, operations, and troubleshooting.
- Added [11 - Glossary](11%20-%20Glossary.md) with practical definitions and small details for Jenkins terms.
- Updated [INDEX](INDEX.md) with the new learning order, source snapshot, and version-sensitive warning.

### Major Improvements

- Added a controller/agent/workspace mental model with Mermaid diagrams.
- Added layered troubleshooting methods for queue, agent, plugin, credentials, test, artifact, and controller failures.
- Added safer credential-handling explanations, including why Groovy interpolation is risky for secrets.
- Added Script Console safety guidance and operational boundaries.
- Added production details around plugin governance, workspace cleanup, Docker socket risk, artifact storage, backups, and restore testing.

### Preservation Notes

- Existing Jenkins chapters were preserved because they already provide useful fundamentals for CI/CD, installation, management, Docker, Declarative Pipeline, and Groovy automation.
- The upgrade is additive rather than duplicative: new files deepen operations and revision coverage without replacing working introductory material.

### Verify Later

- Recheck installed Jenkins plugin versions before using plugin-specific steps such as `cleanWs`, Docker agents, Kubernetes agents, lockable resources, warnings parsers, or credentials bindings in a live controller.
- Recheck Jenkins official documentation before production upgrades because controller, Java baseline, remoting, and plugin compatibility can change.
