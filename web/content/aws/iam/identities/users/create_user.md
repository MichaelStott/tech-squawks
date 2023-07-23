---
title: Create Users
draft: false
weight: 2
---

{{< tabs groupId="code" >}}
{{< tab name="Typescript" >}}
{{< tabs >}}
{{% tab name="Execution" %}}
```
pulumi up -y
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
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/ts" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< tab name="Javascript" >}}
{{< tabs >}}
{{% tab name="Execution" %}}
```
pulumi up -y
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
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/js" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< tab name="Python" >}}
{{< tabs >}}
{{% tab name="Execution" %}}
```
pulumi up -y
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
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/py" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< tab name="Go" >}}
{{< tabs >}}
{{% tab name="Execution" %}}
```
pulumi up -y
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
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/go" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< /tabs >}}