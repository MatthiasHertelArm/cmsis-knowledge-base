---
id: "mbedtls-how-to-put-tls-keys-into-an-extern-cryptographic-data-formats"
type: "concept"
domain: "security"
title: "How to put TLS keys into an external cryptoprocessor: Cryptographic data formats"
summary: "The start callbacks take a cert argument, which is a pointer to the server certificate used for the TLS connection."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/ssl_async.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/ssl_async.md#cryptographic-data-formats"
license: "Apache-2.0"
mode: "V"
---

The `start` callbacks take a `cert` argument, which is a pointer to the server certificate used for the TLS connection. If the server has multiple private keys and associated certificates (for example, because it has a key of each supported type), the callback code must use `cert` to determine which private key to use for signing or decrypting. You can access the public key as `cert->pk`.

In simple cases, the pointer `cert` is one of the pointers passed to `mbedtls_ssl_conf_own_cert` when configuring the TLS connection. However, if you also use other callbacks, this may not apply. For example, if you register an SNI callback with `mbedtls_ssl_conf_sni()`, then this callback determines what certificate object the asynchronous callbacks receive.

Please refer to the documentation on [signature](https://github.com/api/ssl_8h.html#ad57308aa77db11dbc3551fd92deb2520) and [decryption](https://github.com/api/ssl_8h.html#ac18191035f2598e3311d24a3ae40a0fa) callbacks for information about the input and output formats for cryptographic operations.
