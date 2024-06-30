package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create IAM user with password/console credentials
		user, err := iam.NewUser(ctx, "techsquawks-user", &iam.UserArgs{
			Name: pulumi.String("techsquawks-user"),
		})
		if err != nil {
			return err
		}
		loginProfile, err := iam.NewUserLoginProfile(ctx, "loginProfile", &iam.UserLoginProfileArgs{
			User:                  user.Name,
			PasswordLength:        pulumi.Int(15),
			PasswordResetRequired: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}
		ctx.Export("password", loginProfile.Password)
		return nil
	})
}
