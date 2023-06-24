package main

import (
	"fmt"
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
	headers := [...]string{"host:" + HOST, "x-amz-date:" + amazonDate, "x-amz-target:" + AMAZON_TARGET}
	return strings.Join(headers[:], "\n")
}

func main() {
	// Get user input from command args
	// amazon_key_id := os.Args[1]
	// amazon_secret_key := os.Args[2]

	// Fetch the required timestamps
	amazon_timestamp, request_timestamp := signing.getTimestamps()
	fmt.Printf("Amazon Timestamp: %s\n", amazon_timestamp)
	fmt.Printf("Request Timestamp: %s\n", request_timestamp)
}
