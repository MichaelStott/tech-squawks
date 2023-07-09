from signing import *

import requests
import xml.dom.minidom

# Default API parameters provided here for convenience
METHOD = "GET"
SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"
CONTENT_TYPE = "application/x-amz-json-1.1"
SERVICE = "iam"
HOST = "iam.amazonaws.com"
REGION = "us-east-1"
SIGNED_HEADERS = "content-type;host;x-amz-date"
CANONICAL_URI = "/"
CANONICAL_QUERY_STRING = "Action=ListUsers&Version=2010-05-08"


def get_canonical_headers(amzn_date: str) -> str:
    """Get canonical headers in proper format"""
    return "\n".join(
        [
            "content-type:{}".format(CONTENT_TYPE),
            "host:{}".format(HOST),
            "x-amz-date:{}\n".format(amzn_date),
        ]
    )


def get_canonical_requests(canonical_headers: str, payload_hash: str) -> str:
    """Generate canonical request from the provided headers and payload hash"""
    return "\n".join(
        [
            METHOD,
            CANONICAL_URI,
            CANONICAL_QUERY_STRING,
            canonical_headers,
            SIGNED_HEADERS,
            payload_hash,
        ]
    )


def get_authorization_header(scope: str, signature: str, amazon_key_id: str) -> str:
    """Get the authorization header used for verifying the authenticity of the request"""
    return "{} Credential={}/{}, SignedHeaders={}, Signature={}".format(
        SIGNING_ALGORITHM, amazon_key_id, scope, SIGNED_HEADERS, signature
    )


if __name__ == "__main__":
    # Get provided AWS access credentials
    amazon_key_id = sys.argv[1]
    amazon_secret_key = sys.argv[2]

    endpoint = "https://{}/".format(HOST)
    amazon_timestamp, req_timestamp = get_timestamps()
    print("Amazon Timestamp: " + amazon_timestamp)
    print("Request Timestamp: " + req_timestamp)

    credential_scope = get_credential_scope(req_timestamp, REGION, SERVICE)
    print("Credential Scope: " + credential_scope)

    # API  parameters should be listed here when applicable.
    request_paramters = ""
    payload_hash = compute_sha256_hash(request_paramters)

    headers = get_canonical_headers(amazon_timestamp)
    canoniocal_request = get_canonical_requests(headers, str(payload_hash))

    signature_key = get_aws4_signature_key(
        amazon_secret_key, req_timestamp, REGION, SERVICE
    )
    print("Signing Key: " + base64.b64encode(signature_key).decode())
    string_to_sign = get_string_to_sign(
        amazon_timestamp, credential_scope, canoniocal_request
    )
    signature = hmac.new(
        signature_key, (string_to_sign).encode("utf-8"), hashlib.sha256
    ).hexdigest()
    print("Signature: " + signature)

    auth_header = get_authorization_header(credential_scope, signature, amazon_key_id)
    print("Auth Header: " + auth_header)

    # Perform AWS API call
    headers = {
        "Accept-Encoding": "identity",
        "Content-Type": CONTENT_TYPE,
        "X-Amz-Date": amazon_timestamp,
        "Authorization": auth_header,
    }
    resp = requests.get(
        "https://iam.amazonaws.com/?Action=ListUsers&Version=2010-05-08",
        headers=headers,
    )
    print(
        "\nAPI Response:\n"
        + xml.dom.minidom.parseString(resp.content).toprettyxml(indent="", newl="")
    )
