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

```sh
$ curl -X $METHOD -H "Content-Type: $X_Amz_Date" -H "X-Amz-Target: $X_AMX_TARGET" -H "Authorization: $Authorization" $URL --data $PAYLOAD
```

| HTTP Section | Description | Example |
| --- | ----------- | ----- |
|  Method | HTTP method of request being invoked | GET, POST, PUT, PATCH, DELETE |
| URL | The AWS Service URL | ssm.us-west-2.amazonaws.com |
| Content-Type | Requested content type | application/x-amz-json-1.1 |
| X-Amz-Date | UTC timestamp using [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html), exluding milliseconds (YYYYMMDDTHHMMSSZ) | 20230506T203620Z |
| X-Amz-Target | Target AWS service | AmazonSSM.GetParameter |
| Authorization | Authorization header consisting of the name of the signing algorithm, credentials, alphabetically sorted request headers, and signature. | AWS4-HMAC-SHA256 Credential=..., SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=... |
| Payload | Hased JSON payload of the API request | {"Name": "SSMParameterName","WithDecryption": true} |
