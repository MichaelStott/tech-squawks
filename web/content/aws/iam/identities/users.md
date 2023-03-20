---
title: Users
draft: false
weight: 3
---

## Users

IAM users represent a human user or programatic workload that access AWS resources or services. IAM users belong to a single parent account and may contain the following properties and credentials:

- Username/Password
- Email
- Access Keypair
- MFA Device
- SSL Certificates
- SSH Keys for Code Commit
- Service Accounts (Define these)

Upon creating a new AWS account, a new root user is created. This user has complete access to all cloud resourdces with limited exceptions. For this reason, it is reccomended that you create an aministrator user for everyday use and restrict access to root user credentials.

## Console Login Process

There are two possible login flows depending the tpe of user attempting to sign in.[^1]

### Root User

To sign in as a root user, simply navigate to the [sign in page](https://signin.aws.amazon.com/console), select "Root User", and enter the root user credentials.

### IAM (non-root) User

To sign into the AWS console as a non-root user, you can either use standard sign-in webpage and provide the target AWS account number or specify the account alias in the URL as such: https://account_alias_or_id.signin.aws.amazon.com/console/.

## Federated Access

It is considered best practice for organizations to manage user information through some coprorate root directory, such as an IDP, and integrate this directory with AWS IAM. This makes centrally managing authorized users easier and make certains tasks such as offboarding much easier.

Some protocols that are supported:
- SAML2
- OIDC

## Password Management

For isntances where the password information is managed by AWS IAM, passwords can be maanged via the IAM API, most readily by the CLI or web console.

```sh
# Check if login profile exists for target user
$ aws iam get-login-profile --user-name $IAM_USERNAME
# Create new login profile for target user
$ aws iam create-login-profile --user-name $IAM_USERNAME
# Update existing login profile of target user
$ aws iam update-login-profile --user-name $IAM_USERNAME
# Delete existing login profile of target user
$ aws iam delete-login-profile --user-name $IAM_USERNAME
```

[^1]: https://aws.amazon.com/premiumsupport/knowledge-center/sign-in-console/