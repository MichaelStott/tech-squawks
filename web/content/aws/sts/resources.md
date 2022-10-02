---
title: Resources
draft: false
weight: 2
---

The following provides a breif reference of the entities provided by the STS service

### AssumedRoleUser

Provides the identifier information pertaining to a given assumed role during the credential fetch process.

**Properties**
- _Arn_: ARN of the credentials returned when assuming a given Role.
- _AssumedRoleId_: Identifier of the IAM Role.

### Credentials

Credentials for AWS API authentication.

**Properties**
- _AccessKeyId_: Identifier of the temporary access credentials.
- _Expiration_: Date when credentials are invalid.
- _SecretAccessKey_: The secret access key value used to sign request.
- _SessionToken_: Token used to authenticate API requests.

### FederatedUser

Used to identify a federated user associate with credentials.

**Properties**
- _Arn_: ARN of the federated user.
- _FederatedUserId_: Identifier of the federated user associated with the credentials.

### PolicyDescriptorType

A reference to an IAM managed policy that is used as an STS session policy for a role or federated user session.

**Properties**
- _Arn_: ARN Of the IAM policy used as a STS session policy.

### Tag

User-defined metadata defined when you assume a role or federate a user.

**Properties**
- _Key_: Key or label for a session tag
- _Tag_: Value for a session tag.