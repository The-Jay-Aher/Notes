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
the high availability can be passive (for RDS Multi AZ for example)
it can be active for horizontal scaling

### high availability and scaling for ec2

vertical scaling: increase the instance size (=scale up / down)

- From : t2.nano: 0.5G of ram, 1 vCPU
- To: u-l 2tbl.metal - 12.3 TB of RAM, 448v CPU

horizontal scaling: increase the number of instances (= scale out / in)

- auto scaling group
- load balancer

high availability: run instances for the same application across multiple AZ

- auto scaling group multi az
- load balancer multi az

## Elastic Load Balancing (ELB) Overview

### what is load balancing?

load balances are servers that forward traffic, to multiple server (e.g. EC2 instances) downstream

### why use a load balancer?

spread load across multiple downstream instances
expose single point of access(DNS) to your application
seamselly handle failures of downstream instances
do regular health checkups of your ec2 instnaces
provide SSL termination (HTTPS) for your websites
enforece stickiness with cookies
high availability across zones
separate public traffic from private traffic

### why use an load balancer?

an elastic load balancer is a managed load balancer

- aws guarntess that it will work
- aws takes care of upgrade, maintenance, high availability
- aws provides only a few configuration knobs

it costs less to set up your own load balancer, but it will be a lot of effort on your end

it is integrated with many AWS offerings, services

- ec2, ec2 scaling groups, amazon ecs
- aws certificate manager(acm), cloudwatch
- route 53, aws waf, aws global accelarator

### health checks

health checks are crucial for load balancers
they enable the load balancer to know if instances it forwards traffic to are available to reply to requests
the health check is done on a port and a route (/health is common)
if the response is not 200 (OK), then the instance is unhealthy

### types of load balancer is aws

aws has 4 kinds of load balancers

1. classic load balancer (v1 - old generation) - 2009 - CLB
   1. HTTP, HTTPS, TCP, SSL (secure TCP)
2. application load balancer (v2 - new generation) - 2016 - ALB
   1. http, https, web socket
3. network load balancer (v2 - new generation) - 2017 - nlb
   1. tcp, tls (secure tcp), udp
4. gateway load balancer - 2020 - Gwlb
   1. operates at leayer3 (network layer) - ip protocol

overall it's recommended to use the newer generation load balancer, as they provide more features
some load balancers can be setup as internal(private) or external(public) ELBs

## Application Load Balancer (ALB)

### application load balancer (v2)

it is layer 7 (http)

load balancing to multiple https applications across machines (target groups)

load balancing to multiple applications on the same machine (e.g. containers)

support for https2 and web socket

support redirects (from https to https for example)

routing tables to different target groups:

- routing based on path url (/users & /posts)
- routing based on hostname in url (one.example.com & other.example.com)
- routing based on query string & headers(example.com/users?id=123&order=false)

alb are a great fir for micro services & container based application (docker and amamzon ecs)
has port mapping feature to redirect to a dynamic port on ecs
in comparision, we need multiple classic load balancers per application

### target groups

ec2 instances (can be managed by an auto scaling group) - http
ec2 tasks (managed by ecs itself) - http
lambda functions - http request is translated into a json event
ip address - must be private ip address

alb can route to multipel target groups
health checks are at target groups levels

### good to know

fixed hostname (xxx.region.elb.amazonaws.com)
the application servers don't see the ip of the client dorectly,
the true ip of the client is inserted in the header X-Forwarded-For
we can also get port (X-Forward-Port) and proto (X-Forward-Proto)
