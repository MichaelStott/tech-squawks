---
menuTitle: LocalStack
chapter: false
weight: 3
---

 ![LocalStack Logo](https://localstack.cloud/images/header-logo.svg)


While it is preferrable to develop and test applications against actual cloud resources when possible, 
not everyone may have AWS access or be able to set up a private account. Additionally, there is always the 
risk of leaving cloud resources uneccesarily provisioned, which may result unecessary additional costs.
To make these tutorials as accessible as possible, examples in these tutorials leverage the free-tier version 
of LocalStack whenever possible.  

LocalStack is able to simulate an AWS cloud environment on the user's development machine, making it useful 
for both development and testing. Examples that work and function with the free-tier version of LocalStack 
will be appropriately marked.

## Dependencies

LocalStack requires the following be installed on the user's local machine
- Python & PIP
- Docker

Navigate to the Python and Docker installation page for platform-specific setup instruction.

### LocalStack CLI

LocalStack offers a CLI for provisioning an AWS test environment. To install it, execute the following.

```sh
pip3 install localstack
```

### AWS CLI Configuration

### Pulumi Configuration
