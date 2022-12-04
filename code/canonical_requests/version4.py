import binascii
import datetime 
import hashlib
import requests

AMAZON_TARGET = "AmazonSSM.GetParameter"
CONTENT_TYPE = "application/x-amz-json-1.1"
PARAMETER_NAME = "SlawekTestParam"
SERVICE = "ssm"
HOST = "ssm.us-west-2.amazonaws.com"
REGION = "us-west-2"

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

def sign(input: str, key: str):
    pass

def get_endpoint():
    return "https://{}/".format(HOST)

if __name__ == "__main__":
    hex_hash = hex_encode(compute_sha256_hash("hello world!"))
    print ("Comoputed Hash: " + str(hex_hash))
    endpoint = get_endpoint()
    print ("Target AWS Endpoint: " + endpoint)

    # Generate timestamp information
    now = datetime.datetime.now()
    amazon_timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    req_timestamp = now.strftime("%Y%m%d")
    print(amazon_timestamp)
    print(req_timestamp)

    # Perform AWS API call
    headers = {
        "Accept-Encoding": "identity",
        "Content-Type": CONTENT_TYPE,
        "X-Amz-Date": amazon_timestamp,
        "X-Amz-Target": AMAZON_TARGET,
        "Authorization": ""
    }
    resp = requests.get(endpoint, headers=headers)

    print(resp.status_code)



