"use strict";
const aws = require("@pulumi/aws");

// Create IAM user with long-lived access credentials
const user = new aws.iam.User("techsquawks-user", {
    name: "techsquawks-user"
});
const credentials = new aws.iam.AccessKey("techsquawks-user-credentials", {user: user.name});

// Export user information
exports.userArn = user.arn;
exports.userName = user.name;
exports.userAccessKeyId = credentials.id;
exports.userAccessSecret = credentials.secret;
