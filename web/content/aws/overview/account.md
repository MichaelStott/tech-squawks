---
title: Accounts
draft: false
weight: 1
---

After initially signing up for AWS, a default _root account_ is created. AWS _accounts_ function as containers for organizing and isolating cloud resources. For example, deployment environments, such as development, staging, and production, often utilize distinct AWS accounts. In addition, accounts act as a security boundary, ensuring only authorized users can access particular cloud resources. [^1]

![Regions and Availability Zones](/images/aws/aws_accounts.png)

An AWS account has the following unique identifiers[^2]:
- _AWS Account Id_: 12 digit unique ID (i.e. _123456789012_)
- _Canonical User Id_: Obfuscated form of the account ID (i.e. _79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be_), used to identify an account when granting cross-account access to cloud resources.

The active account ID can be fetched from the Security Token Service (STS) with the following CLI command:
{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws sts get-caller-identity --query Account --output text
```
**Output**
```
123456789012
```
{{% /tab %}}
{{< /tabs >}}

The command `aws sts get-caller-identity` fetches the active user information leveraged by the CLI, which includes the user ID, the account ID, and the user access resource number (ARN). The `--query` flag enables users to target a particular field to output in the response and `--output` specifies the desired format (yaml, josn, text, etc.) [^3] [^4] 

The simplest way to fetch the canonical ID is via the Simple Storage Service (S3) API CLI command.
{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws s3api list-buckets --query Owner.ID --output text
```
**Output**
```
79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be
```
{{% /tab %}}
{{< /tabs >}}

[^1]: https://docs.aws.amazon.com/accounts/latest/reference/accounts-welcome.html
[^2]: https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html
[^3]: https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html
[^4]: https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html
