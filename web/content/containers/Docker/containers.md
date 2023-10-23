---
title: Containers
draft: false
chapter: false
weight: 7
---

running instances of images

When run, docker will choose a random name unless you specify one:

```sh
docker run -t techsquawks/scatch
```

get all containers

```sh
docker container ls
```

may also be stopped, paused, started, and deleted.

Even after deletion, the original image containing instructions for creating a new container remains.
