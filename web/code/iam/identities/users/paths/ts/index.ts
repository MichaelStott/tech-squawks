import * as aws from "@pulumi/aws";

// Create IAM user with long-lived access credentials
const user1 = new aws.iam.User("techsquawks-user-1", {
    name: "techsquawks-user",
    path: "/example/path/1/"
});
const user2 = new aws.iam.User("techsquawks-user-2", {
    name: "techsquawks-user-2",
    path: "/example/path/2/"
});
const user2a = new aws.iam.User("techsquawks-user-2a", {
    name: "techsquawks-user-2a",
    path: "/example/path/2/"
});
