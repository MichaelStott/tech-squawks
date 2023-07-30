---
title: Groups
draft: false
weight: 2
---

## Groups

IAM groups act as containers for multiple IAM users. Groups can have IAM policies associated with them, which are automatically inherited by child users when evaluating access. This allows administrators to more easily manage access for multiple users simultaneously. User may belong to several groups, but groups cannot contain other groups.

There is no default group for newly created users. Therefore, any groups must be explicitly created and poclicies must be explicitly assigned to the groups.[^1]

{{< figure src="/images/iam/groups.png" caption="_Figure 1: Permissions may be assigned to groups which are automatically applied to assigned users._">}}

Groups are represented rather simply, with the main component required being the group name.

{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws iam list-groups
```
**Output**
```
{
    "Groups": [
        {
            "Path": "/",
            "GroupName": "Admins",
            "GroupId": "AGPAYGH7AQ44DKI7UGME4",
            "Arn": "arn:aws:iam::012345678910:group/Administrators",
            "CreateDate": "2019-10-01T22:50:30+00:00"
        },
        {
            "Path": "/",
            "GroupName": "Developers",
            "GroupId": "AGPAYGH7AQ44BVG3THNH7",
            "Arn": "arn:aws:iam::012345678910:group/Developers",
            "CreateDate": "2019-07-10T23:10:47+00:00"
        },
        {
            "Path": "/",
            "GroupName": "Devops",
            "GroupId": "ADSAYFF72444NEI6MNIOP",
            "Arn": "arn:aws:iam::012345678910:group/Devops",
            "CreateDate": "2019-07-10T23:10:47+00:00"
        }
    ]
}
```
{{% /tab %}}
{{< /tabs >}}

[^1]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html
