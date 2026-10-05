---
id: "mbedtls-mbed-tls-abstraction-layers-standard-function-abstraction"
type: "concept"
domain: "security"
title: "Mbed TLS abstraction layers: Standard function abstraction"
summary: "These are standard functions from libc that are always needed. However, they will have different implementations and behave differently on some platforms."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/generic/abstraction-layers.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/generic/abstraction-layers.md#standard-function-abstraction"
license: "Apache-2.0"
mode: "V"
---

These are standard functions from libc that are always needed. However, they will have different implementations and behave differently on some platforms.

Examples: `calloc()`, `free()`, `printf()` and `fprintf()`.

These standard functions are abstracted in the **platform layer**. The layer core is enabled by default in `mbedtls_config.h` with `MBEDTLS_PLATFORM_C`, and allows the runtime customization of the relevant function.

The `MBEDTLS_PLATFORM_XXX` defined in `mbedtls_config.h` enables support for abstracting different functions.

For example, after enabling `MBEDTLS_PLATFORM_PRINTF_ALT`, you can set an alternative for `printf()` by calling `mbedtls_platform_set_printf()`.
