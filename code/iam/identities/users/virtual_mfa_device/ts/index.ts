import * as aws from "@pulumi/aws";
import * as fs from "fs";

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
const mfa = new aws.iam.VirtualMfaDevice("tstest", {virtualMfaDeviceName: "tstest"});

export const password = loginProfile.password;

var callback = (err) => {
  if (err) throw err;
  console.log('It\'s saved!');
}
mfa.qrCodePng.apply(qrCodePng => fs.writeFile('qrcode.png', `${qrCodePng}`, callback))
