---
title: Caller Information
draft: false
weight: 2
---

In addition to fetching short term credentials, STS can be used to acquire information pertaining to the active caller or given access key.

## Caller Identity 

To fetch information pertaining to the credentials actively used in signing requests, STS provides GetCallerIdentityInfo endpoint. This endpoint returns the following information:[^1]
- UserId: The account unique ID of the caller associated with the credentials.
- Account: The globally unique 12-digit ID of the parent account
- Arn: The access resource number for the resource

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws sts get-caller-identity
```
**Output**
```
{
    "UserId": "AIDAYJG7SY44NDI7LOIES",
    "Account": "012345678910",
    "Arn": "arn:aws:iam::012345678910:user/username"
}
```
{{% /tab %}}
{{< /tabs >}}

## Access Key

For a given access key ID, it is possible to get the parent account ID of the credentials using the GetAccessKeyInfo endpoint.[^2]

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws sts get-access-key-info --access-key-id $AWS_ACCESS_KEY_ID
```
**Output**
```
{
    "Account": "012345678910"
}
```
{{% /tab %}}
{{< /tabs >}}

[^1]: https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html
[^2]: https://docs.aws.amazon.com/STS/latest/APIReference/API_GetAccessKeyInfo.html