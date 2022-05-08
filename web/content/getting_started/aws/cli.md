---
title: CLI
draft: false
chapter: false
weight: 4
---

The AWS CLI is used to interact with AWS resources and services through a local terminal or shell by making AWS API calls on your behalf with local credentials.

The following instructions target *version 2* of the AWS CLI. See these [instructions](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html) if you would prefer *version 1*. Note that these versions are not backwards compatible, so commands may differ between the two.

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
For x86 (64-bit) distributions:
```sh
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
```

For ARM distributions, execute the following: 
```sh
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
```
{{% /tab %}}
{{< /tabs >}}

2. To confirm that your CLI has been successfully installed, run the following in your shell/terminal:
```sh
aws --version
```
If everything was successful, this command should output the CLI versioning information. 

3. Using the credentials that were generated in the previous section, 

```sh
aws configure
```
```
AWS Access Key ID [None]: access-key-value-here
AWS Secret Access Key [None]: secret-key-value-here
Default region name [None]: us-east-2
Default output format [None]:
```

4. To ensure that your CLI is able to perform API calls, run the following, which should return the user and account information of the active credentials used by the CLI.
```sh
aws sts get-caller-identity
```

