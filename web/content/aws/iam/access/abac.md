---
title: ABAC
draft: false
weight: 5
---

To more easily maange associations between identities and policies, IAM allows you to associate the two entities together via AWS tagging.

The following is an example policy that allows us to define a tagged policy:
```
{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": [
            "secretsmanager:CreateSecret",
            "secretsmanager:TagResource"
        ],
        "Resource": "*",
        "Condition": {
            "ForAllValues:StringEquals": {
                "aws:TagKeys": [
                    "environment",
                    "cost-center"
                ]
            }
        }
    }
```