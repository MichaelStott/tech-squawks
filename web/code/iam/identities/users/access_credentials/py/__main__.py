import pulumi
from pulumi_aws import iam

# Create IAM user with long-lived access credentials
user = iam.User("techsquawks-user", name="techsquawks-user")
credentials = iam.AccessKey("techsquawks-user-credentials", user=user.name)

# Export user information
pulumi.export('userArn', user.arn)
pulumi.export('userName', user.name)
pulumi.export('userAccessKeyId', credentials.id)
pulumi.export('userSecretKey', credentials.secret)
