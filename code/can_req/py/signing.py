import base64, datetime, hashlib, hmac, json, sys

SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"


def get_timestamps() -> tuple[str, str]:
    """Get strings of required timestamps for canonical requests"""
    now = datetime.datetime.utcnow()
    amazon_timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    req_timestamp = now.strftime("%Y%m%d")
    return amazon_timestamp, req_timestamp


def get_credential_scope(req_timestamp: str, region: str, service: str) -> str:
    """Define the scope of the request, which includes the target region and service"""
    return "{}/{}/{}/aws4_request".format(req_timestamp, region, service)


def sign(key: str, msg: str) -> bytes:
    """Generate the HMAC-SHA256 hash of a target string using the provided secret key"""
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def compute_sha256_hash(input: str) -> str:
    """Create SHA256 hash of a target string"""
    m = hashlib.sha256()
    m.update(input.encode("utf-8"))
    result = m.hexdigest()
    return result


def get_string_to_sign(amzn_date_stamp: str, scope: str, can_req: str) -> str:
    """Get string to sign from request parameters"""
    return "\n".join(
        [SIGNING_ALGORITHM, amzn_date_stamp, scope, compute_sha256_hash(can_req)]
    )


def get_aws4_signature_key(
    key: str, datestamp: str, region: str, service_name: str
) -> bytes:
    """Generature canonical requests signature"""
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
    print("Amazon Timestamp: " + amazon_timestamp)
    print("Request Timestamp: " + req_timestamp)

    # The scope/action permitted by the signed credentials
    credential_scope = get_credential_scope(req_timestamp, region, service)
    print("Credential Scope: " + credential_scope)

    # Generate and print signed string
    signature_key = get_aws4_signature_key(
        amazon_secret_key, req_timestamp, region, service
    )
    print("Signing Key: " + base64.b64encode(signature_key).decode())
    string_to_sign = get_string_to_sign(amazon_timestamp, credential_scope, user_input)
    print("String to sign: " + json.dumps(string_to_sign))
    signature = hmac.new(
        signature_key, string_to_sign.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    print("Signed String: " + signature)
