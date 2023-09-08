---
title: Requests
draft: false
weight: 3
---

The below steps provide a broad overview for how to successfully perform a canonical request to AWS services.

#### Canonical Requests

1. Procure AWS credentials, an access key ID and a secret key value, for generating the canonical request. The access key ID will indicate the identity of the caller and the secret value will be used to generate the request signature. 

2. Creating the _credential scope_: This value restricts the request to the target service and region and is of the following format: `TIMESTAMP/REGION/SERVICE/SIGNING_VERSION` where the timestamp value is of form _YYYYMMDD_.

3. Generate a SHA256 hash of the parameters included in the request body.
{{< tabs groupId="pseudo" >}}
{{% tab name="Pseudocode" %}}
```
payloadHash = SHA256(CANONICAL_REQUEST_STRING)
```
{{% /tab %}}
{{< /tabs >}}

4. Generate a string containing a list of request headers, with each key/value pair separated by newline characters. Ensure that the headers are listed alphabetically and that the resulting string is also newline terminated.
{{< tabs groupId="pseudo" >}}
{{% tab name="Pseudocode" %}}
```
canonicalHeadersString = ""
headers.sort()
for headerName, headerValue in headers:
  canonicalHeadersString += headerName + ":" + headerValue + "\n"
```
{{% /tab %}}
{{< /tabs >}}

5. Generate a string containing all the canonical request information, including the HTTP method, request URI, query parameters, the previously generated header string, alphabetically listed headers used in signing process, and the previously generated request payload hash separated by newline characters. 
{{< tabs groupId="pseudo" >}}
{{% tab name="Pseudocode" %}}
```
canonicalRequest = httpMethod + "\n" +
  requestUri + "\m" + 
  queryString + "\n" + 
  canonicalHeadersString + "\m"  + 
  SIGNED_HEADERS + "\m" +
  payloadHash
```
{{% /tab %}}
{{< /tabs >}}

6. Following the steps outline in the previous [section]({{< ref "signing.md" >}} "Request Signing Instructions"), generate the request signature.

7. Generate the authorization header from the following components.
{{< tabs groupId="pseudo" >}}
{{% tab name="Pseudocode" %}}
```
authorizationHeader = `${SIGNING_ALGORITHM} Credential=${amazonKeyId}/${scope}, SignedHeaders=${SIGNED_HEADERS}, Signature=${signature}`;
```
{{% /tab %}}
{{< /tabs >}}

8. Perform an HTTP request with the canonical request parameters.
{{< tabs groupId="pseudo" >}}
{{% tab name="Pseudocode" %}}
```
http_request(endpoint=URI + QUERY_PARAMATERS, headers={header_1=value_1, header_2=value_2, ..., header_n=value_n, Authorization=authorizationHeader}, data=apiParameters, method=httpMethod)
```
{{% /tab %}}
{{< /tabs >}}

#### Demo

The following are concrete code examples demonstrating how to generate and send a canonical request to list the AWS account users. For those interested, the AWS SDKs can provide further concrete examples for handling canonical requests in a more general manner.

{{< tabs groupId="code" >}}
{{< tab name="Typescript" >}}
{{< tabs >}}
{{% tab name="Execution" %}}
```
ts-node request.ts $AWS_ACCESS_KEY_ID $AWS_SECRET_KEY
```
{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="request.ts" %}}
```ts
// can_req/ts/request.ts

import * as signing from "./signing";
import * as https from "https";

const METHOD = "GET";
const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256";
const CONTENT_TYPE = "application/x-amz-json-1.1";
const SERVICE = "iam";
const HOST = "iam.amazonaws.com";
const REGION = "us-east-1";
const SIGNED_HEADERS = "content-type;host;x-amz-date";
const CANONICAL_URI = "/";
const CANONICAL_QUERY_STRING = "Action=ListUsers&Version=2010-05-08";

function getCanonicalHeaders(amzTimestamp: string) {
  return [
    "content-type:" + CONTENT_TYPE,
    "host:" + HOST,
    "x-amz-date:" + amzTimestamp + "\n",
  ].join("\n");
}

function getCanonicalRequest(canonicalHeaders: string, payloadHash: string) {
  return [
    METHOD,
    CANONICAL_URI,
    CANONICAL_QUERY_STRING,
    canonicalHeaders,
    SIGNED_HEADERS,
    payloadHash,
  ].join("\n");
}

function getAuthorizationHeader(
  scope: string,
  signature: string,
  amazonKeyId: string
) {
  return `${SIGNING_ALGORITHM} Credential=${amazonKeyId}/${scope}, SignedHeaders=${SIGNED_HEADERS}, Signature=${signature}`;
}

if (require.main === module) {
  // Get user input
  const amazonKeyId = process.argv[2];
  const secretKey = process.argv[3];

  // Get the required timestamp strings
  let [amzTimestamp, reqTimestamp] = signing.getTimestamps();
  console.log("Amazon Timestamp: " + amzTimestamp);
  console.log("Req Timestamp: " + reqTimestamp);

  // Get the scope of the request (the timestamp and the target service)
  const scope = signing.getCredentialScope(reqTimestamp, REGION, SERVICE);
  console.log("Credential Scope: " + scope);
  
  // API  parameters should be listed here when applicable.
  const requestParamters = ``;
  const payloadHash = signing.computeSHA256SignatureHash(requestParamters);

  const headers = getCanonicalHeaders(amzTimestamp);
  const canonicalRequest = getCanonicalRequest(headers, payloadHash);

  //  Get the AWS v4 signing key
  const key = signing.getAWS4SignatureKey(
    secretKey,
    reqTimestamp,
    REGION,
    SERVICE
  );
  const stringToSign = signing.getStringToSign(
    amzTimestamp,
    scope,
    canonicalRequest
  );

  // Sign and output user string
  const signature = signing.signHex(key, Buffer.from(stringToSign));
  console.log("Signature: " + signature);

  const authHeader = getAuthorizationHeader(scope, signature, amazonKeyId);
  console.log("Auth Header: " + authHeader);

  const canReqHeaders = {
    "Accept-Encoding": "identity",
    "Content-Type": CONTENT_TYPE,
    "X-Amz-Date": amzTimestamp,
    Authorization: authHeader,
    "Content-Length": requestParamters.length,
  };

  var options = {
    hostname: HOST,
    path: "/?Action=ListUsers&Version=2010-05-08",
    port: 443,
    method: METHOD,
    headers: canReqHeaders,
  };
  var req = https.request(options, function (res) {
    res.on("data", (d) => {
      process.stdout.write(d);
    });
  });
  req.write(requestParamters);
  req.end();
}

```
{{% /tab %}}
{{% tab name="signing.ts" %}}
```ts
// can_req/ts/signing.ts

import * as crypto from "crypto";

const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256";

export function getTimestamps(): [string, string] {
  const now = new Date();
  const year = now.getUTCFullYear();
  const month = String(now.getUTCMonth() + 1).padStart(2, "0");
  const day = String(now.getUTCDate()).padStart(2, "0");
  const hours = String(now.getUTCHours()).padStart(2, "0");
  const minutes = String(now.getUTCMinutes()).padStart(2, "0");
  const seconds = String(now.getUTCSeconds()).padStart(2, "0");

  const amzTimestamp = `${year}${month}${day}T${hours}${minutes}${seconds}Z`;
  const reqTimestamp = `${year}${month}${day}`;
  return [amzTimestamp, reqTimestamp];
}

export function getCredentialScope(
  reqTimestamp: string,
  region: string,
  service: string
): string {
  return `${reqTimestamp}/${region}/${service}/aws4_request`;
}

export function getStringToSign(
  amzTimestamp: string,
  scope: string,
  message: string
): string {
  return [
    SIGNING_ALGORITHM,
    amzTimestamp,
    scope,
    computeSHA256SignatureHash(message),
  ].join("\n");
}

export function sign(key: Buffer, message: Buffer): Buffer {
  return crypto.createHmac("SHA256", key).update(message).digest();
}

export function signHex(key: Buffer, message: Buffer): string {
  return crypto.createHmac("SHA256", key).update(message).digest("hex");
}

export function computeSHA256SignatureHash(input: string): string {
  return crypto.createHash("SHA256").update(input).digest("hex");
}

export function getAWS4SignatureKey(
  key: string,
  reqTimestamp: string,
  region: string,
  service: string
): Buffer {
  const kDate = sign(Buffer.from("AWS4" + key), Buffer.from(reqTimestamp));
  const kRegion = sign(kDate, Buffer.from(region));
  const kService = sign(kRegion, Buffer.from(service));
  const kSigning = sign(kService, Buffer.from("aws4_request"));
  return kSigning;
}

if (require.main === module) {
  // Get user input
  const secretKey = process.argv[2];
  const region = process.argv[3];
  const service = process.argv[4];
  const userInput = process.argv[5];

  // Get the required timestamp strings
  let [amzTimestamp, reqTimestamp] = getTimestamps();
  console.log("Amazon Timestamp: " + amzTimestamp);
  console.log("Requset Timestamp: " + reqTimestamp);

  // Get the scope of the request (the timestamp and the target service)
  const scope = getCredentialScope(reqTimestamp, region, service);
  console.log("Credential Scope: " + scope);

  //  Get the AWS v4 signing key
  const key = getAWS4SignatureKey(secretKey, reqTimestamp, region, service);
  console.log("Signing Key: " + key.toString("hex"));

  // Prepare string value to sign from user input
  const stringToSign = getStringToSign(amzTimestamp, scope, userInput);
  console.log("String to sign: " + JSON.stringify(stringToSign));

  // Sign and output user string
  const signature = signHex(key, Buffer.from(stringToSign));
  console.log("Signed String: " + signature);
}

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/ts" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< tab name="Javascript" >}}
{{< tabs >}}
{{% tab name="Execution" %}}
```
node request.js $AWS_ACCESS_KEY_ID $AWS_SECRET_KEY
```
{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="request.js" %}}
```js
// can_req/js/request.js

const signing = require(`./signing.js`);
const https = require("https");

const METHOD = "GET";
const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256";
const CONTENT_TYPE = "application/x-amz-json-1.1";
const SERVICE = "iam";
const HOST = "iam.amazonaws.com";
const REGION = "us-east-1";
const SIGNED_HEADERS = "content-type;host;x-amz-date";
const CANONICAL_URI = "/";
const CANONICAL_QUERY_STRING = "Action=ListUsers&Version=2010-05-08";

function getCanonicalHeaders(amzTimestamp) {
  return [
    "content-type:" + CONTENT_TYPE,
    "host:" + HOST,
    "x-amz-date:" + amzTimestamp + "\n",
  ].join("\n");
}

function getCanonicalRequest(canonicalHeaders, payloadHash) {
  return [
    METHOD,
    CANONICAL_URI,
    CANONICAL_QUERY_STRING,
    canonicalHeaders,
    SIGNED_HEADERS,
    payloadHash,
  ].join("\n");
}

function getAuthorizationHeader(scope, signature, amazonKeyId) {
  return `${SIGNING_ALGORITHM} Credential=${amazonKeyId}/${scope}, SignedHeaders=${SIGNED_HEADERS}, Signature=${signature}`;
}

if (require.main === module) {
  // Get user input
  const amazonKeyId = process.argv[2];
  const secretKey = process.argv[3];

  // Get the required timestamp strings
  [amzTimestamp, reqTimestamp] = signing.getTimestamps();
  console.log("Amazon Timestamp: " + amzTimestamp);
  console.log("Request Timestamp: " + reqTimestamp);

  // Get the scope of the request (the timestamp and the target service)
  const scope = signing.getCredentialScope(reqTimestamp, REGION, SERVICE);
  console.log("Credential Scope: " + scope);

  const requestParamters = ``;
  const payloadHash = signing.computeSHA256SignatureHash(requestParamters);

  const headers = getCanonicalHeaders(amzTimestamp);
  const canonicalRequest = getCanonicalRequest(headers, payloadHash);

  //  Get the AWS v4 signing key
  const key = signing.getAWS4SignatureKey(
    secretKey,
    reqTimestamp,
    REGION,
    SERVICE
  );
  console.log("Signing Key: " + key.toString("hex"));

  // Prepare string value to sign from user input
  const stringToSign = signing.getStringToSign(
    amzTimestamp,
    scope,
    canonicalRequest
  );

  // Sign and output user string
  const signature = signing.signHex(key, stringToSign);
  console.log("Signature: " + signature);

  const authHeader = getAuthorizationHeader(scope, signature, amazonKeyId);
  console.log("Auth Header: " + authHeader);

  const canReqHeaders = {
    "Accept-Encoding": "identity",
    "Content-Type": CONTENT_TYPE,
    "X-Amz-Date": amzTimestamp,
    Authorization: authHeader,
    "Content-Length": requestParamters.length,
  };

  var options = {
    hostname: HOST,
    path: "/?" + CANONICAL_QUERY_STRING,
    port: 443,
    method: METHOD,
    headers: canReqHeaders,
  };
  var req = https.request(options, function (res) {
    res.on("data", (d) => {
      process.stdout.write(d);
    });
  });
  req.write(requestParamters);
  req.end(options.body || "").on("error", (err) => {
    console.log("Error: " + err.message);
  });
}

```
{{% /tab %}}
{{% tab name="signing.js" %}}
```js
// can_req/js/signing.js

var crypto = require("crypto");

const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256";

function getTimestamps() {
  const now = new Date();
  const year = now.getUTCFullYear();
  const month = String(now.getUTCMonth() + 1).padStart(2, "0");
  const day = String(now.getUTCDate()).padStart(2, "0");
  const hours = String(now.getUTCHours()).padStart(2, "0");
  const minutes = String(now.getUTCMinutes()).padStart(2, "0");
  const seconds = String(now.getUTCSeconds()).padStart(2, "0");

  const amzTimestamp = `${year}${month}${day}T${hours}${minutes}${seconds}Z`;
  const reqTimestamp = `${year}${month}${day}`;
  return [amzTimestamp, reqTimestamp];
}

function getCredentialScope(reqTimestamp, region, service) {
  return `${reqTimestamp}/${region}/${service}/aws4_request`;
}

function getStringToSign(amzTimestamp, scope, message) {
  return [
    SIGNING_ALGORITHM,
    amzTimestamp,
    scope,
    computeSHA256SignatureHash(message),
  ].join("\n");
}

function sign(key, msg) {
  return crypto
    .createHmac("SHA256", key)
    .update(Buffer.from(msg, "utf-8"))
    .digest();
}

function signHex(key, msg) {
  return crypto.createHmac("SHA256", key).update(msg).digest("hex");
}

function computeSHA256SignatureHash(input) {
  return crypto
    .createHash("SHA256")
    .update(Buffer.from(input, "utf-8"))
    .digest("hex");
}

function getAWS4SignatureKey(key, reqTimestamp, region, service) {
  const kDate = sign(Buffer.from("AWS4" + key, "utf-8"), reqTimestamp);
  const kRegion = sign(kDate, region);
  const kService = sign(kRegion, service);
  const kSigning = sign(kService, "aws4_request");
  return kSigning;
}

if (require.main === module) {
  // Get user input
  const secretKey = process.argv[2];
  const region = process.argv[3];
  const service = process.argv[4];
  const userInput = process.argv[5];

  // Get the required timestamp strings
  [amzTimestamp, reqTimestamp] = getTimestamps();
  console.log("Amazon Timestamp: " + amzTimestamp);
  console.log("Request Timestamp: " + reqTimestamp);

  // Get the scope of the request (the timestamp and the target service)
  const scope = getCredentialScope(reqTimestamp, region, service);
  console.log("Credential Scope: " + scope);

  //  Get the AWS v4 signing key
  const key = getAWS4SignatureKey(secretKey, reqTimestamp, region, service);
  console.log("Signing Key: " + key.toString("hex"));

  // Prepare string value to sign from user input
  const stringToSign = getStringToSign(amzTimestamp, scope, userInput);
  console.log("String to sign: " + JSON.stringify(stringToSign));

  // Sign and output user string
  const signature = signHex(key, stringToSign);
  console.log("Signed String: " + signature);
}

module.exports = {
  getTimestamps,
  getCredentialScope,
  computeSHA256SignatureHash,
  getAWS4SignatureKey,
  getStringToSign,
  signHex,
};

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/js" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< tab name="Python" >}}
{{< tabs >}}
{{% tab name="Execution" %}}
```
python3 request.py $AWS_ACCESS_KEY_ID $AWS_SECRET_KEY
```
{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="request.py" %}}
```py
# can_req/py/request.py

from signing import *

import requests
import xml.dom.minidom

# Default API parameters provided here for convenience
METHOD = "GET"
SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"
CONTENT_TYPE = "application/x-amz-json-1.1"
SERVICE = "iam"
HOST = "iam.amazonaws.com"
REGION = "us-east-1"
SIGNED_HEADERS = "content-type;host;x-amz-date"
CANONICAL_URI = "/"
CANONICAL_QUERY_STRING = "Action=ListUsers&Version=2010-05-08"


def get_canonical_headers(amzn_date: str) -> str:
    """Get canonical headers in proper format"""
    return "\n".join(
        [
            "content-type:{}".format(CONTENT_TYPE),
            "host:{}".format(HOST),
            "x-amz-date:{}\n".format(amzn_date),
        ]
    )


def get_canonical_requests(canonical_headers: str, payload_hash: str) -> str:
    """Generate canonical request from the provided headers and payload hash"""
    return "\n".join(
        [
            METHOD,
            CANONICAL_URI,
            CANONICAL_QUERY_STRING,
            canonical_headers,
            SIGNED_HEADERS,
            payload_hash,
        ]
    )


def get_authorization_header(scope: str, signature: str, amazon_key_id: str) -> str:
    """Get the authorization header used for verifying the authenticity of the request"""
    return "{} Credential={}/{}, SignedHeaders={}, Signature={}".format(
        SIGNING_ALGORITHM, amazon_key_id, scope, SIGNED_HEADERS, signature
    )


if __name__ == "__main__":
    # Get provided AWS access credentials
    amazon_key_id = sys.argv[1]
    amazon_secret_key = sys.argv[2]

    endpoint = "https://{}/".format(HOST)
    amazon_timestamp, req_timestamp = get_timestamps()
    print("Amazon Timestamp: " + amazon_timestamp)
    print("Request Timestamp: " + req_timestamp)

    credential_scope = get_credential_scope(req_timestamp, REGION, SERVICE)
    print("Credential Scope: " + credential_scope)

    # API parameters should be listed here when applicable.
    request_paramters = ""
    payload_hash = compute_sha256_hash(request_paramters)

    headers = get_canonical_headers(amazon_timestamp)
    canoniocal_request = get_canonical_requests(headers, str(payload_hash))

    signature_key = get_aws4_signature_key(
        amazon_secret_key, req_timestamp, REGION, SERVICE
    )
    print("Signing Key: " + base64.b64encode(signature_key).decode())
    string_to_sign = get_string_to_sign(
        amazon_timestamp, credential_scope, canoniocal_request
    )
    signature = hmac.new(
        signature_key, (string_to_sign).encode("utf-8"), hashlib.sha256
    ).hexdigest()
    print("Signature: " + signature)

    auth_header = get_authorization_header(credential_scope, signature, amazon_key_id)
    print("Auth Header: " + auth_header)

    # Perform AWS API call
    headers = {
        "Accept-Encoding": "identity",
        "Content-Type": CONTENT_TYPE,
        "X-Amz-Date": amazon_timestamp,
        "Authorization": auth_header,
    }
    resp = requests.get(
        "https://iam.amazonaws.com/?Action=ListUsers&Version=2010-05-08",
        headers=headers,
    )
    print(
        "\nAPI Response:\n"
        + xml.dom.minidom.parseString(resp.content).toprettyxml(indent="", newl="")
    )

```
{{% /tab %}}
{{% tab name="signing.py" %}}
```py
# can_req/py/signing.py

import base64, datetime, hashlib, hmac, json, sys

SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"


def get_timestamps() -> tuple[str, str]:
    """Get strings of required timestamps for canonical requests"""
    now = datetime.datetime.utcnow()
    amazon_timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    req_timestamp = now.strftime("%Y%m%d")
    return amazon_timestamp, req_timestamp


def get_credential_scope(req_timestamp: str, region: str, service: str) -> str:
    """Define the scope of the request, which includes the target region and service"""
    return "{}/{}/{}/aws4_request".format(req_timestamp, region, service)


def sign(key: str, msg: str) -> bytes:
    """Generate the HMAC-SHA256 hash of a target string using the provided secret key"""
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def compute_sha256_hash(input: str) -> str:
    """Create SHA256 hash of a target string"""
    m = hashlib.sha256()
    m.update(input.encode("utf-8"))
    result = m.hexdigest()
    return result


def get_string_to_sign(amzn_date_stamp: str, scope: str, can_req: str) -> str:
    """Get string to sign from request parameters"""
    return "\n".join(
        [SIGNING_ALGORITHM, amzn_date_stamp, scope, compute_sha256_hash(can_req)]
    )


def get_aws4_signature_key(
    key: str, datestamp: str, region: str, service_name: str
) -> bytes:
    """Generature canonical requests signature"""
    kdate = sign(("AWS4" + key).encode("utf-8"), datestamp)
    kregion = sign(kdate, region)
    kservice = sign(kregion, service_name)
    ksigning = sign(kservice, "aws4_request")
    return ksigning


if __name__ == "__main__":
    # Get user input from command args
    amazon_secret_key = sys.argv[1]
    region = sys.argv[2]
    service = sys.argv[3]
    user_input = sys.argv[4]

    # Fetch the required timestamps
    amazon_timestamp, req_timestamp = get_timestamps()
    print("Amazon Timestamp: " + amazon_timestamp)
    print("Request Timestamp: " + req_timestamp)

    # The scope/action permitted by the signed credentials
    credential_scope = get_credential_scope(req_timestamp, region, service)
    print("Credential Scope: " + credential_scope)

    # Generate and print signed string
    signature_key = get_aws4_signature_key(
        amazon_secret_key, req_timestamp, region, service
    )
    print("Signing Key: " + base64.b64encode(signature_key).decode())
    string_to_sign = get_string_to_sign(amazon_timestamp, credential_scope, user_input)
    print("String to sign: " + json.dumps(string_to_sign))
    signature = hmac.new(
        signature_key, string_to_sign.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    print("Signed String: " + signature)

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/py" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< tab name="Go" >}}
{{< tabs >}}
{{% tab name="Execution" %}}
```
go run request.go signing.go $AWS_ACCESS_KEY_ID $AWS_SECRET_KEY
```
{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="request.go" %}}
```go
// can_req/go/request.go

package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
)

const METHOD = "GET"
const CONTENT_TYPE = "application/x-amz-json-1.1"
const SERVICE = "iam"
const HOST = "iam.amazonaws.com"
const REGION = "us-east-1"
const SIGNED_HEADERS = "content-type;host;x-amz-date"
const CANONICAL_URI = "/"
const CANONICAL_QUERY_STRING = "Action=ListUsers&Version=2010-05-08"

func getCanonicalHeaders(amazonDate string) string {
	headers := [...]string{"content-type:" + CONTENT_TYPE, "host:" + HOST, "x-amz-date:" + amazonDate + "\n"}
	return strings.Join(headers[:], "\n")
}

func getCanonicalRequest(canonicalHeaders string, payloadHash string) string {
	requestComponents := [...]string{METHOD, CANONICAL_URI, CANONICAL_QUERY_STRING, canonicalHeaders, SIGNED_HEADERS, payloadHash}
	return strings.Join(requestComponents[:], "\n")
}

func getAuthorizationHeader(scope string, signature string, amazonKeyId string) string {
	return fmt.Sprintf("%s Credential=%s/%s, SignedHeaders=%s, Signature=%s", SIGNING_ALGORITHM, amazonKeyId, scope, SIGNED_HEADERS, signature)
}

func main() {
	// Get user input from command args
	amazon_key_id := os.Args[1]
	amazon_secret_key := os.Args[2]

	// Fetch the required timestamps
	amazon_timestamp, request_timestamp := getTimestamps()
	fmt.Printf("Amazon Timestamp: %s\n", amazon_timestamp)
	fmt.Printf("Request Timestamp: %s\n", request_timestamp)

	// Get the scope of the request (the timestamp and the target service)
	scope := getCredentialScope(request_timestamp, REGION, SERVICE)
	fmt.Printf("Credential Scope: %s\n", scope)

	// API parameters should be listed here when applicable.
	requestParamters := ``
	payloadHash := computeSHA256Hash(requestParamters)

	headers := getCanonicalHeaders(amazon_timestamp)
	canonical_request := getCanonicalRequest(headers, payloadHash)

	signature_key := getAWS4SignatureKey(amazon_secret_key, request_timestamp, REGION, SERVICE)
	fmt.Printf("Signing Key: %x\n", signature_key)
	string_to_sign := getStringToSign(amazon_timestamp, scope, canonical_request)

	// Sign and output user string
	signature := signHex(signature_key, string_to_sign)
	fmt.Printf("Signature: %s\n", signature)

	auth_header := getAuthorizationHeader(scope, signature, amazon_key_id)
	fmt.Printf("Auth Header: %s\n", auth_header)

	client := &http.Client{}
	endpoint := fmt.Sprintf("https://%s/?"+CANONICAL_QUERY_STRING, HOST)
	req, err := http.NewRequest(METHOD, endpoint, bytes.NewBuffer([]byte(requestParamters)))
	if err != nil {
		fmt.Println(err)
		return
	}
	req.Header.Add("Accept-Encoding", "identity")
	req.Header.Add("Content-Type", CONTENT_TYPE)
	req.Header.Add("X-Amz-Date", amazon_timestamp)
	req.Header.Add("Authorization", auth_header)
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(string(body))
}

```
{{% /tab %}}
{{% tab name="signing.go" %}}
```go
// can_req/go/signing.go

ackage main

import (
	hmac "crypto/hmac"
	"crypto/sha256"
	"encoding/json"
	"fmt"
	"os"
	"strings"
	"time"
)

const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"

func getTimestamps() (string, string) {
	now := time.Now().UTC()
	return now.Format("20060102T150405Z"), now.Format("20060102")
}

func getCredentialScope(request_timestamp string, region string, service string) string {
	return fmt.Sprintf("%s/%s/%s/aws4_request", request_timestamp, region, service)
}

func sign(key string, message string) string {
	mac := hmac.New(sha256.New, []byte(key))
	mac.Write([]byte(message))
	return string(mac.Sum(nil))
}

func signHex(key string, message string) string {
	mac := hmac.New(sha256.New, []byte(key))
	mac.Write([]byte(message))
	return fmt.Sprintf("%x", string(mac.Sum(nil)))
}

func computeSHA256Hash(input string) string {
	hash := sha256.New()
	hash.Write([]byte(input))
	return fmt.Sprintf("%x", string(hash.Sum(nil)))
}

func getStringToSign(amazon_timestamp string, scope string, can_req string) string {
	components := [...]string{SIGNING_ALGORITHM, amazon_timestamp, scope, computeSHA256Hash(can_req)}
	return strings.Join(components[:], "\n")
}

func getAWS4SignatureKey(secret_key string, request_timestamp string, region string, service string) string {
	kdate := sign("AWS4"+secret_key, request_timestamp)
	kregion := sign(kdate, region)
	kservice := sign(kregion, service)
	ksigning := sign(kservice, "aws4_request")
	return ksigning
}

func runDemo() {
	// Get user input from command args
	amazon_secret_key := os.Args[1]
	region := os.Args[2]
	service := os.Args[3]
	user_input := os.Args[4]

	// Fetch the required timestamps
	amazon_timestamp, request_timestamp := getTimestamps()
	fmt.Printf("Amazon Timestamp: %s\n", amazon_timestamp)
	fmt.Printf("Request Timestamp: %s\n", request_timestamp)

	// Get the scope/permitted API action for the signed credentials
	credential_scope := getCredentialScope(request_timestamp, region, service)
	fmt.Printf("Credential Scope: %s\n", credential_scope)

	// Generate and print signed string
	signature_key := getAWS4SignatureKey(amazon_secret_key, request_timestamp, region, service)
	fmt.Printf("Signing Key: %x\n", signature_key)
	string_to_sign := getStringToSign(amazon_timestamp, credential_scope, user_input)
	string_to_sign_formatted, _ := json.Marshal(string_to_sign)
	fmt.Printf("String to sign: `%s`\n", string_to_sign_formatted)
	signature := signHex(signature_key, string_to_sign)
	fmt.Printf("Signed String: " + signature)
}

```
{{% /tab %}}
{{< /tabs >}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/go" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< /tabs >}}

**Output**
```
Amazon Timestamp: 20230625T182331Z
Req Timestamp: 20230625
Credential Scope: 20230625/us-west-2/ssm/aws4_request
Signature: 5a5ebdb8797f0568c19f2ea45d70bc77309ae11eff9a69990202871db3cdbcde
Auth Header: AWS4-HMAC-SHA256 Credential=BKDZY123A2Z4DV37XABC/20230625/us-west-2/ssm/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=5a5ebdb8797f0568c19f2ea45d70bc77309ae11eff9a69990202871db3cdbcde

API Response:
<?xml version="1.0" ?>
<ListUsersResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ListUsersResult>
    <IsTruncated>false</IsTruncated>
    <Users>
      <member>
        <Path>/</Path>
        <UserName>username</UserName>
        <Arn>arn:aws:iam::563175520123456789104152:user/username</Arn>
        <UserId>BIDAFHH7AT44NDI6LEIYP</UserId>
        <CreateDate>2019-07-10T23:13:11Z</CreateDate>
      </member>
    </Users>
  </ListUsersResult>
  <ResponseMetadata>
    <RequestId>482ac647-51b2-47cd-9aa2-2eafe6bb8c8b</RequestId>
  </ResponseMetadata>
</ListUsersResponse>
```