---
id: "mbedtls-rsassa-pss-introduction"
type: "concept"
domain: "security"
title: "RSASSA-PSS: Introduction"
summary: "RSASSA-PSS was standardized in PKCS#1 v2.1. It can be used as an alternative to the more widespread RSASSA algorithm in PKCS#1 v1.5."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/generic/rsassa-pss.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/generic/rsassa-pss.md#introduction"
license: "Apache-2.0"
mode: "V"
---

**RSASSA-PSS** is an improved probabilistic signature scheme with appendix. This means that you can use a private RSA key to sign data in combination with random input. The other side of the communication can then verify the signature with the corresponding public RSA key. Because random data is used in this signature scheme, the two signatures for the same input are different and both can be used to verify the original data.

RSASSA-PSS was standardized in [PKCS#1 v2.1](https://tools.ietf.org/html/rfc3447). It can be used as an alternative to the more widespread RSASSA algorithm in PKCS#1 v1.5.
