---
id: "mbedtls-the-external-dependencies-mbed-tls-memory-functions"
type: "concept"
domain: "security"
title: "The external dependencies Mbed TLS relies on: Memory functions"
summary: "The functions memcmp(), memcpy() and memset() are really basic in any system and used in several places. The assumption is that everybody has support for these."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/what-external-dependencies-does-mbedtls-rely-on.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/what-external-dependencies-does-mbedtls-rely-on.md#memory-functions"
license: "Apache-2.0"
mode: "V"
---

The functions `memcmp()`, `memcpy()` and `memset()` are really basic in any system and used in several places. The assumption is that everybody has support for these.

**Functions covered:** 

- `memcmp()`
- `memcpy()`
- `memset()`

The `memmove()` function is used as an optimization in the *TLS* module. It is also used in the nist key wrapping module (`nist_kw.c`) and in the NULL cipher wrap (`null_crypt_stream`) to avoid buffer overlapping. You can remove this dependency by providing your own implementation of the same functionality.

**Functions covered:** `memmove()`
