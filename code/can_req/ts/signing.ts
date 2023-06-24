import * as crypto from "crypto"

const SIGNING_ALGORITHM = "AWS4-HMAC-SHA256"

export function getTimestamps(): [string, string] {
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

export function getCredentialScope(reqTimestamp: string, region: string, service: string): string {
    return `${reqTimestamp}/${region}/${service}/aws4_request`
}

export function getStringToSign(amzTimestamp: string, scope: string, message: string): string {
    return [SIGNING_ALGORITHM, amzTimestamp, scope, computeSHA256SignatureHash(message)].join("\n")
}

export function sign(key: Buffer, message: Buffer): Buffer {
    return crypto.createHmac('SHA256', key).update(message).digest()
}

export function signHex(key: Buffer, message: Buffer): string {
    return crypto.createHmac('SHA256', key).update(message).digest('hex')
}

export function computeSHA256SignatureHash(input: string): string {
    return crypto.createHash("SHA256").update(input).digest("hex")
}

export function getAWS4SignatureKey(key: string, reqTimestamp: string, region: string, service: string): Buffer {
    const kDate = sign(Buffer.from("AWS4" + key), Buffer.from(reqTimestamp))
    const kRegion = sign(kDate, Buffer.from(region))
    const kService = sign(kRegion, Buffer.from(service))
    const kSigning = sign(kService, Buffer.from("aws4_request"))
    return kSigning
}

if (require.main === module) {
    // Get user input
    const secretKey = process.argv[2];
    const region = process.argv[3];
    const service = process.argv[4];
    const userInput = process.argv[5];

    // Get the required timestamp strings
    let [amzTimestamp, reqTimestamp] = getTimestamps()
    console.log("Amazon Timestamp: " + amzTimestamp)
    console.log("Requset Timestamp: " + reqTimestamp)

    // Get the scope of the request (the timestamp and the target service)
    const scope = getCredentialScope(reqTimestamp, region, service)
    console.log("Credential Scope: " + scope)

    //  Get the AWS v4 signing key
    const key = getAWS4SignatureKey(secretKey, reqTimestamp, region, service)
    console.log("Signing Key: " + key)

    // Prepare string value to sign from user input
    const stringToSign = getStringToSign(amzTimestamp, scope, userInput)
    console.log("String to sign: `" + stringToSign + "`")

    // Sign and output user string
    const signature = signHex(key, Buffer.from(stringToSign))
    console.log("Signed String: " + signature)
}
