---
title: Overview
draft: true
weight: 1
---

AWS enables customers to provision cloud infrastructure via its public-facing REST API endpoints. To access these APIs however, developers must first procure valid credentials. _Secure Token Service_, abbreviated _STS_, can be used to fetch short-lived AWS tokens for this purpose. Such credentials consist of the following properties:

- Access Key ID: Unique identifier for provided credentials
- Secret Access Key: Used for signing API requests
- Session Token: Used to authenticate the API request
- Expiration Time: Date when credentials are no longer valid

```sh
$ aws sts get-session-token

{
    "Credentials": {
        "AccessKeyId": "ASIAYGH7AT44NA7VMLAO",
        "SecretAccessKey": "0zaJykOHUUQV2lalUAgoXcNoXZ2OKfxau//tAck+",
        "SessionToken": "SESSION_TOKEN_VALUE",
        "Expiration": "2022-09-19T08:42:24+00:00"
    }
}
```

[//]: # (This should be moved to the AWS account overview)

## Global and Regional Endpoints

STS is a global service, meaning the API is available in all AWS regions. The default global endpoint, https://sts.amazonaws.com, is hosted in `us-east-1`. However, AWS recommends leveraging region-specific API endpoints when possible for the following reasons:

- Lower STS response latency
- Adds redundancy should certain STS endpoints become available
- Increase token validity

For example, while it is possible to request `eu-central-1`-scoped credentials from the global STS endpoint, services hosted in `eu-central-1` should target https://sts.eu-central-1.amazonaws.com for deacreased latency. The following two STS commands were executed on an AWS server instance hosted in `eu-central-1` to further illustrate this:

```sh
$ export TIMEFORMAT=%R
$ time aws sts get-session-token  --region eu-central-1
...
0.834
$ time aws sts get-session-token  --region eu-central-1 --endpoint-url https://sts.eu-central-1.amazonaws.com
...
0.469
```

Repeated calls from the `eu-central-1` server demonstrate this latency decrease consistently:

![STS Endpoint Latency](/images/sts/sts_endpoint_latency.png)

{{% notice info %}}
Generally, global AWS services have corresponding regional endpoints to reduce latency. Developers should ensure their 
applications target the appropriate regional endpoint when possible.
{{% /notice %}}

## SDK and CLI Integration

While cloud developers may manually fetch STS credentials to sign and perform AWS API calls, the provided CLI and SDK tools automatically manage calls to STS in the background. Developers should only consider using the STS endpoints and direct API calls to AWS should only be used when developing in languages that are not supported by AWS or when fine-grain control over AWS API calls is required. See here for a list of supported languages. (https://aws.amazon.com/developer/tools/) 

The AWS CLI and SDK will typically look for credentials in the following order:
- Credentials provided to the SDK or CLI invocation
- From available environment variables (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY)
- The .aws/config and  .aws/credentials folder: AWS will use the credentials found in the credentials file. Similarly, it will request the STS role for a given profile.

The easiest way to use STS credentials with CLI calls is simply to set the environment variables as such:

```sh
$ export AWS_ACCESS_KEY_ID=”STS_PROVIDED_ACCESS_KEY_ID”
$ export AWS_SECRET_ACCESS_KEY=”STS_PROVIDED_SECRET_ACCESS_KEY”
$ aws sts get-caller-identity
```
