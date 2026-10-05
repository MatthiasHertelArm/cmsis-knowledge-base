---
id: "mbedtls-sample-applications-aes"
type: "concept"
domain: "security"
title: "Sample Applications: *`aes`*"
summary: "These example programs demonstrate the usage of the symmetric cipher API."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/sample_applications.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/sample_applications.md#aes"
license: "Apache-2.0"
mode: "V"
---

These example programs demonstrate the usage of the symmetric cipher API.
  
- `aescrypt2` - A sample application that performs authenticated encryption and decryption of a buffer, using `mbedtls_aes_crypt_ecb`, with AES-256. The application reads from a file, ciphers it and writes output to a file.
- `crypt_and_hash` - A file encryption application using the generic cipher and message digest (`md`) modules (only available in versions prior to 4.0).
