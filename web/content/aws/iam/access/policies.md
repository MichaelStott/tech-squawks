---
title: Policies
draft: false
weight: 4
---

IAM Policies define the permissions required for performing a given action on some target resource. A permission directly correlates to an AWS API request. Policies are associated with identities and allow cloud engineers to target specific resources. (UGHHH)

For common use cases, AWS provides managed resources to be assocaited with identities (Admin roles, S3 only roles, etc.), which may help reduce the amount of custom resources that an organization needs to manage.

## Permission Boundaries 

Permission boundaries define the maximum amount of permissions an identity can have. The effective permissions for an identity are the permissions that are granted by all the policies that affect the user or role, including identity-based policies, resource-based policies and permissions boundaries.

## Validation

IAM policies schemas may be validated using the IAM policy analyzer:

```
$ aws accessanalyzer validate-policy
```