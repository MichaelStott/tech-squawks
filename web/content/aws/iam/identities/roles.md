---
title: Roles
draft: false
weight: 5
---

## Roles

Similar to users, roles are IAM identities intended to grant access to AWS resources. However, unlike users, roles lack any long-lived credentials such as console passwords and access key pairs. Rather, they are assumed by other authorized identities temporarily to obtain a certain level of access. For instance:

- An IAM users in the same AWS account can assume an IAM role
- An IAM user in a separate account can assume a role
- An AWS web service (Such as AWS EC2 servers) can assume roles
- Users that are authenticated via some third-party IDP.

Once assumed, roles produce temporary short-lived credentials via the AWS STS service.

[Diagram]

## Use Cases

Roles can be leveraged for:
- Federated Access
- Granting managed services access
- Granting temporary access to certain users or third-parties for sensitive accounts

## Examples

### Creating a Role

```ts
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const testRole = new aws.iam.Role("testRole", {
    assumeRolePolicy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Action: "sts:AssumeRole",
            Effect: "Allow",
            Sid: "",
            Principal: {
                Service: "ec2.amazonaws.com",
            },
        }],
    }),
    tags: {
        "tag-key": "tag-value",
    },
});
```
