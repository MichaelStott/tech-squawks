---
title: Classifications
draft: false
weight: 3
---

### Cloud Computing Service Classifications

For on-premise applications, companies manage all the underlying compute, storage, and networking infrastructure for their systems and services.

![Cloud Classifications](/images/cc/cloud_classifications.png)

Cloud computing can manage some or all of these aspects, depending on the type of service offering. There are three cloud computing models, Infrastructure as a Service (IaaS) Platform as a Service (PaaS), and Software as a Service (SaaS). [^1] [^2]

#### Infrastructure as a Service - IaaS

_IaaS_ provides virtualized or physical servers for hosting applications. Cloud providers maintain the underlying network and hardware infrastructure while allowing cloud engineers control of the host OS and software. The compute hardware can be configured upon initially provisioning a new service, such as CPU, memory, storage, networking, GPU, etc. _AWS EC2_ service provides virtual servers known as instances for developers to host applications.

#### Platform as a Service - PaaS

_PaaS_ manages all the compopnents maintained by IaaS services in addition to host operating system and execution runtime, allowing users to primarily focus on application development. PaaS offerings typically manage infrastructure autoscaling, monitoring, and logging. Examples of PaaS would be Heroku, which allows developers to upload their applications to a server without having to worry about provisioning the underlying hardware or OS. The AWS offers a similar service known as Elastic Beanstalk.

A related offering would be _Functions as a Service (FaaS)_, which, similar to PaaS services, allows for developers to execute and deploy code in the cloud. However, unlike PaaS, FaaS services tend to run in more restricted environments, such as limited CPU and memory configuration, execution time, application size, etc. while running in a more ephemeral environment. 

#### Software as a Service - SaaS

For _SaaS_ services, users manage none of the underlying instrastructure or application logic and simply and consume the result of an application. An example of this would be Dropbox or the AWS S3 service, where users can upload data through a web console or API while AWS maintains all backend storage.

[^1]: NIST Definition of Cloud Computing: https://csrc.nist.gov/publications/detail/sp/800-145/final
[^2]: AWS Types of Cloud Computing:  https://aws.amazon.com/types-of-cloud-computing/
