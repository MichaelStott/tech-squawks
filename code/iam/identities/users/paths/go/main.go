package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create IAM user with long-lived access credentials
		user1, err := iam.NewUser(ctx, "techsquawks-user1", &iam.UserArgs{
			Name: pulumi.String("techsquawks-user1"),
			Path: pulumi.String("example/path/1"),
		})
		if err != nil {
			return err
		}
		user2, err := iam.NewUser(ctx, "techsquawks-user2", &iam.UserArgs{
			Name: pulumi.String("techsquawks-user2"),
			Path: pulumi.String("example/path/2"),
		})
		if err != nil {
			return err
		}
		user2a, err := iam.NewUser(ctx, "techsquawks-user2a", &iam.UserArgs{
			Name: pulumi.String("techsquawks-user2a"),
			Path: pulumi.String("example/path/2a"),
		})
		if err != nil {
			return err
		}
		return nil
	})
}
