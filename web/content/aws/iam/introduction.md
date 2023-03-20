---
title: Introduction
draft: false
weight: 1
---

IAM, which stands for Identity Access Management, is an AWS service used to manage API and console access to cloud resources.

## Overview

When a user or web service needs to access an AWS resource through the API, web console, or SDK, an HTTP request is sent to the endpoint for that AWS service. This request is then evaluated against all relevant IAM policies, which dictate the permissions for the caller. As long as there exists at least one permission granting access and no explicit deny effect in any policies or permission boundaries, then the request is granted. Otherwise, it is rejected.

![IAM Access Flow](/images/iam/iam_flow.png)

All AWS users, by default, have no default permissions associated upon creation. Thus, any permissions must be granted explicitly. The exception to this is the account root user, which has unlimited access.

## Features

IAM primarily handles all aspects of authentication and authorization when accessing cloud services. Authentication is determining the validity of the identity of a user and authorization determines whether a given identity is allowed to perform a given action.

### Authentication

Authentication verifies the idenitty of the caller. To accomplish this, IAM provides user and group entities for managing user identity information. Users, which typically define human users, groups, which can manage permissions for a group of users, and roles, which can be assumed by a caller to perform a given set of actions.

### Authorization

Once the identity of the caller has been verified, the next step is to determine whether they are authorized to perform the requested action. To accomplish this, IAM checks identitiy permissions against policies, which determine the allowed and restricted actions for a given user. Additionally, IAM also provides Attribute Access Control (ABAC), which allows or denies a given action based on the tags associated with a given caller.

## Non-Features

IAM handles authentication and authorization when accessing resources via the AWS APIs. It is not intended for the following use-cases:

- Network Security: IAM does not evaluate non-AWS API traffic to AWS resources, including servers, databases, or other resources. Network security 
- Application Identity Management: IAM is not intended to provide identity functionality for third-party applications and services, such as storing user credentials, handling login flows, password resets, etc. For such use cases, AWS Cognito would be a vastly better git.