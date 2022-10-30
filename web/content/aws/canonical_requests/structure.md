---
title: Request Structure
draft: false
weight: 2
---

Canonical requests are of the following structure:

```
 CanonicalRequest =
  HTTPRequestMethod + '\n' +
  CanonicalURI + '\n' +
  CanonicalQueryString + '\n' +
  CanonicalHeaders + '\n' +
  SignedHeaders + '\n' +
  HexEncode(Hash(RequestPayload))
```

The individual fields are defined below:
- HTTPRequestMethod: The HTTP operation
- CanonicalURI: Absolute path of the target resouce, including the base service domain.
- CanonicalQueryString: URI-encoded query parameters
- CanonicalHeaders: List of all the HTTP headers included with the signed requests.
- SignedHeaders: Alphabetically sorted, semicolon-separated list of lowercase request header names
- RequestPayload: Payload of the target request. This is hashed and hex encoded for additional security.