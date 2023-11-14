---
title: Images & Containers
draft: false
chapter: false
weight: 8
---

// Containers or images first. Kinda chicken and egg here. 0\_-

#### Images

When containers are initially built, the end result is what is known as an _image_. This image contains the filesystem, configuration, scripts and binaries packaged in the container needed for the application to run.

In Docker, the first line of the file indicates which parent image the container should be built from. Here we can define which environment and technologies we want to be included in our image.

##### Ubuntu Image Examples

The COPY command packages the hello_world file into the image filesystem so it can be accessed as the container runs. The entrypoint indicates the executable that should be run when running our container. This can be a system command or

The highest level of image would be the SCRATCH image, indicating that we are starting from an empty filesystem

##### Empty Image example

In the above, we copy the `hello` binary executable into the image, which has been compiled for the Docker scratch image architecture. We can then execute the binary via the entrypoint.

#### Containers

When the docker host runs an image, it produces a _containers_.
