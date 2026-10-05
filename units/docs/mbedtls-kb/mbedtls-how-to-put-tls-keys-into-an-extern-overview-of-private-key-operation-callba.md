---
id: "mbedtls-how-to-put-tls-keys-into-an-extern-overview-of-private-key-operation-callba"
type: "concept"
domain: "security"
title: "How to put TLS keys into an external cryptoprocessor: Overview of private key operation callbacks in TLS"
summary: "Private key operation callbacks allow you to offload operations on a server's private key to an external cryptoprocessor."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/ssl_async.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/ssl_async.md#overview-of-private-key-operation-callbacks-in-tls"
license: "Apache-2.0"
mode: "V"
---

Private key operation callbacks allow you to offload operations on a server's private key to an external cryptoprocessor. When a callback is registered, the cryptographic operations involving the private key are performed by the callback instead of Mbed TLS's own cryptographic code. It is up to the callback to make calls to the external cryptoprocessor.

The interface has four callback functions:

* [`f_async_sign_start`](https://github.com/api/ssl_8h.html#ad57308aa77db11dbc3551fd92deb2520) receives the data to sign and must initiate the signature operation.
* [`f_async_decrypt_start`](https://github.com/api/ssl_8h.html#ac18191035f2598e3311d24a3ae40a0fa) receives the data to decrypt and must initiate the decryption operation.
* [`f_async_resume`](https://github.com/api/ssl_8h.html#a6a67de0c00f4aff4500ece33645a96cd) is called after `f_async_sign_start` or `f_async_decrypt_start`, and must return the signature or the decrypted data.
* [`f_async_cancel`](https://github.com/api/ssl_8h.html#a084ed94ac531cfde7dcd0d0c05d392bd) is called if the TLS connection is closed after a call to `f_async_sign_start` or `f_async_decrypt_start`, and before `f_async_resume` has returned the result.

The interface defines separate `start` and `resume` functions, to allow **asynchronous** calls to the external cryptoprocessor. For example, the `start` functions may send the request to the external cryptoprocessor and return without waiting for a response, and the `resume` function would read the response when it is available. In the sections below, we show how to [use the callbacks in the synchronous case](#using-private-key-operation-callbacks-synchronously), then how to [run a non-blocking server with asynchronous callbacks](#using-private-key-operation-callbacks-asynchonously).

To declare the callbacks, call the function [`mbedtls_ssl_conf_async_private_cb`](https://github.com/api/ssl_8h.html#a0675aed5a2b2b9ff219a62ed28b50819):
```
mbedtls_ssl_conf_async_private_cb( ssl->config,
                                   f_async_sign_start,
                                   f_async_decrypt_start,
                                   f_async_resume,
                                   f_async_cancel,
                                   config_data );
```

If you don't use any decryption-based cipher suite, or if the decryption keys are on the server, you can set `f_async_decrypt_start` to `NULL`. In this case, the TLS stack doesn't try to use an external cryptoprocessor for decryption. Likewise, you can set `f_async_sign_start` to `NULL`, and the TLS stack doesn't call the external cryptoprocessor to sign anything. You can also pass `NULL` for `f_async_cancel` if you don't have any data to clean up when a TLS connection is closed during the cryptographic operation.

If you need to return an error from the callbacks, you should use an [`MBEDTLS_PK_xxx`](https://github.com/api/pk_8h.html#define-members) error code. This is because the callbacks simulate calls to the `pk` module. Do not use `MBEDTLS_SSL_xxx` error codes except as directed in the callback documentation.
