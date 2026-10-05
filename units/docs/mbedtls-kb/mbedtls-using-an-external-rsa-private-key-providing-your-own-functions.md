---
id: "mbedtls-using-an-external-rsa-private-key-providing-your-own-functions"
type: "concept"
domain: "security"
title: "Using an external RSA private key: Providing your own functions"
summary: "Mbed TLS is designed for this, and allows you to set your own functions to be used for RSA decryption and signing during the SSL handshake."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/use-external-rsa-private-key.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/use-external-rsa-private-key.md#providing-your-own-functions"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS is designed for this, and allows you to set your own functions to be used for RSA decryption and signing during the SSL handshake.

Set these functions by using `mbedtls_pk_setup_rsa_alt()`. This allows your application to provide an arbitrary blob as your RSA private key, accept function pointers performing decryption and signature, and return the key size, as above.

You can then use the normal `mbedtls_set_own_cert()` function. From the perspective of the SSL module, the external RSA private key is just another PK context.
