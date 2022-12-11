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
PARAMETER_NAME = "SlawekTestParam"
SERVICE = "ssm"
HOST = "ssm.us-west-2.amazonaws.com"
REGION = "us-west-2"

SIGNED_HEADERS = "content-type;host;x-amz-date;x-amz-target"

CANONICAL_URI = "/"
CANONICAL_QUERY_STRING = ""

def hex_encode(input: str):
    return str(binascii.hexlify(bytes(input,"ascii")))

def hex_encode(input: bytes):
    return str(binascii.hexlify(input))

def compute_sha256_hash(input: str):
    m = hashlib.sha256()
    m.update(bytes(input, "ascii"))
    # Note: hexdigest can be used to produce the hex encoded hash. 
    # Performed seperately here to better illustrate process.
    return m.digest()

def sign(key: str, input: str):
    m = hmac.HMAC(bytes(key, "ascii"), msg=input.encode("utf-8"), digestmod=hashlib.sha256)
    return m.digest() 

def get_signature_key(key, datestamp, region, service_name):
    kdate = sign(str(hex_encode(bytes("AWS4" + str(key), "ascii"))), str(datestamp))
    kregion = sign(str(kdate), region)
    kservice = sign(str(kregion), service_name)
    ksigning = sign(str(kservice), "aws4_request")
    return ksigning

def get_credential_scope(date_stamp: str):
    return "{}/{}/{}/aws4_request".format(date_stamp, REGION, SERVICE)

def get_string_to_sign(amzn_date_stamp, scope, can_req):
    return SIGNING_ALGORITHM + "\n" +\
        str(amzn_date_stamp) + "\n" +\
        scope + "\n" + str(compute_sha256_hash(can_req))

def get_endpoint():
    return "https://{}/".format(HOST)

def get_canonical_headers(amzn_date):
    headers = "content-type:" + CONTENT_TYPE + "\nhost:" + HOST + "\nx-amz-date:" + amzn_date + "\nx-amz-target:" + AMAZON_TARGET + "\n"
    return headers

def get_canonical_requests(canonical_headers: str, payload_hash):
    return "\n".join([METHOD, CANONICAL_URI, CANONICAL_QUERY_STRING, canonical_headers, SIGNED_HEADERS, str(payload_hash)])

def get_authorization_header(scope, signature):
    return SIGNING_ALGORITHM + " Credential=" + AWS_ACCESS_KEY_ID + "/" + scope + ", SignedHeaders=" + SIGNED_HEADERS + ", Signature=" + signature

if __name__ == "__main__":
    endpoint = get_endpoint()
    print ("Target AWS Endpoint: " + endpoint)

    # Generate timestamp information
    now = datetime.datetime.now()
    amazon_timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    req_timestamp = now.strftime("%Y%m%d")
    print("amzn_time: " + amazon_timestamp)
    print("req_time: " + req_timestamp)

    request_paramters = '{"Name":"' + PARAMETER_NAME + '","WithDecryption":true}'
    payload_hash = compute_sha256_hash(request_paramters)
    headers = get_canonical_headers(amazon_timestamp)
    canoniocal_request = get_canonical_requests(headers, payload_hash)
    credential_scope = get_credential_scope(req_timestamp)

    string_to_sign = get_string_to_sign(amazon_timestamp, credential_scope, canoniocal_request)
    print(AWS_SECRET_ACCESS_KEY)
    signature_key = get_signature_key(AWS_SECRET_ACCESS_KEY, req_timestamp, REGION, SERVICE)
    signature = sign(str(signature_key), string_to_sign)

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
