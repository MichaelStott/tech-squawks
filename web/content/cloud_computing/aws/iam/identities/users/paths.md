---
title: Paths
draft: false
weight: 3
---

_Paths_ are analogous to namespaces and help in organizing IAM users both for reporting and associating permissions.

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
// iam/identities/users/paths/ts/index.ts

import * as aws from "@pulumi/aws";

// Create IAM user with long-lived access credentials
const user1 = new aws.iam.User("techsquawks-user-1", {
    name: "techsquawks-user",
    path: "/example/path/1/"
});
const user2 = new aws.iam.User("techsquawks-user-2", {
    name: "techsquawks-user-2",
    path: "/example/path/2/"
});
const user2a = new aws.iam.User("techsquawks-user-2a", {
    name: "techsquawks-user-2a",
    path: "/example/path/2/"
});

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/paths/ts" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/paths/ts" icon="code" %}}Repository{{% /button %}}
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
// iam/identities/users/paths/js/index.js

"use strict";
const aws = require("@pulumi/aws");

// Create IAM user with long-lived access credentials
const user1 = new aws.iam.User("techsquawks-user-1", {
    name: "techsquawks-user1",
    path: "/example/path/1/"
});
const user2 = new aws.iam.User("techsquawks-user-2", {
    name: "techsquawks-user-2",
    path: "/example/path/2/"
});
const user2a = new aws.iam.User("techsquawks-user-2a", {
    name: "techsquawks-user-2a",
    path: "/example/path/2/"
});
```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/paths/js" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/paths/js" icon="code" %}}Repository{{% /button %}}
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
# iam/identities/users/paths/py/__main__.py

import pulumi
from pulumi_aws import iam

# Create IAM user with long-lived access credentials
user1 = iam.User("techsquawks-user-1", name="techsquawks-user1", path="/example/path/1/")
user2 = iam.User("techsquawks-user-2a", name="techsquawks-user2", path="/example/path/2/")
user2a = iam.User("techsquawks-user-2b", name="techsquawks-user2a", path="/example/path/2/")

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/paths/py" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/paths/py" icon="code" %}}Repository{{% /button %}}
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
// iam/identities/users/paths/go/main.go

package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create IAM user with long-lived access credentials
		_, err := iam.NewUser(ctx, "techsquawks-user1", &iam.UserArgs{
			Name: pulumi.String("techsquawks-user1"),
			Path: pulumi.String("/example/path/1/"),
		})
		if err != nil {
			return err
		}
		_, err = iam.NewUser(ctx, "techsquawks-user2", &iam.UserArgs{
			Name: pulumi.String("techsquawks-user2"),
			Path: pulumi.String("/example/path/2/"),
		})
		if err != nil {
			return err
		}
		_, err = iam.NewUser(ctx, "techsquawks-user2a", &iam.UserArgs{
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
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/paths/go" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/paths/go" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< /tabs >}}

Users who belong to the same path can be targeted in certain IAM operations, such as listing users:

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws iam list-users --path "/example/path/2/"
```
**Output**
```
{
    "Users": [
        {
            "Path": "/example/path/2/",
            "UserName": "techsquawks-user-2",
            "UserId": "AFCAYGH7AQ44FXTSPCX55",
            "Arn": "arn:aws:iam::012345678910:user/example/path/2/techsquawks-user-2",
            "CreateDate": "2023-07-24T22:39:32+00:00"
        },
		{
            "Path": "/example/path/2/",
            "UserName": "techsquawks-user-2a",
            "UserId": "BEAAYHI7AQ45GXTQPCX44",
            "Arn": "arn:aws:iam::012345678910:user/example/path/2/techsquawks-user-2a",
            "CreateDate": "2023-07-24T22:39:32+00:00"
        }
    ]
}
```
{{% /tab %}}
{{< /tabs >}}