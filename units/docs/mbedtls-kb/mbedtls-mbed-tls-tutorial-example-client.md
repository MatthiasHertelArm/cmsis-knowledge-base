---
id: "mbedtls-mbed-tls-tutorial-example-client"
type: "concept"
domain: "security"
title: "Mbed TLS tutorial: Example client"
summary: "Let's assume you have a simple network client that tries to open a connection to an HTTP server and read the default page. That application would probably look something like this:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/mbedtls-tutorial.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/mbedtls-tutorial.md#example-client"
license: "Apache-2.0"
mode: "V"
---

Let's assume you have a simple network client that tries to open a connection to an HTTP server and read the default page. That application would probably look something like this:

    #include <sys/types.h>
    #include <sys/socket.h>
    #include <netinet/in.h>
    #include <arpa/inet.h>
    #include `<string.h>`
    #include `<stdio.h>`
    #include `<netdb.h>`

    #define SERVER_PORT 80
    #define SERVER_NAME "localhost"
    #define GET_REQUEST "GET / HTTP/1.0\r\n\r\n"

    int main( void )
    {
        int ret, len, server_fd;
        unsigned char buf[1024];
        struct sockaddr_in server_addr;
        struct hostent *server_host;

        /*
         * Start the connection
         */
        printf( "\n  . Connecting to tcp/%s/%4d...", SERVER_NAME,
                                                     SERVER_PORT );
        fflush( stdout );

        if( ( server_host = gethostbyname( SERVER_NAME ) ) == NULL )
        {
            printf( " failed\n  ! gethostbyname failed\n\n");
            goto exit;
        }

        if( ( server_fd = socket( AF_INET, SOCK_STREAM, IPPROTO_IP) ) < 0 )
        {
            printf( " failed\n  ! socket returned %d\n\n", server_fd );
            goto exit;
        }

        memcpy( (void *) &server_addr.sin_addr,
                (void *) server_host->h_addr,
                         server_host->h_length );

        server_addr.sin_family = AF_INET;
        server_addr.sin_port = htons( SERVER_PORT );

        if( ( ret = connect( server_fd, (struct sockaddr *) &server_addr,
                             sizeof( server_addr ) ) ) < 0 )
        {
            printf( " failed\n  ! connect returned %d\n\n", ret );
            goto exit;
        }

        printf( " ok\n" );

        /*
         * Write the GET request
         */
        printf( "  > Write to server:" );
        fflush( stdout );

        len = sprintf( (char *) buf, GET_REQUEST );

        while( ( ret = write( server_fd, buf, len ) ) <= 0 )
        {
            if( ret != 0 )
            {
                printf( " failed\n  ! write returned %d\n\n", ret );
                goto exit;
            }
        }

        len = ret;
        printf( " %d bytes written\n\n%s", len, (char *) buf );

        /*
         * Read the HTTP response
         */
        printf( "  < Read from server:" );
        fflush( stdout );
        do
        {
            len = sizeof( buf ) - 1;
            memset( buf, 0, sizeof( buf ) );
            ret = read( server_fd, buf, len );

            if( ret <= 0 )
            {
                printf( "failed\n  ! ssl_read returned %d\n\n", ret );
                break;
            }

            len = ret;
            printf( " %d bytes read\n\n%s", len, (char *) buf );
        }
        while( 1 );

    exit:

        close( server_fd );

    #ifdef WIN32
        printf( "  + Press Enter to exit this program.\n" );
        fflush( stdout ); getchar();
    #endif

        return( ret );
    }

This is a simple client application that does the following:

* Opens a connection on port 80 to a server-
* Writes a standard HTTP GET request for the main page.
* Reads the result until nothing more is sent.
