---
id: "mbedtls-how-to-encrypt-and-decrypt-with-rs-rsa-2048-bit-decryption-in-c-with-mbed-t"
type: "concept"
domain: "security"
title: "How to encrypt and decrypt with RSA: RSA 2048-bit decryption in C with Mbed TLS"
summary: "Decryption is very similar in set-up. The main difference is that you need the private key instead of the public key to perform the decryption."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/encrypt-and-decrypt-with-rsa.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/encrypt-and-decrypt-with-rsa.md#rsa-2048-bit-decryption-in-c-with-mbed-tls"
license: "Apache-2.0"
mode: "V"
---

Decryption is very similar in set-up. The main difference is that you need the **private key** instead of the **public key** to perform the decryption.

Start by initializing the PK context and reading in the 2048-bit private key:
```
    int ret = 0;
    mbedtls_pk_context pk;

    mbedtls_pk_init( &pk );

    /*
     * Read the RSA privatekey
     */
    if( ( ret = mbedtls_pk_parse_keyfile( &pk, "our-key.pem", "" ) ) != 0 )
    {
        printf( " failed\n  ! mbedtls_pk_parse_keyfile returned -0x%04x\n", -ret );
        goto exit;
    }
```
Store data to be decrypted and its length in variables. This tutorial stores the data in `to_decrypt`, and its length in `to_decrypt_len`:
```
    unsigned char result[MBEDTLS_MPI_MAX_SIZE];
    size_t olen = 0;

    /*
     * Calculate the RSA encryption of the data.
     */
    printf( "\n  . Generating the encrypted value" );
    fflush( stdout );

    if( ( ret = mbedtls_pk_decrypt( &pk, to_decrypt, to_decrypt_len, result, &olen, sizeof(result),
                                    mbedtls_ctr_drbg_random, &ctr_drbg ) ) != 0 )
    {
        printf( " failed\n  ! mbedtls_pk_decrypt returned -0x%04x\n", -ret );
        goto exit;
    }
```
So after the call to `mbedtls_pk_decrypt()`, the result is in `result` with the actual size of the decrypted data in `olen`.

<!---",encrypt-and-decrypt-with-rsa,"Article on encrypting and decrypting data with RSA",,"rsa, encrypt, decrypt",published,"2014-05-20 09:21:00",2,26498,"2015-07-24 09:47:00","Paul Bakker"--->
