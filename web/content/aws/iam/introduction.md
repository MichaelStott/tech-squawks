---
title: Introduction
draft: false
weight: 1
---

_IAM_, which stands for _Identity Access Management_, is an AWS service used to manage API and web console access to cloud resources.

## Overview

When a user attempts to access an AWS resource through the API or web console, an HTTP request is sent to the endpoint for the target AWS service. After verifying the request signature, it is evaluated against all relevant IAM access policies, which dictate the allowed actions for the caller. If there exists at least one rule granting access and no explicit deny rule in any policies or permission boundaries, then the request is granted. Otherwise, it is rejected.

![IAM Access Flow](/images/iam/iam_flow.png)

## Features

IAM primarily handles all aspects of authentication and authorization when accessing cloud services.[^1] Authentication determines the validity of the identity of a user while authorization determines whether a given identity is permitted to perform a given action.

### Identity

Identity is an entity that enables access to an AWS account's cloud resources.[^1] IAM provides the following entities for managing identity information:
- _Users_: Represents an entity, typically a human user, that accesses AWS resources or services
- _Groups_: Manages access for a collection of AWS users.
- _Roles_: Temporarily assumed by an identity to perform a given set of actions.

### Access

Once the identity of the caller has been established, the next step is to determine whether they are authorized to perform the requested action. To accomplish this, IAM evaluates the identity against all relevant _policies_, which specifies the allowed and restricted actions for a given user. These IAM policies can be directly assigned to users or groups or through Attribute Access Control (ABAC), which associates a policy with an identity based on the identity's tags.[^2]

### Management

In addition to providing services to define identity information and access, IAM also provides services to ensure best practices are enforced regarding access. Some of this tooling includes analyzing user's access patterns to refine permissions, identifying unused permissions, and other auditing capabilities.

## Non-Features

IAM handles authentication and authorization when accessing resources via the AWS APIs. It is not intended for the following use-cases:

- Network Security: IAM does not evaluate non-AWS API traffic to AWS resources, such as network connections to public servers or databases.
- Application Identity Management: IAM is not intended to provide identity functionality for third-party applications and services, such as storing user credentials, and handling of login/account-reset flows.

[^1]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html
[^2]: https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html