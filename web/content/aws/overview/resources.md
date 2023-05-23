---
title: Resources
draft: false
weight: 4
---

A _resource_ is a broad term for any cloud entity that can be provisioned in AWS. For instance, servers, virtual private networks, networking policies, and account users are considered AWS resources. Every resource is associated with an Amazon Resource Number (ARN),
which uniquely identifies it. ARNs have the following format[^1]:

```
arn:aws:[service]:[region]:[account-id]:[resource-id]
arn:aws:[service]:[region]:[account-id]:[resource-type]:[resource-id]
arn:aws:[service]:[region]:[account-id]:[resource-type]/[resource-id]
```

A breakdown of the above fields is provided below:
- service: The AWS service which the resource is associated with 
- region: Region in which the resource is located.
- account-id: The account which contains the resource
- resource-type: The type of service resource (i.e. users, compute servers, managed databases, etc.)
- resource-id: The unique resource identifier

{{% notice info %}}
Certain resources may omit either or both the region, account-id from the ARN. 
{{% /notice %}}


For instance, the following fetches the ARN of the active AWS user associated with the local developers AWS credentials.

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws sts get-caller-identity --query Arn --output text --region us-east1
```
**Output**
```
arn:aws:iam::[account-number]:user/[username]
```
{{% /tab %}}
{{< /tabs >}}

For the above output, `iam` refers to the AWS Identity Access Management service. This is followed by the account number which owns 
the user entity and the IAM resource is of type `user`.
### Tags

Tags are user-defined metadata that can be attached to resources. This 
can be used to distinguish and group resources.

For instance, to add a tag to your active user.

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
export USERNAME=$(aws iam get-user --query  User.UserName)
aws iam tag-user --user-name $USERNAME --tags '{"Tag": "Your it!"}'
aws iam list-user-tags --user-name $USERNAME
```
**Output**
```
{
    "Tags": [
        {
            "Tag": "Your it!"
        }
    ]
}
```
{{% /tab %}}
{{< /tabs >}}

[^1]: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html