---
title: Containers
draft: false
chapter: false
weight: 9
---

A _container_ is the actual running instance of an application that has been packaged from an image. It includes all the specified files, libraries, and settings from the image it was based upon, and may be aallocated a certain percentage of the host machine's CPU, meomry, and storrage from the container runtime. Containers run inside a host operating system but are isolated from it, sharing the kernel and resources while having their own file system and network interface.

For instance, consider the previous image example:

{{< tabs groupId="code" >}}
{{< tab name="Example 1: Ubuntu Image" >}}
{{< tabs >}}
{{% tab name="Build" %}}

```sh
docker build . -t techsquawks/ubuntu
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

#### Container Management

The following are common commands for managing containers in the Docker runtime.

##### docker run

Executes a specified Docker image, opening a new container from it and running the commands or processes within it. This command allows you to interact with the container's filesystem, environment variables, ports, and volumes, making it suitable for running applications or other tasks in a managed and isolated environment.

##### docker exec

Executes a command or start a process within one or more existing Docker containers. This command allows you to interact with the processes in a container without starting a new one, which makes it ideal for managing and controlling the applications or services already running inside a container.

##### docker logs

Displays the output of the standard output and standard error streams of one or more Docker containers or images. This command shows the most recent log data by default, but you can use options to display older log data, filter by specific patterns, or follow log output in real-time as it becomes available. The `docker logs` command is a valuable tool for monitoring and troubleshooting applications running within containers.

##### docker stop

Stops a running container in Docker. When executed, it sends an SIGTERM signal to the container, which initiates the process of stopping the container's services and processes. If the container does not respond to the SIGTERM signal within 10 seconds, a second signal, usually SIGKILL, is sent to terminate the container forcefully. This command can be used with options to specify additional behaviors, such as `-t` or `--timeouts` to set stop timeouts, or `-f` or `--force-exit` to force stop a container that's not responding.

##### docker rm

Removes stopped, exited, or running containers. By default, it removes only stopped containers that do not have any instances running in them. When executed, `docker rm CONTAINER_IDS` or `docker rm IMAGE@TAG` will remove the specified container(s), effectively deleting their files and state from the local machine.

However, note that `docker rm` does not remove images associated with a container if those images are not in use by other containers. To completely remove an image, you would have to use `docker rmi`. You can also use various options with the `rm` command, like `-f`, `--force`, or `-v`, to modify its behavior, e.g., to force removal without prompting for user confirmation, or to include volumes in removal.
