---
id: "mbedtls-how-to-fill-an-rsa-context-from-n-filling-the-context"
type: "concept"
domain: "security"
title: "How to fill an RSA context from N, E, P and Q: Filling the context"
summary: "To fill the context you should use the following sequence of function calls. You will have to define and initialize the appropriate variables for E, P and Q."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/how-to-fill-rsa-context-from-n-e-p-and-q.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/how-to-fill-rsa-context-from-n-e-p-and-q.md#filling-the-context"
license: "Apache-2.0"
mode: "V"
---

To fill the context you should use the following sequence of function calls. You will have to define and initialize the appropriate variables for `E`, `P` and `Q`.

    ret = mbedtls_rsa_import( &ctx, NULL, &P, &Q, NULL, &E );
    if( ret != 0 )
    {
        mbedtls_printf( " failed\n  ! mbedtls_rsa_import returned %d\n\n",
                        ret );
        goto exit;
    }
    if( ( ret = mbedtls_rsa_complete( &ctx ) ) != 0 )
    {
        mbedtls_printf( " failed\n  ! mbedtls_rsa_complete returned %d\n\n",
                        ret );
        goto exit;
    }
    
The function `mbedtls_rsa_complete()` deduces all the other components in the RSA context. Of course, if all components are known in advance and imported using the `mbedtls_rsa_import()` or `mbedtls_rsa_import_raw()`, the computation time of `mbedtls_rsa_complete()` will be shorter.
