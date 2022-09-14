---
title: "Welcome!"
date: 2021-01-23T16:49:34-05:00

weight: 1
---

# Howdy!

Welcome to Tech Squawks, a website for learning cloud computing technologies and concepts, using popular programming languages such as Typescript, Javascript, Python, or Go. This site is a work in progress, so check back frequently for new tutorials and updates!

### Hands-On Learning

Cloud computing documentation often provides lengthy descriptions of cloud concepts, functionality, or architecture without providing concrete examples. The goal of this website is to offer a more hands-on approach to learning cloud development beyond the first-party documentation by providing code examples which clearly demonstrate key concepts and design patterns.

For instance, the below examples demonstrate a small serverless AWS app in multiple languages:

{{< tabs groupId="code" >}}
{{% tab name="Typescript" %}}
```ts
// homepage/ts/index.ts

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
```js
// homepage/js/index.js

"use strict";
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

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
exports.url = api.url;
```
{{% /tab %}}
{{% tab name="Python" %}}
```py
# homepage/py/__main__.py

import pulumi
import pulumi_aws

from lambda_util import create_python_lambda

LAMBDA_SOURCE = 'lambda.py'
LAMBDA_PACKAGE = 'lambda'
LAMBDA_VERSION = '1.0.0'

# Provision Lambda function which will be invoked upon an http request.
lambda_function = create_python_lambda(LAMBDA_PACKAGE, LAMBDA_SOURCE, LAMBDA_VERSION)

# Give API Gateway permissions to invoke the Lambda
lambda_permission = pulumi_aws.lambda_.Permission("lambdaPermission", 
    action="lambda:InvokeFunction",
    principal="apigateway.amazonaws.com",
    function=lambda_function)

# Set up the API Gateway
apigw = pulumi_aws.apigatewayv2.Api("httpApiGateway", 
    protocol_type="HTTP",
    route_key="GET /",
    target=lambda_function.invoke_arn)

# Export the API endpoint for easy access
pulumi.export("url", apigw.api_endpoint)
pulumi.export("invoke_arn", lambda_function.name)
```
{{% /tab %}}
{{% tab name="Go" %}}
```go
// homepage/go/main.go

package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/apigatewayv2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create lambda function that will return HTML.
		lambda, err := CreateGoLambda(ctx)
		if err != nil {
			panic(err)
		}

		// Provision API Gateway instance to invoke Lambda
		api, err := apigatewayv2.NewApi(ctx,
			"serverless-parrot-demo-gov2",
			&apigatewayv2.ApiArgs{
				ProtocolType: pulumi.String("HTTP"),
				RouteKey:     pulumi.String("GET /"),
				Target:       lambda.InvokeArn,
			},
			nil,
		)

		ctx.Export("url", api.ApiEndpoint)

		return nil
	})
}

```
{{% /tab %}}
{{< /tabs >}}

The exported URL will display the following image in your web browser: 

![squawk](https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif)

### Try Locally

Cloud computing examples are often difficult to demonstrate, due to the need for cloud access and the time required for deploying resources. Additionally, there is the risk of leaving resources provisioned and incurring unintended costs.

In an effort to make these tutorials accesible to those without cloud access and minimize costs, examples are designed 
to support local execution, using technologies such as [LocalStack](https://localstack.cloud/), [Cloud Code](https://cloud.google.com/code), [Kind](https://kind.sigs.k8s.io/), etc., whenever possible. 

### Study Buddy

While any specific certification preparation is beyond the scope of this site, flashcards are included at the end of each section for additional study and review. Cheatsheats for certain topics are also included for easy reference.

### Prerequisites

Before continuing, readers should be:

- Experienced with Typescript, Javascript, Python, or Go
- Comfortable with shell/bash scripting
- Familiar with basic computer networking concepts

For setting up your development environment, see the  [Getting Started]({{< ref "getting_started" >}}) section.
