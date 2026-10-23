---
id: "mbedtls-psa-generating-a-random-value"
type: "concept"
domain: "security"
title: "psa: Using PSA / Generating a random value"
summary: "The PSA Crypto API can generate random data."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:getting_started/psa.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/getting_started/psa.md#generating-a-random-value"
license: "Apache-2.0"
mode: "V"
---

_Part of: Using PSA_

The PSA Crypto API can generate random data.

**Prerequisites to generating random data:**
* Initialize the library with a successful call to `psa_crypto_init()`.

**Note:** To generate a random key, use `psa_generate_key()`
instead of `psa_generate_random()`.

This example shows how to generate ten bytes of random data by calling
`psa_generate_random()`:
```C
    psa_status_t status;
    uint8_t random[10] = { 0 };

    printf("Generate random...\t");
    fflush(stdout);

    /* Initialize PSA Crypto */
    status = psa_crypto_init();
    if (status != PSA_SUCCESS) {
        printf("Failed to initialize PSA Crypto\n");
        return;
    }

    status = psa_generate_random(random, sizeof(random));
    if (status != PSA_SUCCESS) {
        printf("Failed to generate a random value\n");
        return;
    }

    printf("Generated random data\n");

    /* Clean up */
    mbedtls_psa_crypto_free();
```
