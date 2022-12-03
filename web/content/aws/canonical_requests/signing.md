---
title: Signing
draft: false
weight: 2
---

All canonical requests include a hash of the request parameters, generated using the client secret. When AWS recieves an API requests, it generates this same hash from the provided API parameters and compares this to the client-generated hash, similar to a JWT token. If the hashes do not match, the request is denied. This process of generating this hash for canonical requests is known as siigning and is required when invoking AWS API calls.[^1]

### Signing Versions

There are two versions of AWS signing, version 4 and version 2. Version 4 is predominantly used, however DynamoDB, AWS's NoSQL database solution, still leverages version 2 signing in AWS requests. While an overview of version 4 signatures is explored, those interested in signing version 2 signatures may find more information [here](https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html).

#### Version 4

Below provides a general procedure for producing a version 4 signature [^2]:

1. Create a canonical requests
2. Use the cnanoical request and additional metadata to createa  string for signing.
3. Derive a signing key from your AWS secret access key. Then use the signing key, and the string from the previous step, to create a signature.
4.Add the resulting signature ot the HTTP request in a header or as a query string parameter

[^1]: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html

[^2]: https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html
    