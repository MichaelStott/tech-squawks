package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create IAM user with long-lived access credentials
		user, err := iam.NewUser(ctx, "techsquawks-user", &iam.UserArgs{
			Name: pulumi.String("techsquawks-user"),
		})
		if err != nil {
			return err
		}
		credentials, err := iam.NewAccessKey(ctx, "techsquawks-user-credentials", &iam.AccessKeyArgs{
			User: user.Name,
		})
		if err != nil {
			return err
		}

		// Export user information
		ctx.Export("userArn", user.Arn)
		ctx.Export("userName", user.Name)
		ctx.Export("userAccessKeyId", credentials.ID())
		ctx.Export("userSecretKey", credentials.Secret)
		return nil
	})
}