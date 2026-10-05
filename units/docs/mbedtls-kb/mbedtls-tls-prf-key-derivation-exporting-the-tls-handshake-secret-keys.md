---
id: "mbedtls-tls-prf-key-derivation-exporting-the-tls-handshake-secret-keys"
type: "concept"
domain: "security"
title: "TLS PRF key derivation: Exporting the TLS handshake secret keys"
summary: "With the configuration option MBEDTLS_SSL_EXPORT_KEYS enabled, the keys generated in the TLS handshake are exported to a callback you define and set."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/tls_prf.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/tls_prf.md#exporting-the-tls-handshake-secret-keys"
license: "Apache-2.0"
mode: "V"
---

**Note:** Exporting the secret information can affect the security of your application! You should not expose this information outside of your application. Clear the information after use with `mbedtls_platform_zeroize()`!

With the configuration option `MBEDTLS_SSL_EXPORT_KEYS` enabled, the keys generated in the TLS handshake are exported to a callback you define and set.

The prototype of the callback is:

```
  typedef int mbedtls_ssl_export_keys_ext_t( void *p_expkey,
                                         const unsigned char *ms,
                                         const unsigned char *kb,
                                         size_t maclen,
                                         size_t keylen,
                                         size_t ivlen,
                                         unsigned char client_random[32],
                                         unsigned char server_random[32],
                                         mbedtls_tls_prf_types tls_prf_type );
```

Set the callback function in your SSL configuration structure by calling `mbedtls_ssl_conf_export_keys_ext_cb` before you start the TLS handshake.

**Note:** There is another callback function, called `mbedtls_ssl_export_keys_t`, that the TLS library calls during the handshake; however, it doesn't export the random bytes and the tls-prf function used in the handshake. We recommend not to use `mbedtls_ssl_export_keys_t` because it will probably be deprecated in the future.

After you extract the required information in your callback to your given context (`p_expkey`), you can use it to call `mbedtls_ssl_tls_prf()`, which is described in the previous section, or for other purposes.
