---
id: "mbedtls-how-to-fill-an-rsa-context-from-n-getting-the-modulus-n"
type: "concept"
domain: "security"
title: "How to fill an RSA context from N, E, P and Q: Getting the modulus (N)"
summary: "If the modulus (N) is known, you should send it as parameter to mbedtls_rsa_import() (or mbedtls_rsa_import_raw()). However if it is not known, it is calculated within the mbedtls_rsa_complete() function, if P and Q have been imported to the context."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/how-to-fill-rsa-context-from-n-e-p-and-q.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/how-to-fill-rsa-context-from-n-e-p-and-q.md#getting-the-modulus-n"
license: "Apache-2.0"
mode: "V"
---

If the modulus (**N**) is known, you should send it as parameter to `mbedtls_rsa_import()` (or `mbedtls_rsa_import_raw()`). However if it is not known, it is calculated within the `mbedtls_rsa_complete()` function, if **P** and **Q** have been imported to the context.
