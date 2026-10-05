---
id: "mbedtls-nonblocking-ecc-restartable-ecdh-flow"
type: "concept"
domain: "security"
title: "Nonblocking ECC: Restartable ECDH flow"
summary: "Nonblocking ECC: Restartable ECDH flow"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/restartable-ecc.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/restartable-ecc.md#restartable-ecdh-flow"
license: "Apache-2.0"
mode: "V"
---

* Set maximal number of operations with `mbedtls_ecp_set_max_ops()`.
* Enable support for restarting with `mbedtls_ecdh_enable_restart()`.
* Call the ecdh operation as long as the return code is `MBEDTLS_ERR_ECP_IN_PROGRESS`.

For example:
    
```
    mbedtls_ecdh_context srv;
    mbedtls_ecdh_init( &srv );
    mbedtls_ecdh_enable_restart( &srv );
    mbedtls_ecp_set_max_ops( max_ops );

    do {
        ret = mbedtls_ecdh_make_params( &srv, &len, buf, sizeof( buf ),
                                        rnd_buffer_rand, &rnd_info_A );
        /* Here you can attend to other tasks */
    } while( ret == MBEDTLS_ERR_ECP_IN_PROGRESS );
    if( ret != 0 )
    {
        /* Handle your error here*/
    }
    mbedtls_ecdh_free( &srv );
```
