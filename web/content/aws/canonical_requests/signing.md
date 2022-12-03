---
title: Signing
draft: false
weight: 2
---

I. Overview
    A. Definition
    B. Purpose
    C. Types of request siging
        1. Signature Version 2
        2. Signature Version 4


https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html

https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html

II. Signature 4
    A. Process
        1. Create a canonical requests
        2. Use the cnanoical request and additional metadata to createa  string for signing.
        3. Derive a signing key from your AWS secret access key. Then use the signing key, and the string from the previous step, to create a signature.
        4.Add the resulting signature ot the HTTP request in a header or as a query string parameter
    B. AWS Validation process
        1. Performs above steps
        2. Compares the hash (denied if hash does not match)
        3. Similar to a JWT signature
    