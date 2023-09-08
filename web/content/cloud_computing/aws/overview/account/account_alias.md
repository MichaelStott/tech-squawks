---
title: Account Alias
draft: false
weight: 2
---

Account aliases are public-facing, globally unique labels to simplify the console sign-in URL.

```
https://<account_alias>.signin.aws.amazon.com/console/
```

While the original sign-in URL `https://<account_id>.signin.aws.amazon.com/console/` remains active, the account alias may provide a more user-friendly identifier. A single account may have multiple account aliases associated with it. 

## CLI Overview

Account aliases are managed through the Identity and Access Management (IAM) service and may be provisioned, listed, and deleted using the AWS CLI.

**Example 1: Creating an Account Alias**

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws iam create-account-alias --account-alias techsquawks
```
{{% /tab %}}
{{< /tabs >}}

**Example 2: Listing Account Aliases**

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws iam list-account-aliases
```
**Output**
```
{
    "AccountAliases": [
        "techsquawks"
    ]
}
```
{{% /tab %}}
{{< /tabs >}}

**Example 3: Deleting an Account Alias**

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws iam delete-account-alias --account-alias techsquawks
```
{{% /tab %}}
{{< /tabs >}}