---
id: "mbedtls-tls-prf-key-derivation-example-of-tls-prf-key-derivation-eap-tl"
type: "concept"
domain: "security"
title: "TLS PRF key derivation: Example of tls-prf key derivation - EAP-TLS use case"
summary: "Following is an example of the process described before, deriving the eap-tls key material, as described in RFC 5216 section 2.3."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/tls_prf.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/tls_prf.md#example-of-tls-prf-key-derivation-eap-tls-use-case"
license: "Apache-2.0"
mode: "V"
---

Following is an example of the process described before, deriving the eap-tls key material, as described in [RFC 5216 section 2.3](https://tools.ietf.org/html/rfc5216#section-2.3).

### Defining the callback-specific context:

```
  typedef struct eap_tls_keys
  {
      unsigned char master_secret[48];
      unsigned char randbytes[64];
      mbedtls_tls_prf_types tls_prf_type;
  } eap_tls_keys;
```

### Defining the key export callback

```
  static int eap_tls_key_derivation ( void *p_expkey,
                                  const unsigned char *ms,
                                  const unsigned char *kb,
                                  size_t maclen,
                                  size_t keylen,
                                  size_t ivlen,
                                  unsigned char client_random[32],
                                  unsigned char server_random[32],
                                  mbedtls_tls_prf_types tls_prf_type )
  {
      eap_tls_keys *keys = (eap_tls_keys *)p_expkey;

      ( ( void ) kb );
      ( ( void ) maclen );
      ( ( void ) keylen );
      ( ( void ) ivlen );
      memcpy( keys->master_secret, ms, sizeof( keys->master_secret ) );
      memcpy( keys->randbytes, client_random, 32 );
      memcpy( keys->randbytes + 32, server_random, 32 );
      keys->tls_prf_type = tls_prf_type;

      return( 0 );
  }
```

### The main application

* Variable declarations:

    ```
    #if defined(MBEDTLS_SSL_EXPORT_KEYS)
        unsigned char eap_tls_keymaterial[16];
        unsigned char eap_tls_iv[8];
        const char* eap_tls_label = "client EAP encryption";
        eap_tls_keys eap_tls_keying;
    #endif
    ```

* Initialize the structures:

    ```
    #if defined(MBEDTLS_SSL_EXPORT_KEYS)
        mbedtls_ssl_conf_export_keys_ext_cb( &conf, eap_tls_key_derivation,
                                             &eap_tls_keying );
    #endif
    ```

* Perform TLS handshake.
* After a successful TLS handshake, derive the key material:
    ```
    #if defined(MBEDTLS_SSL_EXPORT_KEYS)
    {
        size_t j = 0;

        if( ( ret = mbedtls_ssl_tls_prf( eap_tls_keying.tls_prf_type,
                                         eap_tls_keying.master_secret,
                                         sizeof( eap_tls_keying.master_secret ),
                                         eap_tls_label,
                                         eap_tls_keying.randbytes,
                                         sizeof( eap_tls_keying.randbytes ),
                                         eap_tls_keymaterial,
                                         sizeof( eap_tls_keymaterial ) ) )
                                         != 0 )
        {
            mbedtls_printf( " failed\n  ! mbedtls_ssl_tls_prf returned -0x%x\n\n",
                            -ret );
            goto exit;
        }

        mbedtls_printf( "    EAP-TLS key material is:" );
        for( j = 0; j < sizeof( eap_tls_keymaterial ); j++ )
        {
            if( j % 8 == 0 )
                mbedtls_printf( "\n    " );
            mbedtls_printf( "%02x ", eap_tls_keymaterial[j] );
        }
        mbedtls_printf( "\n" );

        if( ( ret = mbedtls_ssl_tls_prf( eap_tls_keying.tls_prf_type, NULL, 0,
                                         eap_tls_label,
                                         eap_tls_keying.randbytes,
                                         sizeof( eap_tls_keying.randbytes ),
                                         eap_tls_iv,
                                         sizeof( eap_tls_iv ) ) ) != 0 )
         {
             mbedtls_printf( " failed\n  ! mbedtls_ssl_tls_prf returned -0x%x\n\n",
                             -ret );
             goto exit;
         }

        mbedtls_printf( "    EAP-TLS IV is:" );
        for( j = 0; j < sizeof( eap_tls_iv ); j++ )
        {
            if( j % 8 == 0 )
                mbedtls_printf( "\n    " );
            mbedtls_printf( "%02x ", eap_tls_iv[j] );
        }
        mbedtls_printf( "\n" );
    }
    #endif /* MBEDTLS_SSL_EXPORT_KEYS */
    ```
