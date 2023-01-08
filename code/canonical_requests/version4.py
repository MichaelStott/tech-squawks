import binascii
import datetime 
import hashlib
import hmac
import requests
from boto3 import Session

session = Session()
credentials = session.get_credentials()
current_credentials = credentials.get_frozen_credentials()

AWS_ACCESS_KEY_ID = current_credentials.access_key
AWS_SECRET_ACCESS_KEY = current_credentials.secret_key

METHOD = "POST"
SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"
AMAZON_TARGET = "AmazonSSM.GetParameter"
CONTENT_TYPE = "application/x-amz-json-1.1"
PARAMETER_NAME = "TechSquawkParam"
SERVICE = "ssm"
HOST = "ssm.us-west-2.amazonaws.com"
REGION = "us-west-2"

# Headers listed in alphabetical order
SIGNED_HEADERS = "content-type;host;x-amz-date;x-amz-target"

CANONICAL_URI = "/"
CANONICAL_QUERY_STRING = ""

def compute_sha256_hash(input: str):
    m = hashlib.sha256()
    m.update(input.encode("utf-8"))
    result =  m.hexdigest()
    return result

def sign(key: str, msg: str):
    return hmac.new(key , msg.encode('utf-8'), hashlib.sha256).digest()

def get_aws4_signature_key(key: str, datestamp: str, region: str, service_name: str):
    kdate = sign(("AWS4" + key).encode("utf-8"), datestamp)
    kregion = sign(kdate, region)
    kservice = sign(kregion, service_name)
    ksigning = sign(kservice, "aws4_request")
    return ksigning

def get_credential_scope(date_stamp: str):
    return "{}/{}/{}/aws4_request".format(date_stamp, REGION, SERVICE)

def get_string_to_sign(amzn_date_stamp: str, scope: str, can_req: str):
    return "\n".join([SIGNING_ALGORITHM, amzn_date_stamp, scope, compute_sha256_hash(can_req)])

def get_canonical_headers(amzn_date: str):
    return "\n".join(["content-type:{}".format(CONTENT_TYPE), "host:{}".format(HOST), "x-amz-date:{}".format(amzn_date), "x-amz-target:{}\n".format(AMAZON_TARGET)])

def get_canonical_requests(canonical_headers: str, payload_hash: str):
    return "\n".join([METHOD, CANONICAL_URI, CANONICAL_QUERY_STRING, canonical_headers, SIGNED_HEADERS, payload_hash])

def get_authorization_header(scope: str, signature: str):
    return "{} Credential={}/{}, SignedHeaders={}, Signature={}".format(SIGNING_ALGORITHM, AWS_ACCESS_KEY_ID, scope, SIGNED_HEADERS, signature)

if __name__ == "__main__":
    endpoint = "https://{}/".format(HOST)

    now = datetime.datetime.utcnow()
    amazon_timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    req_timestamp = now.strftime("%Y%m%d")

    request_paramters = '{"Name":"' + PARAMETER_NAME + '","WithDecryption":true}'
    payload_hash = compute_sha256_hash(request_paramters)
    
    headers = get_canonical_headers(amazon_timestamp)
    canoniocal_request = get_canonical_requests(headers, str(payload_hash))
    credential_scope = get_credential_scope(req_timestamp)

    string_to_sign = get_string_to_sign(amazon_timestamp, credential_scope, canoniocal_request)
    signature_key = get_aws4_signature_key(AWS_SECRET_ACCESS_KEY, req_timestamp, REGION, SERVICE)
    signature = hmac.new(signature_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

    auth_header = get_authorization_header(credential_scope, str(signature))

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

