# EC2 Basics

## Amazon EC2

EC2 is one most popular of AWS offering
EC2 = Elastic Cloud Compute = Infrastructure as a Service
It mainly consists of:

-   Renting Virtual machines (EC2)
-   Storing data on virtual drives (EBS)
-   Distributing load across machines (ELB)
-   Scaling the services using an auto-scaling group (ASG)
    Knowing EC2 is fundamental to understand how cloud works

### EC2 sizing and configuration options

1. Operating System
2. CPU
3. RAM
4. Storage space:
    1. Network-attached (EBS & EFS)
    2. Hardware (EC2 Instance store)
5. Network Card: speed of the card, Public IP address
6. Firewall rules: security group
7. Bootstrap script (configure at first launch): EC2 User Data

## EC2 Instance Types basics

You can use different types of EC2 Instances that are optimized different use-cases
[AWS-Instance-Types](https://aws.amazon.com/ec2/instance-types/)

There are 7 Different types of Instances:

1. General Purpose
2. Compute Optimized
3. Memory Optimized
4. Accelerated Optimized
5. Storage Optimized
6. Instance Features
7. Measuring Instance Performance

AWS has the following naming conventions:
`m5.2xlarge`

m: instance class
5: generation (aws improves them over time) (higher the better)
2xlarge: size within the instance class
 
### EC2 Instance Types - General Purpose

