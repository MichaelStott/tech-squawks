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
