
import * as pulumi from "@pulumi/pulumi"
import * as s3 from "./res/s3"
import * as cf from './res/cloudfront'

export const s3WebsiteEndpoint = s3.staticSiteBucket.websiteEndpoint

export const cfdEndpoint = cf.cdn !== undefined ? cf.cdn?.domainName : "N/A"