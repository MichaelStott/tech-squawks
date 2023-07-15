---
title: Introduction
draft: false
weight: 1
---

AWS cloud services are available through public API endpoints. Whether invoked via the AWS CLI, SDKs, or Infrastructure as Code (IaC) tools, each approach ultimately results in sending HTTP requests to AWS service endpoints. These underlying HTTP requests are referred to as _canonical requests_.

AWS canonical requests include a _signature_ generated with request parameters and _AWS secret key_. This signature enables AWS to validate the identity of the client, protect the API request data in transit, and mitigate potential relay attacks.

![Cloud Computing Overview](/images/can_req/can_req2.png)

While developers may directly create, sign, and transmit canonical requests to AWS, it is often preferable to utilize the AWS-provided CLI and SDKs. Direct canonical calls to AWS are primarily recommended in cases when developing in unsupported programming languages or where fine-grained API control is required.

#### Request Structure

<!--- Include AWS breakdown here, with below as a further breakdown-->
Canonical requests are composed of the following component:[^1]
```
CanonicalRequest =
    HTTPRequestMethod + '\n' +
    CanonicalURI + '\n' +
    CanonicalQueryString + '\n' +
    CanonicalHeaders + '\n' +
    SignedHeaders + '\n' +
    HexEncode(Hash(RequestPayload))
```

The individual components are defined below:
- HTTPRequestMethod: The HTTP operation
- CanonicalURI: Absolute path of the target resource, including the base service domain.
- CanonicalQueryString: URI-encoded query parameters
- CanonicalHeaders: List of all the HTTP headers included with the signed requests.
- SignedHeaders: Alphabetically sorted, semicolon-separated list of lowercase request header names
- RequestPayload: Payload of the target request. This is hashed and hex encoded for additional security.

<!--
The below curl example shows a more concrete example of invoking a canoincal requests using these fields:

```sh
$ curl -X $METHOD $URL \
    --header "Content-Type: $CONTENT_TYPE" \
    --header "X-Amz-Date: $X_AMZ_DATE" \
    --header "X-Amz-Target: $X_AMZ_TARGET" \
    --header "Authoziation: $SIGNING_ALGORITHM Credential=$ACCESS_KEY_ID/$REGION/$SERVICE/$SIGNING_VERSION, SignedHeaders=$SIGNED_HEADERS, Signature=$SIGNATURE" \
    --data $HASHED_PAYLOAD
```

| Property | Description | Example |
| --- | ----------- | ----- |
|  Method | HTTP method of request being invoked | GET, POST, PUT, PATCH, DELETE |
| URL | The AWS Service URL | ssm.us-west-2.amazonaws.com |
| Content-Type | Requested content type | application/x-amz-json-1.1 |
| X-Amz-Date | UTC timestamp using [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html), exluding milliseconds (YYYYMMDDTHHMMSSZ) | 20230506T203620Z |
| X-Amz-Target | Target AWS API call | AmazonSSM.GetParameter |
| Signing Algorithm | The signing algorithm used to generate the signature | AWS4-HMAC-SHA256 |
| Access Key ID | The access key ID of the credentials used to generate the signature | AKIAZGHDAQ498VRWTOBYQ |
| Region | The target AWS region | us-west-1 |
| Signed Headers | Alphabetically sorted headers used in request | content-type;host;x-amz-date;x-amz-target |
| Service | The target AWS service name | ssm |
| Signing Version | Indicates the version of the signing algorithm used when generating the signature | aws4_request |
| Signature | Signature generated from request parameters and access credentials | N/A |
| Hashed Payload | Encoded JSON payload of the API request | N/A |

The following [curl](https://curl.se/) command illustrates how these properties are used. Signature generation and payload encoding will be covered in subsequent sections.
-->
[^1]: https://docs.aws.amazon.com/IAM/latest/UserGuide/create-signed-request.html