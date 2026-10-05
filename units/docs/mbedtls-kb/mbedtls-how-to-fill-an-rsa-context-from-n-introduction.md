---
id: "mbedtls-how-to-fill-an-rsa-context-from-n-introduction"
type: "concept"
domain: "security"
title: "How to fill an RSA context from N, E, P and Q: Introduction"
summary: "In some cases, you only have the base values for RSA at your disposal and want to use those within Mbed TLS. Mbed TLS, specifically the mbedtls_rsa_context structure, requires more than the base values to perform optimized operations for RSA."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/how-to-fill-rsa-context-from-n-e-p-and-q.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/how-to-fill-rsa-context-from-n-e-p-and-q.md#introduction"
license: "Apache-2.0"
mode: "V"
---

In some cases, you only have the base values for RSA at your disposal and want to use those within Mbed TLS. Mbed TLS, specifically the `mbedtls_rsa_context` structure, requires more than the base values to perform optimized operations for RSA.

You can deduce the other values if you have access to your **E**, **P** and **Q**. In most cases, you already have your **N**, so you can skip the next section.

You can import these values to your `mbedtls_rsa_context` structure with their raw value, in Big Endian, using the `mbedtls_rsa_import_raw()` function, or as `mbedtls_mpi` structures, using the `mbedtls_rsa_import()` function.
If you do not wish to set a component to the context, whether you do not know it or it is already set, you can just set it as `NULL` as the function parameter.

The following example shows you how to correctly initialize the RSA context named **ctx** with the values for **P,** **Q** and **E** into `mbedtls_rsa_context`.
