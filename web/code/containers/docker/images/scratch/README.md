This example demonstrates how to create a "hello world" images using the base image.

To compile the binary to copy into the image.

```sh
GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -o hello
```

The example can be build via:

```sh
$ docker build . -t techsqauwks/scatch
```

And run via:

```sh
$ docker run -t techsqauwks/scatch
```
