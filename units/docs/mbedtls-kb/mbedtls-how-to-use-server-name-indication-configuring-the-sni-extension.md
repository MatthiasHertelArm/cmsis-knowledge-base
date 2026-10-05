---
id: "mbedtls-how-to-use-server-name-indication-configuring-the-sni-extension"
type: "concept"
domain: "security"
title: "How to use Server Name Indication: Configuring the SNI extension"
summary: "You need to configure SNI on both the client side and the server side."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/use-sni.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/use-sni.md#configuring-the-sni-extension"
license: "Apache-2.0"
mode: "V"
---

You need to configure SNI on both the [client side](#client-side) and the [server side](#server-side).

### Client side

The SNI extension uses the same server name that the client uses to verify the server certificates during the handshake. You can set it in the same [function](https://github.com/api/ssl_8h.html):
```
    mbedtls_ssl_set_hostname( context, "virtualserver15.myhost.com" );
```
**Warning:** If the hostname is not set with this function, Mbed TLS will silently skip certificate verification entirely. Always set the hostname with this function - even when not using SNI!

### Server side

Mbed TLS provides a very flexible solution for selecting the right certificate. The server application developer has to implement and set a callback function that:
1. Receives the server name and a pointer to the SSL context as a parameter.
1. Uses any means available in its environment to choose the appropriate certificate.
1. Sets the certificate in the SSL context.

**Example:**

The sample application `programs/ssl/ssl_server2.c` does this as follows:
```
    int sni_callback( void *p_info, mbedtls_ssl_context *ssl,
                  const unsigned char *name, size_t name_len )
    {
        const sni_entry *cur = (const sni_entry *) p_info;

        /* traverse the certificate info list */
        while( cur != NULL )
        {
            /* find the one with the name requested */
            if( name_len == strlen( cur->name ) &&
                memcmp( name, cur->name, name_len ) == 0 )
            {
                /* set the corresponding CA if applicable */
                if( cur->ca != NULL )
                    mbedtls_ssl_set_hs_ca_chain( ssl, cur->ca, cur->crl );

                /* set the authentication mode if it differs from the default */
                if( cur->authmode != DFL_AUTH_MODE )
                     mbedtls_ssl_set_hs_authmode( ssl, cur->authmode );

                /* set the certificate in the context */
                return( mbedtls_ssl_set_hs_own_cert( ssl, cur->cert, cur->key ) );
            }

            /* step to the next certificate info in the list */
            cur = cur->next;
        }

        /* certificate not found: return an error code */
        return( -1 );
    }
```
Here the pointer `p_info` points to a structure with sextuples of `<name, certificate, certificate authority, certificate revocation list, authentication mode>`, but it may change depending on the needs of a particular application.

To enable Mbed TLS using the callback function, you also have to register it:
```
    mbedtls_ssl_conf_sni( &conf, sni_callback, sni_info );
```
Here `conf` is an `mbedtls_ssl_config` structure, and the framework will pass `sni_info` to the callback function as the first parameter. Please make sure that the structure `sni_info` points to is properly initialised before calling this function, and stays consistent with the application's needs during the SSL context lifetime.
