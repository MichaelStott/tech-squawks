---
title: Overview

weight: 1
---

### Definition

*Cloud computing* is essentially the ability to provision and manage computational and network resources, such as servers, networks, or data stores, through a web interface, such as a web page or API.  The National Institute of Standards and Technology (NIST) formally [define](https://csrc.nist.gov/publications/detail/sp/800-145/final) cloud computing as follows:

> Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction.

Companies and third-parties with cloud computing platform offerings are known as *cloud providers*. Popular cloud providers incude [Amazon Web Services (AWS)](https://aws.amazon.com/), [Microsoft Azure](https://azure.microsoft.com/en-us/), and [Google Cloud Platform (GCP)](https://cloud.google.com/).

![The Big Three: AWS, Azure, and GCP](/parrots/parrotnotfound.gif)

### Benefits and Drawbacks

Cloud computing affords engineers numerous benefits when developing applications, such as:
- On-demand provisioning: Servers, networks, and other cloud resources and be rapidly provisioned.
- Cost-effectiveness: Cloud providers are able to leverage the enconomy of scale when purchasing hardware and pass those savings onto developers.
- Scalability: Infrastructure can be horizontally and vertically scaled as needed.

Simultaneously, developing within a cloud environment brings additional considerations:
- Security: Ensure only authorized individuals are able to access and modify an organization's cloud resources.
- Visibility: Ascertaining pertinent resources and activity are acruing charges within a cloud envirornment.
- Observability: Assessing the state of applications deployed to the cloud.


### Classifications

Various offerings that provide trade-offs between environment configuration, costs, and overhead, ranging from fully user-configurable servers and virtual environments to completely managed services, such as for databases. Cloud services are broadly categorized as:
- _Infrastructure as a Service (IaaS)_: Provides access to the underlying infrastructure.
- _Platform as a Service (PaaS)_: Provides a runtime environment for easily deploying applications to the ecloud.
- _Software as a Service (SaaS)_: Software hosted in the cloud where end-users are not conernced with the underlying platform or infrastructure.

![Cloud Classifications](/parrots/parrotnotfound.gif)

### Cloud Native

The rise of cloud computing has accelerated the adoption of practices for developing robust cloud applications, collectively known as cloud-native development. These practices include _microservices_, _containerization_, and _serverless_ development for improving application scalability, portability, deployability, and development.

### AWS

These tutorials will target AWS for deploying examples and exploring cloud computing design. AWS is one the earliest and, at the time of writing, most popular cloud provider. While the individual implementation of computing, data-store, networking, and other cloud services varies between cloud-providers, the principles learned here can be applied to all platforms.
