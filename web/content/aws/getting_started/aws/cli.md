---
title: CLI
draft: false
chapter: false

weight: 4
---

AWS provides a CLI tool for facilitating the invocation of cloud APIs, leveraging a user's local credentials.

The following instructions target *version 2* of the AWS CLI. For *version 1*, see these [instructions](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html). Note that these versions are not backwards compatible.

### Instructions 
S
1. Download and install the CLI for the desired operating system:
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

2. Run the following too confirm that the CLI has been successfully installed:
{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws --version
```
**Output**
```
aws-cli/2.5.8 Python/3.9.11 Windows/10 exe/AMD64 prompt/off
```
{{% /tab %}}
{{< /tabs >}}

3. Run the following and enter the credentials downloaded from the previous section when prompted. This will enable the
CLI to authenitcate with AWS services.
{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws configure
```
**Interactive Prompt**
```
AWS Access Key ID [None]: access-key-value-here
AWS Secret Access Key [None]: secret-key-value-here
Default region name [None]: us-east-1
Default output format [None]:
```
{{% /tab %}}
{{< /tabs >}}

4. Run the following to ensure the CLI is properly configured, which will return the active user and account information.
{{< tabs groupId="CLI" >}}
{{% tab name="CLI" %}}
**Command**
```sh
aws sts get-caller-identity
```
**Output**
```
{
    "UserId": "BIDAYGZ7AN44NDI6LOIG4",
    "Account": "012345678910",
    "Arn": "arn:aws:iam::012345678910:user/username"
}
```
{{% /tab %}}
{{< /tabs >}}
