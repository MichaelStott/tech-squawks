---
title: Setup
draft: false
chapter: false
weight: 5
---

To install Docker, follow the official instructions provided [here](https://docs.docker.com/get-docker/). Once installed, validate the following:

1. The `docker` CLI is installed and accessible from your command line.

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**

```sh
docker --version
```

**Output**

```
Docker version 20.10.21, build baeda1f
```

{{% /tab %}}
{{< /tabs >}}

2. Validate that you can successfully pull images from Docker hub, Docker's image repository.

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**

```sh
docker pull hello-world
```

**Output**

```
Using default tag: latest
latest: Pulling from library/hello-world
719385e32844: Pull complete
Digest: sha256:c79d06dfdfd3d3eb04cafd0dc2bacab0992ebc243e083cabe208bac4dd7759e0
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
```

{{% /tab %}}
{{< /tabs >}}

3. Lastly, validate that you are able exwcute containers locally.

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**

```sh
docker run hello-world
```

**Output**

```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:

1.  The Docker client contacted the Docker daemon.
2.  The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
3.  The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
4.  The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
    ...
```

{{% /tab %}}
{{< /tabs >}}
