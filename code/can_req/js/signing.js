var crypto = require('crypto');

const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"

function getTimestamps() {
    const now = new Date()
    const year = now.getUTCFullYear()
    const month = String(now.getUTCMonth() + 1).padStart(2, '0')
    const day = String(now.getUTCDate()).padStart(2, '0')
    const hours = String(now.getUTCHours()).padStart(2, '0')
    const minutes = String(now.getUTCMinutes()).padStart(2, '0')
    const seconds = String(now.getUTCSeconds()).padStart(2, '0')

    const amzTimestamp = `${year}${month}${day}T${hours}${minutes}${seconds}Z`
    const reqTimestamp = `${year}${month}${day}`
    return [amzTimestamp, reqTimestamp]
}

function getCredentialScope(reqTimestamp, region, service) {
    return `${reqTimestamp}/${region}/${service}/aws4_request`
}

function getStringToSign(amzTimestamp, scope, message) {
    return [SIGNING_ALGORITHM, amzTimestamp, scope, computeSHA256SignatureHash(message)].join("\n")
}

function sign(key, msg) {
    return crypto.createHmac('SHA256', key).update(Buffer.from(msg, "utf-8")).digest()
}

function signHex(key, msg) {
    return crypto.createHmac('SHA256', key).update(msg).digest('hex')
}

function computeSHA256SignatureHash(input) {
    return crypto.createHash("SHA256").update(Buffer.from(input, "utf-8")).digest("hex")
}

function getAWS4SignatureKey(key, reqTimestamp, region, service) {
    const kDate = sign(Buffer.from("AWS4" + key, "utf-8"), reqTimestamp)
    const kRegion = sign(kDate, region)
    const kService = sign(kRegion, service)
    const kSigning = sign(kService, "aws4_request")
    return kSigning
}

if (require.main === module) {
    // Get user input
    const secretKey = process.argv[2];
    const region = process.argv[3];
    const service = process.argv[4];
    const userInput = process.argv[5];

    // Get the required timestamp strings
    [amzTimestamp, reqTimestamp] = getTimestamps()
    console.log("Amazon Timestamp: " + amzTimestamp)
    console.log("Request Timestamp: " + reqTimestamp)

    // Get the scope of the request (the timestamp and the target service)
    const scope = getCredentialScope(reqTimestamp, region, service)
    console.log("Credential Scope: " + scope)

    //  Get the AWS v4 signing key
    const key = getAWS4SignatureKey(secretKey, reqTimestamp, region, service)
    console.log("Signing Key: " + key.toString('hex'))

    // Prepare string value to sign from user input
    const stringToSign = getStringToSign(amzTimestamp, scope, userInput)
    console.log("String to sign: `" + stringToSign + "`")

    // Sign and output user string
    const signature = signHex(key, stringToSign)
    console.log("Signed String: " + signature)
}


module.exports = { getTimestamps, getCredentialScope, computeSHA256SignatureHash, getAWS4SignatureKey, getStringToSign, signHex }