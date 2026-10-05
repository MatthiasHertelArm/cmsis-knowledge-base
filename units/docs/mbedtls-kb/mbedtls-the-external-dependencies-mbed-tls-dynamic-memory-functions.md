---
id: "mbedtls-the-external-dependencies-mbed-tls-dynamic-memory-functions"
type: "concept"
domain: "security"
title: "The external dependencies Mbed TLS relies on: Dynamic memory functions"
summary: "A number of modules (ASN1, Bignum/MPI, Cipher, CMAC, DHM, ECP, MD, PEM, PK, PKCS11, RSA, TLS, X.509) use dynamic memory allocation. You can provide your own implementations, and we even provide a buffer-based memory allocator."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/what-external-dependencies-does-mbedtls-rely-on.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/what-external-dependencies-does-mbedtls-rely-on.md#dynamic-memory-functions"
license: "Apache-2.0"
mode: "V"
---

A number of modules (ASN1, Bignum/MPI, Cipher, CMAC, DHM, ECP, MD, PEM, PK, PKCS11, RSA, TLS, X.509) use dynamic memory allocation. You can provide your own implementations, and we even provide a buffer-based memory allocator. For further details, read [Letting Mbed TLS use static memory instead of the heap](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/../how-to/using-static-memory-instead-of-the-heap.md).

**Functions covered:** 

- `free()`
- `calloc()`
