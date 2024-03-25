# Canonical Requests Example (Go)

To run the signing portion of the demo, execute the following:
```
$ go run signingDriver.go signing.go $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

For invoking canonical requests, run the following:
```
$ go run request.go signing.go $AWS_ACCESS_KEY_ID $AWS_SECRET_KEY
```