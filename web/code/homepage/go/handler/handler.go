package main

import (
	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

// handler is a simple function that takes a string and does a ToUpper.
func handler(request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
	return events.APIGatewayProxyResponse{
		StatusCode: 200,
		Headers: map[string]string{
			"Content-Type": "text/html",
		},
		Body: "<img src=\"https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif\">",
	}, nil
}

func main() {
	lambda.Start(handler)
}
