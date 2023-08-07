"use strict";
const aws = require("@pulumi/aws");

// Create IAM user with password/console credentials
const user = new aws.iam.User("techsquawks-user", {
    name: "techsquawks-user",
    forceDestroy: true
});
const loginProfile = new aws.iam.UserLoginProfile("techsquawks-user-login-profile", {
    user: user.name,
    passwordLength: 15,
    passwordResetRequired: true
});
exports.password = loginProfile.password;
