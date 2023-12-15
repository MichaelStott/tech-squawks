---
title: Overview
draft: false
chapter: false
weight: 6
---

_Docker_ is an open-source platform for developing, deploying, and distributing containerized software.

### Images and Containers

The two primary Docker entities are _images_ and _containers_. Images provide information for constructing the private filesystem and including any process executables. Images may be published and shared with others through _registeries_, such as _Docker Hub_. Images are defined via _Dockerfiles_ which provides a set of sequential instructions for building an image.

Containers are running instances of images. These container processes are isolated from each other and may be started, stopped, moved, or deleted via the _Docker CLI_. Any data within a container's private filesystem that is not written to persistent storage will be lost upon deleting the container.

#### Building and Running Containers

{{< tabs groupId="code" >}}
{{< tab name="Example 1: Hello World!" >}}
{{< tabs >}}
{{% tab name="Build" %}}

```sh
docker build . -t techsqauwks/hello-world
```

{{% /tab %}}
{{% tab name="Run" %}}

```sh
docker run -t techsqauwks/hello-world
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="Dockerfile" %}}

<!-- embedme containers\docker\overview\Dockerfile -->

```dockerfile
FROM alpine:3.14

ENTRYPOINT [ "echo", "hello world!" ]
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="Output" %}}

```
hello world!
```

{{% /tab %}}
{{< /tabs >}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/tech-squawks/tree/main/code/homepage/go" icon="rocket" %}}Deploy{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/ts" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< /tabs >}}

The first line of the Dockerfile defines the _base image_ version to use when building the image. In this case, `alpine` is leveraged due to its lightweight nature. The second line defines the container _entrypoint_, or the underlying command that will be executed upon running the container.

### Architecture

Docker consists of three primary components, the Docker client, Docker Host, and Docker Hub. The Docker client is used to interact the Docker engine and invoke certain actions. The docker engine builds images and manages containers. Lastly, Docker Hub is an _image registry_, and is used to distribute images for both public and private use cases.

{{< figure src="/images/containers/docker_architecture.png" caption="_Figure 1: The three primary Docker components, the Docker Client, Docker Host, and Docker Hub. The Docker Host manages containers and images on a particular machine, the Docker Client invokes certain Docker operations, and the images may be distributed (pushed and pulled) from Docker Hub._">}}
