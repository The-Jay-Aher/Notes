# 1 - Getting Started with AWS

## AWS Global Infrastructure Basics

AWS infrastructure is organized into:

- **Regions:** Physical geographic areas (for example, `us-east-1`, `eu-west-1`).
- **Availability Zones (AZs):** One or more discrete data centers in a Region with independent power/networking.
- **Edge Locations:** Sites used by edge services (for example CloudFront) to cache and deliver content closer to users.
- **Local Zones (selected metros):** Extensions of Regions for low-latency workloads near end users.

## How to Choose an AWS Region

When selecting a Region, evaluate:

1. **Compliance and data residency**
   - Regulatory or legal requirements may require data to stay in specific countries/regions.
2. **Proximity to users**
   - Closer Region usually means lower latency and better user experience.
3. **Service availability**
   - Not all AWS services/features are available in every Region.
4. **Pricing**
   - Prices vary by Region for compute, storage, and data transfer.
5. **Disaster recovery strategy**
   - Multi-Region design improves resilience for critical workloads.

## Availability Zones (AZs)

### Key Points

- Each Region contains **multiple AZs**.
- Many Regions have 3 or more AZs, but this is not guaranteed as a universal minimum for every Region.
- AZs are physically separated to reduce correlated failure risk.
- AZs within a Region are connected through high-bandwidth, low-latency private networking.

### Why AZ Design Matters

Architecting across at least two AZs improves:

- **High availability** (application remains available during an AZ issue)
- **Fault tolerance** (failure in one AZ has reduced blast radius)
- **Operational resilience** (maintenance/failures are easier to absorb)

## Quick Example Architecture Pattern

A common starter production pattern:

1. Deploy application instances in at least two AZs.
2. Place an Application Load Balancer in front.
3. Use Auto Scaling groups to maintain healthy capacity.
4. Store persistent data in managed services with built-in durability options.

## Practical Starter Guidance

- Start in one Region close to your users.
- Use multiple AZs from day one for production workloads.
- Tag resources consistently (`Environment`, `Owner`, `Application`).
- Review pricing and service availability before committing to a Region.
