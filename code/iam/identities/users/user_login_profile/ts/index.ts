import * as aws from "@pulumi/aws";

// Create IAM user with long-lived access credentials
const user = new aws.iam.User("techsquawks-userz", {
    name: "techsquawks-userz",
    forceDestroy: true
});
const loginProfile = new aws.iam.UserLoginProfile("techsquawks-user-login-profile", {
    user: user.name,
    passwordLength: 15,
    passwordResetRequired: true
});
export const password = loginProfile.password;
