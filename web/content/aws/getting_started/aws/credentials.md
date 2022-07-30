---
title: Programatic Credentials
draft: false
chapter: false

weight: 3
---

After successfully setting up an account, AWS automatically creates a default user entity known as the [root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html), 
which has unlimited access to all cloud resources. Because of this, it is considered [best practice](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials) to create a separate 
AWS user for development and rectrict access to the root user. The folowing instructions cover enabling MFA 
(multi-factor authentication) to secure access to the root user and creating a separate developer user with 
programtic credentials for the AWS CLI and SDK.

### Activate MFA for Root Account

1. Log into the AWS console. Type "IAM" into the top search bar and click on the first result from the dropdown.

2. On the IAM dashboard, select the option to configure MFA on the root account.

3. Select "Virtual MFA Device" for the MFA type.
{{% notice info %}}
You can download the Google Authenticator app for 
both [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_US&gl=US) and 
[iOS](https://apps.apple.com/us/app/google-authenticator/id388497605). 
{{% /notice %}}

4. Scan the resulting QR code and enter the two resulting codes.
{{% notice info %}}
It may be beneficial to save a screenshot of the QR code image. In the event that readers lose their MFA device,
MFA can then be easily reconfigured on a separate device.
{{% /notice %}}

### Create Admin User

1. Within the IAM menu, go to the users tab and press the "Add Users"

2. Select both "Programatic access" and "AWS Management Console access" options. Enter an AWS console password and unselect "Require password reset"

3. Under "Attach existing policies directly", check "Aministrator Access".

4. Skip the tags section and click Create User

5. After the user is generated, click "Download .csv" to download the access and secret key pair and a user-specific sign-in URL.
{{% notice warning %}}
Credentials are only available for download immediately after generation. Afterwards, the credentials will be unrecoverable.
{{% /notice %}}