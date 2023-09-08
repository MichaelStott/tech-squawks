---
title: Password Policy
draft: false
weight: 3
---

Accounts may optionally be associated with a single password policy which dictates the minimum password complexity for account users, to avoid potentially weak password. Password policies consist of the following components[^1]: 

- _AllowUsersToChangePassword_: Boolean allowing users to change their own passwords from the AWS console. (Default value: false)
- _HardExpiry_: Boolean indicating that users will be unable to reset their password via the AWS Console after their current password has expired. (Default value: false)
- _MaxPasswordAge_: The number of days that a password is valid for, no less than 0 but not exceeding 1095 (with 0 indicating that the password never expires). (Default value: 0)
- _MinimumPasswordLength_: The minimum number of password characters, no less than 6 but not exceeding 128. (Default value: 6)
- _PasswordReusePrevention_: The number of previous passwords that account users are prevented from reusing.
- _RequireLowercaseCharacters_: Boolean indicating that passwords must contain at least one lowercase character from the ISO basic Latin alphabet (a to z). (Default value: false)
- _RequireNumbers_: Boolean indicating that passwords must contain at least one numeric character (0 to 9). (Default value: false)
- _RequireSymbols_: Boolean indicating passwords must contain at least one of the following non-alphanumeric characters: `! @ # $ % ^ & * ( ) _ + - = [ ] { } | '` (Default value: false)
- _RequireUppercaseCharacters_: Boolean indicating passwords must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z). (Default value: false)

## CLI Overview

**Example 1: Creating/Updating Password Policy**

See [here](https://docs.aws.amazon.com/cli/latest/reference/iam/update-account-password-policy.html) for additional CLI arguments. Fields not specified in the arguments are set to their default values.

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws iam update-account-password-policy
```
{{% /tab %}}
{{< /tabs >}}

**Example 2: Fetch Account Password Policy**

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws iam get-account-password-policy
```
**Output**
```
{
    "PasswordPolicy": {
        "MinimumPasswordLength": 6,
        "RequireSymbols": false,
        "RequireNumbers": false,
        "RequireUppercaseCharacters": false,
        "RequireLowercaseCharacters": false,
        "AllowUsersToChangePassword": false,
        "ExpirePasswords": false
    }
}
```
{{% /tab %}}
{{< /tabs >}}

**Example 3: Deleting Account Password Policy**

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws iam delete-account-password-policy
```
{{% /tab %}}
{{< /tabs >}}

[^1]:https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAccountPasswordPolicy.html