# Canonical Requests Example (Typescript)

## Instructions

To install the dependencies, run the following:

```
$ npm i
```

## Demo

To run the signing portion of the demo, execute the following:
```
# Provide the AWS Secret Key, region, service name, and message to encrypt
$ ts-node index.ts $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

For invoking canonical requests, run the following:
```
$ ts-node request.ts $AWS_ACCESS_KEY_ID $AWS_SECRET_KEY 
```