---
title: Signing
draft: false
weight: 2
---

All canonical requests include a hash value generated from the API parameters and account credentials. When AWS recieves an API request, it generates the same hash from the provided API parameters and compares it to the original request. If the request hash and the AWS-generated hash do not match, the request is denied. The process of generating this request hash is known as _signing_.[^1]

{{% notice info %}}
There are two versions of AWS signing, version 4 and version 2, with version 2 actively being deprecated at the time of writing. As such, only version 4 is explored here.
{{% /notice %}}

#### Version 4 Signing

 The version 4 signing process consists of the following steps and components[^2]:

1. Creating the _credential scope_: This value restricts the request to the target service and region and is of the following format: `TIMESTAMP/REGION/SERVICE/SIGNING_VERSION` where the timestamp value is of form _YYYYMMDD_.

2. Generate the target string to sign: This consists of the signing algorithm used to produce the signature (AWS4-HMAC-SHA256), the Amzaon-formatted request timestamp (i.e. _YYYYMMDDHHMMSSZ_), the previously produced credential scope, and a hash of the canonical requests string, all separated by newline characters:
{{< tabs groupId="pseudo" >}}
{{% tab name="pseudocode" %}}
```
signatureString = SIGNING_ALGORITHM + "\n" +
AMAZON_DATE_TIMESTAMP + "\n" + 
CREDENTIAL_SCOPE + "\n" + 
SHA256(CANONICAL_REQUEST_STRING)
```
{{% /tab %}}
{{< /tabs >}}

3. Create the signature key: The _signature key_, used to sign the request string, is derived from the AWS secret key, Amazon-formatted request timestamp, region, and service. The folling pseudocode illustrates this process:
{{< tabs groupId="pseudo" >}}
{{% tab name="pseudocode" %}}
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
{{% tab name="pseudocode" %}}
```
signature = hexEncode(hash(signatureKey, signatureString))
```
{{% /tab %}}
{{< /tabs >}}

##### Demo

Below provides a concrete example for generating a version 4 signature from an arbitrary string:

{{< tabs groupId="code" >}}
{{% tab name="Typescript" %}}
```ts
// can_req/ts/index.ts

import * as crypto from "crypto"

const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"

function getTimestamps(): [string, string] {
    const now = new Date()
    const year = now.getUTCFullYear()
    const month = String(now.getUTCMonth()).padStart(2, '0')
    const day = String(now.getUTCDate()).padStart(2, '0')
    const hours = String(now.getUTCHours())
    const minutes = String(now.getUTCMinutes())
    const seconds = String(now.getUTCSeconds())

    const amzTimestamp = `${year}${month}${day}T${hours}${minutes}${seconds}Z`
    const reqTimestamp = `${year}${month}${day}`
    return [amzTimestamp, reqTimestamp]
}

function getCredentialScope(reqTimestamp: string, region: string, service: string): string {
    return `${reqTimestamp}/${region}/${service}/aws4_request`
}

function getStringToSign(amzTimestamp: string, scope: string, message: string): string {
    return [SIGNING_ALGORITHM, amzTimestamp, scope, computeSHA256SignatureHash(message)].join("\n")
}

function sign(key: string, message: string): string {
    return crypto.createHmac('SHA256', key).update(message).digest('base64')
}

function signHex(key: string, message: string): string {
    return crypto.createHmac('SHA256', key).update(message).digest('base64')
}

function computeSHA256SignatureHash(input: string): string {
    return crypto.createHash("SHA256").update(input).digest("hex")
}

function getAWS4SignatureKey(key: string, reqTimestamp: string, region: string, service: string): string {
    const kDate = sign("AWS4" + key, reqTimestamp)
    const kRegion = sign(kDate, region)
    const kService = sign(kRegion, service)
    const kSigning = sign(kService, "aws4_request")
    return kSigning
}

if (require.main === module) {
    // Get user input
    const secretKey = process.argv[2];
    const region = process.argv[3];
    const service = process.argv[4];
    const userInput = process.argv[5];

    // Get the required timestamp strings
    let [amzTimestamp, reqTimestamp] = getTimestamps()
    console.log("Amazon Timestamp: " + amzTimestamp)
    console.log("Req Timestamp: " + reqTimestamp)

    // Get the scope of the request (the timestamp and the target service)
    const scope = getCredentialScope(reqTimestamp, region, service)
    console.log("Credential Scope: " + scope)

    //  Get the AWS v4 signing key
    const key = getAWS4SignatureKey(secretKey, reqTimestamp, region, service)
    console.log("Signing Key: " + key)

    // Prepare string value to sign from user input
    const stringToSign = getStringToSign(amzTimestamp, scope, userInput)
    console.log("String to sign: `" + stringToSign + "`")

    // Sign and output user string
    const signature = signHex(key, stringToSign)
    console.log("Signed String: " + signature)
}

```
{{% /tab %}}
{{% tab name="Javascript" %}}
```js
// can_req/js/index.js

var crypto = require('crypto');

const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"

function getTimestamps() {
    const now = new Date()
    const year = now.getUTCFullYear()
    const month = String(now.getUTCMonth()).padStart(2, '0')
    const day = String(now.getUTCDate()).padStart(2, '0')
    const hours = String(now.getUTCHours())
    const minutes = String(now.getUTCMinutes())
    const seconds = String(now.getUTCSeconds())

    const amzTimestamp = `${year}${month}${day}T${hours}${minutes}${seconds}Z`
    const reqTimestamp = `${year}${month}${day}`
    return [amzTimestamp, reqTimestamp]
}

function getCredentialScope(reqTimestamp, region, service) {
    return `${reqTimestamp}/${region}/${service}/aws4_request`
}

function getStringToSign(amzTimestamp, scope, message) {
    return [SIGNING_ALGORITHM, amzTimestamp, scope, computeSHA256SignatureHash(message)].join("\n")
}

function sign(key, msg) {
    return crypto.createHmac('SHA256', key).update(msg).digest('base64')
}

function signHex(key, msg) {
    return crypto.createHmac('SHA256', key).update(msg).digest('base64')
}

function computeSHA256SignatureHash(input) {
    return crypto.createHash("SHA256").update(input).digest("hex")
}

function getAWS4SignatureKey(key, reqTimestamp, region, service) {
    const kDate = sign("AWS4" + key, reqTimestamp)
    const kRegion = sign(kDate, region)
    const kService = sign(kRegion, service)
    const kSigning = sign(kService, "aws4_request")
    return kSigning
}

if (require.main === module) {
    // Get user input
    const secretKey = process.argv[2];
    const region = process.argv[3];
    const service = process.argv[4];
    const userInput = process.argv[5];

    // Get the required timestamp strings
    [amzTimestamp, reqTimestamp] = getTimestamps()
    console.log("Amazon Timestamp: " + amzTimestamp)
    console.log("Req Timestamp: " + reqTimestamp)

    // Get the scope of the request (the timestamp and the target service)
    const scope = getCredentialScope(reqTimestamp, region, service)
    console.log("Credential Scope: " + scope)

    //  Get the AWS v4 signing key
    const key = getAWS4SignatureKey(secretKey, reqTimestamp, region, service)
    console.log("Signing Key: " + key)

    // Prepare string value to sign from user input
    const stringToSign = getStringToSign(amzTimestamp, scope, userInput)
    console.log("String to sign: `" + stringToSign + "`")

    // Sign and output user string
    const signature = signHex(key, stringToSign)
    console.log("Signed String: " + signature)
}

```
{{% /tab %}}
{{% tab name="Python" %}}
```py
# can_req/py/signing.py

import datetime, hashlib, hmac, sys

SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"


def get_timestamps() -> tuple[str, str]:
    """ Get strings of required timestamps for canonical requests
    """
    now = datetime.datetime.utcnow()
    amazon_timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    req_timestamp = now.strftime("%Y%m%d")
    return amazon_timestamp, req_timestamp


def get_credential_scope(req_timestamp: str, region: str, service: str) -> str:
    """ Define the scope of the request, which includes the target region and service
    """
    return "{}/{}/{}/aws4_request".format(req_timestamp, region, service)


def sign(key: str, msg: str) -> bytes:
    """ Generate the HMAC-SHA256 hash of a target string using the provided secret key
    """
    return hmac.new(key , msg.encode('utf-8'), hashlib.sha256).digest()


def compute_sha256_hash(input: str) -> str:
    """ Create SHA256 hash of a target string
    """
    m = hashlib.sha256()
    m.update(input.encode("utf-8"))
    result =  m.hexdigest()
    return result


def get_string_to_sign(amzn_date_stamp: str, scope: str, can_req: str) -> str:
    """ Get string to sign from request parameters
    """
    return "\n".join([SIGNING_ALGORITHM, amzn_date_stamp, scope, compute_sha256_hash(can_req)]).encode("utf-8")


def get_aws4_signature_key(key: str, datestamp: str, region: str, service_name: str) -> bytes:
    """ Generature canonical requests signature
    """
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

    # The scope/action permitted by the signed token
    credential_scope = get_credential_scope(req_timestamp, region, service)
    print('Credential Scope: ' + credential_scope)

    # Generate and print signed string 
    signature_key = get_aws4_signature_key(amazon_secret_key, req_timestamp, region, service)
    print ("Signing Key: " + str(signature_key))
    string_to_sign = get_string_to_sign(amazon_timestamp, credential_scope, user_input)
    print ("String to sign: " + str(string_to_sign))
    signature = hmac.new(signature_key, string_to_sign, hashlib.sha256).hexdigest()
    print("Signature: " + signature)
```
{{% /tab %}}
{{% tab name="Go" %}}
Not yet available.

![Not Found (yet)](/parrots/parrotnotfound.gif)
{{% /tab %}}
{{< /tabs >}}

[^1]: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html

[^2]: https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html
    