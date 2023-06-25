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
