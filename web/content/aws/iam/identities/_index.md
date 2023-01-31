---
title: Identities
draft: false
weight: 2
---

Identity information serves to represent the end user of AWS services. There are three idienties in AWS IAM service, users, groups and roles respectively.

## Users

User entities represenent a single entity, whether that be a human user or service. They may have credentials associated with them (long-term API keypairs, passwords, MFA information, etc). 

By default, user entities have no permissions, following the principle of least privliges. Users must be assigned
permissions via IAM policies to be able to perform actions

## Groups

A collection of user entities. Similar to users, groups may have permissions assigned to them via IAM policies. This allows administrators to more easily manage different groups of users. 

## Roles

A role idenitty allows other authorized identities to assume it temporarily for elevated permissions. Useful for granting permissions to various AWS services which may need to peform AWS API operations.
