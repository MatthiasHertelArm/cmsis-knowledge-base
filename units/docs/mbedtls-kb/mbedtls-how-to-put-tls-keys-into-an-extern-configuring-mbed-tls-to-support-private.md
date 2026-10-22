---
id: "mbedtls-how-to-put-tls-keys-into-an-extern-configuring-mbed-tls-to-support-private"
type: "concept"
domain: "security"
title: "How to put TLS keys into an external cryptoprocessor: Configuring Mbed TLS to support private key operation callbacks"
summary: "This feature is only available for server-side asymmetric cryptography. In Mbed TLS version 2.11, it is not available for clients or Pre-shared Keys."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/ssl_async.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/ssl_async.md#configuring-mbed-tls-to-support-private-key-operation-callbacks"
license: "Apache-2.0"
mode: "V"
---

**Note:** Private key operation callbacks are available with Mbed TLS version 2.11 onwards.

This feature is only available for server-side asymmetric cryptography. In Mbed TLS version 2.11, it is not available for clients or Pre-shared Keys.

Support for private key operation callbacks in TLS is turned off by default. To activate it, build the library with the option `MBEDTLS_SSL_ASYNC_PRIVATE` turned on in the configuration. You can use the following command in the Mbed TLS build tree:
```
scripts/config.py set MBEDTLS_SSL_ASYNC_PRIVATE
```
Alternatively, ensure that the [configuration file](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../compiling-and-building/how-do-i-configure-mbedtls.md) contains the following line (a commented-out version of this line is in the default configuration):
```
#define MBEDTLS_SSL_ASYNC_PRIVATE
```

Note that this changes the application binary interface (ABI) of the TLS library (`libmbedtls.so` or `mbedtls.dll`) so you need to rebuild any library that depends on it. The `mbedcrypto` and `mbedx509` libraries are not affected.
