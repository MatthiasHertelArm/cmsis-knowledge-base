---
id: "mbedtls-how-to-generate-a-self-signed-cert-generating-a-rsa-key-file"
type: "concept"
domain: "security"
title: "How to generate a self-signed certificate: Generating a RSA key file"
summary: "The first step for generating a self-signed certificate is to generate a private/public key pair for the certificate."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/generate-a-self-signed-certificate.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/generate-a-self-signed-certificate.md#generating-a-rsa-key-file"
license: "Apache-2.0"
mode: "V"
---

The first step for generating a self-signed certificate is to generate a private/public key pair for the certificate.

Use OpenSSL to generate a 4096-bit RSA key file, as explained [here](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/../cryptography/rsa-key-pair-generator.md):
```
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out our_key.key
```
