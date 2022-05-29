---
title: Benefits & Considerations
draft: false
weight: 2
---

An increasing number of organizations are leveraging cloud computing or considering migrating existing applications to the cloud. Because of this, it is important for developers to evaluate the common benefits and additional considerations of working in such environments. 

### Benefits

#### On-Demand 

In traditional on-premise environments, if engineers required new infrastructure, a considerable amount of time was required  to install and configure the hardware in an organization's data center. Alternatively, cloud resources can typically be provisioned within a few seconds to a few minutes. This on-demand provisioning of resources enables more rapid experimentation and application development. 

#### Economical 

Cloud computing can potentially be more economical than traditional on-premise environments. Cloud resources can be provisioned usually with no up-front cost, such as purchasing hardwares, utilizing a pay-as-you-go model. All hardware management is offloaded from organizations to the cloud provider. Additionally, because cloud providers purchase hardware in bulk, they are able to leverage economies of scale and pass those savings onto cloud customers.

{{% notice info %}}
Readers should note that these benefits are broad generalities and should always take into account the specifics of their organization when performing a cost-benefit analysis. For instance, Dropbox initially developed their platform using cloud technologies, notably AWS S3, before later [migrating to their own infrastructure](https://www.geekwire.com/2018/dropbox-saved-almost-75-million-two-years-building-tech-infrastructure), which increased their performance and costs. 
{{% /notice %}}

#### Scalability 

Whereas traditional on-prem applications may be limited by the machines limited to an organization's data center, cloud services can be easily scaled in the cloud to account for an increase in load. A common example would be organizations provisioning more servers or compute capacity on Black Friday to handle holiday traffic.  Conversely, resources can be scaled down to save on costs. 

There are two types of scaling, horizontal and vertical. Horizontal scaling refers to adding additional nodes/services/concurrent processes to your application to handle an increase in load. Vertical scaling refers to increasing CPU, memory, or storage of your application.

### Considerations

#### Security

 The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) outlines the security responsibilities of both cloud providers and cloud customers. Broadly speaking, cloud providers are responsible for securing the hardware in their data center, such that unauthorized access to data centers does not happen and that customer data is appropriately segregated using techniques such as virtualization. Cloud customers are responsible for ensuring their applications are properly configured so that data is not leaked unintentionally.

 Additionally, because the cloud can provide a theoretically limitless amount of computational power, customers are responsible for ensuring that their cloud access is secure and that services and organization users have the appropriate credentials. Generally, it is recommended that administrators follow the principle of least privilege, granting the minimum amount of permissions users need for a specific task,  when providing access.

#### Cost Management

While there are economical benefits to leveraging the cloud, unintended costs can easily accrue if unused resources are left provisioned or if budgeting is done improperly Cloud providers often have budgeting alarms and tools that can assist customers with monitoring their cloud usage to curb costs

Info: There is often a trade-off in cloud services between cost and convenience. The less managerial work required by engineers to use the service, the more expensive it tends to be. For instance, manually provisioning servers for a database cluster can be cumbersome because engineers are responsible for all maintenance tasks associated with the cluster, but it is significantly cheaper than most cloud provider options for managed database solutions, where the cloud provider manages all maintenance tasks for updating the database.

#### Visibility

Keeping track of your cloud resources can appear to be a daunting task when numbers members of your organization may be provisioning new or updating existing resources in the cloud. When cloud resource specifications differ from what is specified in IaC ((?), that is known as Infrastructure Drift. One must also ensure that appropriate monitoring and alerting is setup in their environment in the event that there is an infrastructure or application failure.