# 7 - AWS Databases: RDS, Aurora and ElastiCache

## Quick Summary

This note covers managed database and caching services that appear frequently in AWS Solutions Architect questions: Amazon RDS, Amazon Aurora, and Amazon ElastiCache. The key is to understand when you need a relational database, when Aurora is a better cloud-native relational option, and when caching reduces database load.

## Core Idea

```text
RDS/Aurora = persistent relational database
ElastiCache = fast in-memory cache
```

Use a database when the data must be stored reliably. Use a cache when you want to speed up reads, reduce database load, or store short-lived data.

## Amazon RDS

Amazon Relational Database Service is a managed service for relational databases.

Supported engines commonly include:

- Amazon Aurora.
- PostgreSQL.
- MySQL.
- MariaDB.
- Oracle.
- SQL Server.

RDS manages much of the undifferentiated work:

- Provisioning.
- Backups.
- Patching.
- Monitoring integrations.
- Multi-AZ high availability options.
- Read replicas for selected engines.

You still manage:

- Schema design.
- Query performance.
- Indexes.
- User permissions inside the database.
- Application connection behavior.
- Some engine-specific tuning.

## RDS Storage And Backups

Important backup concepts:

- Automated backups support point-in-time recovery within the configured retention window.
- Manual snapshots are retained until deleted.
- Snapshots can be copied across Regions.
- Backups and snapshots are useful for restore, migration, and disaster recovery planning.

Beginner warning:

```text
Backup exists does not mean recovery is tested.
```

Always know restore time and recovery process.

## Multi-AZ

Multi-AZ is for high availability.

In a typical RDS Multi-AZ deployment:

```text
Primary DB instance in AZ A
Standby DB instance in AZ B
Synchronous replication
Automatic failover if primary fails
```

Use Multi-AZ when the database must survive an Availability Zone or instance failure.

Important:

- Multi-AZ is not mainly for read scaling.
- The standby is generally not used for normal reads in the classic model.
- Failover changes the underlying target behind the same endpoint.

## Read Replicas

Read replicas are for read scaling.

```text
Primary DB -> asynchronous replication -> read replica
```

Use read replicas when:

- Read traffic is heavy.
- Reporting queries should not overload primary.
- You need cross-Region read copies for selected engines.

Important:

- Replication is asynchronous.
- Replicas can lag behind primary.
- Application must direct read queries to replicas.

## Multi-AZ vs Read Replica

| Feature | Multi-AZ | Read Replica |
| --- | --- | --- |
| Main purpose | High availability. | Read scaling. |
| Replication | Synchronous in classic HA model. | Asynchronous. |
| Used for reads | Usually no for standby. | Yes. |
| Failover | Automatic. | May need promotion/manual design. |
| Data lag | Designed for low/no committed data loss in HA failover. | Lag possible. |

## Amazon Aurora

Aurora is AWS's cloud-optimized relational database compatible with MySQL and PostgreSQL patterns.

Aurora architecture separates compute and storage:

```text
Aurora DB instances = compute
Aurora cluster volume = distributed storage
```

Key points:

- Storage automatically grows.
- Replication is built into the storage layer.
- Supports reader endpoints and replicas.
- Designed for high availability and performance.

## Aurora Cluster Endpoints

Common endpoints:

| Endpoint | Use |
| --- | --- |
| Writer endpoint | Connect application writes to current primary writer. |
| Reader endpoint | Load-balance reads across Aurora replicas. |
| Instance endpoint | Connect to a specific DB instance. |
| Custom endpoint | Route to a selected subset of instances. |

Beginner pattern:

```text
writes -> writer endpoint
reads -> reader endpoint
```

## Aurora Serverless

Aurora Serverless automatically adjusts capacity for variable workloads.

Use when:

- Workload is intermittent or unpredictable.
- You want simpler capacity management.
- The app can tolerate serverless scaling characteristics.

Check current Aurora Serverless version and feature support before production design.

## Global Database

Aurora Global Database supports low-latency global reads and disaster recovery patterns across Regions.

Use when:

- Users are global and need fast reads.
- Cross-Region DR is required.
- RPO/RTO requirements justify complexity and cost.

## ElastiCache

ElastiCache is a managed in-memory data store/caching service.

Common engines:

- Redis-compatible Valkey/Redis OSS style workloads depending on current AWS offering.
- Memcached.

Use cases:

- Cache database query results.
- Store sessions.
- Leaderboards.
- Rate limiting.
- Real-time counters.
- Pub/sub patterns with Redis-compatible engines.

## Cache Patterns

### Lazy Loading

```text
App checks cache
if miss -> read database -> store result in cache -> return result
```

Pros:

- Cache only stores requested data.
- Simple.

Cons:

- First request after miss is slower.
- Stale data possible.

### Write Through

```text
App writes data -> update database and cache together
```

Pros:

- Cache stays warmer.

Cons:

- More write complexity.

## Cache TTL

TTL means time to live.

Example:

```text
Cache product details for 10 minutes.
```

TTL prevents stale data from living forever.

## When To Use What

| Need | Service |
| --- | --- |
| Managed relational database | RDS. |
| Cloud-native high-performance relational database | Aurora. |
| High availability relational DB | RDS Multi-AZ or Aurora. |
| Read scaling relational DB | Read replicas or Aurora replicas. |
| Fast temporary lookup/session data | ElastiCache. |
| Key-value/document NoSQL | DynamoDB, covered later. |

## Benefits

- Managed operations reduce admin burden.
- Multi-AZ improves availability.
- Backups and snapshots simplify recovery.
- Read replicas help read-heavy systems.
- Caching can reduce latency and database load.

## Drawbacks / Limitations

- Managed does not mean no design work.
- Bad queries still perform badly.
- Read replicas can lag.
- Cache invalidation is hard.
- Multi-AZ and replicas add cost.
- Application connection pooling still matters.

## Hidden Details / Caveats

- RDS storage autoscaling and engine support vary by engine/version.
- Read replica lag can cause stale reads.
- RDS failover changes the active host behind the endpoint; clients must reconnect.
- Caches are not durable databases.
- Do not store irreplaceable data only in ElastiCache.
- Security groups must allow app-to-database/cache traffic.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Using Multi-AZ for read scaling | Use read replicas or Aurora reader endpoint. |
| Using read replica as HA replacement | Use Multi-AZ for HA. |
| No connection pooling | Add pooling/proxy where appropriate. |
| Cache without TTL/invalidation | Define freshness strategy. |
| Publicly exposing database | Keep DB private and restrict security groups. |
| Assuming backup means tested recovery | Run restore drills. |

## Troubleshooting

| Problem | Check |
| --- | --- |
| App cannot connect | Security group, subnet, DNS endpoint, credentials, port. |
| Slow queries | Indexes, query plan, CPU, IOPS, locks, connection count. |
| Failover caused errors | Client retry/reconnect logic, DNS caching, connection pooling. |
| Stale reads | Replica lag or cache TTL. |
| Cache miss spike | Eviction, memory pressure, TTL, deploy flush. |

## Interview Notes

- RDS Multi-AZ is for high availability.
- RDS read replicas are for read scaling.
- Aurora separates compute from distributed storage.
- Aurora writer endpoint is for writes; reader endpoint is for reads.
- ElastiCache is not a durable database.
- Cache reduces latency and database load but introduces invalidation/staleness issues.

## Official References

- Amazon RDS documentation: <https://docs.aws.amazon.com/rds/>
- Amazon Aurora documentation: <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>
- Amazon ElastiCache documentation: <https://docs.aws.amazon.com/elasticache/>
