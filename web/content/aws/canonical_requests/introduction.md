---
title: Introduction
draft: false
weight: 1
---

AWS cloud services are available to users through global or regional API endpoints. Whether users invoke these services via the AWS CLI, SDKs, or Infrastructure as Code (IaC) tools, each method ultimately results in sending HTTP requests to the desired endpoint. These raw HTTP API requests are reffered to as _canonical requests_.

AWS API requests include a _signature_ generated with a credential key pair (AWS access key ID and secret key). This signature is leveraged by AWS to validate the identity of the client, protect the API request data in transit, and mitigate potential relay attacks.

![Cloud Computing Overview](/images/can_req/can_req2.png)

While it is possible to directly create and sign canonical requests to communicate with AWS services, it is often more preferable to utilize the AWS-provided CLI and SDKs. Direct canonoical calls to AWS are primarily reccomended in cases when using the available AWS SDKs or CLI is not possible (i.e. using an unsupported programming language) or where fine-grained API control is required.

#### Request Structure

Canonical requests are of the following structure:

```
 CanonicalRequest =
  HTTPRequestMethod + '\n' +
  CanonicalURI + '\n' +
  CanonicalQueryString + '\n' +
  CanonicalHeaders + '\n' +
  SignedHeaders + '\n' +
  HexEncode(Hash(RequestPayload))
```

The individual fields are defined below:
- HTTPRequestMethod: The HTTP operation
- CanonicalURI: Absolute path of the target resouce, including the base service domain.
- CanonicalQueryString: URI-encoded query parameters
- CanonicalHeaders: List of all the HTTP headers included with the signed requests.
- SignedHeaders: Alphabetically sorted, semicolon-separated list of lowercase request header names
- RequestPayload: Payload of the target request. This is hashed and hex encoded for additional security.

