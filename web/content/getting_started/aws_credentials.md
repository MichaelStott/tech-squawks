---
title: AWS Account Credentials
chapter: false
weight: 3
---

In order to provision and modify cloud resources using the AWS SDK and CLI from our local development environment, we need to 
generate and download credentials from AWS's IAM console. IAM, which stands for Identity Access Management, is a service provided 
by AWS to manage access to cloud resources. IAM is covered in greater detail in the next section, but we will need to leverage it 
here to generate the initial account credentials.

### Instructions 

1. Log onto your AWS account which was set up in the previous section.

2. Generate an access key and secret access key.

3. Download and save the credentials to the `.aws` folder.

{{% notice warning %}}
You must download and save the credentials upon generation. Otherwise, the credentials will be lost forever and you will need to 
generate a new access key and secret access key.
{{% /notice %}}