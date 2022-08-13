---
title: Introduction
draft: false
weight: 1
---

IAM, which stands for Identity Access Management, is an AWS service used to manage access to resources through the AWS API. As previously covered in the AWS overview, resource is a broad term that refers to any infrastructure or entity within AWS. It is used to manage user and service permissions and access within an AWS account.

## Access Overview

When a user or web service needs to access an AWS resource through the API, web console, or SDK, an HTTP request is sent to the endpoint for that AWS service. This request is then evaluated against all relevant IAM policies, which dictate the permissions for the caller. As long as there exists at least one permission granting access and no explicit deny effect in any policies or permission boundaries, then the request is granted. Otherwise, it is rejected.

![IAM Access Flow](/images/iam/iam_flow.png)

All AWS users, by default, have no default permissions associated upon creation. Thus, any permissions must be granted explicitly. The exception to this is the account root user, which has unlimited access.
