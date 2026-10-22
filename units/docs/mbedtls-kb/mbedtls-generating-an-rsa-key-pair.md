---
id: "mbedtls-generating-an-rsa-key-pair"
type: "concept"
domain: "security"
title: "Generating an RSA key pair"
summary: "To use RSA with Mbed TLS or any other application, you will most likely need an RSA key pair. An RSA key pair is often stored in either a PEM file or a DER file."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/cryptography/rsa-key-pair-generator.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/cryptography/rsa-key-pair-generator.md"
license: "Apache-2.0"
mode: "V"
---

To use RSA with Mbed TLS or any other application, you will most likely need an RSA key pair. An RSA key pair is often stored in [either a PEM file or a DER file](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/cryptography/asn1-key-structures-in-der-and-pem.md).

Mbed TLS 4 does not provide a command-line program for generating RSA key pairs. Use a dedicated tool such as OpenSSL to create a key file for use with Mbed TLS:

```
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out private.key
```

The rest of this article documents the `gen_key` program that was available in Mbed TLS versions before 4.0.
