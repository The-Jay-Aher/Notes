# AWS Solution Architect Changelog

## 2026-08-17

### Upgraded

- Rebuilt [7 - AWS Databases - RDS, Aurora and ElastiCache](7%20-%20AWS%20Databases%20-%20RDS,%20Aurora%20and%20ElastiCache.md) as the canonical union of the prior generated chapter and the user's manual RDS/Aurora/ElastiCache chapter.
- Removed the duplicate `Manual/7 - AWS Databases - RDS + Aurora + ElastiCache.md` after preserving its useful concepts in the canonical chapter.

### Major Improvements

- Replaced terse facts with first-principles explanations of relational persistence, ACID, managed-service responsibility, caching, consistency, RPO, and RTO.
- Added architecture and sequence diagrams for RDS connectivity, Multi-AZ, read replicas, Aurora distributed storage and Global Database, RDS Proxy, cache-aside, session storage, and integrated database/cache flows.
- Added deep coverage of storage autoscaling, modern RDS Multi-AZ topology distinctions, RDS Custom, backup/restore and import paths, security, monitoring, performance analysis, and RDS Proxy.
- Added Aurora quorum/storage internals, endpoints, replica auto scaling, Serverless v2, Global Database, Backtrack, cloning, machine-learning integration, and Babelfish limitations.
- Updated ElastiCache terminology for Valkey, Redis OSS, and Memcached; added cache invalidation, stampede/hot-key handling, TTL/eviction behavior, security planes, failure modes, and the Serverless Memcached backup distinction.
- Added scenario-based SAA decision tables, debugging flowcharts, safe read-only CLI inspection examples, ports, a rapid revision sheet, glossary, and 20 questions with reasoned answers.
- Added a categorized “Further Exploration — Remaining Knowledge Gaps” research backlog covering engine administration, APIs and automation, compatibility matrices, cache internals, quotas, pricing, migration runbooks, performance engineering, reliability, security, and operations.
- Added a matching “Further Exploration — Remaining Knowledge Gaps” research backlog to [6 - High Availability and Scalability with ELB and ASG](6%20-%20High%20Availability%20and%20Scalability%20ELB%20and%20ASG.md), covering distributed-systems foundations, networking protocols, ALB/NLB/GWLB internals, target health, TLS, Auto Scaling control behavior, Spot and warm pools, deployments, observability, automation, quotas, pricing, performance, and resilience testing.

### Corrected or Qualified

- Corrected Aurora's storage model from eight copies to six copies across three AZs and explained the 4/6 write and 3/6 read quorum model.
- Replaced outdated storage-autoscaling timing, universal replica-count, guaranteed failover/RTO, fixed-price-premium, and absolute cache durability statements with current, version-aware explanations.
- Distinguished classic Multi-AZ DB instances from readable Multi-AZ DB clusters, and AZ-level high availability from Region-level disaster recovery.

### Verify Later

- Recheck engine versions, Regions, quotas, storage limits, Aurora Global Database topology limits, ElastiCache engine lifecycle, and RDS/ElastiCache feature compatibility before production design or exam booking.
- Recalculate pricing from current AWS pricing pages and the measured workload; no fixed Aurora-versus-RDS percentage is assumed.

## 2026-05-27

### Upgraded

- Added [28 - SAA-C03 Alignment Audit and Scenario Playbook](28%20-%20SAA-C03%20Alignment%20Audit%20and%20Scenario%20Playbook.md).
- Added [29 - SAA-C03 Practice Questions and Rationales](29%20-%20SAA-C03%20Practice%20Questions%20and%20Rationales.md).
- Added [30 - SAA-C03 Rapid Revision Cheatsheet and Glossary](30%20-%20SAA-C03%20Rapid%20Revision%20Cheatsheet%20and%20Glossary.md).
- Updated [INDEX](INDEX.md) with the 2026-05-27 source snapshot and final SAA revision path.

### Major Improvements

- Refreshed the SAA-C03 exam alignment against the official AWS exam guide.
- Added official domain weights: secure architectures 30%, resilient architectures 26%, high-performing architectures 24%, cost-optimized architectures 20%.
- Added scenario reasoning chains for security, resilience, performance, and cost decisions.
- Added practice questions with rationales to train exam-style elimination rather than memorized service names.
- Added rapid service-decision clues, traps, patterns, and glossary terms.

### Preservation Notes

- Existing 27 service chapters were preserved because they already cover the main AWS SAA service families.
- The upgrade adds an exam-alignment layer instead of duplicating existing service explanations.

### Verify Later

- Recheck the official AWS SAA-C03 guide before booking or revising for the exam.
- Recheck service-specific docs for pricing, quotas, new features, deprecations, and managed-service behavior.
