---
id: "mbedtls-nonblocking-ecc-restartable-ecdsa-flow"
type: "concept"
domain: "security"
title: "Nonblocking ECC: Restartable ECDSA flow"
summary: "Nonblocking ECC: Restartable ECDSA flow"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/restartable-ecc.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/restartable-ecc.md#restartable-ecdsa-flow"
license: "Apache-2.0"
mode: "V"
---

* Define `mbedtls_ecdsa_restart_ctx`, and call `mbedtls_ecdsa_restart_init()` with the defined context.
* Set maximal number of operations with `mbedtls_ecp_set_max_ops()`.
* Call `mbedtls_ecdsa_xxx_restartable()`, as long as the return code is `MBEDTLS_ERR_ECP_IN_PROGRESS`.
* Free the restartable context with `mbedtls_ecdsa_restart_free()`.

For example:

```
    mbedtls_ecdsa_context ctx;
    mbedtls_ecdsa_restart_ctx rs_ctx;
    mbedtls_ecdsa_init( &ctx );
    mbedtls_ecdsa_restart_init( &rs_ctx );
    mbedtls_ecp_set_max_ops( max_ops );

    do {
        ret = mbedtls_ecdsa_read_signature_restartable( &ctx,
                      hash, hash_len, sig, sig_len, &rs_ctx );
        /* Here you can attend to other tasks */
    } while( ret == MBEDTLS_ERR_ECP_IN_PROGRESS );
    if( ret != 0 )
    {
        /* Handle your error here*/
    }
    mbedtls_ecdsa_restart_free( &rs_ctx );
    mbedtls_ecdsa_free( &ctx );
```
