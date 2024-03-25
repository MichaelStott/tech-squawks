# Canonical Requests Example (Javascript)

## Instructions

To install the dependencies, run the following:

```
$ npm i
```

## Demo

To run the signing portion of the demo, execute the following:
```
# Provide the AWS Secret Key, region, service name, and message to encrypt
$ node index.js $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

For invoking canonical requests, run the following:
```
$ node request.js $AWS_ACCESS_KEY_ID $AWS_SECRET_KEY 
```