---
title: AWS CLI
chapter: false
weight: 4
---

The AWS CLI is used to interact with AWS resources and services through a local terminal or shell by making AWS API calls on your behalf with your local credentials.

The following instructions are for installing the latest version of the AWS CLI (version 2 at the time of writing). See these [instructions](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html) if you would prefer version 1 of the CLI.

### Instructions 

1. Download and install the CLI for your development environment's OS:

{{< tabs groupId="os" >}}
{{% tab name="Windows" %}}

Download and run the [CLI installer](https://awscli.amazonaws.com/AWSCLIV2.msi).

{{% /tab %}}
{{% tab name="MacOS" %}}

##### User Interface:

Download the latest pkg file [here](https://awscli.amazonaws.com/AWSCLIV2.pkg) and double-click to
install.

##### Command Line:

Execute the following:

```sh
$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
$ sudo installer -pkg AWSCLIV2.pkg -target /
```

{{% /tab %}}
{{% tab name="Linux" %}}
For x86 (64-bit) distrobutions:
```sh
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
```

For ARM distrobutions, execute the following: 
```sh
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
```
{{% /tab %}}
{{< /tabs >}}

2. To confirm that your CLI has been successfully installed, run the following in your shell/terminal:
```
aws --version
```
If everything was successful, this command should output the CLI versioning information. 

3. To ensure that your CLI is able to perform API calls, run the following:
```
aws sts get-caller-identity
```

This could return the user and account information of the active credentials used by the CLI.

