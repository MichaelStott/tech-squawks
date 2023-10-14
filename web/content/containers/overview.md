---
title: Overview
draft: false
weight: 2
---

### Definition

_Containers_ enable developers to package and distribute software in such a manner that building and execution is repeatable across hardware, OS environments, and cloud providers.[^1] NIST more formally defines containers as follows:

> A method for packaging and securely running an application within an application virtualization environment. Also known as an application container or a server application container.

Because of their portability, containers are considered a facet of cloud native design, a collection of best practices and technologies for developing applications. [^2]

### Virtualization vs Containerization

While internally both technologies operate quite differently, containers are often compared to _virtualization_. With virtualization, users run one or more operating systems on their host machine via individual _virtual machines_ (VMs), each consisting of a guest OS and child processes. These VMs are managed by a host machine via a _hypervisor_, which mediates access to the underlying hardware resources for the guest operating systems. [^3]

{{< figure src="/images/containers/virtualization.png" caption="_Figure 1: Virtualization overview. Guest virtual machines, containing an OS and child processes, are isolated from each other via the hypervisor._">}}

Containers isolate processes rather than operating systems. However, instead of leveraging a hypervisor, containers are managed by a _container engine_, which achieves process isolation and resource allocation via the host OS system calls.

{{< figure src="/images/containers/containers.png" caption="_Figure 2: Containerization overview. Container processes are managed via the container engine, which runs on the host machine OS._">}}

### Benefits of Containerization

Containers offer a plethora of benefits when developing applications:

- _Portability_: Able to be distributed and executed on any platform that supports the container engine.
- _Consistency_: May be built across multiple development environments.
- _Lighweight_: Can be provisioned quite rapidly, especially compared to VMs.

[^1]: https://cloud.google.com/learn/what-are-containers
[^2]: https://glossary.cncf.io/cloud-native-tech/
[^3]: https://glossary.cncf.io/virtualization/
