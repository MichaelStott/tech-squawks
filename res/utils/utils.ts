
import * as pulumi from "@pulumi/pulumi";

export const getResourceLabel = (name: string): string => {
    return `${pulumi.getProject()}-${pulumi.getStack()}-${name}`
}

export const isProd = (): boolean => {
    return pulumi.getStack() === "production"
}