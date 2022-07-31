---
title: CLI
draft: false
chapter: false

weight: 4
---

The AWS CLI is used to interact with AWS resources and services through a local terminal or shell. It leverages local 
credentials on the developers machine to successfully perform API calls.

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

2. To confirm that your CLI has been successfully installed, run the following in your shell/terminal to output the CLI version:
```sh
aws --version
```

3. Run the following and enter the credentials downloaded from the previous section when prompted. This will enable the
CLI to authenitcate with AWS and perform API calls.
```sh
aws configure
```
```
AWS Access Key ID [None]: access-key-value-here
AWS Secret Access Key [None]: secret-key-value-here
Default region name [None]: us-east-1
Default output format [None]:
```

4. Run the following to ensure the CLI is properly configured, which will return the active user and account information.
```sh
aws sts get-caller-identity
```

