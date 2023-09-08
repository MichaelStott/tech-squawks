---
title: Access
draft: true
weight: 3
---

By default, identities in AWS have no access to any resources. To enable or explicitly deny access to certain AWS services and resources, we need to associate  with identities, which define the allowed actions of an identity for given resources or services. Cloud developers may either create their own custom policies or use one of the many of the pre-existing AWS policies for common usecases. 

Policies may also be associated via ABAC rules, which determines relevant policies from an identity's tags. This can potentially simplify the IAM flow for managing, rather than directly associateing policies with entities (why?)

