# Amazon RDS Overview
- RDS stands for relational database service
- It's a managed DB service for DB that uses SQL as a query language
- It allows you to create databases in cloud that are managed by AWS
	- Postgres
	- MySQL
	- MariaDB
	- Oracle
	- Microsoft SQL Server
	- IBM DB2
	- Aurora (AWS Proprietary Database)
## Advantage of using RDS vs deploying DB on EC2
RDS is a managed service:
- Automated provisioning, OS patching
- Continuous backups and restore to specific timestamps
- Monitoring Dashboards
- Read replicas for improved read performance
- Multi AZ setup for (DR recovery)
- Maintenance window for upgrades
- Scaling capability (vertical and horizontal)
- Storage backed by EBS
But we can't SSH into RDS instances (RDS is implemented on an EC2 instance, but we are not able to SSH into that EC2 instance)
## RDS  - Auto Scaling
Helps you increase storage on your RDS DB instance dynamically
When RDS detects, you are running out of free database storage, it scales automatically
Avoid manually scaling your database storage
You have to set Maximum Storage Threshold (max limit for DB storage)
Automatically modify storage if:
- Free storage less than 10% of allocated storage
- Low-storage lasts at least 5 min
- 6 hours have passed since last modification
Useful for applications with unpredictable workloads
Supports all RDS and database engines
# RDS Read Replicas vs Multi AZ
## RDS Read replica for read scalability
Up to 15 read replicas
Within AZ, Cross AZ or Cross Region
Replication is ASYNC, so reads are eventually consistent
Replicas can be promoted to their databases
Applications must update the connection string to leverage replicas
## RDS Read Replicas  - Use case
You have production database that is taking on normal mode
You want to run some reporting application to run some analytics
You create a read replica to run the new workload run
The production application is unaffected
Read replicas are used for SELECT(=read) only kind of statements (not INSERT, UPDATE, DELETE)
## RDS Read Replicas - Network Costs
In AWS, there's a network cost when data goes from one AZ to another
For RDS, Read Replicas within the same region, you don't pay that fee
But fee is there for cross-region read replicas
## RDS Multi AZ  (Disaster Recovery)
SYNC replication
One DNS Name - automatic app failover to standby
Increase availability
Failover, in case loss of AZ,  loss of network, instance of storage failure
No manual intervention in apps
Not used for scaling
Note: the read replicas can be setup as multi az for disaster recovery (dr)
## rds -singe az to multi az
zero downtime operation (no need to stop the db)
just click on "modify" for the database
the following happens internally:
- a new snapshot is taken
- a new db is restored from the snapshot in a new az
- synchronization is setup between the two databases
# rds custom for oracle and microsoft sql server
## rds custom
managed oracle and microsoft sql server database with os and databse customization
rds: automates setup, operation and scaling of databases in aws
custom: access to the underlying database and os so you can
- configure settings
- install patches
- enable native features
- access to underlying ec2 instances using ssh or ssm session manager
de-activate automation mode to perform your customization, better to take a DB snapshot before 
rds vs rds custom:
- rds: entire database and the os to be managed by AWS
- rds cutom: full admin access to the underlying os and the database
# amazon aurora
aurora is a proproeitary technology from aws (not open sourced)
postgres and mysql are both supported as aurora db (that means your driver will work as if Aurora was postgres or MySQL database)
aurora is "aws cloud optimized" and claim 5x performance imporvement over mysql on rds, over 3x the performance of postgres on rds
aurora storage automatically grows in increments of 10GB, upto 256tb
aurora can have upto 15 replicas and the replication process is faster than mysql  (sub 10ms replica lag)
failover in aurora is instantaneous. it's high availability native
aurora costs more than rds (20% more) - but is more  efficient
## aurora high availability and read scaling
8 copies of your across 3 AZ:
- 4 copies out of 6 for writes
- 3 copies out of 6 for reads
- self healing with peer to peer replication
- storage is striped across 100s of volumes
one aurora instance takes writes (master)
automated failover for master in less than 30 sec
master + up to 15 aurora read replicas server reads
support for cross region replication
## features of aurora
1. automatic failover
2. backup and recovery
3. isolation and security
4. industry compliance
5. push button scaling
6. automated pipeline with zero downtime
7. advanced monitoring
8. routine maintenance
9. backtrack: retore data at any point of time without using backups
