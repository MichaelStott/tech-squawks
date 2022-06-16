---
title: Resources
draft: false
weight: 4
---

An AWS _resource_ is a broad term for any cloud resource that can be provisioned in AWS. Anything from a server, a virtual network, security policy, account user, etc. is considered a resource. Every resource has an associated Amazon Resource Number (ARN)
which uniquely identifies it. For instance, the following fetches the ARN of the active AWS user associated with 
the local developers AWS credentials.

**CLI**
```sh
aws sts get-caller-identity --query Arn --output text
```
**Output**
```
arn:aws:iam::[account-number]:user/[username]
```

### Tags

Tags are user-defined metadata that can be attached to resources. This 
can be used to distinguish and group resources.

For instance, to add a tag to your active user.

**CLI**
```sh
aws iam tag-user --user-name [username] --tags '{"Key": "Tagged", "Value": "True"}'
aws iam list-user-tags --user-name [username]
```
**Output**
```
arn:aws:iam::[account-number]:user/[username]
```