---
id: "mbedtls-how-to-encrypt-and-decrypt-with-rs-rsa-2048-bit-encryption-in-c-with-mbed-t"
type: "concept"
domain: "security"
title: "How to encrypt and decrypt with RSA: RSA 2048-bit encryption in C with Mbed TLS"
summary: "Start by initializing the public key context and reading in the public key:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/encrypt-and-decrypt-with-rsa.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/encrypt-and-decrypt-with-rsa.md#rsa-2048-bit-encryption-in-c-with-mbed-tls"
license: "Apache-2.0"
mode: "V"
---

Start by initializing the public key context and reading in the public key:
```
    int ret = 0;
    mbedtls_pk_context pk;

    mbedtls_pk_init( &pk );

    /*
     * Read the RSA public key
     */
    if( ( ret = mbedtls_pk_parse_public_keyfile( &pk, "our-key.pub" ) ) != 0 )
    {
        printf( " failed\n  ! mbedtls_pk_parse_public_keyfile returned -0x%04x\n", -ret );
        goto exit;
    }
```
**Note:** There is a [maximum amount of data you can encrypt with RSA](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/../cryptography/rsa-encryption-maximum-data-size.md). For a 2048 bit RSA key, the maximum you can encrypt is 245 bytes (or 1960 bits).

Store the data to be encrypted and its length in variables. This tutorial uses `to_encrypt` for the data, and its length in `to_encrypt_len`:
```
    unsigned char buf[MBEDTLS_MPI_MAX_SIZE];
    size_t olen = 0;

    /*
     * Calculate the RSA encryption of the data.
     */
    printf( "\n  . Generating the encrypted value" );
    fflush( stdout );

    if( ( ret = mbedtls_pk_encrypt( &pk, to_encrypt, to_encrypt_len,
                                    buf, &olen, sizeof(buf),
                                    mbedtls_ctr_drbg_random, &ctr_drbg ) ) != 0 )
    {
        printf( " failed\n  ! mbedtls_pk_encrypt returned -0x%04x\n", -ret );
        goto exit;
    }
```
The result is in `buf`, with the actual size you should copy out in `olen`.
