---
title: Signing
draft: false
weight: 2
---

All canonical requests include a hash value generated from the API parameters and account credentials. When AWS receives an API request, it generates the same hash from the provided API parameters and compares it to the original request to validate the identity of the caller. If the request hash and the AWS-generated hash do not match, the request is denied. The process of generating this request hash is known as _signing_.[^1]

{{% notice info %}}
There are two versions of AWS signing, version 4 and version 2, with version 2 being deprecated at the time of writing. As such, only version 4 is explored here.
{{% /notice %}}

#### Version 4 Signing

The version 4 signing process consists of the following steps and components[^2]:

1. Creating the _credential scope_: This value restricts the request to the target service and region and is of the following format: `TIMESTAMP/REGION/SERVICE/SIGNING_VERSION` where the timestamp value is of form _YYYYMMDD_.

2. Generate the target string to sign: This consists of the signing algorithm used to produce the signature (AWS4-HMAC-SHA256), the Amzaon-formatted request timestamp (i.e. _YYYYMMDDHHMMSSZ_), the previously produced credential scope, and a hash of the canonical requests string, all separated by newline characters:
   {{< tabs groupId="pseudo" >}}
   {{% tab name="Pseudocode" %}}

```
signatureString = SIGNING_ALGORITHM + "\n" +
AMAZON_DATE_TIMESTAMP + "\n" +
CREDENTIAL_SCOPE + "\n" +
SHA256(CANONICAL_REQUEST_STRING)
```

{{% /tab %}}
{{< /tabs >}}

3. Create the signature key: The _signature key_, used to sign the request string, is derived from the AWS secret key, Amazon-formatted request timestamp, region, and service. The following Pseudocode illustrates this process:
   {{< tabs groupId="pseudo" >}}
   {{% tab name="Pseudocode" %}}

```
kDate = hash("AWS4" + Key, Date)
kRegion = hash(kDate, Region)
kService = hash(kRegion, Service)
signatureKey = hash(kService, "aws4_request")
```

{{% /tab %}}
{{< /tabs >}}

4. Sign the previously generated signature string with the signature key and encode the hexadecimal representation.
   {{< tabs groupId="pseudo" >}}
   {{% tab name="Pseudocode" %}}

```
signature = hexEncode(hash(signatureKey, signatureString))
```

{{% /tab %}}
{{< /tabs >}}

##### Demo

Below provides a concrete example for generating a version 4 signature from an arbitrary string:

{{< tabs groupId="code" >}}
{{< tab name="Typescript" >}}
{{< tabs >}}
{{% tab name="Execution" %}}

```
ts-node signing.ts $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="signing.ts" %}}

```ts
{{% include file="assets\can_req\ts\signing.ts" %}}
```

{{% /tab %}}
{{< /tabs >}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/ts" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< tab name="Javascript" >}}
{{< tabs >}}
{{% tab name="Execution" %}}

```
node signing.js $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="signing.js" %}}

```js
{{% include file="assets\can_req\js\signing.js" %}}
```

{{% /tab %}}
{{< /tabs >}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/js" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< tab name="Python" >}}
{{< tabs >}}
{{% tab name="Execution" %}}

```
python3 signing.py $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="signing.py" %}}

```py
{{% include file="assets\can_req\py\signing.py" %}}
```

{{% /tab %}}
{{< /tabs >}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/py" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< tab name="Go" >}}
{{< tabs >}}
{{% tab name="Execution" %}}

```
go run signing_driver.go signing.go $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

{{% /tab %}}
{{< /tabs >}}
{{< tabs >}}
{{% tab name="signing.go" %}}

```go
{{% include file="assets\can_req\go\signing.go" %}}
```

{{% /tab %}}
{{% tab name="signing_driver.go" %}}

```go
{{% include file="assets\can_req\go\signing_driver.go" %}}
```

{{% /tab %}}
{{< /tabs >}}
{{% button href="https://github.com/MichaelStott/tech-squawks/tree/main/code/can_req/go" icon="code" %}}Repository{{% /button %}}
{{% button href="https://github.com/MichaelStott/tech-squawks/issues/new/choose" icon="bug" %}}Report Issue{{% /button %}}
{{< /tab >}}
{{< /tabs >}}

**Output**

```
Amazon Timestamp: 20230625T174754Z
Requset Timestamp: 20230625
Credential Scope: 20230625/us-west-1/ssm/aws4_request
Signing Key: 843b458b4664ec9c54e42274a490b2c7cb2802cc104dcba2ad2df8fe71c008ff
String to sign: "AWS4-HMAC-SHA256\n20230625T174754Z\n20230625/us-west-1/ssm/aws4_request\n7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069"
Signed String: cc1a8368f317707c89b33e8f627f722819ed4d28341fef7b56720103b5d3fe79
```

[^1]: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
[^2]: https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html
