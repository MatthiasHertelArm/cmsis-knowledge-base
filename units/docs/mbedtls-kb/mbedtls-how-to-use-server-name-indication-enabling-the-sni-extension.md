---
id: "mbedtls-how-to-use-server-name-indication-enabling-the-sni-extension"
type: "concept"
domain: "security"
title: "How to use Server Name Indication: Enabling the SNI extension"
summary: "SNI is enabled in the default configuration."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/use-sni.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/use-sni.md#enabling-the-sni-extension"
license: "Apache-2.0"
mode: "V"
---

SNI is enabled in the default configuration.

**SNI requires X509 certificates**, so the first step is to enable X509 in your Mbed TLS [configuration file](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/../compiling-and-building/how-do-i-configure-mbedtls.md):
```
    ./scripts/config.py set MBEDTLS_X509_CRT_PARSE_C
    ./scripts/config.py set MBEDTLS_SSL_SERVER_NAME_INDICATION
```
These are usual Mbed TLS compile time options, so you need to set them before compiling the library. For more information on configuring Mbed TLS please visit this [knowledge base article](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/../compiling-and-building/how-do-i-configure-mbedtls.md).
