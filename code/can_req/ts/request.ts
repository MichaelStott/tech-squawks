import * as signing from "./signing";
import * as https from "https";

const METHOD = "GET";
const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256";
const CONTENT_TYPE = "application/x-amz-json-1.1";
const SERVICE = "iam";
const HOST = "iam.amazonaws.com";
const REGION = "us-east-1";
const SIGNED_HEADERS = "content-type;host;x-amz-date";
const CANONICAL_URI = "/";
const CANONICAL_QUERY_STRING = "Action=ListUsers&Version=2010-05-08";

function getCanonicalHeaders(amzTimestamp: string) {
  return [
    "content-type:" + CONTENT_TYPE,
    "host:" + HOST,
    "x-amz-date:" + amzTimestamp + "\n",
  ].join("\n");
}

function getCanonicalRequest(canonicalHeaders: string, payloadHash: string) {
  return [
    METHOD,
    CANONICAL_URI,
    CANONICAL_QUERY_STRING,
    canonicalHeaders,
    SIGNED_HEADERS,
    payloadHash,
  ].join("\n");
}

function getAuthorizationHeader(
  scope: string,
  signature: string,
  amazonKeyId: string
) {
  return `${SIGNING_ALGORITHM} Credential=${amazonKeyId}/${scope}, SignedHeaders=${SIGNED_HEADERS}, Signature=${signature}`;
}

if (require.main === module) {
  // Get user input
  const amazonKeyId = process.argv[2];
  const secretKey = process.argv[3];

  // Get the required timestamp strings
  let [amzTimestamp, reqTimestamp] = signing.getTimestamps();
  console.log("Amazon Timestamp: " + amzTimestamp);
  console.log("Req Timestamp: " + reqTimestamp);

  // Get the scope of the request (the timestamp and the target service)
  const scope = signing.getCredentialScope(reqTimestamp, REGION, SERVICE);
  console.log("Credential Scope: " + scope);
  
  // API  parameters should be listed here when applicable.
  const requestParamters = ``;
  const payloadHash = signing.computeSHA256SignatureHash(requestParamters);

  const headers = getCanonicalHeaders(amzTimestamp);
  const canonicalRequest = getCanonicalRequest(headers, payloadHash);

  //  Get the AWS v4 signing key
  const key = signing.getAWS4SignatureKey(
    secretKey,
    reqTimestamp,
    REGION,
    SERVICE
  );
  const stringToSign = signing.getStringToSign(
    amzTimestamp,
    scope,
    canonicalRequest
  );

  // Sign and output user string
  const signature = signing.signHex(key, Buffer.from(stringToSign));
  console.log("Signature: " + signature);

  const authHeader = getAuthorizationHeader(scope, signature, amazonKeyId);
  console.log("Auth Header: " + authHeader);

  const canReqHeaders = {
    "Accept-Encoding": "identity",
    "Content-Type": CONTENT_TYPE,
    "X-Amz-Date": amzTimestamp,
    Authorization: authHeader,
    "Content-Length": requestParamters.length,
  };

  var options = {
    hostname: HOST,
    path: "/?Action=ListUsers&Version=2010-05-08",
    port: 443,
    method: METHOD,
    headers: canReqHeaders,
  };
  var req = https.request(options, function (res) {
    res.on("data", (d) => {
      process.stdout.write(d);
    });
  });
  req.write(requestParamters);
  req.end();
}
