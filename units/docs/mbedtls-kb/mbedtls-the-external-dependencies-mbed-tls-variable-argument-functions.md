---
id: "mbedtls-the-external-dependencies-mbed-tls-variable-argument-functions"
type: "concept"
domain: "security"
title: "The external dependencies Mbed TLS relies on: Variable argument functions"
summary: "To make a half-compatible snprintf() function under Windows, you can use va_start(), va_end(), and vsnprintf(). All three are also used in the Debug module (debug.c). You can remove vsnprintf() by commenting MBEDTLS_DEBUG_C."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/what-external-dependencies-does-mbedtls-rely-on.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/what-external-dependencies-does-mbedtls-rely-on.md#variable-argument-functions"
license: "Apache-2.0"
mode: "V"
---

To make a half-compatible `snprintf()` function under Windows, you can use `va_start()`, `va_end()`, and `vsnprintf()`. All three are also used in the *Debug* module (`debug.c`). You can remove `vsnprintf()` by commenting `MBEDTLS_DEBUG_C`. 

**Functions covered:** 

- `va_start()`
- `va_end()`
- `vsnprintf()`
