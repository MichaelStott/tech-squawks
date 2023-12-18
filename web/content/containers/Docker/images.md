---
title: Images & Containers
draft: true
chapter: false
weight: 8
---

_Images_ and _containers_ are closely related, with images being files which contain application and containers being running instances of those images.

#### Images

Containers images are portable files which contain the containerized application executable, configuration, dependencies, and runtime command. These images can be distributed and executed in other environments which the Docker Engine supports.

##### Ubuntu Image Examples

To illustrate this, we first start with a Docker image that leverages an existing Ubuntu base image. Similar to how code can utilize libraries and packages to simplify development, images can reference existing images to simplify what application dependencies are required.

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

##### Empty Image example

In the above, we copy the `hello` binary executable into the image, which has been compiled for the Docker scratch image architecture. We can then execute the binary via the entrypoint.

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

The COPY command packages the hello_world file into the image filesystem so it can be accessed as the container runs. The entrypoint indicates the executable that should be run when running our container. This can be a system command or

The highest level of image would be the SCRATCH image, indicating that we are starting from an empty filesystem

#### Containers

When the docker host runs an image, it produces a _containers_.
