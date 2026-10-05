---
id: "mbedtls-tls-prf-key-derivation-exporting-key-material-using-mbed-tls"
type: "concept"
domain: "security"
title: "TLS PRF key derivation: Exporting key material using Mbed TLS"
summary: "The Mbed TLS mbedtls_ssl_tls_prf() API uses the tls_prf function, which you set as an input parameter. You must set the tls_prf function to one of the following options:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/tls_prf.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/tls_prf.md#exporting-key-material-using-mbed-tls"
license: "Apache-2.0"
mode: "V"
---

The Mbed TLS `mbedtls_ssl_tls_prf()` API uses the `tls_prf` function, which you set as an input parameter. You must set the `tls_prf` function to one of the following options:

```
  typedef enum
  {
     MBEDTLS_SSL_TLS_PRF_NONE,
     MBEDTLS_SSL_TLS_PRF_SSL3,
     MBEDTLS_SSL_TLS_PRF_TLS1,
     MBEDTLS_SSL_TLS_PRF_SHA384,
     MBEDTLS_SSL_TLS_PRF_SHA256
  }
  mbedtls_tls_prf_types;
```

This function also receives the secret to derive the key material from. The secret is usually the TLS handshake master key, and the random bytes generated in the TLS handshake.

The following section explains how to export the handshake-generated secret information.
