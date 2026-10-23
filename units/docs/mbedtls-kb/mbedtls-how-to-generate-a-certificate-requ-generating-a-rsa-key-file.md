---
id: "mbedtls-how-to-generate-a-certificate-requ-generating-a-rsa-key-file"
type: "concept"
domain: "security"
title: "How to generate a Certificate Request (CSR): Generating a RSA key file"
summary: "The first step for generating a certificate request, is to generate a private-public key pair for the certificate."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/generate-a-certificate-request-csr.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/generate-a-certificate-request-csr.md#generating-a-rsa-key-file"
license: "Apache-2.0"
mode: "V"
---

The first step for generating a certificate request, is to generate a private-public key pair for the certificate.

Use OpenSSL to generate a 2048-bit RSA key file, as explained [here](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../cryptography/rsa-key-pair-generator.md):
```
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out example.com.key
```
