```
go run signingDriver.go signing.go $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

```
go run request.go signing.go $AWS_ACCESS_KEY_ID $AWS_SECRET_KEY
```