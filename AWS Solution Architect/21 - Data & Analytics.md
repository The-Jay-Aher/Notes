# Data and Analytics

## Quick Summary
- Data analytics on AWS usually starts with S3 as a durable data lake.
- Glue catalogs and prepares data, Athena queries data in S3, Redshift warehouses structured analytics data, and QuickSight visualizes results.
- Kinesis handles streaming data, while EMR runs big data frameworks such as Spark and Hadoop.
- Lake Formation helps govern data lake permissions.
- Good analytics design separates ingestion, storage, cataloging, processing, querying, visualization, and governance.

## The Analytics Pipeline
Most analytics architectures can be understood as a pipeline.

```text
Ingest -> Store -> Catalog -> Process -> Query -> Visualize -> Govern
```

AWS examples:

| Stage | AWS services |
|---|---|
| Ingest | Kinesis, DataSync, DMS, Transfer Family, MSK, Glue connectors |
| Store | S3, Redshift, OpenSearch |
| Catalog | AWS Glue Data Catalog |
| Process | Glue ETL, EMR, Lambda, Kinesis Data Analytics |
| Query | Athena, Redshift, OpenSearch |
| Visualize | QuickSight |
| Govern | Lake Formation, IAM, KMS, Macie |

## Data Lake
A data lake stores raw and processed data, often in S3.

Why S3 is common:
- Highly durable object storage.
- Stores many data formats.
- Integrates with analytics services.
- Supports lifecycle policies.
- Supports encryption and access controls.

Common zones:

```text
raw/        original data
cleaned/    validated and standardized data
curated/    business-ready datasets
archive/    old data retained for compliance
```

Good data lake design:
- Use clear bucket and prefix naming.
- Partition data by useful fields, often date.
- Use columnar formats such as Parquet or ORC for analytics.
- Compress data to reduce cost.
- Use Glue Data Catalog for schema discovery.
- Govern access carefully.

## AWS Glue
AWS Glue is a serverless data integration service.

Common Glue pieces:
- Glue Data Catalog.
- Crawlers.
- ETL jobs.
- Glue Studio.
- Glue DataBrew.

### Glue Data Catalog
The Data Catalog stores metadata about datasets.

It can store:
- Database names.
- Table names.
- Column names and types.
- S3 locations.
- Partition information.

Athena, Redshift Spectrum, EMR, and other services can use the catalog.

### Glue Crawlers
Crawlers inspect data and create/update catalog tables.

Example:

```text
S3 logs -> Glue crawler -> Glue Data Catalog table -> Athena query
```

Be careful:
- Crawlers infer schemas, but inferred schemas can be wrong.
- Production data pipelines often need controlled schemas, not only automatic inference.

### Glue ETL Jobs
Glue ETL jobs transform data.

Examples:
- Convert CSV to Parquet.
- Remove bad records.
- Join datasets.
- Mask sensitive fields.
- Create curated tables.

## Amazon Athena
Athena is a serverless query service for data in S3.

You write SQL. Athena reads data from S3 using table metadata from the Glue Data Catalog.

```text
SQL query -> Athena -> S3 data -> query results
```

Use Athena when:
- You need ad hoc queries on S3 data.
- You do not want to run a data warehouse cluster.
- Data is already in S3.
- Query frequency is moderate or unpredictable.

Performance and cost tips:
- Use Parquet or ORC instead of raw CSV/JSON where possible.
- Partition data.
- Compress data.
- Avoid scanning unnecessary columns and partitions.
- Store query results in a controlled S3 location.

Athena charges based on data scanned, so reducing scanned data matters.

## Amazon Redshift
Redshift is a data warehouse.

Use Redshift when:
- You have regular analytics workloads.
- Many users run dashboards and reports.
- You need high-performance SQL analytics over structured data.
- You need data warehouse features and optimizations.

Redshift options:
- Provisioned clusters.
- Redshift Serverless.
- Redshift Spectrum to query S3 data from Redshift.

Redshift vs Athena:

| Topic | Athena | Redshift |
|---|---|---|
| Infrastructure | Serverless query service | Data warehouse service |
| Data location | S3 | Redshift storage and/or S3 via Spectrum |
| Best for | Ad hoc S3 queries | Frequent warehouse analytics |
| Cost model | Data scanned | Capacity/serverless usage |

## Amazon EMR
Amazon EMR runs big data frameworks.

Frameworks include:
- Apache Spark.
- Hadoop.
- Hive.
- Presto/Trino depending on configuration.

Use EMR when:
- You need big data processing frameworks.
- You have Spark jobs.
- You need more control than Glue.
- You have existing Hadoop/Spark workloads.

Glue vs EMR:
- Glue is more serverless and managed for ETL.
- EMR gives more cluster/framework control.

## Kinesis for Streaming Analytics
Kinesis services handle streaming data.

| Service | Use |
|---|---|
| Kinesis Data Streams | Custom real-time stream processing |
| Kinesis Data Firehose | Managed delivery to S3, Redshift, OpenSearch, and partners |
| Managed Service for Apache Flink | Real-time stream processing with Apache Flink |

Example:

```text
Application events -> Kinesis Data Streams -> Flink app -> real-time metrics
                                      -> Firehose -> S3 data lake
```

## Amazon MSK
Amazon Managed Streaming for Apache Kafka is managed Kafka.

Use MSK when:
- You already use Kafka.
- Applications depend on Kafka APIs.
- Teams need Kafka ecosystem compatibility.

If the requirement is generic AWS-native streaming, Kinesis may be simpler. If it says Kafka, MSK is usually the targeted answer.

## OpenSearch for Analytics
OpenSearch is useful for:
- Log search.
- Full-text search.
- Operational dashboards.
- Near-real-time indexing and filtering.

It is not a replacement for a relational database or warehouse. Use it when search and indexed document queries are central.

## QuickSight
Amazon QuickSight is a business intelligence service.

Use it for:
- Dashboards.
- Reports.
- Data visualization.
- Sharing analytics with business users.

Data sources can include:
- Athena.
- Redshift.
- RDS.
- S3.
- Many other supported sources.

## Lake Formation
AWS Lake Formation helps build and govern data lakes.

It can help with:
- Centralized permissions.
- Data lake access controls.
- Data sharing.
- Integration with Glue Data Catalog.

Use it when data lake governance becomes too complex for simple IAM and bucket policies alone.

## Data Formats
Common formats:

| Format | Notes |
|---|---|
| CSV | Easy to read but inefficient for large analytics |
| JSON | Flexible but can be inefficient and messy |
| Parquet | Columnar, efficient for analytics |
| ORC | Columnar, efficient for analytics |
| Avro | Row-based, common in streaming and schema-based systems |

For analytics over S3, Parquet plus partitioning is often a strong default.

## Common Architectures
### S3 Data Lake with Athena
```text
Files land in S3 -> Glue crawler/catalog -> Athena SQL -> QuickSight dashboard
```

### Streaming Logs to Search
```text
Application logs -> Kinesis Firehose -> OpenSearch -> dashboard
```

### Warehouse Reporting
```text
Operational DB -> DMS/ETL -> Redshift -> QuickSight
```

### Big Data Spark Processing
```text
S3 data -> EMR Spark job -> curated S3 data -> Athena/Redshift
```

## Common Mistakes
- Querying huge CSV files with Athena and wondering why it is expensive.
- Not partitioning data by query patterns.
- Treating S3 folders as real directories instead of object key prefixes.
- Letting every team create inconsistent schemas.
- Using OpenSearch as the only source of truth.
- Choosing EMR when Glue would be simpler.
- Choosing Redshift for a few occasional S3 queries when Athena would be simpler.

## Official References
- [AWS Glue documentation](https://docs.aws.amazon.com/glue/)
- [Amazon Athena documentation](https://docs.aws.amazon.com/athena/)
- [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/)
- [Amazon EMR documentation](https://docs.aws.amazon.com/emr/)
- [Amazon Kinesis documentation](https://docs.aws.amazon.com/kinesis/)
- [Amazon Managed Service for Apache Flink documentation](https://docs.aws.amazon.com/managed-flink/)
- [Amazon MSK documentation](https://docs.aws.amazon.com/msk/)
- [AWS Lake Formation documentation](https://docs.aws.amazon.com/lake-formation/)
- [Amazon QuickSight documentation](https://docs.aws.amazon.com/quicksight/)
