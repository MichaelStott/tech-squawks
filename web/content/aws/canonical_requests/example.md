---
title: Requests
draft: false
weight: 3
---

The following code snippets demonstrate sending canonical rqeuests to AWS. For interested readers, the AWS SDKs can provide
further concrete examples that handle this in a more general fashion.

{{< tabs groupId="code" >}}
{{% tab name="Typescript" %}}
```py
# can_req/py/request.py

from signing import *

import requests
from boto3 import Session

# Default API parameters provided here for convenience
METHOD = "POST"
SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"
AMAZON_TARGET = "AmazonSSM.GetParameter"
CONTENT_TYPE = "application/x-amz-json-1.1"
PARAMETER_NAME = "TechSquawkParam"
SERVICE = "ssm"
HOST = "ssm.us-west-2.amazonaws.com"
REGION = "us-west-2"
SIGNED_HEADERS = "content-type;host;x-amz-date;x-amz-target"
CANONICAL_URI = "/"
CANONICAL_QUERY_STRING = ""


def get_canonical_headers(amzn_date: str):
    """ Get canonical headers in proper format
    """
    return "\n".join(["content-type:{}".format(CONTENT_TYPE), "host:{}".format(HOST), "x-amz-date:{}".format(amzn_date), "x-amz-target:{}\n".format(AMAZON_TARGET)])

def get_canonical_requests(canonical_headers: str, payload_hash: str):
    """ Generate canonical request from the provided headers and payload hash
    """
    return "\n".join([METHOD, CANONICAL_URI, CANONICAL_QUERY_STRING, canonical_headers, SIGNED_HEADERS, payload_hash])

def get_authorization_header(scope: str, signature: str, amazon_key_id: str):
    """ Get the authorization header used for verifying the authenticity of the request
    """
    return "{} Credential={}/{}, SignedHeaders={}, Signature={}".format(SIGNING_ALGORITHM, amazon_key_id, scope, SIGNED_HEADERS, signature)

if __name__ == "__main__":
    # Get provided AWS access credentials
    amazon_key_id = sys.argv[1]
    amazon_secret_key = sys.argv[2]

    endpoint = "https://{}/".format(HOST)
    amazon_timestamp, req_timestamp = get_timestamps()
    credential_scope = get_credential_scope(req_timestamp)

    request_paramters = '{"Name":"' + PARAMETER_NAME + '","WithDecryption":true}'
    payload_hash = compute_sha256_hash(request_paramters)

    headers = get_canonical_headers(amazon_timestamp)
    canoniocal_request = get_canonical_requests(headers, str(payload_hash))
    credential_scope = get_credential_scope(req_timestamp)

    string_to_sign = get_string_to_sign(amazon_timestamp, credential_scope, canoniocal_request)
    signature_key = get_aws4_signature_key(amazon_secret_key, req_timestamp, REGION, SERVICE)
    signature = hmac.new(signature_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

    auth_header = get_authorization_header(credential_scope, signature, amazon_key_id)

    # Perform AWS API call
    headers = {
        "Accept-Encoding": "identity",
        "Content-Type": CONTENT_TYPE,
        "X-Amz-Date": amazon_timestamp,
        "X-Amz-Target": AMAZON_TARGET,
        "Authorization": auth_header
    }

    resp = requests.post(endpoint, headers=headers, data=request_paramters)

    print(resp.content)

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