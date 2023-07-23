import * as aws from "@pulumi/aws";

// Create IAM user with long-lived access credentials
const user = new aws.iam.User("techsquawks-user", {
    name: "techsquawks-user"
});
const credentials = new aws.iam.AccessKey("techsquawks-user-credentials", {user: user.name});

// Export user information
export const userArn = user.arn;
export const userName = user.name;
export const userAccessKeyId = credentials.id;
export const userAccessSecret = credentials.secret;
