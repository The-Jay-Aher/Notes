# High Availability and Scalability
## Scalability and High Availability

Scalability mean that an application/system can handle greater loads by adapting
There are 2 types of scalability:
- Vertical
- Horizontal (=elasticity)
Scalability is linked but different to High Availability
## Vertical Scalability
- Increasing the size of the instance
- Running an application from t2.micro to t2.large
- Very common for non-distributed systems, such as databases
- RDS, ElastiCache can scale vertically
- There's usually a limit on how much you can scale vertically (hardware limit)
## Horizontal Scalability
- Horizontal scalability means increasing the number of instances/systems for your application
- Horizontal Scaling implies distributed systems
- Easier to scale horizontally using EC2
## High Availability
- High Availability usually goes hand in hand with horizontal scaling
- High Availability means running your application in at least 2 data centres (== Availability Zones)
- The main goal is to survive data centre loss
- The high availability can be:
	- passive (r.g. RDS Multi AZ)
	- Active (Horizontal Scaling)
## High Availability and scalability for EC2
- Vertical Scaling -> Increase instance size (= scale up/down)
	- From t2.nano
	- To: i12tbI.metal
- Horizontal Scaling -> Increase the number of instance (= scale out / in)
	- Auto scaling group
	- Load Balancer
- High Availability: Run instances of the same application across multiple AZ's
	- Auto Scaling group Multi-AZ
	- Load balancer multi AZ
# Elastic Load Balancer (ELB Overview)
## What is Load Balancing?
- Load Balancers are servers that forward traffic to multiple servers (e.g. EC2 instances) downstream
## Why use load balancer?
- Spread load across multiple downstream services
- Expose a single point of access (DNS) to your application
- Seamlessly handle failures of downstream services
- Do regular health checks of your application
- Provide SSL termination (HTTPS) for your websites
- Enforce stickiness with cookies
- High Availability across zones
- Separate public traffic form private traffic

An Elastic Load Balancer is a managed load balancer
- AWS guarantees:
	- It will be working
	- Takes care of Maintenance, upgrades, high availability
	- Provides a few configuration knobs
- It costs less to setup your own load balancer but it will be a lot more effort on your end
- It is integrated with many AWS offerings and services
	- EC2, EC2 Auto Scaling Groups, ECS
	- AWS Certificate Manager, Cloud Watch
	- Route 53, AWS WAF, AWS Global Accelerate
## Health Checks
- Health checks are crucial for load balancers
- They enable the load balancer to know if instances it forwards traffic to are available to reply to requests
- The health check is done on a port and a route (/health is common)
- If it's not 200(OK), then the instance is unhealthy
## Types of load Balancers
AWS has 4 kinds of load balancers
1. Classic Load Balancer (v1 - old generation) - 2009 - CLB
	1. HTTP, HTTPS, TCP, SSL (secure TCP)
2. Application Load Balancer (v2 - new generation) - 2016 - ALB
	1. HTTP, HTTPS, WebSocket
3. Network Load Balancer (v2 - new genration) - 2017  - NLB
	1. TCP, TLS (secure TCP), UDP
4. Gateway Load Balancer - 2020 - GWLB
	1. Operates at Layer 3 (Network Layer) - IP Protocol
Overall it's recommended to use newer generation load balancers as they provide more features
Some load balancers can be setup as internal (private) or external (ELBs) 
##  Load Balancer Security Groups
Load Balancer can get traffic from both HTTP and HTTPS
But the EC2 instance will get the traffic only from the load balancer, so we are going to link the security group of load balancer to the security group of the EC2 instance
# Application Load Balancer (ALB)
- Application Load Balancer is layer 7 (HTTP) 
- Load Balancing to multiple HTTP applications across machines (target groups)
- Load Balancing to multiple application on the same machine (e.g. container)
- Support for HTTP/2 and WebSocket
- Supports redirects from HTTP and HTTPS

- Routing tables to different target groups:
	- Path in URL (example.com/users & example.com/posts)
	- Hostname in URL (one.example.com & other.example.com)
	- Query String. Headers (example.com/users?id=123&order=false)

- ALB are a great fit for micro services and container based applications (e.g. Docker & Amazon ECS)
	- It has port mapping feature which allows to redirect to a dynamic port in ECS

In comparison, we'd need multiple Classic Load Balancer per application
## Target Groups
EC2 instance (can be managed by an Auto Scaling Group) - HTTP
ECS Task (managed by ECS itself) - HTTP
Lambda functions - HTTP requests is translated into a JSON event
IP address's - must be private IP's

ALB can route to multiple target groups
Health checks are at the target groups level
## Good to Know
Fixed host name (xxx.region.elb.amazonaws.com)
The application IP don't see the IP of the client directly:
	- The true IP of the client is inserted in the header X-Forwarded-For
	- We can also get Port (X-Forwarded-For) and proto (X-Forwarded-Proto)

# Network Load Balancer
## Network Load Balancer (v2)
Network Load Balancer (Layer 4) allow to:
- Forward TCP & UDP traffic to your instances
- Handle millions of requests per second
- Ultra-low latency

NLB has one static IP per AZ, and supports assigning Elastic IP (helpful for whitelisting IP)
NLB are used to extreme performance, TCP and UDP traffic
##  Target Groups
- EC2 Instances
- IP Addresses - must be private IPs
- Application Load Balancer
- Health checks supports the TCP, HTTP, and HTTPS protocols
# Gateway Load Balancer
deploy, scale and manage, a fleet of 3rd Party network virtual appliances in AWS
e.g: firewalls, intrusion detection and prevention system, deep packet inspection systems, payload manipulation
Operated at Layer 3 (Network Layer) - IP Packets
Combines the following functions:
- Transparent network gateway - single entry/exit for all traffic
- Load Balancer - distributes traffic to your virtual appliances
Uses the GENEVE protocol on port 6081
## Target Groups:
- EC2 Instances
- IP Addresses - must be private IP's
## Sticky Session 
### Session Affinity
- It is possible to implement stickiness so that the same client is always redirected to the same instance behind a load balancer
- This works for Classic, Application, Network Load Balancer
- The "cookie" used for stickiness has an expiration date we control
- Use Case: Make sure user doesn't lose his session data
- Enabling Stickiness may bring imbalance to the load over the backend EC2 instance
### Cookie Names
- Application based cookie
	- Custom cookie
		- Generated by the client
		- Can include any custom attributes required by the application
		- Cookie name must be specified individually for each target group
		- Don't use AWSALB, AWSALBAPP, AWSAWBTG -> These are reserved for use by the ELB
	- Application cookie
		- Generated by the load balancer
		- Cookie name is AWSALBAPP
- Duration Based Cookies
	- Cookie generated by the load balancer
	- Cookie name is AWSALB for ALB, and AWSELB for CLB
# Cross-Zone Load Balancing
With Cross Load zone balancing: 
	Each load balancer instance distributes evenly across all registered instances in all AZ
Without:
	Requests are distributed in the instances of the node of the Elastic Load Balancer

- Application Load Balancer:
	- Enabled by default (can be disabled at the target group level)
	- No charges for inter AZ data
- Network Load Balancer
	- Disabled by default
	- You pay for charges ($) for inter AZ data if enabled
- Classic Load Balancer
	- Disabled y default
	- No charges for inter AZ data if enabled
# SSL/TLS - Basics
- An SSL certificate allows traffic between your clients and your load balancer to be encrypted in transit (in-flight encryption)
- SSL refers to Secure Sockets Layer, used to encrypt connections
- TLS refers to Transport Layer Security, which is newer version
- Nowadays, TLS certificates are mainly used, but people still refer it as SSL

Public SSL certificates are issued by Certificate Authorities(CA)

SSL certificates have an expiration date (you set), and must be renewed
## Load Balancer
The load balancer uses an X.509 certificate (SSL/TLS server certificate)
You can manage certificates using ACM (AWS Certificate Manager)
You can create upload your own certificates alternatively
HTTPS listener:
	You must specify a default certificate
	You can add an optional lists of certs to support multiple domains
	Clients use SNI (Server Name Indication) to specify the hostname they reach
	Ability to specify a security policy to support older versions of SSL/TLS (legacy clients)
## Server Name Indication (SNI)
SNI Solves the problem of loading multiple SSL certificates onto a web server(to serve multiple websites)
It's a newer protocol, and requires the client to indicate the host name of the target server in the initial SSL handshake
The server will then find the correct certificate, or return the default one
Note:
- Only works for ALB, NLB, CloudFront
- Does not work for CLB
## Elastic Load Balancer
1. Classic Load Balancer:
	1. Supports only one SSL certificate
	2. Must use multiple hostname with multiple SSL certificates
2. Application Load Balancer
	1. Supports multiple listeners with multiple SSL certificates
	2. Uses Server Name Indication (SNI) to make it work
3. Network Load Balancer:
	1. Supports multiple listeners with multiple SSL certificates
	2. Uses Server Name Indication (SNI) to make it work
## Connection Draining
Feature Naming 
	Connection Draining - for CLB
	Deregistration Delay - for ALB & NLB
	- time to complete "in-flight" requests while the instance is de-registering or unhealthy
	- stops sending new request to the EC2 instance which is de-registering
	- Value can be set between: 1 - 3600 seconds (default: 300 second)
	- Can be disabled if value set to 0
	- Set a low value if requests are short
## Auto Scaling Group
In real-life, the load on your website and application can change
In the cloud,  you can create and get rid of the servers very quickly
The goal of the ASG is:
- Scale out (add EC2 instances) to match an increased lead
- Scale in (remove EC2 instances) to match decreased load
- Ensure we have minimum and maximum number of EC2 instances running
- Automatically register new instances to load balancer
- Re-create an EC2 instance in case a previous one is terminated (e.g.: if unhealthy)
ASG is free (you only pay for the underlying EC2)
### Group Attributes
A launch Template (older "Launch Configurations" are depriciated)
- AMI + Instance data
- EC2 user data
- EBS Volumes
- Security groups
- SSH Key Pair
- IAM Roles for your EC2 Instances
- network + subnets information 
- Load balancer information
Min Size/ Max Size / Initial capacity
Scaling policies
### CloudWatch Alarms Scaling
It is possible to scale an ASG, based on cloudwatch alarms
An alarm monitors a metric (such as Average CPU, or a custom metric)
Metrics such as average CPU are computed based on overall ASG Instances
Based on the Alarm, we can create scale-in or scale-out properties
## Scaling Policies
1. Dynamic Scaling:
	1. Target Tracking Scaling
		1. Simple to setup
		2. E.g.: I want the average ASG CPU to stay around 40%
	2. Simple / Step Scaling
		1. When a cloud watch alarm is triggered (e.g. CPU > 70%), add 2 units
		2. When a cloud watch alarm is triggered (e.g. CPU < 40%), remove 1 unit
2. Scheduled Scaling:
	1. Anticipate scaling based on known usage patters
	2. E.g.: Increase max capacity to 10 at 5pm friday
3. Predictive Scaling: 
	1. Continuously forecast load schedule scaling ahead

Good Metrics to scale on :
CPUUtilization: Average CPU utilization across your instances
RequestCountPerTarget: to make sure number of requests per EC2 instances is stable
Average Network In / Out: if your application is network bound
Any custom metric, that is pushed using Cloudwatch
### Scaling Cooldowns
After a scaling activity happens, you are in the cooldown period (default 300 sec)
During the cooldown period, ASG, will not launch or terminate additional instances ( to allow metrics to stabalize)
Advice: Use a ready to use AMI to reduce configuration time in order to be serving requests faster and reduce this cooldown period