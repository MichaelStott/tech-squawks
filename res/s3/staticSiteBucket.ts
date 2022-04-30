import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi"
import * as mime from "mime"
import * as glob from "glob"
import * as fs from "fs"

export const staticSiteBucket = new aws.s3.Bucket("tech-squawks-bucket-" + pulumi.getStack(), {
    acl: "public-read",
    website: {
        indexDocument: "index.html",
        errorDocument: "404.html",
        routingRules: `[{
            "Condition": {
                "KeyPrefixEquals": "docs/"
            },
            "Redirect": {
                "ReplaceKeyPrefixWith": "documents/"
            }
        }]
        `,
    },
    versioning: {
        enabled: true
    },
    forceDestroy: true
})

glob.sync("./web/public/**/*", {}).map((filePath: string) => {
    if (fs.lstatSync(filePath).isFile()) {
        let obj = new aws.s3.BucketObject(filePath.replace('./web/public/',''), {
            bucket: staticSiteBucket,
            source: new pulumi.asset.FileAsset(filePath),
            contentType: mime.getType(filePath) || undefined,
        })
    }
})