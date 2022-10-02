---
title: Operations
draft: false
weight: 3
---

### AssumeRole

Returns a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to. These temporary credentials consist of an access key ID, a secret access key, and a security token. Typically, you use AssumeRole within your account or for cross-account access.

### AssumeRoleWithSAML

Returns a set of temporary security credentials for users who have been authenticated via a SAML authentication response. This operation provides a mechanism for tying an enterprise identity store or directory to role-based AWS access without user-specific credentials or configuration.

### AssumeROleWithWebIdentity

Returns a set of temporary security credentials for users who have been authenticated in a mobile or web application with a web identity provider. 

### DecodeAuthorizationMessage

Decodes additional information about the authorization status of a request from an encoded message returned in response to an AWS request.

### GetAccessKeyInfo

Returns the account identifier for the specified access key ID.

Access keys consist of two parts: an access key ID (for example, AKIAIOSFODNN7EXAMPLE) and a secret access key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY). For more information about access keys, see Managing Access Keys for IAM Users in the IAM User Guide.

### GetCallerIdentity

Returns details about the IAM user or role whose credentials are used to call the operation.

### GetFederatedToken

Returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for a federated user. 

### GetSessionToken

Returns a set of temporary credentials for an AWS account or IAM user. The credentials consist of an access key ID, a secret access key, and a security token. Typically, you use GetSessionToken if you want to use MFA to protect programmatic calls to specific AWS API operations.
