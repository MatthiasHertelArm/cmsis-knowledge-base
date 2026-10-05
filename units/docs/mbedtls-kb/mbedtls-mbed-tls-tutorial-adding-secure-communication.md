---
id: "mbedtls-mbed-tls-tutorial-adding-secure-communication"
type: "concept"
domain: "security"
title: "Mbed TLS tutorial: Adding secure communication"
summary: "Adding SSL/TLS to an application requires a number of modifications. The main modifications are setup, configuration and teardown of the SSL contexts and structures."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/mbedtls-tutorial.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/mbedtls-tutorial.md#adding-secure-communication"
license: "Apache-2.0"
mode: "V"
---

Adding SSL/TLS to an application requires a number of modifications. The main modifications are setup, configuration and teardown of the SSL contexts and structures. Smaller changes are those made to the network functions for connecting to a server, reading and writing data.

### Setup

Mbed TLS requires a good random number generator and its own SSL context and SSL session store. For random number generation, Mbed TLS contains the CTR_DRBG random number generator, which is used here as well.

The headers required for Mbed TLS:

    #include "mbedtls/net_sockets.h"
    #include "mbedtls/ssl.h"
    #include "mbedtls/entropy.h"
    #include "mbedtls/ctr_drbg.h"
    #include "mbedtls/debug.h"

The creation and initialization of the Mbed TLS structures looks as follows:

    mbedtls_net_context server_fd;
    mbedtls_entropy_context entropy;
    mbedtls_ctr_drbg_context ctr_drbg;
    mbedtls_ssl_context ssl;
    mbedtls_ssl_config conf;

    mbedtls_net_init( &server_fd );
    mbedtls_ssl_init( &ssl );
    mbedtls_ssl_config_init( &conf );
    mbedtls_x509_crt_init( &cacert );
    mbedtls_ctr_drbg_init( &ctr_drbg );

    mbedtls_entropy_init( &entropy );
    if( ( ret = mbedtls_ctr_drbg_seed( &ctr_drbg, mbedtls_entropy_func, &entropy,
                               (const unsigned char *) pers,
                               strlen( pers ) ) ) != 0 )
    {
        printf( " failed\n  ! mbedtls_ctr_drbg_seed returned %d\n", ret );
        goto exit;
    }

### SSL Connection

In a generic TCP/IP client application, the application handles the `socket()` and `connect()` calls. Mbed TLS generally abstracts this inside its network layer (`net_sockets.c`). Thus, the following code gets simplified.

    if( ( server_host = gethostbyname( SERVER_NAME ) ) == NULL )
        goto exit;

    if( ( server_fd = socket( AF_INET, SOCK_STREAM, IPPROTO_IP) ) < 0 )
        goto exit;

    memcpy( (void *) &server_addr.sin_addr, (void *) server_host->h_addr,
                     server_host->h_length );

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons( SERVER_PORT );

    if( ( ret = connect( server_fd, (struct sockaddr *) &server_addr,
                         sizeof( server_addr ) ) ) < 0 )
        goto exit;

Starting the actual connection through Mbed TLS is as follows:

    if( ( ret = mbedtls_net_connect( &server_fd, SERVER_NAME,
                                         SERVER_PORT, MBEDTLS_NET_PROTO_TCP ) ) != 0 )
    {
        printf( " failed\n  ! mbedtls_net_connect returned %d\n\n", ret );
        goto exit;
    }

### Configuring SSL/TLS

Now that the low level socket connection is up and running, you need to configure the SSL/TLS layer.

1. Prepare the SSL configuration by setting the endpoint and transport type, and loading reasonable defaults for the security parameters. The endpoint determines if the SSL/TLS layer acts as a server (`MBEDTLS_SSL_IS_SERVER`) or a client (`MBEDTLS_SSL_IS_CLIENT`). The transport type determines if you are using TLS (`MBEDTLS_SSL_TRANSPORT_STREAM`) or DTLS (`MBEDTLS_SSL_TRANSPORT_DATAGRAM`).

    ```
    if( ( ret = mbedtls_ssl_config_defaults( &conf,
                    MBEDTLS_SSL_IS_CLIENT,
                    MBEDTLS_SSL_TRANSPORT_STREAM,
                    MBEDTLS_SSL_PRESET_DEFAULT ) ) != 0 )
    {
        mbedtls_printf( " failed\n  ! mbedtls_ssl_config_defaults returned %d\n\n", ret );
        goto exit;
    }
    ```

2. Set the authentication mode. It determines how strictly the certificates are checked. For this tutorial, we are not checking anything.

    **Note:**: Do not use this in a full application.

    ```
    mbedtls_ssl_conf_authmode( &conf, MBEDTLS_SSL_VERIFY_NONE );
    ```

3. Set the random engine and debug function. The library needs to know what to use as callback.

    ```
    mbedtls_ssl_conf_rng( &conf, mbedtls_ctr_drbg_random, &ctr_drbg );
    mbedtls_ssl_conf_dbg( &conf, my_debug, stdout );
    ```

4. For the debug function to work, add a debug callback called `my_debug` above our `main()` function.

    ```
    static void my_debug( void *ctx, int level,
                          const char *file, int line, const char *str )
    {
        ((void) level);
        fprintf( (FILE *) ctx, "%s:%04d: %s", file, line, str );
        fflush(  (FILE *) ctx  );
    }
    ```

5. Now that the configuration is ready, set up the SSL context to use it.

    ```
    if( ( ret = mbedtls_ssl_set_hostname( &ssl, "Mbed TLS Server 1" ) ) != 0 )
    {
        mbedtls_printf( " failed\n  ! mbedtls_ssl_set_hostname returned %d\n\n", ret );
        goto exit;
    }
    ```

6. Finally, the SSL context needs to know the input and output functions it needs to use for sending out network traffic.

    ```
    mbedtls_ssl_set_bio( &ssl, &server_fd, mbedtls_net_send, mbedtls_net_recv, NULL );
    ```

### Reading and writing data

After configuring the SSL/TLS layer, you need to actually write and read through it.

For writing to the network layer:

    while( ( ret = write( server_fd, buf, len ) ) <= 0 )

becomes

    while( ( ret = mbedtls_ssl_write( &ssl, buf, len ) ) <= 0 )

For reading from the network layer:

    ret = read( server_fd, buf, len );

becomes

     ret = mbedtls_ssl_read( &ssl, buf, len );

**Note:**: If `mbedtls_ssl_read()` or `mbedtls_ssl_write()` returns an error, the connection must be closed.

### Teardown

When closing the application you need to close the SSL/TLS connection cleanly and also destroy any SSL/TLS related information. Finally, free the resources allocated.

    close( server_fd );

becomes:

    mbedtls_net_free( &server_fd );
    mbedtls_ssl_free( &ssl );
    mbedtls_ssl_config_free( &conf );
    mbedtls_ctr_drbg_free( &ctr_drbg );
    mbedtls_entropy_free( &entropy );

### Server authentication

A real application needs to properly authenticate the server. For this you need a set of trusted CAs. How to get or choose this set depends on your use case: to connect to a web server, you can use a list provided by a trusted browser vendor; if your client is a device connecting only to a set of servers you control, you may want to be your own CA.

Code-wise, here is what you need to do in order to enable the verification of the server certificate:

    mbedtls_x509_crt cacert;
    const char *cafile = "/path/to/trusted-ca-list.pem";

    mbedtls_x509_crt_init( &cacert );

    if( ( ret = mbedtls_x509_crt_parse_file( &cacert, cafile ) ) != 0 )
    {
        mbedtls_printf( " failed\n  !  mbedtls_x509_crt_parse returned -0x%x\n\n", -ret );
        goto exit;
    }

    mbedtls_ssl_conf_ca_chain( &conf, &cacert, NULL );

    // remove the following line
    // mbedtls_ssl_conf_authmode( &conf, MBEDTLS_SSL_VERIFY_NONE );
