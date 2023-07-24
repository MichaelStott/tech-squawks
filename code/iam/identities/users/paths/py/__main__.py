import pulumi
from pulumi_aws import iam

# Create IAM user with long-lived access credentials
user1 = iam.User("techsquawks-user", name="techsquawks-user1", path="example/path/1")
user2 = iam.User("techsquawks-user", name="techsquawks-user2", path="example/path/2")
user2a = iam.User("techsquawks-user", name="techsquawks-user2a", path="example/path/2a")
