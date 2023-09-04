---
title: Roles
draft: false
weight: 3
---

## Roles

Similar to users, roles are IAM identities intended to grant access to AWS resources. However, unlike users, roles lack any long-lived credentials such as console passwords and access key pairs. Rather, they are assumed by other authorized identities temporarily to obtain a certain level of access. [^1] Once assumed, the user is given temporary short-lived credentials via the AWS STS service, which are associated with the role permissions.

In addition to authorizing other human users to perform certain actions, roles may also be associated with AWS services to perform certain API calls. These are known as _service-linked roles_. [^2] 

## Use Cases [^3]

- _Provide access across multiple AWS accounts_: Enables users to have certain role-defined access for a given account.
- _Provide access for non-AWS workloads_: Third-party applications may assume the role to assume access to AWS resources.
- _Provide access to third-party AWS accounts_: Allows other organizations with AWS users and services to access your account as permitted by a given role.
- _Provide access through identity federation_: Enables organizations to leverage their existing user information and define role mappings for given groups.

[^1]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html
[^2]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html
[^3]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios.html