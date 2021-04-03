import { getResourceLabel, isProd } from '../utils';
import * as aws from "@pulumi/aws"

/**
 * Contains the compiled static website contents.
 */
const websiteBucket = new aws.s3.Bucket(
    getResourceLabel("techsquawks-site-bucket"), {
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
        forceDestroy: !isProd()
    }
);
