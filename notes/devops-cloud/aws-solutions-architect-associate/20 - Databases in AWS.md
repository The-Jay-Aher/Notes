# Databases in AWS

## Quick Summary
- AWS has multiple database services because different applications need different data models and scaling patterns.
- RDS and Aurora are relational databases for SQL and transactions.
- DynamoDB is serverless NoSQL for key-value and document access patterns at large scale.
- ElastiCache is an in-memory cache for low-latency reads and session-like data.
- Redshift is a data warehouse for analytics.
- OpenSearch is for search and log analytics.
- DocumentDB, Neptune, Timestream, and QLDB serve specialized use cases.

## Why So Many Databases?
Do not choose a database only because it is popular.

Choose based on:
- Data model.
- Query pattern.
- Transaction requirements.
- Scaling needs.
- Latency needs.
- Operational control.
- Availability and disaster recovery.
- Cost.

AWS calls this purpose-built databases: different databases for different jobs.

## Relational Databases: RDS
Amazon RDS is managed relational database service.

Supported engines include:
- MySQL.
- PostgreSQL.
- MariaDB.
- Oracle.
- SQL Server.
- Db2.

Use RDS when:
- You need SQL.
- You need joins and relational constraints.
- You are migrating an existing relational application.
- You need transactions.
- You prefer managed backups, patching, and Multi-AZ options.

Common RDS features:
- Automated backups.
- Snapshots.
- Read replicas.
- Multi-AZ deployments.
- Monitoring.
- Minor version patching options.

Important distinction:
- Multi-AZ is mainly for high availability.
- Read replicas are mainly for read scaling.

## Amazon Aurora
Aurora is an AWS-designed relational database compatible with MySQL and PostgreSQL.

Use Aurora when:
- You want relational database features with AWS-optimized storage and availability.
- You need high performance compared with standard MySQL/PostgreSQL RDS options.
- You want Aurora features such as reader endpoints, fast replicas, global databases, and serverless options.

Aurora storage:
- Distributed across multiple AZs.
- Grows automatically up to service limits.
- Designed for high durability.

Aurora endpoints:
- Cluster endpoint for writes.
- Reader endpoint for read replicas.
- Instance endpoints for specific instances.

## DynamoDB
DynamoDB is a serverless NoSQL database.

Use DynamoDB when:
- Access patterns are known and key-based.
- You need very high scale.
- You need low-latency reads and writes.
- You do not want to manage servers.
- You can design around partition keys and indexes.

### DynamoDB Data Model
Core concepts:
- Table.
- Item.
- Attribute.
- Partition key.
- Sort key.
- Global secondary index.
- Local secondary index.

Beginner comparison:
- In SQL, you often design tables first and query flexibly later.
- In DynamoDB, you design around queries first.

### DynamoDB Capacity
Capacity modes:
- On-demand: pay per request, good for unpredictable workloads.
- Provisioned: configure read/write capacity, good for predictable workloads.

Features:
- DynamoDB Streams.
- TTL.
- Global tables.
- Point-in-time recovery.
- Transactions.
- DAX caching.

## ElastiCache
Amazon ElastiCache is managed in-memory data store service.

Supported engines:
- Redis-compatible options.
- Memcached.

Use ElastiCache for:
- Caching database query results.
- Session-like fast lookup data.
- Leaderboards.
- Rate limiting.
- Pub/sub patterns with Redis-compatible workloads.

Why use a cache?
- Databases are slower and more expensive for repeated hot reads.
- Cache can reduce load and improve response time.

Cache-aside pattern:

```text
App checks cache -> cache miss -> read database -> store result in cache
```

Common risk:
- Cache invalidation. The app must decide when cached data is stale.

## Redshift
Amazon Redshift is a data warehouse.

Use Redshift when:
- You need analytics over large datasets.
- You run SQL reports over structured/semi-structured data.
- You need OLAP, not OLTP.

OLTP vs OLAP:

| Type | Meaning | Example |
|---|---|---|
| OLTP | Transaction processing | Create order, update payment |
| OLAP | Analytical processing | Monthly sales report, trend analysis |

Do not use Redshift for normal application transactions.

## OpenSearch Service
Amazon OpenSearch Service is used for search, log analytics, and observability use cases.

Use it when:
- Users need full-text search.
- You need log analytics.
- You need searchable operational data.
- You need aggregations over indexed documents.

Common pattern:

```text
Application logs -> Kinesis/Firehose/Fluent Bit -> OpenSearch -> dashboards/search
```

Do not treat OpenSearch as the primary source of truth for transactional records.

## DocumentDB
Amazon DocumentDB is a managed document database with MongoDB compatibility.

Use it when:
- Application data is document-shaped.
- You are migrating MongoDB-compatible workloads.
- You want managed operations on AWS.

Exam clue:
- "MongoDB-compatible managed database" usually points to DocumentDB.

## Neptune
Amazon Neptune is a graph database.

Use it when relationships are the main query problem.

Examples:
- Fraud rings.
- Social networks.
- Recommendation graphs.
- Knowledge graphs.
- Network topology relationships.

If the question asks for complex relationship traversal, graph database thinking matters.

## Timestream
Amazon Timestream is a time series database.

Use it for:
- IoT metrics.
- Application metrics.
- DevOps telemetry.
- Time-stamped measurements.

Time series data is usually:
- Append-heavy.
- Queried by time ranges.
- Aggregated over windows.

## QLDB
Amazon Quantum Ledger Database is a ledger database.

Use it when:
- You need a verifiable history of changes.
- You need an immutable journal owned by a trusted central authority.

Do not confuse it with blockchain. QLDB is centralized, not decentralized.

## MemoryDB for Redis
Amazon MemoryDB for Redis is a durable, Redis-compatible, in-memory database.

Use it when:
- You need Redis-compatible low-latency access.
- You need durability as part of the database design, not only a cache.

ElastiCache is commonly used as a cache. MemoryDB is positioned as a durable in-memory database.

## Database Migration Service
AWS Database Migration Service helps migrate databases.

Use DMS for:
- Homogeneous migrations such as Oracle to Oracle.
- Heterogeneous migrations such as Oracle to PostgreSQL, often with Schema Conversion Tool support.
- Ongoing replication during migration.

Common pattern:

```text
Source database -> DMS replication instance -> target database
```

## Database Selection Table
| Requirement | Good choice |
|---|---|
| SQL app with joins and transactions | RDS or Aurora |
| MySQL/PostgreSQL-compatible high-performance managed relational DB | Aurora |
| Key-value access at huge scale | DynamoDB |
| Read cache in front of database | ElastiCache |
| Durable Redis-compatible in-memory database | MemoryDB |
| Analytics warehouse | Redshift |
| Full-text search and logs | OpenSearch Service |
| MongoDB-compatible document database | DocumentDB |
| Relationship graph traversal | Neptune |
| Time series metrics | Timestream |
| Immutable ledger history | QLDB |
| Database migration | DMS |

## High Availability and Backups
Common database protection options:
- RDS Multi-AZ.
- Aurora multi-AZ storage and replicas.
- DynamoDB point-in-time recovery and global tables.
- ElastiCache replication groups and Multi-AZ options.
- Redshift snapshots.
- Cross-Region replicas or copies where supported.

Always test restore. A backup plan is not complete until restore is proven.

## Common Mistakes
- Choosing DynamoDB when the app needs ad hoc joins and flexible relational queries.
- Choosing RDS when the workload is massive key-value access with simple queries.
- Using read replicas as a high-availability replacement for Multi-AZ without understanding failover.
- Using a cache as the only copy of important data.
- Using Redshift for user-facing transactional writes.
- Using OpenSearch as the source of truth for orders or payments.
- Ignoring database connection limits when Lambda scales.

## Official References
- [Amazon RDS documentation](https://docs.aws.amazon.com/rds/)
- [Amazon Aurora documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
- [Amazon DynamoDB documentation](https://docs.aws.amazon.com/dynamodb/)
- [Amazon ElastiCache documentation](https://docs.aws.amazon.com/elasticache/)
- [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/)
- [Amazon OpenSearch Service documentation](https://docs.aws.amazon.com/opensearch-service/)
- [Amazon DocumentDB documentation](https://docs.aws.amazon.com/documentdb/)
- [Amazon Neptune documentation](https://docs.aws.amazon.com/neptune/)
- [Amazon Timestream documentation](https://docs.aws.amazon.com/timestream/)
- [AWS Database Migration Service documentation](https://docs.aws.amazon.com/dms/)
