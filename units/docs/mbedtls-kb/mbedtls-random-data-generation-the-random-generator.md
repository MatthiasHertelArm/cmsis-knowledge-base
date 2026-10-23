---
id: "mbedtls-random-data-generation-the-random-generator"
type: "concept"
domain: "security"
title: "Random data generation: The random generator"
summary: "To use the CTR-DRBG module in your code, you need to include the header file:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/add-a-random-generator.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-a-random-generator.md#the-random-generator"
license: "Apache-2.0"
mode: "V"
---

To use the CTR-DRBG module in your code, you need to include the header file:

```c
#include "mbedtls/ctr_drbg.h"
```

Add:

```c
    mbedtls_ctr_drbg_context ctr_drbg;
    char *personalization = "my_app_specific_string";

    mbedtls_ctr_drbg_init( &ctr_drbg );

    ret = mbedtls_ctr_drbg_seed( &ctr_drbg , mbedtls_entropy_func, &entropy,
                     (const unsigned char *) personalization,
                     strlen( personalization ) );
    if( ret != 0 )
    {
        // ERROR HANDLING CODE FOR YOUR APP
    }
```

The **personalization** string is a small protection against a lack of startup entropy and ensures each application has at least a different starting point.
