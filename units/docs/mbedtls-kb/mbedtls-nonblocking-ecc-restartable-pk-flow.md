---
id: "mbedtls-nonblocking-ecc-restartable-pk-flow"
type: "concept"
domain: "security"
title: "Nonblocking ECC: Restartable PK flow"
summary: "Nonblocking ECC: Restartable PK flow"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/restartable-ecc.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/restartable-ecc.md#restartable-pk-flow"
license: "Apache-2.0"
mode: "V"
---

* Define `mbedtls_pk_restart_ctx` and call `mbedtls_pk_restart_init()` with the defined context.
* Set maximal number of operations with `mbedtls_ecp_set_max_ops()`.
* Call `mbedtls_pk_xxx_restartable()`, as long as the return code is `MBEDTLS_ERR_ECP_IN_PROGRESS`.
* Free the restartable context with `mbedtls_pk_restart_free()`.

**Note**: Call these functions for ECDSA only. If `PK` is `RSA`, then set `mbedtls_pk_restart_ctx` to NULL.

For example:

```
    mbedtls_pk_restart_ctx ctx;

    mbedtls_pk_restart_init( &ctx );
    mbedtls_ecp_set_max_ops( max_ops );

    do {
        ret = mbedtls_pk_verify_restartable(  &pk, digest, hash_result, 0,
                    result_str, mbedtls_pk_get_len( &pk ), &ctx  );
        /* Here you can attend to other tasks */
    } while( ret == MBEDTLS_ERR_ECP_IN_PROGRESS );
    if( ret != 0 )
    {
        /* Handle your error here*/
    }
    mbedtls_pk_restart_free( &ctx );
```
