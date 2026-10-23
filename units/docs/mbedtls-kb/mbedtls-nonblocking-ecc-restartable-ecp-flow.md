---
id: "mbedtls-nonblocking-ecc-restartable-ecp-flow"
type: "concept"
domain: "security"
title: "Nonblocking ECC: Restartable ECP flow"
summary: "Nonblocking ECC: Restartable ECP flow"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/restartable-ecc.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/restartable-ecc.md#restartable-ecp-flow"
license: "Apache-2.0"
mode: "V"
---

* Define `mbedtls_ecp_restart_ctx` and call `mbedtls_ecp_restart_init()` with the defined context.
* Set maximal number of operations with `mbedtls_ecp_set_max_ops()`.
* Call `mbedtls_ecp_xxx_restartable()`, as long as the return code is `MBEDTLS_ERR_ECP_IN_PROGRESS`.

For example:

```
    mbedtls_ecp_restart_ctx ctx;
    mbedtls_ecp_restart_init( &ctx );
    mbedtls_ecp_set_max_ops( max_ops );

    do {
        ret = mbedtls_ecp_mul_restartable( &grp, &R, &dA, &grp.G, NULL, NULL, &ctx );
        /* Here you can attend to other tasks */
    } while( ret == MBEDTLS_ERR_ECP_IN_PROGRESS );
    if( ret != 0 )
    {
        /* Handle your error here*/
    }
    mbedtls_ecp_restart_free( &ctx );
```
