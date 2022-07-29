---
title: Services
draft: false
weight: 5
---

AWS makes cloud resources available through _services_, which are APIs available either through the _AWS console_, a webpage for AWS account access, or using programtic credentials. Individual AWS service offerings and pricings can differ between regions. For instance, new service offergings tend to be rolled out in the `us-east-1` region initially, and gradually made available to other regions after a period of time.

AWS provides many different service classifications for use cases, such as machine learning, analytics, quantum computing, and many more.[^1] We will explore some of the more common services here.

#### Compute

Compute services enables users to run and host programs and applications. _AWS EC2_ enables cloud engineers to provision virtual and private servers for hosting applications. _AWS Lambda_ allows developers to execute code snippets in ephemeral environments without needing to provision or manage underlying compute infrastructure, which can be useful for executing arbitrary code or scripts in cloud environments. [^2]

#### Storage

AWS offers various storage offerings of the following types[^3]:
- Object Storage: Stores objects, composed of data and user metadata, with an associate unique identifier.
- Block Storage: Data is stored within a block of memory, similar to hard disk storage.
- File Storage: Storage provided via a file system.

AWS S3 offers object storage where data can be uploaded to uniquely named data buckets with a unique key. Block storage is most similar 
to harddrive storage, and is offered via AWS EBS, which are mounted onto AWS EC2 instances. AWS EFS provides remote files storate via the NFSv4 protocol. 

#### Database

While databases can be provisioned by using both Compute and Storage services, AWS offers managed database services for easily standing up storage for development. They offer databases for the following stoarge use cases:
- Relational - Tabular row data, similar to data stored in spreadsheets. Data typically well-defined.
- NoSQL - Data stored in documents (key-value pairs) that may not necessarily have a well-defined schema.
- Time Series - Data is indexed in such a manner so that is easy to query and analyze within a given date range.
- Columnar - Similar to relational databases, columnar stores tabular data by column rather than row. While computationally more expensive, this can enable fast querying of large datasets.

Relational databases can be provisioned via AWS RDS. AWS offers several NoSQL offerings, such as DynamoDB and Document storage. AWS timestream data can be useful for analyzing within a certain data range, such as IoT information. Redshift is AWS's data warehouse solution that provides columnar stoarge. 

#### Networking & Content Delivery

AWS allows users/cloud-engineers to define networking rules. VPC (virtual private cloud) allows users to define virtual private networks and subnets within a given IP range. AWS Cloudfront provides a managed CDN network for content delivery in different regions of the globe. Security groups and NACLs (Network Access Control Lists) can be used to define firewall rules to permit/deny traffic. Route53 can be used for DNS management.

#### Security, Identity, and Compliance

AWS offers multiple services to help ensure both the customer's cloud account and hosted applications are secure.

- IAM: Ensures authorized access to cloud resources.
- Cloudwatch: Provides application and service logging.
- CLoudtrail: Logging of cloud account activities.
- Security Advisor: Analyzes cloud configuration for potential threats.

[^1]: https://aws.amazon.com/products
[^2]: https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html
[^3]: https://www.ibm.com/cloud/learn/block-storage


