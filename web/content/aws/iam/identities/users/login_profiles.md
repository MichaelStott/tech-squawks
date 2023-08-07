---
title: Console Passwords
draft: false
weight: 5
---

While API access requires user access keys, password credentials are required for accessing the AWS account resources via the web console. IAM provides various API methods and resources for managing user passwords. For instance, login profiles define the password constraints for a given user.

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
// iam/identities/users/user_login_profile/ts/index.ts

import * as aws from "@pulumi/aws";

// Create IAM user with password/console credentials
const user = new aws.iam.User("techsquawks-user", {
    name: "techsquawks-user",
    forceDestroy: true
});
const loginProfile = new aws.iam.UserLoginProfile("techsquawks-user-login-profile", {
    user: user.name,
    passwordLength: 15,
    passwordResetRequired: true
});
export const password = loginProfile.password;

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/go" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/ts" icon="code" %}}Repository{{% /button %}}
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
// iam/identities/users/user_login_profile/js/index.js

"use strict";
const aws = require("@pulumi/aws");

// Create IAM user with password/console credentials
const user = new aws.iam.User("techsquawks-user", {
    name: "techsquawks-user",
    forceDestroy: true
});
const loginProfile = new aws.iam.UserLoginProfile("techsquawks-user-login-profile", {
    user: user.name,
    passwordLength: 15,
    passwordResetRequired: true
});
export const password = loginProfile.password;

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/go" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/js" icon="code" %}}Repository{{% /button %}}
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
# iam/identities/users/user_login_profile/py/__main__.py

import pulumi
from pulumi_aws import iam

# Create IAM user with long-lived access credentials
user = iam.User("techsquawks-user", name="techsquawks-user")
login_profile = iam.UserLoginProfile("techsquawks-user-login-profile",
    user=user.name,
    passwordLength=15,
    passwordResetRequired=True
);

pulumi.export('password', login_profile.password)

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/go" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/py" icon="code" %}}Repository{{% /button %}}
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
// iam/identities/users/user_login_profile/go/main.go

package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create IAM user with long-lived access credentials
		user1, err := iam.NewUser(ctx, "techsquawks-user1", &iam.UserArgs{
			Name: pulumi.String("techsquawks-user1"),
			Path: pulumi.String("/example/path/1/"),
		})
		if err != nil {
			return err
		}
		user2, err := iam.NewUser(ctx, "techsquawks-user2", &iam.UserArgs{
			Name: pulumi.String("techsquawks-user2"),
			Path: pulumi.String("/example/path/2/"),
		})
		if err != nil {
			return err
		}
		user2a, err := iam.NewUser(ctx, "techsquawks-user2a", &iam.UserArgs{
			Name: pulumi.String("techsquawks-user2a"),
			Path: pulumi.String("/example/path/2/"),
		})
		if err != nil {
			return err
		}
		return nil
	})
}

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/go" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/go" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< /tabs >}}