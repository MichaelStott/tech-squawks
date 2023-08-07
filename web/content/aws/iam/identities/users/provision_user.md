---
title: Provision Users
draft: false
weight: 2
---

To provision an IAM user, the only required property is the username, which is unique within the AWS account.

{{< tabs groupId="code" >}}
{{< tab name="Typescript" >}}
{{< tabs >}}
{{% tab name="Provision" %}}
```
pulumi up -y
```
{{% /tab %}}
{{% tab name="Teardown" %}}
```
pulumi destroy -y
```
{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="index.ts" %}}
```ts
// iam/identities/users/create_user/ts/index.ts

import * as aws from "@pulumi/aws";

// Create IAM user with long-lived access credentials
const user = new aws.iam.User("techsquawks-user", {
    name: "techsquawks-user"
});

// Export user information
export const userArn = user.arn;
export const userName = user.name;

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/create_user/ts" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/create_user/ts" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< tab name="Javascript" >}}
{{< tabs >}}
{{% tab name="Provision" %}}
```
pulumi up -y
```
{{% /tab %}}
{{% tab name="Teardown" %}}
```
pulumi destroy -y
```
{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="index.js" %}}
```js
// iam/identities/users/create_user/js/index.js

"use strict";
const aws = require("@pulumi/aws");

// Create IAM user with long-lived access credentials
const user = new aws.iam.User("techsquawks-user", {
    name: "techsquawks-user"
});

// Export user information
exports.userArn = user.arn;
exports.userName = user.name;

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/create_user/js" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/create_user/js" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< tab name="Python" >}}
{{< tabs >}}
{{% tab name="Provision" %}}
```
pulumi up -y
```
{{% /tab %}}
{{% tab name="Teardown" %}}
```
pulumi destroy -y
```
{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="__main__.py" %}}
```py
# iam/identities/users/create_user/py/__main__.py

import pulumi
from pulumi_aws import iam

# Create IAM user with long-lived access credentials
user = iam.User("techsquawks-user", name="techsquawks-user")

# Export user information
pulumi.export('userArn', user.arn)
pulumi.export('userName', user.name)

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/create_user/py" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/create_user/py" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< tab name="Go" >}}
{{< tabs >}}
{{% tab name="Provision" %}}
```
pulumi up -y
```
{{% /tab %}}
{{% tab name="Teardown" %}}
```
pulumi destroy -y
```
{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="main.go" %}}
```go
// iam/identities/users/create_user/go/main.go

package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create IAM user with long-lived access credentials
		user, err := iam.NewUser(ctx, "techsquawks-user", &iam.UserArgs{
			Name: pulumi.String("techsquawks-user"),
		})
		if err != nil {
			return err
		}

		// Export user information
		ctx.Export("userArn", user.Arn)
		ctx.Export("userName", user.Name)
		return nil
	})
}

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/create_user/go" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/create_user/go" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< /tabs >}}

**Stack Outputs**
```
Outputs:
    userArn : "arn:aws:iam::012345678910:user/techsquawks-user"
    userName: "techsquawks-user"
```

To further verify that the user was provisioned correctly, the identity can be fetched via the `get-user` IAM API call. 

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws iam get-user --user-name techsquawks-user
```
**Output**
```
{
    "User": {
        "Path": "/",
        "UserName": "techsquawks-user",
        "UserId": "DBSAYFF32444NEI6MNIOP",
        "Arn": "arn:aws:iam::012345678910:user/techsquawks-user",
        "CreateDate": "2023-07-10T23:13:11+00:00",
    }
}
```
{{% /tab %}}
{{< /tabs >}}