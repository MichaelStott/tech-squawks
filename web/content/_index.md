---
title: "Welcome!"
date: 2021-01-23T16:49:34-05:00
weight: 1
---

# Howdy!

Welcome to Tech Squawks, a website for learning AWS cloud development and design using programming languages such as Typescript, Javascript, Python,
or Go.

AWS can seem like a daunting platform to master. At the time of writing, there are over 200 cloud services offered by AWS. 
The goal of Tech Squawks is to provide straightforward explanations of cloud computing concepts using with short W3-esque examples of 
small self-contained AWS apps that can be swiftly compiled and deployed.

In an effort to make these tutorials accesible to those without an AWS account, examples are designed to be compatible with
[LocalStack](https://github.com/localstack/localstack), a framework for running AWS cloud applications on the user's local machine, whenever possible. 

Flashcards are included at the end of each section for additional study and review, which may be useful for those who wish to pursue 
certification. These flaschards are publicly hosted on [Cram](https://www.cram.com/) and accesible through both the website and mobile app.

### Severless Webpage Demo

Below is a short example of deploying a small serverless web app. The deploy button will create the stack in the reader's Pulumi account, which can then be deployed using the Pulumi CLI tool.

{{< tabs groupId="code" >}}
{{% tab name="Typescript" %}}
```Typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Provision an API Gateway instance.
const api = new awsx.apigateway.API("serverless-party-parrot", {
    routes: [{
        // Define an HTTP endpoint.
        path: "/",
        method: "GET",
        // Create a Lambda function that will be triggered upon accessing this endpoint.
        eventHandler: new aws.lambda.CallbackFunction("handler", {
            callback: async (event) => {
                // Cry havoc and let slip the parrots of war.
                return {
                    statusCode: 200,
                    headers: {"Content-Type": "text/html"},
                    body: '<img src="https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif">',
                };
            },
        }),
    }],
})

// The URL of the deployed serverless webpage.
export const url = api.url;
```
{{% /tab %}}
{{% tab name="Javascript" %}}
TODO
{{% /tab %}}
{{% tab name="Python" %}}
TODO
{{% /tab %}}
{{% tab name="Go" %}}
TODO
{{% /tab %}}
{{< /tabs >}}

The result speaks for itself:

![squawk](https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif)

### Prerequisites

Before continuing, readers should be:

- Knowledgeable of at least one of the following programming languages: Typescript, Javascript, Python, or Go.
- Comfortable with using the shell or terminal on their OS.
- Familiar with basic computer networking concepts.

For setting up your development environment, see the  [Getting Started]({{< ref "getting_started" >}}) section.