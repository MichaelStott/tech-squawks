---
title: Virtualization
draft: true
weight: 4
---


### Overview

Cloud providers typically manage a pool of computational, storage, and network resources that are dynamically allocated for cloud customers. Special care must be taken to ensure these processes remain isolated from one of another for security and data integrity reasons. While exact implementation details are not publicly known, cloud providers largely accomplish this via virtualization, which allows shared access to hardware resources for isolated processes.

![Virtualization](/images/cc/virtualization.png)

Virtualization makes use of either software or hardware provided hypervisor which manages access to underlying host memory and CPU resources. This allows several OS's to run efficiently on a parent OS. While exact implementation details will vary between cloud providers (and be private), similar mechanisms are used when provisioning virtual servers in the cloud.

## Host and Guests Isolation

The hyperviser ensures that resources belonging to the guest VMs are isolated both from one another and prevents guest VMs from accessing unallocated resources on the host machine. Because of this VMs are useful for testing potentially risky or damaging code, such as malware, for research and cybersecurity purposes, or even allowing developers to reliably test applications across multiple OS types and version.

[TODO add more specifics regarding this]

### VirtualBox

For those wishing to experiment with virtualization on their local machine, VirtualBox is a versatile opensource virtualization tool. While exact instructions and configuration will differ from machine to machine, the following will provide local instrucitons for standing up a local guest linux OS on your machine.

1. Download and install VirtualBox
2. Download Arch Linux Iso
3. Configure VirtualBox to boot from the local ISO image
4. Allocate 1 CPU core and 1 GB of RAM
5. Launch the guest OS.
