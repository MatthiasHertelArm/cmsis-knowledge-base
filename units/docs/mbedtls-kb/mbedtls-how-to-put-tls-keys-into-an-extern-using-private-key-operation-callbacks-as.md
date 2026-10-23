---
id: "mbedtls-how-to-put-tls-keys-into-an-extern-using-private-key-operation-callbacks-as"
type: "concept"
domain: "security"
title: "How to put TLS keys into an external cryptoprocessor: Using private key operation callbacks asynchonously"
summary: "Private key operation callbacks are split in two steps: start and resume. This allows the server to remain non-blocking even if calls to the external cryptoprocessor are blocking."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/ssl_async.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/ssl_async.md#using-private-key-operation-callbacks-asynchonously"
license: "Apache-2.0"
mode: "V"
---

Private key operation callbacks are split in two steps: `start` and `resume`. This allows the server to remain non-blocking even if calls to the external cryptoprocessor are blocking. You can use the start callback to send a request to the external cryptoprocessor and use the resume callback to retrieve the external cryptoprocessor's response. This way, the private key operation is executed asynchronously, without blocking the calling thread on the server.

When the TLS stack calls a callback, the thread executing the callback is blocked until the callback returns. To unblock the thread if the requested operation is not finished, a callback can return the special error code `MBEDTLS_ERR_SSL_ASYNC_IN_PROGRESS`. This code indicates that the operation is still in progress. The TLS stack reports this error code to the application, so high-level functions such as `mbedtls_ssl_step()` return `MBEDTLS_ERR_SSL_ASYNC_IN_PROGRESS`. On the next function call on this SSL connection, the TLS stack calls the resume callback.

In your application, if an `mbedtls_ssl_xxx` function returns `MBEDTLS_ERR_SSL_ASYNC_IN_PROGRESS`, call the same function with the same arguments when the external cryptoprocessor's response is ready. You can call it at any time, and the TLS stack calls the resume callback. The resume callback might itself return `MBEDTLS_ERR_SSL_ASYNC_IN_PROGRESS` if the result of the operation is still not ready.

In a TLS connection, the private key is used during the handshake phase. After the initial handshake at the beginning of the connection, the private key is usually not used anymore, therefore later functions such as `mbedtls_ssl_read()` and `mbedtls_ssl_write()` do not return `MBEDTLS_ERR_SSL_ASYNC_IN_PROGRESS`. However, if renegotiation is enabled, most functions can trigger a new handshake, which results in a callback returning `MBEDTLS_ERR_SSL_ASYNC_IN_PROGRESS`.

The following code sample illustrates how to define callbacks that use an external cryptoprocessor asynchronously:

```
int f_async_sign_start( mbedtls_ssl_context *ssl,
                        mbedtls_x509_crt *cert,
                        mbedtls_md_type_t md_alg,
                        const unsigned char *hash,
                        size_t hash_len )
{
    /* Create an HSM request */
    request_handle_t *request = new_signing_request( cert, md_alg, hash, hash_len );
    if( request == NULL )
        return( MBEDTLS_ERR_PK_ALLOC_FAILED );
    /* Enqueue the request. Do not wait for it to complete. */
    enqueue_request_for_hsm( request );
    /* Remember the request and return without blocking. */
    request->origin = ssl;
    mbedtls_ssl_set_async_operation_data( ssl, request_handle );
    return( MBEDTLS_ERR_SSL_ASYNC_IN_PROGRESS );
}

int f_async_resume( mbedtls_ssl_context *ssl,
                    unsigned char *output,
                    size_t *output_len,
                    size_t output_size )
{
    request_handle_t *request = mbedtls_ssl_get_async_operation_data( ssl );
    if( response_is_available( request ) )
    {
        return( read_response( request, output, output_len, output_size ) );
    }
    else
    {
        /* No response available. Try again later. */
        return( MBEDTLS_ERR_SSL_ASYNC_IN_PROGRESS );
    }
}

void f_async_cancel( mbedtls_ssl_context *ssl )
{
    request_handle_t *request = mbedtls_ssl_get_async_operation_data( ssl );
    cancel_request( request );
}

/* Example simplified structure of application code using poll(2) */
{
    struct pollfd poll_fds[NUM_POLL_FDS];
    /* Omitted: set up poll_fds */
    poll( poll_fds, NUM_POLL_FDS, 0 );
    for( i = 0; i < NUM_POLL_FDS; i++ )
    {
        int fd = poll_fds[i].fd;
        if( fd == hsm_fd )
        {
            /* Read a response from the HSM and resume the associated
               SSL connection. */
            hsm_response = read_hsm_response();
            mbedtls_ssl_handshake_step( hsm_response->request->origin );
        }
    }
}
```
