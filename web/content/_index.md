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
// homepage/ts/index.ts

import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const payload =
  '<img src="https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif">';

// Provision an API Gateway instance.
const api = new awsx.classic.apigateway.API("serverless-party-parrot", {
  routes: [
    {
      // Define an HTTP endpoint.
      path: "/",
      method: "GET",
      // Create a Lambda function that will be triggered upon accessing this endpoint.
      eventHandler: new aws.lambda.CallbackFunction("handler", {
        callback: async (event) => {
          // Cry havoc and let slip the parrots of war.
          return {
            statusCode: 200,
            headers: { "Content-Type": "text/html" },
            body: payload,
          };
        },
      }),
    },
  ],
});

// The URL of the deployed serverless webpage.
export const url = api.url;

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
// homepage/js/index.js

"use strict";
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

const payload =
  '<img src="https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif">';

// Provision an API Gateway instance.
const api = new awsx.classic.apigateway.API("serverless-party-parrot", {
  routes: [
    {
      // Define an HTTP endpoint.
      path: "/",
      method: "GET",
      // Create a Lambda function that will be triggered upon accessing this endpoint.
      eventHandler: new aws.lambda.CallbackFunction("handler", {
        callback: async (event) => {
          // Cry havoc and let slip the parrots of war.
          return {
            statusCode: 200,
            headers: { "Content-Type": "text/html" },
            body: payload,
          };
        },
      }),
    },
  ],
});

// The URL of the deployed serverless webpage.
exports.url = api.url;

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
# homepage/py/__main__.py

import pulumi
import pulumi_aws

from lambda_util import create_python_lambda

LAMBDA_SOURCE = "lambda.py"
LAMBDA_PACKAGE = "lambda"
LAMBDA_VERSION = "1.0.0"

# Provision Lambda function which will be invoked upon an http request.
lambda_function = create_python_lambda(LAMBDA_PACKAGE, LAMBDA_SOURCE, LAMBDA_VERSION)

# Give API Gateway permissions to invoke the Lambda
lambda_permission = pulumi_aws.lambda_.Permission(
    "lambdaPermission",
    action="lambda:InvokeFunction",
    principal="apigateway.amazonaws.com",
    function=lambda_function,
)

# Set up the API Gateway
apigw = pulumi_aws.apigatewayv2.Api(
    "httpApiGateway",
    protocol_type="HTTP",
    route_key="GET /",
    target=lambda_function.invoke_arn,
)

# Export the API endpoint for easy access
pulumi.export("url", apigw.api_endpoint)
pulumi.export("invoke_arn", lambda_function.name)

```
{{% /tab %}}
{{% tab name="lambda.py" %}}
```py
# homepage/py/lambda.py

# Define handler logic and Lambda function
def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": '<img src="https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif">',
    }

```
{{% /tab %}}
{{% tab name="lambda_util.py" %}}
```py
# homepage/py/lambda_util.py

import json, mimetypes, shutil, os
import pulumi_aws as aws
from pulumi_aws import lambda_, s3
from pulumi import FileAsset

lambda_role = aws.iam.Role(
    "apiGatewayLambdaRole",
    assume_role_policy=json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Principal": {
                        "Service": "lambda.amazonaws.com",
                    },
                    "Effect": "Allow",
                    "Sid": "",
                }
            ],
        }
    ),
)
role_policy_attachment = aws.iam.RolePolicyAttachment(
    "lambdaRoleAttachment",
    role=lambda_role,
    policy_arn=aws.iam.ManagedPolicy.AWS_LAMBDA_BASIC_EXECUTION_ROLE,
)


def create_python_lambda(package, source, version, bucket_name="ts-test-lambda-py"):
    """Uploads handler project to S3 and returns S3 object."""
    shutil.make_archive(package, "zip", ".", source)

    # Create an AWS resource (S3 Bucket)c
    bucket = s3.Bucket(bucket_name)
    package += ".zip"
    mime_type, _ = mimetypes.guess_type(package)
    obj = s3.BucketObject(
        version + "/" + package,
        bucket=bucket.id,
        source=FileAsset(package),
        content_type=mime_type,
    )

    lambda_function = lambda_.Function(
        "ServerlessExample",
        s3_bucket=bucket.id,
        s3_key=obj.key,
        handler="lambda.handler",
        runtime="python3.7",
        role=lambda_role.arn,
    )

    return lambda_function

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
// homepage/go/main.go

ackage main

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
{{% tab name="handler.go" %}}
```go
// homepage/go/handler/handler.go

ackage main

import (
	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

// handler is a simple function that takes a string and does a ToUpper.
func handler(request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
	return events.APIGatewayProxyResponse{
		StatusCode: 200,
		Headers: map[string]string{
			"Content-Type": "text/html",
		},
		Body: "<img src=\"https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif\">",
	}, nil
}

func main() {
	lambda.Start(handler)
}

```
{{% /tab %}}
{{% tab name="lambda_util.go" %}}
```go
// homepage/go/lambda_util.go

ackage main

import (
	"archive/zip"
	"encoding/json"
	"io"
	"os"
	"path/filepath"

	"github.com/gabriel-vasile/mimetype"
	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/iam"
	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/s3"
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/lambda"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func zipSource(source, target string) error {
	// 1. Create a ZIP file and zip.Writer
	f, err := os.Create(target)
	if err != nil {
		return err
	}
	defer f.Close()

	writer := zip.NewWriter(f)
	defer writer.Close()

	// 2. Go through all the files of the source
	return filepath.Walk(source, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		// 3. Create a local file header
		header, err := zip.FileInfoHeader(info)
		if err != nil {
			return err
		}

		// set compression
		header.Method = zip.Deflate

		// 4. Set relative path of a file as the header name
		header.Name, err = filepath.Rel(filepath.Dir(source), path)
		if err != nil {
			return err
		}
		if info.IsDir() {
			header.Name += "/"
		}

		// 5. Create writer for the file header and save content of the file
		headerWriter, err := writer.CreateHeader(header)
		if err != nil {
			return err
		}

		if info.IsDir() {
			return nil
		}

		f, err := os.Open(path)
		if err != nil {
			return err
		}
		defer f.Close()

		_, err = io.Copy(headerWriter, f)
		return err
	})
}

func CreateLambdaRole(ctx *pulumi.Context) (*iam.Role, error) {
	tmpJSON0, err := json.Marshal(map[string]interface{}{
		"Version": "2012-10-17",
		"Statement": []map[string]interface{}{
			map[string]interface{}{
				"Action": "sts:AssumeRole",
				"Effect": "Allow",
				"Sid":    "",
				"Principal": map[string]interface{}{
					"Service": "lambda.amazonaws.com",
				},
			},
		},
	})
	if err != nil {
		return nil, err
	}
	json0 := string(tmpJSON0)
	lambdaRole, err := iam.NewRole(ctx, "lambdaRole", &iam.RoleArgs{
		AssumeRolePolicy: pulumi.String(json0),
	})
	if err != nil {
		return nil, err
	}
	_, err = iam.NewRolePolicyAttachment(ctx, "lambdaRoleAttach", &iam.RolePolicyAttachmentArgs{
		Role:      lambdaRole.Name,
		PolicyArn: iam.ManagedPolicyIAMReadOnlyAccess,
	})
	if err != nil {
		return nil, err
	}
	return lambdaRole, nil
}

func CreateGoLambda(ctx *pulumi.Context) (*lambda.Function, error) {
	// Package lambda function.
	err := zipSource("handler/handler", "handler.zip")
	if err != nil {
		return nil, err
	}

	// Allow API Gateway to invoke Lambda functions.
	role, err := CreateLambdaRole(ctx)
	if err != nil {
		return nil, err
	}

	// Provision bucket for uploading Lambda handler.
	bucket, err := s3.NewBucket(ctx, "ts-test-bucket-go", nil)
	if err != nil {
		return nil, err
	}

	// Upload handler to S3 bucket.
	mtype, err := mimetype.DetectFile("./handler.zip")
	if err != nil {
		return nil, err
	}
	obj, err := s3.NewBucketObject(ctx, "1.0.0/handler.zip", &s3.BucketObjectArgs{
		Bucket:      bucket.ID(),
		Source:      pulumi.NewFileAsset("./handler.zip"),
		ContentType: pulumi.String(mtype.String()),
	})

	// Create and return lambda function
	function, err := lambda.NewFunction(
		ctx, "lambdaAPIGatewayFunction", &lambda.FunctionArgs{
			S3Bucket: bucket.ID(),
			S3Key:    obj.Key,
			Runtime:  pulumi.String("go1.x"),
			Handler:  pulumi.String("handler"),
			Role:     role.Arn,
		},
		nil,
	)

	lambda.NewPermission(ctx, "lambdaPermission", &lambda.PermissionArgs{
		Action:    pulumi.String("lambda:InvokeFunction"),
		Principal: pulumi.String("apigateway.amazonaws.com"),
		Function:  function,
	})

	// Enable API Gateway to invoke the Lambda
	return function, err
}

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
