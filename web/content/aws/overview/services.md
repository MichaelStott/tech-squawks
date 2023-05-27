---
title: Services
draft: false
weight: 5
---

AWS cloud resources are available through _services_, APIs accessible through the _AWS console_ or programtically. As an introduction, common service categories and offerings are briefly explored here.

{{% notice info %}}
Service offerings and pricing may differ between regions. This should be taken into account when designing cloud applications. A complete listing of AWS services by region is available [here](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)
{{% /notice %}}

#### Compute

_Compute services_ enable users to run and host programs and applications. 

| Name | Logo | Description |
| ------:|:------:|:----------- |
| EC2 | {{< figure src="/images/aws/ec2_logo.png" width="48">}} | Elastic Cloud Compute. Provisioning and managing of virtual and private physical servers |
| Lambda |  {{< figure src="/images/aws/lambda_logo.png" width="48">}} | Code execution in ephemeral environments without need for provisioning/managing underlying infrastructure |
| ECS |  {{< figure src="/images/aws/ecs_logo.png" width="48">}} | Elastic Container Service. Executing containerized applications in the cloud |
| EKS |  {{< figure src="/images/aws/eks_logo.png" width="48">}} | Elastic Kubernetes Service. Managed Kubernetes clusters |

#### Storage

AWS offers various storage offerings of the following types[^3]:
- Object Storage: Stores objects, composed of data and user metadata, with an associate unique identifier.
- Block Storage: Data is stored within a block of memory, similar to hard disk storage.
- File Storage: Storage provided via a file system.

| Name | Logo | Description |
| ------:|:------:|:----------- |
| S3 | {{< figure src="/images/aws/s3_logo.png" width="48">}} | Simple Storage Service. Object storage where data can be uploaded to uniquely named data buckets under a unique key  |
| EBS|  {{< figure src="/images/aws/ebs_logo.png" width="48">}} | Elastic Block Storage. Provides SSD and HDD block storage for EC2 servers |
| EFS |  {{< figure src="/images/aws/efs_logo.png" width="48">}} | Elastic File Storage. Serverless remote storage via the NFSv4 protocol |

#### Database

While databases can be configured by leveraging both compute and storage services, AWS offers managed database solutions to facilitate proviioning, managing, and monitoring such systems. These offerings include the following database types:
- Caches - Intended to store frequently accessed values for increased performance.
- Relational - Tabular row data, similar to data stored in spreadsheets. Data typically well-defined.
- NoSQL - Data stored in documents (key-value pairs) that may not necessarily have a well-defined schema.
- Time Series - Data is indexed in such a manner so that is easy to query and analyze within a given date range.
- Columnar - Similar to relational databases, columnar stores tabular data by column rather than row. While computationally more expensive, this can enable fast querying of large datasets.

| Name | Logo | Description |
| ------:|:------:|:----------- |
| Elasticache | {{< figure src="/images/aws/elasticache_logo.png" width="32">}} | Managed caching services |
| RDS | {{< figure src="/images/aws/rds_logo.png" width="32">}} | Relational Database Service |
| DynamoDB| {{< figure src="/images/aws/dynamodb_logo.png" width="32">}} | Document-based storage |
| DocumentDB | {{< figure src="/images/aws/documentdb_logo.png" width="32">}} | MonoDB-esque NoSQL database |
| Timestream | {{< figure src="/images/aws/timestream_logo.png" width="32">}} | Enables querying for data within a certain date range. |
| Redshift | {{< figure src="/images/aws/redshift_logo.png" width="32">}} | Data warehouse solution that provides columnar stoarge |

#### Networking & Content Delivery

AWS allows users/cloud-engineers to define networking rules. 

| Name | Logo | Description |
| ------:|:------:|:----------- |
| VPC | {{< figure src="/images/aws/vpc_logo.png" width="32">}} | Define virtual private networks within a given IP range |
| Cloudfront|  {{< figure src="/images/aws/cloudfront_logo.png" width="32">}} | Managed CDN network for content delivery in different regions of the globe |
| Route53 |  {{< figure src="/images/aws/route53_logo.png" width="32">}} | Amazon's DNS service |

#### Security, Identity, and Compliance

AWS offers multiple services for securing access to both AWS account resources and customer hosted applications.

| Name | Logo | Description |
| ------:|:------:|:----------- |
| IAM | {{< figure src="/images/aws/iam_logo.png" width="32">}} | Ensures authorized access to AWS cloud resources |
| Cognito | {{< figure src="/images/aws/cognito_logo.png" width="32">}} | Provides identity and login managmenet for cloud applications |
| Secret Manager | {{< figure src="/images/aws/secretmanager_logo.png" width="32">}} | Manages storage and access of private application values |

## Management and Governance

Services responsible for providing visibility into finacial, application, and user activity. 

| Name | Logo | Description |
| ------:|:------:|:----------- |
| Cloudwatch|  {{< figure src="/images/aws/cloudfront_logo.png" width="32">}} | Provides application and service logging |
| Cloudtrail |  {{< figure src="/images/aws/route53_logo.png" width="32">}} | Audit trail of cloud account activities |

[^1]: https://aws.amazon.com/products
[^2]: https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html
[^3]: https://www.ibm.com/cloud/learn/block-storage


