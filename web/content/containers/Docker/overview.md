---
title: Overview
draft: false
chapter: false
weight: 5
---

_Docker_ is a platform for developing software, most notably for containerizing applications. Rather than being a comprehensive overview of Docker's features, this guide is intended to highlight aspects most important for developers.

### Docker Entities

There are two main docker objects, _images_ and _containers_. Docker images provide instructions for creating containers, including the filesystem, users, processes, and starting command. These images may be published and shared with others through the _Docker Registry_.

Docker containers are running instances of images. These container processes are isolated from each other and may be started, stopped, moved, or deleted via the Docker CLI. Any data within a container's private filesystem that is not written to persistent storage will be lost upon deleting the container.

### Architecture

