---
title: Requests
draft: false
weight: 3
---

The following code snippets demonstrate sending canonical rqeuests to AWS. For interested readers, the AWS SDKs can provide
further concrete examples that handle this in a more general fashion.

{{< tabs groupId="code" >}}
{{% tab name="Typescript" %}}
```ts
// can_req/ts/request.ts

import * as signing from './signing';
import * as https from 'https';

const METHOD = "POST"
const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"
const AMAZON_TARGET = "AmazonSSM.GetParameter"
const CONTENT_TYPE = "application/x-amz-json-1.1"
const PARAMETER_NAME = "TechSquawkParam"
const SERVICE = "ssm"
const HOST = "ssm.us-west-2.amazonaws.com"
const REGION = "us-west-2"
const SIGNED_HEADERS = "content-type;host;x-amz-date;x-amz-target"
const CANONICAL_URI = "/"
const CANONICAL_QUERY_STRING = ""

function getCanonicalHeaders(amzTimestamp: string) {
    return ["content-type:" +  CONTENT_TYPE, "host:" + HOST, "x-amz-date:" + amzTimestamp, "x-amz-target:" + AMAZON_TARGET + "\n"].join("\n")
}

function getCanonicalRequest(canonicalHeaders: string, payloadHash: string) {
    return [METHOD, CANONICAL_URI, CANONICAL_QUERY_STRING, canonicalHeaders, SIGNED_HEADERS, payloadHash].join("\n")
}

function getAuthorizationHeader(scope:string , signature: string, amazonKeyId: string) {
    return `${SIGNING_ALGORITHM} Credential=${amazonKeyId}/${scope}, SignedHeaders=${SIGNED_HEADERS}, Signature=${signature}`
}

if (require.main === module) {
    // Get user input
    const amazonKeyId = process.argv[2];
    const secretKey = process.argv[3];

    // Get the required timestamp strings
    let [amzTimestamp, reqTimestamp] = signing.getTimestamps()
    console.log("Amazon Timestamp: " + amzTimestamp)
    console.log("Req Timestamp: " + reqTimestamp)

     // Get the scope of the request (the timestamp and the target service)
    const scope = signing.getCredentialScope(reqTimestamp, REGION, SERVICE)
    console.log("Credential Scope: " + scope)

    const requestParamters = `{"Name":"` + PARAMETER_NAME + `","WithDecryption":true}`
    const payloadHash = signing.computeSHA256SignatureHash(requestParamters)
    console.log("Payload Hash: " + payloadHash)
    const headers = getCanonicalHeaders(amzTimestamp)

    const canonicalRequest = getCanonicalRequest(headers, payloadHash)

    //  Get the AWS v4 signing key
    const key = signing.getAWS4SignatureKey(secretKey, reqTimestamp, REGION, SERVICE)
    //console.log("Signing Key: " + key.toString('base64'))

    // Prepare string value to sign from user input
    const stringToSign = signing.getStringToSign(amzTimestamp, scope, canonicalRequest)
    console.log("String to sign: `" + stringToSign + "`")

    // Sign and output user string
    const signature = signing.signHex(key, Buffer.from(stringToSign))
    console.log("Signature: " + signature)

    const authHeader = getAuthorizationHeader(scope, signature, amazonKeyId)
    console.log("Auth Header: " + authHeader)

    const canReqHeaders = {
        "Accept-Encoding": "identity",
        "Content-Type": CONTENT_TYPE,
        "X-Amz-Date": amzTimestamp,
        "X-Amz-Target": AMAZON_TARGET,
        "Authorization": authHeader,
        'Content-Length': requestParamters.length
    }

    var options = {
        hostname: HOST,
        path: "/",
        port: 443,
        method: 'POST',
        headers: canReqHeaders
    };
    var req = https.request(options, function(res) { 
        res.on('data', (d) => {
            process.stdout.write(d)
        })
    })
    req.write(requestParamters)
    req.end()
}

```
{{% /tab %}}
{{% tab name="Javascript" %}}
```js
// can_req/js/request.js

const signing = require(`./signing.js`);
const https = require('https');

const METHOD = "POST"
const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"
const AMAZON_TARGET = "AmazonSSM.GetParameter"
const CONTENT_TYPE = "application/x-amz-json-1.1"
const PARAMETER_NAME = "TechSquawkParam"
const SERVICE = "ssm"
const HOST = "ssm.us-west-2.amazonaws.com"
const REGION = "us-west-2"
const SIGNED_HEADERS = "content-type;host;x-amz-date;x-amz-target"
const CANONICAL_URI = "/"
const CANONICAL_QUERY_STRING = ""

function getCanonicalHeaders(amzTimestamp) {
    return ["content-type:" +  CONTENT_TYPE, "host:" + HOST, "x-amz-date:" + amzTimestamp, "x-amz-target:" + AMAZON_TARGET + "\n"].join("\n")
}

function getCanonicalRequest(canonicalHeaders, payloadHash) {
    return [METHOD, CANONICAL_URI, CANONICAL_QUERY_STRING, canonicalHeaders, SIGNED_HEADERS, payloadHash].join("\n")
}

function getAuthorizationHeader(scope, signature, amazonKeyId) {
    return `${SIGNING_ALGORITHM} Credential=${amazonKeyId}/${scope}, SignedHeaders=${SIGNED_HEADERS}, Signature=${signature}`
}

if (require.main === module) {
    // Get user input
    const amazonKeyId = process.argv[2];
    const secretKey = process.argv[3];

    // Get the required timestamp strings
    [amzTimestamp, reqTimestamp] = signing.getTimestamps()
    console.log("Amazon Timestamp: " + amzTimestamp)
    console.log("Request Timestamp: " + reqTimestamp)

    // Get the scope of the request (the timestamp and the target service)
    const scope = signing.getCredentialScope(reqTimestamp, REGION, SERVICE)
    console.log("Credential Scope: " + scope)

    const requestParamters = `{"Name":"` + PARAMETER_NAME + `","WithDecryption":true}`
    const payloadHash = signing.computeSHA256SignatureHash(requestParamters)

    const headers = getCanonicalHeaders(amzTimestamp)
    const canonicalRequest = getCanonicalRequest(headers, payloadHash)

    //  Get the AWS v4 signing key
    const key = signing.getAWS4SignatureKey(secretKey, reqTimestamp, REGION, SERVICE)
    console.log("Signing Key: " + key.toString('hex'))

    // Prepare string value to sign from user input
    const stringToSign = signing.getStringToSign(amzTimestamp, scope, canonicalRequest)
    console.log("String to sign: `" + stringToSign + "`")

    // Sign and output user string
    const signature = signing.signHex(key, stringToSign)
    console.log("Signature: " + signature)

    const authHeader = getAuthorizationHeader(scope, signature, amazonKeyId)
    console.log("Auth Header: " + authHeader)

    const canReqHeaders = {
        "Accept-Encoding": "identity",
        "Content-Type": CONTENT_TYPE,
        "X-Amz-Date": amzTimestamp,
        "X-Amz-Target": AMAZON_TARGET,
        "Authorization": authHeader,
        'Content-Length': requestParamters.length
    }

    var options = {
        hostname: HOST,
        path: "/",
        port: 443,
        method: 'POST',
        headers: canReqHeaders
    };
    var req = https.request(options, function(res) { 
        res.on('data', (d) => {
            process.stdout.write(d)
        })
    })
    req.write(requestParamters)
    req.end(options.body || '').on("error", err => {
        console.log("Error: " + err.message);
    });
}

```
{{% /tab %}}
{{% tab name="Python" %}}
```py
# can_req/py/request.py

from signing import *

import requests

# Default API parameters provided here for convenience
METHOD = "POST"
SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"
AMAZON_TARGET = "AmazonSSM.GetParameter"
CONTENT_TYPE = "application/x-amz-json-1.1"
PARAMETER_NAME = "TechSquawkParam"
SERVICE = "ssm"
HOST = "ssm.us-west-2.amazonaws.com"
REGION = "us-west-2"
SIGNED_HEADERS = "content-type;host;x-amz-date;x-amz-target"
CANONICAL_URI = "/"
CANONICAL_QUERY_STRING = ""


def get_canonical_headers(amzn_date: str) -> str:
    """ Get canonical headers in proper format
    """
    return "\n".join(["content-type:{}".format(CONTENT_TYPE), "host:{}".format(HOST), "x-amz-date:{}".format(amzn_date), "x-amz-target:{}\n".format(AMAZON_TARGET)])

def get_canonical_requests(canonical_headers: str, payload_hash: str) -> str:
    """ Generate canonical request from the provided headers and payload hash
    """
    return "\n".join([METHOD, CANONICAL_URI, CANONICAL_QUERY_STRING, canonical_headers, SIGNED_HEADERS, payload_hash])

def get_authorization_header(scope: str, signature: str, amazon_key_id: str) -> str:
    """ Get the authorization header used for verifying the authenticity of the request
    """
    return "{} Credential={}/{}, SignedHeaders={}, Signature={}".format(SIGNING_ALGORITHM, amazon_key_id, scope, SIGNED_HEADERS, signature)

if __name__ == "__main__":
    # Get provided AWS access credentials
    amazon_key_id = sys.argv[1]
    amazon_secret_key = sys.argv[2]

    endpoint = "https://{}/".format(HOST)
    amazon_timestamp, req_timestamp = get_timestamps()
    print("Amazon Timestamp: " + amazon_timestamp)
    print("Request Timestamp: " + req_timestamp)

    credential_scope = get_credential_scope(req_timestamp, REGION, SERVICE)
    print('Credential Scope: ' + credential_scope)
          
    request_paramters = '{"Name":"' + PARAMETER_NAME + '","WithDecryption":true}'
    payload_hash = compute_sha256_hash(request_paramters)
    print("Payload Hash: " + payload_hash)

    headers = get_canonical_headers(amazon_timestamp)
    canoniocal_request = get_canonical_requests(headers, str(payload_hash))

    signature_key = get_aws4_signature_key(amazon_secret_key, req_timestamp, REGION, SERVICE)
    print("Signing Key: " + base64.b64encode(signature_key).decode())
    string_to_sign = get_string_to_sign(amazon_timestamp, credential_scope, canoniocal_request)
    print("String to Sign: " + string_to_sign)
    signature = hmac.new(signature_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()
    print("Signature: " + signature)

    auth_header = get_authorization_header(credential_scope, signature, amazon_key_id)
    print("Auth Header: " + auth_header)

    # Perform AWS API call
    headers = {
        "Accept-Encoding": "identity",
        "Content-Type": CONTENT_TYPE,
        "X-Amz-Date": amazon_timestamp,
        "X-Amz-Target": AMAZON_TARGET,
        "Authorization": auth_header
    }

    resp = requests.post(endpoint, headers=headers, data=request_paramters)

    print(resp.content)

```
{{% /tab %}}
{{% tab name="Go" %}}
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

const METHOD = "POST"
const AMAZON_TARGET = "AmazonSSM.GetParameter"
const CONTENT_TYPE = "application/x-amz-json-1.1"
const PARAMETER_NAME = "TechSquawkParam"
const SERVICE = "ssm"
const HOST = "ssm.us-west-2.amazonaws.com"
const REGION = "us-west-2"
const SIGNED_HEADERS = "content-type;host;x-amz-date;x-amz-target"
const CANONICAL_URI = "/"
const CANONICAL_QUERY_STRING = ""

func getCanonicalHeaders(amazonDate string) string {
	headers := [...]string{"content-type:" + CONTENT_TYPE, "host:" + HOST, "x-amz-date:" + amazonDate, "x-amz-target:" + AMAZON_TARGET + "\n"}
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

	requestParamters := `{"Name":"` + PARAMETER_NAME + `","WithDecryption":true}`
	payloadHash := computeSHA256Hash(requestParamters)
	fmt.Printf("Payload Hash: %x\n", payloadHash)

	headers := getCanonicalHeaders(amazon_timestamp)
	canonical_request := getCanonicalRequest(headers, payloadHash)

	signature_key := getAWS4SignatureKey(amazon_secret_key, request_timestamp, REGION, SERVICE)
	fmt.Printf("Signing Key: %x\n", signature_key)
	string_to_sign := getStringToSign(amazon_timestamp, scope, canonical_request)
	fmt.Printf("String to sign: `%s`\n", string_to_sign)

	// Sign and output user string
	signature := signHex(signature_key, string_to_sign)
	fmt.Printf("Signature: %s\n", signature)

	auth_header := getAuthorizationHeader(scope, signature, amazon_key_id)
	fmt.Printf("Auth Header: %s\n", auth_header)

	client := &http.Client{}
	endpoint := fmt.Sprintf("https://%s/", HOST)
	req, err := http.NewRequest("POST", endpoint, bytes.NewBuffer([]byte(requestParamters)))
	if err != nil {
		fmt.Println(err)
		return
	}
	req.Header.Add("Accept-Encoding", "identity")
	req.Header.Add("Content-Type", CONTENT_TYPE)
	req.Header.Add("X-Amz-Date", amazon_timestamp)
	req.Header.Add("X-Amz-Target", AMAZON_TARGET)
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
{{< /tabs >}}