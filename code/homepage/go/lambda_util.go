package main

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
