---
title: Users
draft: false
weight: 1
---

## Users

IAM _users_ represent a human user or programmatic workload and provides access to AWS resources or services. Users belong to a single parent account and consists of the following properties and credentials:

- Access Credentials: Programmatic long-lived credentials consisting of an access key ID and secret key.
- Path: The IAM namespace which contains the user.
- Login Profile: AWS web console credentials.
- MFA Device: MFA devices required for accessing AWS resources, whether through the web console or programmatically.
- SSL Certificates: May be used to authenticate with certain AWS services.
- SSH Keys: SSH public keys to be used with AWS Codecommit, a git repository service, during application development.

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws iam get-user --user-name $USERNAME
```
**Output**
```
{
    "User": {
        "Path": "/",
        "UserName": "username",
        "UserId": "ADSAYFF72444NEI6MNIOP",
        "Arn": "arn:aws:iam::012345678910:user/username",
        "CreateDate": "2019-07-10T23:13:11+00:00",
        "Tags": [
            {
                "Key": "TagName",
                "Value": "TagValue"
            }
        ]
    }
}
```
{{% /tab %}}
{{< /tabs >}}

Upon creating a new AWS account, a _root user_ is automatically created, which has complete access to all cloud resources with limited exceptions. For this reason, it is recommended that you create an administrator user for everyday use and restrict access to root user credentials.

## Console Login Process

There are two possible login flows depending on the type of user attempting to sign in.[^1]

### Root User

To sign in as a root user, simply navigate to the [sign-in page](https://signin.aws.amazon.com/console), select "Root User", and enter the root user credentials and optional MFA code.

### IAM User

To sign in to the AWS console as a non-root user, you can either use standard sign-in webpage and provide the target AWS account number or specify the account alias in the URL as such: https://<account_id_or_alias>.signin.aws.amazon.com/console/.

<!-- ## Federated Access

It is considered best practice for organizations to manage user information through some corporate root directory, such as an IDP, and integrate this directory with AWS IAM. This makes centrally managing authorized users easier and make certain tasks such as offboarding much easier.

Some protocols that are supported:
- SAML2
- OIDC -->

<!-- ## Password Management

For instances where the password information is managed by AWS IAM, passwords can be managed via the IAM API, most readily by the CLI or web console.

```sh
# Check if login profile exists for target user
$ aws iam get-login-profile --user-name $IAM_USERNAME
# Create new login profile for target user
$ aws iam create-login-profile --user-name $IAM_USERNAME
# Update existing login profile of target user
$ aws iam update-login-profile --user-name $IAM_USERNAME
# Delete existing login profile of target user
$ aws iam delete-login-profile --user-name $IAM_USERNAME
``` -->

[^1]: https://aws.amazon.com/premiumsupport/knowledge-center/sign-in-console/