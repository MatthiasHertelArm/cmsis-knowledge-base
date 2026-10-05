---
id: "mbedtls-rsassa-pss-mbed-tls-support-of-rsassa-pss"
type: "concept"
domain: "security"
title: "RSASSA-PSS: Mbed TLS support of RSASSA-PSS"
summary: "Mbed TLS fully supports RSASSA-PSS directly in its RSA module. To use RSA as specified in PKCS#1 v2.1, with SHA1 as the hash method, for example, you should initialize your RSA context with:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/generic/rsassa-pss.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/generic/rsassa-pss.md#mbed-tls-support-of-rsassa-pss"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS fully supports RSASSA-PSS directly in its [RSA module](https://github.com/rsa-source-code). To use RSA as specified in PKCS#1 v2.1, with SHA1 as the hash method, for example, you should initialize your RSA context with:

```
mbedtls_rsainit( &rsa, RSA_PKCS_V21, MBEDTLS_MD_SHA256);
```

After loading the RSA key into that context, you can then use it to sign, with the RSASSA-PSS scheme, by using the generic `mbedtls_rsapkcs1_sign()` for signing and `mbedtls_rsapkcs1_verify()` for verification. Alternatively, you can use the more specific  `mbedtls_rsarsassa_pss_sign()` and `mbedtls_rsarsassa_pss_verify()`.

<!--",Short article on what RSASSA-PSS is, the differences with RSASSA-PKCS#1-v1.5 and how to use RSASSA-PSS within Mbed TLS.",,"RSASSA-PSS, PKCS#1, RSA",published,"2013-12-10 12:52:00",1,9774,"2015-07-24 09:51:00","Paul Bakker"-->
