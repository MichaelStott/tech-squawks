import * as signing from './signing';
import * as https from 'https';

const METHOD = "POST"
const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"
const AMAZON_TARGET = "AmazonSSM.GetParameter"
const CONTENT_TYPE = "application/x-amz-json-1.1"
const PARAMETER_NAME = "TechSquawkParam"
const SERVICE = "ssm"
const HOST = "ssm.us-west-2.amazonaws.com"
const REGION = "us-west-2"
const SIGNED_HEADERS = "content-type;host;x-amz-date;x-amz-target"
const CANONICAL_URI = "/"
const CANONICAL_QUERY_STRING = ""

function getCanonicalHeaders(amzTimestamp: string) {
    return ["content-type:" +  CONTENT_TYPE, "host:" + HOST, "x-amz-date:" + amzTimestamp, "x-amz-target:" + AMAZON_TARGET + "\n"].join("\n")
}

function getCanonicalRequest(canonicalHeaders: string, payloadHash: string) {
    return [METHOD, CANONICAL_URI, CANONICAL_QUERY_STRING, canonicalHeaders, SIGNED_HEADERS, payloadHash].join("\n")
}

function getAuthorizationHeader(scope:string , signature: string, amazonKeyId: string) {
    return `${SIGNING_ALGORITHM} Credential=${amazonKeyId}/${scope}, SignedHeaders=${SIGNED_HEADERS}, Signature=${signature}`
}

if (require.main === module) {
    // Get user input
    const amazonKeyId = process.argv[2];
    const secretKey = process.argv[3];

    // Get the required timestamp strings
    let [amzTimestamp, reqTimestamp] = signing.getTimestamps()
    console.log("Amazon Timestamp: " + amzTimestamp)
    console.log("Req Timestamp: " + reqTimestamp)

     // Get the scope of the request (the timestamp and the target service)
    const scope = signing.getCredentialScope(reqTimestamp, REGION, SERVICE)
    console.log("Credential Scope: " + scope)

    const requestParamters = `{"Name":"` + PARAMETER_NAME + `","WithDecryption":true}`
    const payloadHash = signing.computeSHA256SignatureHash(requestParamters)

    const headers = getCanonicalHeaders(amzTimestamp)
    const canonicalRequest = getCanonicalRequest(headers, payloadHash)

    //  Get the AWS v4 signing key
    const key = signing.getAWS4SignatureKey(secretKey, reqTimestamp, REGION, SERVICE)
    const stringToSign = signing.getStringToSign(amzTimestamp, scope, canonicalRequest)

    // Sign and output user string
    const signature = signing.signHex(key, Buffer.from(stringToSign))
    console.log("Signature: " + signature)

    const authHeader = getAuthorizationHeader(scope, signature, amazonKeyId)
    console.log("Auth Header: " + authHeader)

    const canReqHeaders = {
        "Accept-Encoding": "identity",
        "Content-Type": CONTENT_TYPE,
        "X-Amz-Date": amzTimestamp,
        "X-Amz-Target": AMAZON_TARGET,
        "Authorization": authHeader,
        'Content-Length': requestParamters.length
    }

    var options = {
        hostname: HOST,
        path: "/",
        port: 443,
        method: 'POST',
        headers: canReqHeaders
    };
    var req = https.request(options, function(res) { 
        res.on('data', (d) => {
            process.stdout.write(d)
        })
    })
    req.write(requestParamters)
    req.end()
}
