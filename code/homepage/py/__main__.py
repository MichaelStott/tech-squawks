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