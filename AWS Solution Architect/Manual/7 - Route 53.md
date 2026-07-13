[]()# What is a DNS?
## What is DNS?
Domain name system which translates the human friendly host names into machine name IP addresses
www.google.com -> 172.217.18.36
DNS is the backbone of the internet
DNS uses hierarchical naming structure
- .com
- example.com
- www.example.com
- api.example.com
## DNS Terminologies
Domain Registrar: Amazon Route 63, GO Daddy, ...
DNS Records: A, AAAA, CNAME, NS, ....
Zone file: contains DNS records
Name server: resolved DNS queries (Authorative or Non-Authoritative)
Top Level Domain (TLD): .com, .us, .in, .gov, .org, ...
Second Level domain (SLD): amazon.com, google.com

http://api.www.example.com.
. (Last one) -> Root
.com -> TLD
.example -> SLD
.www -> Sub domain
api. -> Fully Qualified Domain Name (FQDN)
http:// -> protocol
# Route 53  overview
## Amazon Route 53
A highly available, scaleless, fully maintained and authoritative DNS
- Authoritative = the customer (you) can update DNS records
Route 53 is also a Domain Registrar
Ability to check the health of your resources
The only AWS services which provide 100% availability SLA
Why Route 53? 53 is a reference to traditional DNS port
## Route 63 - Records
How you want to route traffic for a domain
Each record contains:
- Domain/subdomain Name: e.g., example.com
- Record Type: A or AAAA
- Value: 12.34.56.78
- Routing Value: how Route 53 responds to queries
- TTL: amount of time the record cached at DNS Resolvers
Route 53 supports the following DNS record types:
- (must know) A/AAAA/CNAME/NS
- (advanced) CAA/DS/MX/NAPTR/PTR/SOA/TXT/SPF/SRV
## Route 52 - Record Type
1. A: maps hostname to IPv4
2. AAAA: maps hostname to IPv6
3. CNAME: maps a hostname to another hostname
	1. The target is a domain name which must have an A or AAAA record
	2. Can't create a CNAME record for the top node of a DNS namespace (Zone Apex)
	3. Example: you can't create for example.com, but you can create for www.example.com
4. NS - Name Server for the Hosted Zone
	1. Control how traffic is routed for a domain
## Route 53 - Hosted Zones
A container for records that define how to route traffic to a domain and it's subdomain

Public Hosted Zones: contains records that specify how to route traffic on the internet (public domain names)
	applicationI.mypublicdomain.com

Private Hosted Zones: contains records that specify how to route traffic within one or more VPC's (private domain names)
	applicationI.company.internal

You pay $0..50 per month per hosted zone
# Route 53 - TTL (Time to Live)
High TTL - e.g. 24hr
- Less traffic on Route 53
- Probably outdated records
Low TTL - e.g., 60 sec
 - More traffic on Route 53
 - Records are outdated for less time
 - EAsy to change records