import * as aws from "@pulumi/aws";

// Create IAM user with long-lived access credentials
const user = new aws.iam.User("techsquawks-user", {
    name: "techsquawks-user"
});

// Export user information
export const userArn = user.arn;
export const userName = user.name;
