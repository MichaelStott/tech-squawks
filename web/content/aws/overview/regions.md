---
title: Regions and Availability Zones
draft: false
weight: 2
---

### Regions

An _AWS region_ is a geographic area that contains interconnected AWS data centers used for provisioning cloud resources. Available regions can be listed with the following CLI command:

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
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
{{% /tab %}}
{{< /tabs >}}

Regions are isolated from one another for additional fault tolerance and stability.[^1] AWS cloud service offerings
may differ between regions. Therefore, cloud engineers should verify that any required cloud services are available in the desired regions before beginning development.

### Availability Zones

An _availabiilty zone_ (commonly abreviated as _AZ_) is one or more discrete AWS data centers that have redundant connectivity, networking, and power within a given AWS region. AZs are interconnected through low-latency networking and resource/data replciation.[^2]. It is considered best practice to deploy cloud applications across multiple AZs for increased fault tolerance, in the event that one or more AZs experience technical outages.[^2]

![Regions and Availability Zones](/images/aws/regions.png)

AZ names are of the following format "_\<region-name\>\<letter[a-z]\>_". For example:.
{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
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
{{% /tab %}}
{{< /tabs >}}

[^1]: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
[^2]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html