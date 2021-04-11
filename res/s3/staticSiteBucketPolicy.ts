import * as aws from "@pulumi/aws"
import { staticSiteBucket } from "./staticSiteBucket"

function publicReadPolicyForBucket(bucketName: string) {
    return JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
        Effect: "Allow",
        Principal: "*",
        Action: [
        "s3:GetObject"
        ],
        Resource: [
        `arn:aws:s3:::${bucketName}/*`
        ]
        }]
    })
}
  
  
export const staticSiteBucketPolicy = new aws.s3.BucketPolicy("staticSiteBucketPolicy", {
    bucket: staticSiteBucket.bucket,
    policy: staticSiteBucket.bucket.apply(publicReadPolicyForBucket)
})