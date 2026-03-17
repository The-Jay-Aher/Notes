# High Availability and Scalability in ELB & ASG

## High Availability and Scalability

### Scalability & High Availability

scalability means that an application / system can handle grater loads by adapting
there are 2 types of scalability:

- vertical
- horizontal (=elasticity)
  scalability is linked but different to High Availability

### Vertical scalability

vertical scalability means increasing the size of the instance
for example, your application run on t2.micro
scalling that application means running it on t2.large
vertical scalability is very common for non-distributive systems, such as databases
RDS, Elasticache are services that can scale vertically
there's a limit on how much you can vertically scale(hardware limit)

### horizontal scalability

horizontal scalability means increasing the number of instances / systems for your applications
horizontal scaling implies distributed systems
this is very common for web application / modern application
It's easy to scale thanks to the cloud offering such as amazon ec2

### high availability

it goes hand in hand with horizontal scaling
it means running your applications in at least 2 data centres (== availability zones)
the goal is to survive a data centre loss
the high availablity can be passive (for RDS Multi AZ for example)
it can be active for horizontal scaling

### high availiblity and scaling for ec2

vertical scaling: increase the instnace size (=scale up / down)

- From : t2.nano: 0.5G of ram, 1 vCPU
- To: u-l 2tbl.metal - 12.3 TB of RAM, 448v CPU

horizontal scaling: increase the number of instances (= scale out / in)

- auto scaling group
- load balancer

high availability: run instances for the same application across multiple AZ

- auto scaling group multi az
- load balancer multi az
