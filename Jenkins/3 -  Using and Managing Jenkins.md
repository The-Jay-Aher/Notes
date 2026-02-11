# 3 - Using and Managing Jenkins

## Jenkins Plugin Model

Jenkins functionality is heavily plugin-driven.

Key points:

- Most plugins are Java-based.
- Plugin projects commonly use Maven.
- Plugin compatibility depends on Jenkins core version + plugin dependency graph.

## Plugin Packaging Basics

Common file extensions:

- `.hpi` (legacy Hudson/Jenkins plugin package)
- `.jpi` (Jenkins plugin package)

Both are package formats used by Jenkins plugin ecosystem.

## Plugin Versioning and Compatibility

Common versioning patterns include:

- Semantic versioning
- Build metadata/hash-based versions

Why compatibility matters:

- Plugins depend on specific Jenkins core APIs.
- Plugins may also depend on other plugin versions.
- Upgrades should be tested in non-production first.

## Plugin Management Best Practices

- Install plugins from official update center.
- Limit who can install/update plugins.
- Keep a tested plugin baseline list.
- Back up Jenkins home before major updates.
- Roll updates in controlled batches.

## Managing Plugin State

A plugin can be:

- Installed or not installed
- Enabled or disabled

Troubleshooting tip:

- Broken plugins can be temporarily disabled while you recover.

## Plugin Automation with Groovy/Pipelines

Automation options:

- Script Console
- Startup scripts (`init.groovy.d`)
- Policy pipelines (periodic enforcement)

Use cases:

- Enforce approved plugin set
- Detect/remove unapproved plugins
- Maintain pinned versions for sensitive plugins

## Plugin Security Guidance

- Follow least privilege for Jenkins administration.
- Review plugin advisories regularly.
- Avoid untrusted third-party plugin sources.
- Validate plugin communication/security behavior for high-risk plugins.

## Quick Summary

1. Plugins drive Jenkins capabilities.
2. Plugin lifecycle management is a core ops/security responsibility.
3. Controlled updates and automation reduce plugin-related incidents.
