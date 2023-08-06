import pulumi
from pulumi_aws import iam

# Create IAM user with long-lived access credentials
user = iam.User("techsquawks-user", name="techsquawks-user")
login_profile = iam.UserLoginProfile("techsquawks-user-login-profile",
    user=user.name,
    passwordLength=15,
    passwordResetRequired=True
);

pulumi.export('password', login_profile.password)
