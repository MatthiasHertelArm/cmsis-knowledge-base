---
id: "mbedtls-nonblocking-ecc-restartable-ssl-flow"
type: "concept"
domain: "security"
title: "Nonblocking ECC: Restartable SSL flow"
summary: "The restartable feature is done automatically, as long as:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/restartable-ecc.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/restartable-ecc.md#restartable-ssl-flow"
license: "Apache-2.0"
mode: "V"
---

* Set maximal number of operations with `mbedtls_ecp_set_max_ops()`.
* Call the SSL handshake operation, as long as it returns `MBEDTLS_ERR_SSL_CRYPTO_IN_PROGRESS` (in addition to `MBEDTLS_ERR_SSL_WANT_READ` and `MBEDTLS_ERR_SSL_WANT_WRITE`).

For example:

```
    mbedtls_ecp_set_max_ops( max_ops );

    do {
        ret = mbedtls_ssl_handshake( &ssl );
        /* Here you can attend to other tasks */
    } while( ret == MBEDTLS_ERR_SSL_WANT_READ ||
             ret == MBEDTLS_ERR_SSL_WANT_WRITE ||
             ret == MBEDTLS_ERR_SSL_CRYPTO_IN_PROGRESS );
    if( ret != 0 )
    {
        /* Handle your error here*/
    }
```

The restartable feature is done automatically, as long as:

1. You define `MBEDTLS_ECP_RESTARTABLE` in `mbedtls/mbedtls_config.h`.
1. The TLS protocol is TLS 1.2 and higher.
1. The negotiated key exchange is `MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA`.
1. You call `mbedtls_ecp_set_max_ops()`.
1. **The restartable SSL feature is supported for TLS client only**.
