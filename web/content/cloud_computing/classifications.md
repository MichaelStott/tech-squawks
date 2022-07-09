---
title: Classifications
draft: false
weight: 3
---

### Cloud Computing Service Classifications

For on-premise applications, organizations or individuals manage all the underlying compute, storage, and 
networking infrastructure for their systems and services.

![Cloud Classifications](/images/cc/cloud_classifications.png)

Depending on the type of service offering, cloud computing manages some or all of these components. There 
are three cloud computing models, Infrastructure as a Service (IaaS) Platform as a Service (PaaS), 
and Software as a Service (SaaS). [^1] [^2]

#### Infrastructure as a Service - IaaS

IaaS manages the underlying network and hardware infrastructure, while providing control of the host OS and application/software to the user. Any cloud provider that provides access to virtualized or phsyical servers would be example of this, such as the AWS EC2 service or GCP 
Compute Engine.

#### Platform as a Service - PaaS

PaaS manages everything IaaS manages in addition to the environment OS and runtime, allowing users to primarily focus on developing their applicaiton. An example of PaaS would be Heroku, which allows developers to upload their applications to a server without having to worry about provisioning the underlying hardware or OS. The AWS offers a similar service known as Elastic Beanstalk.

A related offering would be Functions as a Service (FaaS), which, similar to PaaS services,
allows for developers to execute and deploy code in the cloud. However, unlike PaaS, FaaS 
services tend to have more restrictions, such as limited CPU and memory configuration, 
limited execution time, 

#### Software as a Service - SaaS

For SaaS products, the user manages none of the underlying instrastructure or application logic and simply and consumes the end result of an application. An example of this would be Dropbox or the AWS S3 service, where 
users can upload data through a web console or API while AWS maintains all backend services.

### Cloud Computing Deployment Models

There are several deployment models for cloud applications, depending on what kind of cloud 
providers are leveraged and who manages the cloud infrastructure. 

[Diagram]

#### In-Cloud

In-Cloud deployments are, unsuprisingly, hosted entirely in the cloud. This alleviates customers
from having to manage the underlying infrastructure.

#### On-Prem/Private

On-premise or private cloud deployments refer deploying to privately managed clouds.
Rather than leverage a pulic cloud provider such as AWS or GCP, organizations make their
own infrastructure available to developers internally via APIs and virtualization.
OpenShift is one such framework that enables users to create and manage their own private
cloud environments.

#### Hybrid

Some combination of resources provioned from various cloud environments. This is common for 
organizations which orginally self-hosted their services before taking advantage of cloud 
computing.

[^1]: NIST Definition of Cloud Computing: https://csrc.nist.gov/publications/detail/sp/800-145/final
[^2]: AWS Types of Cloud Computing:  https://aws.amazon.com/types-of-cloud-computing/
