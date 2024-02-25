---
title: Images
draft: false
chapter: false
weight: 8
---

An _image_ is a read-only template that contains all the necessary files, libraries, and configuration required to initialize a container. It acts as a blueprint which defines the application, but is not the actual running process.

##### Ubuntu Image Examples

To illustrate this, we first start with a Docker image that leverages an existing Ubuntu base image, which contains all the same shared libraries and utilities found in the Ubuntu OS. Similar to how application code can leverage shared libraries, developers can reference existing base images to simplify what dependencies are needed.

{{< tabs groupId="code" >}}
{{< tab name="Example 1: Ubuntu Image" >}}
{{< tabs >}}
{{% tab name="Build" %}}

```sh
docker build . -t techsquawks/ubuntu
```

{{% /tab %}}
{{% tab name="Run" %}}

```sh
docker run -t techsquawks/ubuntu
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="Dockerfile" %}}

<!-- embedme containers/docker/images/parent/Dockerfile -->

```dockerfile
# Use Ubuntu as base image for container
FROM ubuntu:23.04

# Install latest packages
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8


# Copy local text file into container
COPY message.txt message.txt

# Print message from file
ENTRYPOINT [ "cat", "message.txt" ]
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="Output" %}}

```
ubuntu image example
```

{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/go" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/ts" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< /tabs >}}

##### Scratch Base Image

If we don't want to leverage an existing image, we can leverage the `scartch` base image, which is the most minimal base image Docker provides, containing no directories or files. This can be useful when wanting to minimize the container and image size or for creating custom base images.

{{< tabs groupId="code" >}}
{{< tab name="Example 1: Ubuntu Image" >}}
{{< tabs >}}
{{% tab name="Build" %}}

```sh
docker build . -t techsquawks/ubuntu
```

{{% /tab %}}
{{% tab name="Run" %}}

```sh
docker run -t techsquawks/ubuntu
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="Dockerfile" %}}

<!-- embedme containers/docker/images/scratch/Dockerfile -->

```dockerfile
# A 'scratch' image is an empty base image.
FROM scratch

# Copy binary executable
COPY hello hello

# Run executable
ENTRYPOINT [ "./hello" ]
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="Output" %}}

```
ubuntu image example
```

{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/go" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/ts" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< /tabs >}}

In the above, we copy the `hello` binary executable into the image, which has been compiled for the Docker scratch image architecture. We can then execute the binary via the entrypoint.

The COPY command copies the local `hello` binary executable into the image file system the image file system, so it can be accessed as the container runs. The entrypoint indicates the executable that should be run when running our container.

For a compressive list of Docker commands that can be used when building an image, please refer to the table below:

| Instruction | Description                                                 |
| ----------- | ----------------------------------------------------------- |
| ADD         | Add local or remote files and directories.                  |
| ARG         | Use build-time variables.                                   |
| CMD         | Specify default commands.                                   |
| COPY        | Copy files and directories.                                 |
| ENTRYPOINT  | Specify default executable.                                 |
| ENV         | Set environment variables.                                  |
| EXPOSE      | Describe which ports your application is listening on.      |
| FROM        | Create a new build stage from a base image.                 |
| HEALTHCHECK | Check a container's health on startup.                      |
| LABEL       | Add metadata to an image.                                   |
| MAINTAINER  | Specify the author of an image.                             |
| ONBUILD     | Specify instructions for when the image is used in a build. |
| RUN         | Execute build commands.                                     |
| SHELL       | Set the default shell of an image.                          |
| STOPSIGNAL  | Specify the system call signal for exiting a container.     |
| USER        | Set user and group ID.                                      |
| VOLUME      | Create volume mounts.                                       |
| WORKDIR     | Change working directory.                                   |
