"use strict";
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

const payload =
  '<img src="https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif">';

// Provision an API Gateway instance.
const api = new awsx.classic.apigateway.API("serverless-party-parrot", {
  routes: [
    {
      // Define an HTTP endpoint.
      path: "/",
      method: "GET",
      // Create a Lambda function that will be triggered upon accessing this endpoint.
      eventHandler: new aws.lambda.CallbackFunction("handler", {
        callback: async (event) => {
          // Cry havoc and let slip the parrots of war.
          return {
            statusCode: 200,
            headers: { "Content-Type": "text/html" },
            body: payload,
          };
        },
      }),
    },
  ],
});

// The URL of the deployed serverless webpage.
exports.url = api.url;
