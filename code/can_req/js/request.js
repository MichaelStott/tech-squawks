const signing = require(`./signing.js`);
const https = require("https");

const METHOD = "POST";
const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256";
const AMAZON_TARGET = "AmazonSSM.GetParameter";
const CONTENT_TYPE = "application/x-amz-json-1.1";
const PARAMETER_NAME = "TechSquawkParam";
const SERVICE = "ssm";
const HOST = "ssm.us-west-2.amazonaws.com";
const REGION = "us-west-2";
const SIGNED_HEADERS = "content-type;host;x-amz-date;x-amz-target";
const CANONICAL_URI = "/";
const CANONICAL_QUERY_STRING = "";

function getCanonicalHeaders(amzTimestamp) {
  return [
    "content-type:" + CONTENT_TYPE,
    "host:" + HOST,
    "x-amz-date:" + amzTimestamp,
    "x-amz-target:" + AMAZON_TARGET + "\n",
  ].join("\n");
}

function getCanonicalRequest(canonicalHeaders, payloadHash) {
  return [
    METHOD,
    CANONICAL_URI,
    CANONICAL_QUERY_STRING,
    canonicalHeaders,
    SIGNED_HEADERS,
    payloadHash,
  ].join("\n");
}

function getAuthorizationHeader(scope, signature, amazonKeyId) {
  return `${SIGNING_ALGORITHM} Credential=${amazonKeyId}/${scope}, SignedHeaders=${SIGNED_HEADERS}, Signature=${signature}`;
}

if (require.main === module) {
  // Get user input
  const amazonKeyId = process.argv[2];
  const secretKey = process.argv[3];

  // Get the required timestamp strings
  [amzTimestamp, reqTimestamp] = signing.getTimestamps();
  console.log("Amazon Timestamp: " + amzTimestamp);
  console.log("Request Timestamp: " + reqTimestamp);

  // Get the scope of the request (the timestamp and the target service)
  const scope = signing.getCredentialScope(reqTimestamp, REGION, SERVICE);
  console.log("Credential Scope: " + scope);

  const requestParamters =
    `{"Name":"` + PARAMETER_NAME + `","WithDecryption":true}`;
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
  console.log("Signing Key: " + key.toString("hex"));

  // Prepare string value to sign from user input
  const stringToSign = signing.getStringToSign(
    amzTimestamp,
    scope,
    canonicalRequest
  );

  // Sign and output user string
  const signature = signing.signHex(key, stringToSign);
  console.log("Signature: " + signature);

  const authHeader = getAuthorizationHeader(scope, signature, amazonKeyId);
  console.log("Auth Header: " + authHeader);

  const canReqHeaders = {
    "Accept-Encoding": "identity",
    "Content-Type": CONTENT_TYPE,
    "X-Amz-Date": amzTimestamp,
    "X-Amz-Target": AMAZON_TARGET,
    Authorization: authHeader,
    "Content-Length": requestParamters.length,
  };

  var options = {
    hostname: HOST,
    path: "/",
    port: 443,
    method: "POST",
    headers: canReqHeaders,
  };
  var req = https.request(options, function (res) {
    res.on("data", (d) => {
      process.stdout.write(d);
    });
  });
  req.write(requestParamters);
  req.end(options.body || "").on("error", (err) => {
    console.log("Error: " + err.message);
  });
}
