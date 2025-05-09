---
title: Benefits
draft: false
weight: 2
---

An increasing number of companies are either leveraging cloud computing or considering migrating existing on-premise applications to the cloud. Because of this, it is important for developers to be aware of the common benefits of working in such environments. 

#### On-Demand 

In traditional on-premise environments, if software engineers required additional infrastructure for hosting or scaling web services, a considerable amount of time was necessary to install and configure the hardware within an organization's private data center. Conversely, cloud resources can typically be provisioned anywhere between a few seconds to a few minutes through a web API call. This on-demand provisioning of resources enables more rapid development and experimentation

#### Cost-Effectivness 

Cloud computing can potentially be more economical than traditional on-premise hosting. Cloud resources can be provisioned with no up-front cost, instead utilizing a pay-as-you-go model. All hardware management is offloaded from organizations to the cloud provider. Additionally, because cloud providers purchase hardware in bulk, they are able to leverage economies of scale and pass those savings onto cloud customers.

{{% notice info %}}
Readers should note that the above is a broad generality and should always consider the specifics of their organization when performing a cost-benefit analysis. For instance, Dropbox initially developed their SaaS platform using cloud technologies, notably AWS S3, before later [migrating to their own infrastructure](https://www.geekwire.com/2018/dropbox-saved-almost-75-million-two-years-building-tech-infrastructure), which increased product performance and cost-effectiveness. 
{{% /notice %}}

#### Scalability 

Cloud providers have more computational resources available than most private data centers. Therefore, cloud services can be more readily scaled to account for increases or decreases in application load. A common example would be online retailers provisioning more servers for handling holiday traffic. Conversely, resources can be scaled down to save on costs, such as outside business hours. 

There are two types of scaling, horizontal and vertical. _Horizontal scaling_ refers to the addition or removal of servers to account for increased load in a distributed fashion. This type of scaling typically can be accomplished with minimal delay or application downtime.

{{< figure src="/images/cc/horizontal_scaling.png" caption="_Figure 1: With horizontal scaling, additional resources may be provisioned to handle increases in system load._">}}

_Vertical scaling_ refers to modifying the underlying hardware configuration of cloud resources, such as memory, CPU, or storage. This operation is typically disruptive and may result in application downtime.

{{< figure src="/images/cc/vertical_scaling.png" caption="_Figure 2: Vertical scaling changes the underlying hardware configuration for cloud resources, such as CPU or memory._">}}
