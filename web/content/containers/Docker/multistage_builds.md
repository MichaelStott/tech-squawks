---
title: Multistage Builds
draft: true
chapter: true
weight: 10
---

In certain instances, dependencies initially required when building the image are not required to be packaged in the final compiled image. For instance, for languages that produce a binary executable, source files can be discarded after compilation. To help achieve this, we can leverage multistage builds to reduce our size, which allow us to pull dependencies in one stage and then copy over data that we want to another stage.
