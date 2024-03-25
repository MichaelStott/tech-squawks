---
title: "Welcome!"
weight: 1
---

# Welcome!

Welcome to Tech Squawks, a website for learning cloud computing technologies and design patterns. This website is a work in progress, so check back frequently for new tutorials and updates!

### Hands-On Learning

The aim of this website is to present cloud-computing concepts using small, self-contained code examples. To achieve this, infrastructure and services are managed with Pulumi, which allows cloud resources to be defined using programming languages such as Typescript, Javascript, Python, and Go.

For instance, the below example demonstrates developing and deploying a serverless AWS app in multiple languages. The {{% button icon="rocket" %}}Deploy{{% /button %}} button will create the initial empty stack in the user's Pulumi account and provide instructions for provisioning the project.

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
{{% include file="code\homepage\ts\index.ts" %}}
```

{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/ts" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/ts" icon="code" %}}Repository{{% /button %}}
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
{{% include file="code\homepage\js\index.js" %}}
```

{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/js" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/js" icon="code" %}}Repository{{% /button %}}
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
{{% include file="code\homepage\py\__main__.py" %}}
```

{{% /tab %}}
{{% tab name="lambda.py" %}}

```py
{{% include file="code\homepage\py\lambda.py" %}}
```

{{% /tab %}}
{{% tab name="lambda_util.py" %}}

```py
{{% include file="code\homepage\py\lambda_util.py" %}}
```

{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/py" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/py" icon="code" %}}Repository{{% /button %}}
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
{{% include file="code\homepage\go\main.go" %}}
```

{{% /tab %}}
{{% tab name="handler.go" %}}

```go
{{% include file="code\homepage\go\handler\handler.go" %}}
```

{{% /tab %}}
{{% tab name="lambda_util.go" %}}

```go
{{% include file="code\homepage\go\lambda_util.go" %}}
```

{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/go" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/go" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< /tabs >}}
**Stack Outputs**

```
Outputs:
    invoke_arn: "ServerlessExample-93b31c3"
    url       : "https://pu00gu5pmg.execute-api.us-east-1.amazonaws.com"
```

The exported URL will display the following image in your web browser:

![squawk](https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif)

### Local Development

In an effort to make these tutorials accessible to those without cloud access and minimize costs, examples are designed
to support local execution, using technologies such as [LocalStack](https://localstack.cloud/), [Cloud Code](https://cloud.google.com/code), [Kind](https://kind.sigs.k8s.io/), etc., whenever possible.

### Study Aid

While any specific certification preparation is beyond the scope of this website, flashcards are included at the end of each section for additional study and review.

### Prerequisites

Before continuing, readers should be:

- Experienced with Typescript, Javascript, Python, or Go
- Comfortable with shell/bash scripting
- Familiar with basic computer networking concepts

For setting up your development environment, see the [Getting Started]({{< ref "getting_started" >}}) section.
