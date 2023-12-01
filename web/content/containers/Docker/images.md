---
title: Images & Containers
draft: false
chapter: false
weight: 8
---

Docker _images_ and _containers_ are closely related, with containers being the running process managed by the Docker engine while images provide instructions to the Docker engine on building the container.

#### Images

Containers images are portable and distributable files which contain the containerized application executable, configuration, dependencies, and runtime entrypoint.

##### Ubuntu Image Examples

The COPY command packages the hello_world file into the image filesystem so it can be accessed as the container runs. The entrypoint indicates the executable that should be run when running our container. This can be a system command or

The highest level of image would be the SCRATCH image, indicating that we are starting from an empty filesystem

##### Empty Image example

In the above, we copy the `hello` binary executable into the image, which has been compiled for the Docker scratch image architecture. We can then execute the binary via the entrypoint.

#### Containers

When the docker host runs an image, it produces a _containers_.
