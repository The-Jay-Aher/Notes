# 5 - EC2 Instance Storage

## EBS Overview

An EBS (Elastic Block Storage) Volume is a _network_ drive that you can attach to your instances while they run
It allows your instances to persist data even after their termination
They can only be mounted to one instance at a time (at the CCP level)
They are bound to a specific availability zone
Analogy: THink of it like a "network usb stick"

### EBS Volume

It's a network drive (i.e. Not a network Drive)
It uses network to communicate the instance, which means there might be a bit of latency
It can be detached from an EC2 instance and attached to another one quickly

It's locked to an Availability Zone (AZ)
An EBS Volume in us-east-1a cannot be attached to us-east-1b
To move the volume across, you first need to snapshot it

Have a provisioned capacity (size in GBs, and IOPS)
You can get billed for all the provisioned capacity
YOu can increase the capacity of the drive overtime

### EBS - delete on termination attribute

controls the ebs behaviour when ec2 instance terminates
by default, the root ebs volume is deleted (attribute enabled)
by default, any other attached ebs volume is not deleted (attribute disabled)

this can be controlled by aws cli / aws console
use case: preserve root volume when instance has been terminated

## EBS Snapshot

make a backup (snapshot) of your ebs volume at a point in time
not necessary to detach volume to do a snapshot, but recommended
can copy snapshots across AZ or region

### ebs snapshot features

ebs snapshot archive
move a snapshot to an "archive tier" that is 75% cheaper
takes within 24 to 72 hours for restoring the archive

recycle bin for ebs snapshots
setup rules for ebs snapshots so you can recover them after an accidental deletion
Specify retention (1 day to 1 year)

fast snapshot restore (fsr)
force full initialization of snapshot to have no latency on first use ($$$)

## AMI Overview

AMI = Amazon machine image
ami are customization of an ec2 instance
  you can add your own software, configuration, operating system, monitoring...
  faster boot / configuration time because all your software is pre-packaged
ami are built for a specific region (and can be copied across regions)
you can launch ec2 instance from:
  a public ami: aws provided
  your own ami: you make and maintain them yourself
  an aws marketplace ami: an ami someone makes (and someone sells) 

### AMI Process (from an Ec2 instance)

start and ec2 instance and customize it
stop the instance (for data integrity)
build an ami - this will also create ebs snapshots
launch instances from other amis   
