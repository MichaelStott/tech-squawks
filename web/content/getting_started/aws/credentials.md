---
title: Programatic Credentials
chapter: false
weight: 3
---

After successfully setting up an account, AWS automatically creates a default user entity known as the root user. In the following 
instructions, we will enable MFA (multi-factor authentication) to secure access to the root user, create an admin user for 
development purposes, and generate programtic credentials for the AWS CLI and SDKs.

### Activate MFA for Root Account

{{% notice info %}}
These instructions are for setting up a virtual MFA device. You can download the Google Authenticator app for 
both [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_US&gl=US) and 
[iOS](https://apps.apple.com/us/app/google-authenticator/id388497605). 
{{% /notice %}}

1. Log onto your AWS account. Type "IAM" into the top search bar and click on the first result from the dropdown.

2. On the dashboard, select the option to configure MFA on the root account.

3. Select "Virtual MFA Device" for the MFA type.

4. Using your MFA app on your mobile device of choice, scan the QR code and enter the two resulting codes.

### Create Admin User

1. Within the IAM menu, go to the users tab.

2. Create a user. Under the options, select both "Programatic access" and "AWS Management Console access". Enter an AWS console password and unselect "Require password rest"

3. Under "Attach existing policies directly", check "Aministrator Access".

4. Skip the tags section and click Create User

5. After the user is generated, click "Download .csv" to save the access and secret key to your local machine.
{{% notice warning %}}
You must download and save the credentials upon generation. Otherwise, there will be no way to download retrieve the secret key and
the credentials will be lost forever.
{{% /notice %}}