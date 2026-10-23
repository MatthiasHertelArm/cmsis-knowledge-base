---
id: "mbedtls-generating-an-aes-key-creating-the-aes-key"
type: "concept"
domain: "security"
title: "Generating an AES key: Creating the AES key"
summary: "You need to initialize the entropy pool and the random source and extract data for your key. In this case we generate 32 bytes (256 bits) of random data."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/generate-an-aes-key.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/generate-an-aes-key.md#creating-the-aes-key"
license: "Apache-2.0"
mode: "V"
---

You need to initialize the entropy pool and the random source and extract data for your key. In this case we generate 32 bytes (256 bits) of random data.

    mbedtls_entropy_init( &entropy );

    mbedtls_ctr_drbg_init( &ctr_drbg );

    if( ( ret = mbedtls_ctr_drbg_seed( &ctr_drbg, mbedtls_entropy_func, &entropy,
        (unsigned char *) pers, strlen( pers ) ) ) != 0 )
    {
        printf( " failed\n ! mbedtls_ctr_drbg_init returned -0x%04x\n", -ret );
        goto exit;
    }

    if( ( ret = mbedtls_ctr_drbg_random( &ctr_drbg, key, 32 ) ) != 0 )
    {
        printf( " failed\n ! mbedtls_ctr_drbg_random returned -0x%04x\n", -ret );
        goto exit;
    }

Now you can use the data in `key` as a 256-bit AES key.

<!-- This guide from Mbed TLS explains how to generate an AES key.","AES key generation, generate AES key, AES key","aes, aes key, key generation, snippet, entropy, randomness, random -->
