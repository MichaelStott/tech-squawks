---
title: Regions and Availability Zones
draft: false
weight: 2
---

### Regions

An _AWS region_ is a geographic region that contains interconnected AWS data centers used for provisioning cloud resources. You can get a list of available regions for your AWS account by running the following commnad:

**CLI**
```sh
aws ec2 describe-regions --all-regions --query  Regions[*].RegionName
```
**Output**
```
[
    "af-south-1",
    "eu-north-1",
    "ap-south-1",
    ...
]
```

Each region is isolated from one another for additional fault tolerance and stability.[^1] Regions may also have 
different AWS services available. 

### Availability Zones

An _availabiilty zone_ (abreviated as _AZ_) is one or more discrete AWS data centers that have redundant connectivity, networking, and power within a given AWS region. AZs within a given region are interconnected through low-latency networking and resource/data replciation.[^2]. Applicaitons designed across multiple AZs have increased fault tolerance.[^2]

![Regions and Availability Zones](/images/aws/regions.png)

AZs are named with the following format "_\<region-name\>\<letter[a-z]\>_". This can be validated by enumerating th AZ options within a given region:.

**CLI**
```sh
aws ec2 describe-availability-zones --query AvailabilityZones[*].ZoneName --region us-east-2
```
**Output**
```
[
    "us-east-2a",
    "us-east-2b",
    "us-east-2c"
]
```

[^1]: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
[^2]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html