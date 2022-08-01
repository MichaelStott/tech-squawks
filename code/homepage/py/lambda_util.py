import json, mimetypes, shutil, os
import pulumi_aws as aws
from pulumi_aws import lambda_, s3
from pulumi import FileAsset

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

def create_python_lambda(package, source, version, bucket_name="ts-test-lambda-py"):
    """ Uploads handler project to S3 and returns S3 object.
    """
    #os.system('zip %s %s' % (package, source))
    shutil.make_archive(package, "zip", ".", source)

    # Create an AWS resource (S3 Bucket)c
    bucket = s3.Bucket(bucket_name)
    mime_type, _ = mimetypes.guess_type(package)
    obj = s3.BucketObject(
                version+'/'+package,
                bucket=bucket.id,
                source=FileAsset(package),
                content_type=mime_type
                )

    lambda_function = lambda_.Function(
        'ServerlessExample',
        s3_bucket=bucket.id,
        s3_key=obj.key,
        handler="lambda.handler",
        runtime="python3.7",
        role=lambda_role.arn,
    )

    return lambda_function

    