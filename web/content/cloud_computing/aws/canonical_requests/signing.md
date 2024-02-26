---
title: Signing
draft: false
weight: 2
---

All canonical requests include a hash value generated from the API parameters and account credentials. When AWS receives an API request, it generates the same hash from the provided API parameters and compares it to the original request to validate the identity of the caller. If the request hash and the AWS-generated hash do not match, the request is denied. The process of generating this request hash is known as _signing_.[^1]

{{% notice info %}}
There are two versions of AWS signing, version 4 and version 2, with version 2 being deprecated at the time of writing. As such, only version 4 is explored here.
{{% /notice %}}

#### Version 4 Signing

The version 4 signing process consists of the following steps and components[^2]:

1. Creating the _credential scope_: This value restricts the request to the target service and region and is of the following format: `TIMESTAMP/REGION/SERVICE/SIGNING_VERSION` where the timestamp value is of form _YYYYMMDD_.

2. Generate the target string to sign: This consists of the signing algorithm used to produce the signature (AWS4-HMAC-SHA256), the Amzaon-formatted request timestamp (i.e. _YYYYMMDDHHMMSSZ_), the previously produced credential scope, and a hash of the canonical requests string, all separated by newline characters:
   {{< tabs groupId="pseudo" >}}
   {{% tab name="Pseudocode" %}}

```
signatureString = SIGNING_ALGORITHM + "\n" +
AMAZON_DATE_TIMESTAMP + "\n" +
CREDENTIAL_SCOPE + "\n" +
SHA256(CANONICAL_REQUEST_STRING)
```

{{% /tab %}}
{{< /tabs >}}

3. Create the signature key: The _signature key_, used to sign the request string, is derived from the AWS secret key, Amazon-formatted request timestamp, region, and service. The following Pseudocode illustrates this process:
   {{< tabs groupId="pseudo" >}}
   {{% tab name="Pseudocode" %}}

```
kDate = hash("AWS4" + Key, Date)
kRegion = hash(kDate, Region)
kService = hash(kRegion, Service)
signatureKey = hash(kService, "aws4_request")
```

{{% /tab %}}
{{< /tabs >}}

4. Sign the previously generated signature string with the signature key and encode the hexadecimal representation.
   {{< tabs groupId="pseudo" >}}
   {{% tab name="Pseudocode" %}}

```
signature = hexEncode(hash(signatureKey, signatureString))
```

{{% /tab %}}
{{< /tabs >}}

##### Demo

Below provides a concrete example for generating a version 4 signature from an arbitrary string:

{{< tabs groupId="code" >}}
{{< tab name="Typescript" >}}
{{< tabs >}}
{{% tab name="Execution" %}}

```
ts-node signing.ts $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
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
node signing.js $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
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
python3 signing.py $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
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
go run signing_driver.go signing.go $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
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
{{% tab name="signing_driver.go" %}}

```go
// can_req/go/signing_driver.go

package main

func main() {
	runDemo()
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
Amazon Timestamp: 20230625T174754Z
Requset Timestamp: 20230625
Credential Scope: 20230625/us-west-1/ssm/aws4_request
Signing Key: 843b458b4664ec9c54e42274a490b2c7cb2802cc104dcba2ad2df8fe71c008ff
String to sign: "AWS4-HMAC-SHA256\n20230625T174754Z\n20230625/us-west-1/ssm/aws4_request\n7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069"
Signed String: cc1a8368f317707c89b33e8f627f722819ed4d28341fef7b56720103b5d3fe79
```

[^1]: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
[^2]: https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html
