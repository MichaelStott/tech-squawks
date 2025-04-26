"use strict";
const aws = require("@pulumi/aws");

// Create IAM user with long-lived access credentials
const user = new aws.iam.User("techsquawks-user", {
    name: "techsquawks-user"
});

// Export user information
exports.userArn = user.arn;
exports.userName = user.name;
