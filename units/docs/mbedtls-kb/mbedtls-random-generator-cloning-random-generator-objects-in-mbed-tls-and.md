---
id: "mbedtls-random-generator-cloning-random-generator-objects-in-mbed-tls-and"
type: "concept"
domain: "security"
title: "random generator cloning: Random generator objects in Mbed TLS and TF-PSA-Crypto"
summary: "Since TF-PSA-Crypto 1.0.0 and Mbed TLS 4.0.0, all random generation uses the random generator provided by the PSA subsystem. In previous versions, by default, the PSA subsystem is only used for PSA API calls and parts of TLS 1.3."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/random_generator_cloning.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/random_generator_cloning.md#random-generator-objects-in-mbed-tls-and-tf-psa-crypto"
license: "Apache-2.0"
mode: "V"
---

### PSA random generator

Since TF-PSA-Crypto 1.0.0 and Mbed TLS 4.0.0, all random generation uses the random generator provided by the PSA subsystem. In previous versions, by default, the PSA subsystem is only used for PSA API calls and parts of TLS 1.3. When `MBEDTLS_USE_PSA_CRYPTO` is enabled, the PSA random generator is also used in parts of the PK, X.509 and TLS subsystems.

### Legacy random generators

Up to Mbed TLS 3.x, random generator objects are constructed as follows:

1. Instantiate an `mbedtls_entropy_context` object.
2. Instantiate a DRBG object (`mbedtls_ctr_drbg_context` or `mbedtls_hmac_drbg_context`).
3. Call the DRBG seed function (`mbedtls_ctr_drbg_seed()` or `mbedtls_hmac_drbg_seed()`), passing `mbedtls_entropy_func` as the entropy callback and the entropy object as the entropy context.

These objects are known as legacy random generators. They are passed explicitly to Mbed TLS functions, and used everywhere that doesn't use the [PSA random generator](#psa-random-generator).
