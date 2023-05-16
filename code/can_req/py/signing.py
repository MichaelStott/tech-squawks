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