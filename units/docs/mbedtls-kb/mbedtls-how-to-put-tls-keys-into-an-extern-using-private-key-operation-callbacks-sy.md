---
id: "mbedtls-how-to-put-tls-keys-into-an-extern-using-private-key-operation-callbacks-sy"
type: "concept"
domain: "security"
title: "How to put TLS keys into an external cryptoprocessor: Using private key operation callbacks synchronously"
summary: "In f_async_sign_start or f_async_decrypt_start, make the required calculation, store the result somewhere, and return 0. The TLS stack first calls the appropriate start function, then calls the resume callback. In the resume callback, copy the result to the output buffer."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/ssl_async.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/ssl_async.md#using-private-key-operation-callbacks-synchronously"
license: "Apache-2.0"
mode: "V"
---

In `f_async_sign_start` or `f_async_decrypt_start`, make the required calculation, store the result somewhere, and return `0`. The TLS stack first calls the appropriate `start` function, then calls the resume callback. In the resume callback, copy the result to the output buffer.

You can call [`mbedtls_ssl_set_async_operation_data`](https://github.com/api/ssl_8h.html#ac57fb2abf2a5cd821d0ec8c3d6c59daf) and [`mbedtls_ssl_get_async_operation_data`](https://github.com/api/ssl_8h.html#a7e424db2d8ccc9f0d5fe4ed0a9a5bab2) to store a pointer in the TLS context, in order to remember it between the start and resume calls.

You can define callbacks that use an external cryptoprocessor synchronously:

```
struct buffer {
    size_t size;
    unsigned char data[];
};

int f_async_sign_start( mbedtls_ssl_context *ssl,
                        mbedtls_x509_crt *cert,
                        mbedtls_md_type_t md_alg,
                        const unsigned char *hash,
                        size_t hash_len )
{
    struct buffer *buf = mbedtls_calloc( 1, sizeof(struct buffer) + MAX_SIGNATURE_SIZE );
    if( buf == NULL )
        return( MBEDTLS_ERR_PK_ALLOC_FAILED );
    /* Omitted: calculate the signature and write it to buf->data and
       its size to buf->size. */
    mbedtls_ssl_set_async_operation_data( ssl, buf );
    return( 0 );
}

int f_async_resume( mbedtls_ssl_context *ssl,
                    unsigned char *output,
                    size_t *output_len,
                    size_t output_size )
{
    struct buffer *buf = mbedtls_ssl_get_async_operation_data( ssl );
    if( buf->size > output_size )
        return( MBEDTLS_ERR_PK_BUFFER_TOO_SMALL );
    memcpy( output, &buf->data, buf->size );
    mbedtls_free( buf );
    return( 0 );
}

void f_async_cancel( mbedtls_ssl_context *ssl )
{
    struct buffer *buf = mbedtls_ssl_get_async_operation_data( ssl );
    mbedtls_free( buf );
}
```
