---
title: Groups
draft: false
weight: 4
---

## Groups

IAM groups are non-nested structures which contain multiple IAM users. Users can belong to multiple users.

[Diagram]

Groups can be useful for managing the permissions and access of multiple users in bulk.

## Examples

### Creating a Group

```ts
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const developers = new aws.iam.Group("developers", {path: "/users/"});
```