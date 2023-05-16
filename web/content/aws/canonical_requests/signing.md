---
title: Signing
draft: false
weight: 2
---

All canonical requests include a hash value generated from the API parameters and account credentials. When AWS recieves an API request, it generates the same hash from the provided API parameters and compares it to the original request. If the request hash and the AWS-generated hash match, the request is authenticated and denied otherwise. The process of generating this request hash is known as _signing_.[^1]

There are two versions of AWS signing, version 4 and version 2, with version 2 actively being deprecated at the time of writing. While an overview of version 4 signatures is explored, those interested in signing version 2 signatures may find more information [here](https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html).

#### Version 4 Demo

Below provides a general procedure for producing a version 4 signature [^2]:

1. Use the canonical request and additional metadata to create a string for signing.
2. Derive a signing key from your AWS secret access key. Then use the signing key, and the string from the previous step, to create a signature.
3. Add the resulting signature ot the HTTP request in a header or as a query string parameter

{{< tabs groupId="code" >}}
{{% tab name="Typescript" %}}
```py
# can_req/py/signing.py

import datetime, hashlib, hmac, sys

REGION = "us-west-2"
SERVICE = "ssm"
SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"


def get_timestamps() -> tuple[str, str]:
    """ Get strings of required timestamps for canonical requests
    """
    now = datetime.datetime.utcnow()
    amazon_timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    req_timestamp = now.strftime("%Y%m%d")
    return amazon_timestamp, req_timestamp


def get_credential_scope(date_stamp: str):
    """ Get the scope of the credential, which defines the target region and service
    """
    return "{}/{}/{}/aws4_request".format(date_stamp, REGION, SERVICE)


def sign(key: str, msg: str):
    """ Generate SHA256 hash of string using provided secret key
    """
    return hmac.new(key , msg.encode('utf-8'), hashlib.sha256).digest()


def compute_sha256_hash(input: str):
    """ Create SHA256 hash of string
    """
    m = hashlib.sha256()
    m.update(input.encode("utf-8"))
    result =  m.hexdigest()
    return result


def get_string_to_sign(amzn_date_stamp: str, scope: str, can_req: str):
    """ Get string to sign from request parameters
    """
    return "\n".join([SIGNING_ALGORITHM, amzn_date_stamp, scope, compute_sha256_hash(can_req)])

def get_aws4_signature_key(key: str, datestamp: str, region: str, service_name: str):
    """ Generature canonical requests signature
    """
    kdate = sign(("AWS4" + key).encode("utf-8"), datestamp)
    kregion = sign(kdate, region)
    kservice = sign(kregion, service_name)
    ksigning = sign(kservice, "aws4_request")
    return ksigning


if __name__ == "__main__":
    amazon_timestamp, req_timestamp = get_timestamps()
    credential_scope = get_credential_scope(req_timestamp)

    amazon_secret_key = sys.argv[1]
    string_to_sign = get_string_to_sign(amazon_timestamp, credential_scope, "hello")
    signature_key = get_aws4_signature_key(amazon_secret_key, req_timestamp, REGION, SERVICE)
    signature = hmac.new(signature_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()
    
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
    