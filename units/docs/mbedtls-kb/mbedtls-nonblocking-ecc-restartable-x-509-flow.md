---
id: "mbedtls-nonblocking-ecc-restartable-x-509-flow"
type: "concept"
domain: "security"
title: "Nonblocking ECC: Restartable X.509 flow"
summary: "Nonblocking ECC: Restartable X.509 flow"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/restartable-ecc.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/restartable-ecc.md#restartable-x-509-flow"
license: "Apache-2.0"
mode: "V"
---

*  Define `mbedtls_x509_crt_restart_ctx` and call `mbedtls_x509_crt_restart_init()` with the defined context.
*  Set maximal number of operations with `mbedtls_ecp_set_max_ops()`.
*  Call `mbedtls_x509_crt_xxx_restartable()`, as long as the return code is `MBEDTLS_ERR_ECP_IN_PROGRESS`.
*  Free the restartable context with `mbedtls_x509_crt_restart_free()`.

For example:

```
    mbedtls_x509_crt_restart_ctx ctx;

    mbedtls_x509_crt_restart_init( &ctx );
    mbedtls_ecp_set_max_ops( max_ops );

    do {
        ret = mbedtls_x509_crt_verify_restartable(  &crt, &ca, NULL,
                &mbedtls_x509_crt_profile_default, NULL, &flags,
                NULL, NULL, &rs_ctx );
        /* Here you can attend to other tasks */
    } while( ret == MBEDTLS_ERR_ECP_IN_PROGRESS );
    if( ret != 0 )
    {
        /* Handle your error here*/
    }
    mbedtls_x509_crt_restart_free( &ctx );
```
