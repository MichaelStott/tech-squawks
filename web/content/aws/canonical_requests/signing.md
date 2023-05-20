---
title: Signing
draft: false
weight: 2
---

All canonical requests include a hash value generated from the API parameters and account credentials. When AWS recieves an API request, it generates the same hash from the provided API parameters and compares it to the original request. If the request hash and the AWS-generated hash do not match, the request is denied. The process of generating this request hash is known as _signing_.[^1]

There are two versions of AWS signing, version 4 and version 2, with version 2 actively being deprecated at the time of writing. While an overview of version 4 signatures is explored, those interested in signing version 2 signatures may find more information [here](https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html).

#### Version 4 Signing

 The version 4 signing process consists of the following steps and components:

1. Creating the _credential scope_: This value restricts the request to the target service and region and is of the following format: ```TIMESTAMP/REGION/SERVICE/SIGNING_VERSION``` where the timestamp is of form _YYYYMMDD_.

2. Generate the target string to sign: This consists of the signing algorithm used to produce the signature (AWS4-HMAC-SHA256), the Amzaon-formatted request timestamp (i.e. YYYYMMDDHHMMSSZ), the previously produced credential scope, and a hash of the canonical requests string, all separated by newline characters:
{{< tabs groupId="pseudo" >}}
{{% tab name="pseudocode" %}}
```
signatureString = SIGNING_ALGORITHM + "\n" +
AMAZON_DATE_TIMESTAMP + "\n" + 
CREDENTIAL_SCOPE + "\n" + 
SHA256(CANONICAL_REQUEST_STRING)
```
{{% /tab %}}
{{< /tabs >}}

3. Create the signature key: The _signature key_, used to sign the request string, is derived from the AWS secret key, Amazon-formatted request timestamp, region, and service. The folling pseudocode illustrates this process:
{{< tabs groupId="pseudo" >}}
{{% tab name="pseudocode" %}}
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
{{% tab name="pseudocode" %}}
```
signature = hexEncode(hash(signatureKey, signatureString))
```
{{% /tab %}}
{{< /tabs >}}

##### Demo

Below provides a concrete example for generating a version 4 signature from an arbitrary string [^2]:

{{< tabs groupId="code" >}}
{{% tab name="Typescript" %}}
```py
# can_req/py/signing.py

import datetime, hashlib, hmac, sys


SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"


def get_timestamps() -> tuple[str, str]:
    """ Get strings of required timestamps for canonical requests
    """
    now = datetime.datetime.utcnow()
    amazon_timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    req_timestamp = now.strftime("%Y%m%d")
    return amazon_timestamp, req_timestamp


def get_credential_scope(date_stamp: str) -> str:
    """ Define the scope of the request, which includes the target region and service
    """
    return "{}/{}/{}/aws4_request".format(date_stamp, REGION, SERVICE)


def sign(key: str, msg: str) -> bytes:
    """ Generate the HMAC-SHA256 hash of a target string using the provided secret key
    """
    return hmac.new(key , msg.encode('utf-8'), hashlib.sha256).digest()


def compute_sha256_hash(input: str) -> str:
    """ Create SHA256 hash of a target string
    """
    m = hashlib.sha256()
    m.update(input.encode("utf-8"))
    result =  m.hexdigest()
    return result


def get_string_to_sign(amzn_date_stamp: str, scope: str, can_req: str) -> str:
    """ Get string to sign from request parameters
    """
    return "\n".join([SIGNING_ALGORITHM, amzn_date_stamp, scope, compute_sha256_hash(can_req)]).encode("utf-8")


def get_aws4_signature_key(key: str, datestamp: str, region: str, service_name: str) -> bytes:
    """ Generature canonical requests signature
    """
    kdate = sign(("AWS4" + key).encode("utf-8"), datestamp)
    kregion = sign(kdate, region)
    kservice = sign(kregion, service_name)
    ksigning = sign(kservice, "aws4_request")
    return ksigning


if __name__ == "__main__":
    # Get user input from command args
    amazon_secret_key = sys.argv[1]
    region = sys.argv[2]
    service = sys.argv[3]
    user_input = sys.argv[4]

    # Fetch the required timestamps
    amazon_timestamp, req_timestamp = get_timestamps()

    # The scope/action permitted by the signed token
    credential_scope = get_credential_scope(req_timestamp)

    # Generate string to sign from user input
    string_to_sign = get_string_to_sign(amazon_timestamp, credential_scope, user_input)

    # Generate signature signing key from AWS secret key
    signature_key = get_aws4_signature_key(amazon_secret_key, req_timestamp, REGION, SERVICE)
    
    # Generate and print signed string 
    signature = hmac.new(signature_key, string_to_sign, hashlib.sha256).hexdigest()
    print(signature)
```
{{% /tab %}}
{{% tab name="Javascript" %}}
```py
def sign(key: str, msg: str):
    return hmac.new(key , msg.encode('utf-8'), hashlib.sha256).digest()

def get_aws4_signature_key(key: str, datestamp: str, region: str, service_name: str):
    kdate = sign(("AWS4" + key).encode("utf-8"), datestamp)
    kregion = sign(kdate, region)
    kservice = sign(kregion, service_name)
    ksigning = sign(kservice, "aws4_request")
    return ksigning
```
{{% /tab %}}
{{% tab name="Python" %}}
```py
def sign(key: str, msg: str):
    return hmac.new(key , msg.encode('utf-8'), hashlib.sha256).digest()

def get_aws4_signature_key(key: str, datestamp: str, region: str, service_name: str):
    kdate = sign(("AWS4" + key).encode("utf-8"), datestamp)
    kregion = sign(kdate, region)
    kservice = sign(kregion, service_name)
    ksigning = sign(kservice, "aws4_request")
    return ksigning
```
{{% /tab %}}
{{% tab name="Go" %}}
```py
def sign(key: str, msg: str):
    return hmac.new(key , msg.encode('utf-8'), hashlib.sha256).digest()

def get_aws4_signature_key(key: str, datestamp: str, region: str, service_name: str):
    kdate = sign(("AWS4" + key).encode("utf-8"), datestamp)
    kregion = sign(kdate, region)
    kservice = sign(kregion, service_name)
    ksigning = sign(kservice, "aws4_request")
    return ksigning
```
{{% /tab %}}
{{< /tabs >}}

[^1]: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html

[^2]: https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html
    