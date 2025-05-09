package main

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
