---
menuTitle: LocalStack
chapter: false
weight: 3
---

 ![LocalStack Logo](https://localstack.cloud/images/header-logo.svg)


While it is preferrable to develop and test applications against actual cloud resources when possible, 
not all readers may have AWS access or be able to set up a private account. Additionally, there is always the 
risk of leaving cloud resources provisioned, which may result in unintended charges.
To make these tutorials as accessible and cost-effective as possible, examples in these tutorials leverage the free-tier version 
of [LocalStack](https://localstack.cloud/) whenever possible.  

LocalStack is able to emulate an AWS cloud environment on the user's development machine, making it useful 
for both development and testing. Examples that work and function with the free-tier version of LocalStack 
will be appropriately marked.

## Dependencies

LocalStack requires the following be installed on the user's local machine to function properly.
- Python & PIP
- Docker Desktop

Navigate to the [Python](https://www.python.org/downloads/) and [Docker Desktop](https://www.docker.com/get-started) installation page for platform-specific setup instruction.

### LocalStack CLI

LocalStack offers a CLI for provisioning an AWS test environment. To install it, execute the following.

```sh
pip3 install localstack
```

### AWS CLI Configuration

### Pulumi Configuration
