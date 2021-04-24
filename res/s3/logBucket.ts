import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi"

export const logBucket = new aws.s3.Bucket("tech-squawks-log-bucket-" + pulumi.getStack(), {
    forceDestroy: true
})