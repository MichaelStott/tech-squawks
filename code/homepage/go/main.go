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
			"serverless-parrot-demo-go",
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
