package main

import (
	hmac "crypto/hmac"
	"crypto/sha256"
	"fmt"
	"os"
	"strings"
	"time"
)

const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"

func getTimestamps() (string, string) {
	now := time.Now()
	return now.Format("20060102150405Z"), now.Format("20060102")
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
	return string(mac.Sum(nil))
}

func computeSHA256Hash(input string) string {
	mac := hmac.New(sha256.New, nil)
	mac.Write([]byte(input))
	return string(mac.Sum(nil))
}

func getStringToSign(key string, amazon_timestamp string, can_req string) string {
	components := [...]string{key, amazon_timestamp, can_req}
	return strings.Join(components[:], "\n")
}

func getAWS4SignatureKey(secret_key string, request_timestamp string, region string, service string) string {
	kdate := sign("AWS4"+secret_key, request_timestamp)
	kregion := sign(kdate, region)
	kservice := sign(kregion, service)
	ksigning := sign(kservice, "aws4_request")
	return ksigning
}

func main() {
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
	fmt.Printf("Signature Key: %s\n", signature_key)
	string_to_sign := getStringToSign(amazon_timestamp, credential_scope, user_input)
	fmt.Printf("String to sign: %s\n", string_to_sign)
	signature := signHex(signature_key, string_to_sign)
	print("Signature: " + signature)
}
