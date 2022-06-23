---
title: Accounts
draft: false
weight: 1
---

An _AWS Account_ acts as a container for AWS cloud resources. It can be beneficial to create separate accounts to organize 
and isolate resources. For example, cloud engineers may create separate development, staging, and produciton accounts for their deployment pipeline. It is also not uncommon to create separate environments for different workload types, such as research developoment, consolidate billing, etc. In addition, accounts acts as a security boundary, as only users 
with valid account credentials to access cloud resources. [^1]

An AWS account has the following unique identifiers[^2]:
- _AWS Account Id_: 12 digit unique ID (i.e. _123456789012_)
- _Canonical User Id_: Obfuscated form of the account ID (i.e. _79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be_), used to identify an account when granting cross-account access to cloud resources.

The active account ID can be fetched from the Security Token Service (STS) with the following CLI command:
```sh
aws sts get-caller-identity --query Account --output text
```
The command `aws sts get-caller-identity` fetches the active user information leveraged by the CLI, which includes the user ID, the account ID, and the user access resource number (ARN). The `--query` flag allows to filter only the account ID field [^3]. `--output` specifies the desired format (yaml, josn, text, etc.) [^4] 

The simplest way to fetch the canonical ID is via the Simple Storage Service (S3) API CLI command.
```sh
aws s3api list-buckets --query Owner.ID --output text
```

[^1]: https://docs.aws.amazon.com/accounts/latest/reference/accounts-welcome.html
[^2]: https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html
[^3]: https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html
[^4]: https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html
