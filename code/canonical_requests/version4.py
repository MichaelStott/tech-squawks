import binascii
import datetime 
import hashlib
import hmac
import requests
from boto3 import Session

session = Session()
credentials = session.get_credentials()
current_credentials = credentials.get_frozen_credentials()

# TODO: FETCH THIS DYNAMICALLY. DO NOT HARDCODE THIS.
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

def sign(key: str, input: str,):
    m = hmac.HMAC(bytes(key, "ascii"), digestmod=hashlib.sha512)
    return m.digest() 

def get_signature_key(key, datestamp, region, service_name):
    kdate = sign("AWS4" + key, datestamp)
    kregion = sign(kdate, region)
    kservice = sign(kregion, service_name)
    ksigning = sign(kservice, "aws4_reqquest")
    return ksigning

def get_credential_scope(date_stamp: str):
    return "{}/{}/{}/aws4_request".format(date_stamp, REGION, SERVICE)

def get_endpoint():
    return "https://{}/".format(HOST)

def get_canonical_headers(amzn_date):
    headers = "content-type:" + CONTENT_TYPE + "\nhost:" + HOST + "\nx-amz-date:" + amzn_date + "\nx-amz-target:" + AMAZON_TARGET + "\n"
    return headers

def get_canonical_requests(canonical_headers):
    return [METHOD, CANONICAL_URI, CANONICAL_QUERY_STRING, canonical_headers, SIGNED_HEADERS, payload_hash].join("\n")

if __name__ == "__main__":
    hex_hash = hex_encode(compute_sha256_hash("hello world!"))
    print ("Comoputed Hash: " + str(hex_hash))
    endpoint = get_endpoint()
    print ("Target AWS Endpoint: " + endpoint)

    # Generate timestamp information
    now = datetime.datetime.now()
    amazon_timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    req_timestamp = now.strftime("%Y%m%d")
    print("amzn_time: " + amazon_timestamp)
    print("req_time: " + req_timestamp)

    headers = get_canonical_headers(amazon_timestamp)
    canoniocal_request = get_canonical_requests(headers)
    
    request_paramters = '{"Name":"' + PARAMETER_NAME + '","WithDecryption":true}'
    payload_hash = sign(request_paramters)
    scope = get_credential_scope(req_timestamp)
    print ("scope: " + scope)
    # Perform AWS API call
    headers = {
        "Accept-Encoding": "identity",
        "Content-Type": CONTENT_TYPE,
        "X-Amz-Date": amazon_timestamp,
        "X-Amz-Target": AMAZON_TARGET,
        "Authorization": ""
    }
    resp = requests.get(endpoint, headers=headers, data=request_paramters)

    print(resp.status_code)
