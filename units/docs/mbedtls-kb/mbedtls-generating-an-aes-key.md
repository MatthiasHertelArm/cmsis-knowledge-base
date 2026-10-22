---
id: "mbedtls-generating-an-aes-key"
type: "concept"
domain: "security"
title: "Generating an AES key"
summary: "An AES key is a random bitstring of the right length."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/generate-an-aes-key.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/generate-an-aes-key.md"
license: "Apache-2.0"
mode: "V"
---

An AES key is a random bitstring of the right length.

* For a 128-bit AES key you need 16 bytes.
* For a 256-bit AES key you need 32 bytes.

If you need to generate your own AES key for encrypting data, you should use a good random source. The strength of the key depends on the unpredictability of the random.

Mbed TLS includes the [CTR-DRBG module](https://github.com/ctr-drbg-source-code) and an [Entropy Collection module](https://github.com/entropy-source-code) to help you with making an AES key generator for your key.

To use the AES generator, you need to have the modules enabled in the `mbedtls/config.h` files (`MBEDTLS_CTR_DRBG_C` and `MBEDTLS_ENTROPY_C`), see [How do I configure Mbed TLS](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../compiling-and-building/how-do-i-configure-mbedtls.md).

Include the following headers in your code:

    #include "mbedtls/entropy.h"
    #include "mbedtls/ctr_drbg.h"

Then add the following variable definitions to your code:

    mbedtls_ctr_drbg_context ctr_drbg;
    mbedtls_entropy_context entropy;
    unsigned char key[32];

    char *pers = "aes generate key";
    int ret;

The personalization string needs to be unique to your application to add randomness to your random sources.
