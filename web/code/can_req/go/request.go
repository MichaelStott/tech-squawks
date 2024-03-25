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
