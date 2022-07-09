---
title: Services
draft: false
weight: 5
---

AWS makes certain resources available through _services_, either via the API or the AWS console.

Regions offerings and pricing can differ between various regions. New service offergings tend to be rolled out to us-east-1 initially Because of this, us-east-1 also tends to be the most volatile of AWS regions.

An overview of AWS service classifications is provided below. You can also explore the full service offering/classification [here]( https://aws.amazon.com/products). [^1]

#### Compute

Compute services allow users to execute programs and applications, ranging from virtual servers to providing managed environments for executing code. AWS EC2 enables developers to provision virtual and private servers. AWS Lambda allows developers to execute code snippets in ephemeral environments without needing to provision or manage underlying infrastructure

#### Storage

AWS offers various storage offerings of the following types:
- Object Storage
- Block Storage
- File Storage

AWS S3 offers object storage where data can be uploaded to uniquely named data buckets with a unique key. Block storage is most similar 
to harddrive storage, and is offered via AWS EBS, which are mounted onto AWS EC2 instances. AWS EFS provides remote files storate via the NFTS protocol. 

#### Database

While databases can be provisioned by using both Compute and Storage services, AWS offers managed database services for easily standing up storage for development. They offer databases for the following stoarge use cases:
- Relational
- NoSQL
- Time Series
- Columnar

Relational databases can be provisioned via AWS RDS. AWS offers several NoSQL offerings, such as DynamoDB and Document storage. AWS timestream data can be useful for analyzing within a certain data range, such as IoT information. Redshift is AWS's data warehouse solution that provides columnar stoarge. 

#### Networking & Content Delivery

AWS allows users/cloud-engineers to define networking rules. VPC (virtual private cloud) allows users to define virtual private networks and subnets within a given IP range. AWS Cloudfront provides a managed CDN network for content delivery in different regions of the globe. Security groups and NACLs (Network Access Control Lists) can be used to define firewall rules to permit/deny traffic. Route53 can be used for DNS management.

#### Security, Identity, and Compliance

- IAM
- Cloudwatch
- CLoudtrail
- Security Advisor
- Billing?

#### Analytics

Athena,
Quicksight,
etc.

??? (Remove this)

#### Machine Learning

??? (Remove this)

[^1]: https://aws.amazon.com/products


