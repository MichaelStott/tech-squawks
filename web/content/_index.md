---
title: "Welcome!"
date: 2021-01-23T16:49:34-05:00
weight: 1
---

# Howdy!

Welcome to Tech Squawks, a website for learning cloud computing technologies and concepts, using popular programming languages such as Typescript, Javascript, Python, Go, or Java. This site is a work in progress, so check back frequently for new tutorials and updates!

### Hands-On Learning

Learning cloud computing can seem like a daunting task. In the case of AWS, there are over 200 cloud services offered at the time of writing. The goal of this website is to offer a more hands-on approach to understanding cloud development beyond the first-party documentation by providing code examples of cloud applications to demonstrate cloud computing concepts and common design patterns.

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

"""NOTE: Because Pulumi Crosswalk is only available for Typescript and Javascript,
the Python and Golang based examples are significantly larger.
"""

import json, os, mimetypes

import pulumi
from pulumi import export, FileAsset, ResourceOptions, Output
import pulumi_aws as aws
from pulumi_aws import s3, lambda_, apigateway


# Create Lambda permissions.
lambda_role = aws.iam.Role("apiGatewayLambdaRole", 
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
                "Action": "sts:AssumeRole",
                "Principal": {
                    "Service": "lambda.amazonaws.com",
                },
                "Effect": "Allow",
                "Sid": "",
            }]
    }))
role_policy_attachment = aws.iam.RolePolicyAttachment("lambdaRoleAttachment",
    role=lambda_role,
    policy_arn=aws.iam.ManagedPolicy.AWS_LAMBDA_BASIC_EXECUTION_ROLE)

# Provision Lambda function which will be invoked upon an http request.
LAMBDA_SOURCE = 'lambda.py'
LAMBDA_PACKAGE = 'lambda.zip'
LAMBDA_VERSION = '1.0.0'
os.system('zip %s %s' % (LAMBDA_PACKAGE, LAMBDA_SOURCE))

# Create an AWS resource (S3 Bucket)c
bucket = s3.Bucket('lambda-api-gateway-example')

mime_type, _ = mimetypes.guess_type(LAMBDA_PACKAGE)
obj = s3.BucketObject(
            LAMBDA_VERSION+'/'+LAMBDA_PACKAGE,
            bucket=bucket.id,
            source=FileAsset(LAMBDA_PACKAGE),
            content_type=mime_type
            )

lambda_function = lambda_.Function(
    'ServerlessExample',
    s3_bucket=bucket.id,
    s3_key=LAMBDA_VERSION+'/'+LAMBDA_PACKAGE,
    handler="lambda.handler",
    runtime="python3.7",
    role=lambda_role.arn,
)

# Give API Gateway permissions to invoke the Lambda
lambda_permission = aws.lambda_.Permission("lambdaPermission", 
    action="lambda:InvokeFunction",
    principal="apigateway.amazonaws.com",
    function=lambda_function)

# Set up the API Gateway
apigw = aws.apigatewayv2.Api("httpApiGateway", 
    protocol_type="HTTP",
    route_key="GET /",
    target=lambda_function.invoke_arn)

# Export the API endpoint for easy access
pulumi.export("url", apigw.api_endpoint)
```
{{% /tab %}}
{{< /tabs >}}

The exported URL will display the following image in your web browser: 

![squawk](https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif)

### Try Locally

Cloud computing examples are often difficult to demonstrate, due to the need for cloud access and the time required for deploying resources. Additionally, there is the risk of leaving resources provisioned and incurring unintended costs.

In an effort to make these tutorials accesible to those without cloud access and minimize costs, examples are designed 
to support local execution, using technologies such as `localstack` (AWS Emulator), `kind` (Local Kubernetes Cluster), etc., whenever possible. 

### Study Buddy

While any specific certification preparation is beyond the scope of this site, flashcards are included at the end of each section for additional study and review. Cheatsheats for certain topics are also included to help for easy reference.

### Prerequisites

Before continuing, readers should be:

- Knowledgeable of at least one of the following programming languages: Typescript, Javascript, Python, Go, or Java
- Comfortable shell/bash scripting
- Familiarity with basic computer networking concepts

For setting up your development environment, see the  [Getting Started]({{< ref "getting_started" >}}) section.