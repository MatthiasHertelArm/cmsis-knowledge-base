---
id: "mbedtls-using-an-external-rsa-private-key-pkcs-11"
type: "concept"
domain: "security"
title: "Using an external RSA private key: PKCS#11"
summary: "If you are using a smartcard, you don't have to write your own logic. You can use the libpkcs11-helper library."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/use-external-rsa-private-key.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/use-external-rsa-private-key.md#pkcs-11"
license: "Apache-2.0"
mode: "V"
---

If you are using a smartcard, you don't have to write your own logic. You can use the `libpkcs11-helper` library.

Mbed TLS includes a helper class for using the `libpkcs11-helper` when you enable `MBEDTLS_PKCS11_C` in `config.h`. See [How do I configure Mbed TLS](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/../compiling-and-building/how-do-i-configure-mbedtls.md).
