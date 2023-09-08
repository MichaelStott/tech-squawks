---
title: Access Credentials
draft: false
weight: 4
---

To access cloud resources through the API, users may be associated with a set of long-lived access credential key pair, consisting of an access key ID and secret key for signing requests.

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
// iam/identities/users/access_credentials/ts/index.ts

import * as aws from "@pulumi/aws";

// Create IAM user with long-lived access credentials
const user = new aws.iam.User("techsquawks-user", {
    name: "techsquawks-user"
});
const credentials = new aws.iam.AccessKey("techsquawks-user-credentials", {user: user.name});

// Export user information
export const userArn = user.arn;
export const userName = user.name;
export const userAccessKeyId = credentials.id;
export const userAccessSecret = credentials.secret;

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/access_credentials/ts" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/access_credentials/ts" icon="code" %}}Repository{{% /button %}}
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
// iam/identities/users/access_credentials/js/index.js

"use strict";
const aws = require("@pulumi/aws");

// Create IAM user with long-lived access credentials
const user = new aws.iam.User("techsquawks-user", {
    name: "techsquawks-user"
});
const credentials = new aws.iam.AccessKey("techsquawks-user-credentials", {user: user.name});

// Export user information
exports.userArn = user.arn;
exports.userName = user.name;
exports.userAccessKeyId = credentials.id;
exports.userAccessSecret = credentials.secret;

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/access_credentials/js" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/access_credentials/js" icon="code" %}}Repository{{% /button %}}
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
# iam/identities/users/access_credentials/py/__main__.py

import pulumi
from pulumi_aws import iam

# Create IAM user with long-lived access credentials
user = iam.User("techsquawks-user", name="techsquawks-user")
credentials = iam.AccessKey("techsquawks-user-credentials", user=user.name)

# Export user information
pulumi.export('userArn', user.arn)
pulumi.export('userName', user.name)
pulumi.export('userAccessKeyId', credentials.id)
pulumi.export('userSecretKey', credentials.secret)

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/access_credentials/py" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/access_credentials/py" icon="code" %}}Repository{{% /button %}}
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
// iam/identities/users/access_credentials/go/main.go

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
		credentials, err := iam.NewAccessKey(ctx, "techsquawks-user-credentials", &iam.AccessKeyArgs{
			User: user.Name,
		})
		if err != nil {
			return err
		}

		// Export user information
		ctx.Export("userArn", user.Arn)
		ctx.Export("userName", user.Name)
		ctx.Export("userAccessKeyId", credentials.ID())
		ctx.Export("userSecretKey", credentials.Secret)
		return nil
	})
}

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/access_credentials/go" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/iam/identities/users/access_credentials/go" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< /tabs >}}

**Stack Outputs**
```
Outputs:
    userAccessKeyId: "BKINYAJ78Q44D3CT4NER"
    userArn :        "arn:aws:iam::012345678910:user/techsquawks-user"
    userName:        "techsquawks-user"
    userSecretKey:   [secret]
```

{{% notice style="info" %}}
Sensitive values are hidden by default in the Pulumi stack output. To get the secret key value, execute `pulumi stack output userSecretKey --show-secrets --stack dev`
{{% /notice %}}

To validate that the access credentials work as expected, invoke the caller identity API using the newly provisioned credentials:

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
AWS_ACCESS_KEY_ID=$(pulumi stack output userAccessKeyId --stack dev)
AWS_SECRET_ACCESS_KEY=$(pulumi stack output userSecretKey --stack dev --show-secrets)
aws sts get-caller-identity
```
**Output**
```
{
    "UserId": "BKXNYAA78Q56W3CT4NTJ",
    "Account": "012345678910,
    "Arn": "arn:aws:iam::012345678910:user/techsquawks-user"
}
```
{{% /tab %}}
{{< /tabs >}}
