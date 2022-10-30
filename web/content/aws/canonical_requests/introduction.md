---
title: Introduction
draft: false
weight: 1
---

AWS SDKs, CLI, or IaC tools, unsurprisingly invoke network calls to AWS services when performing cloud infrastructure operations. AWS refers to these API calls as _canonical requests_.

![Cloud Computing Overview](/images/can_req/can_req.png)

While it is possible to use canonical requests to directly communicate with AWS, it is preferable to use the AWS provided CLI and SDKs whenever possible to manage infrastructure for simplicity. Direct canonoical calls to AWS should be utilized in cases where either existing language support does not exist or if one requires fine-grained API control.  

For additional security, AWS enforces that incoming AWS calls are signed with valid credentials. This ensures the AWS can verify the identity of the client, protect the API request data in transit, and mitigate potential relay attacks. AWS offers two versions of signing, V2 and V4, with the majority of AWS services supporting the latest V4 signing method. 

