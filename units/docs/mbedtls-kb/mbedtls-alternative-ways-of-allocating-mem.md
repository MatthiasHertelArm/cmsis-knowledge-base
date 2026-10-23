---
id: "mbedtls-alternative-ways-of-allocating-mem"
type: "concept"
domain: "security"
title: "Alternative ways of allocating memory in Mbed TLS"
summary: "In several situations, like when not having an operating system on an embedded platform, there is no real availability of a heap or calloc()/free(). Mbed TLS still needs some form of dynamic memory allocation to operate the SSL stack."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/using-static-memory-instead-of-the-heap.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/using-static-memory-instead-of-the-heap.md"
license: "Apache-2.0"
mode: "V"
---

In several situations, like when not having an operating system on an embedded platform, there is no real availability of a heap or `calloc()`/`free()`. Mbed TLS still needs some form of dynamic memory allocation to operate the SSL stack. We could just assume the maximum sizes for all structures, but that would consume a lot of memory space. Instead we opted for letting Mbed TLS only use hooks to allocate and free dynamic memory.

This currently gives you two options:

1. Provide your own allocation and freeing functions.
2. Use the buffer allocator feature in Mbed TLS.

To enable the memory allocation layer, define `MBEDTLS_PLATFORM_C` and `MBEDTLS_PLATFORM_MEMORY` in the `mbedtls_config.h` file. See [How do I configure Mbed TLS](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../compiling-and-building/how-do-i-configure-mbedtls.md).

If you do not enable the layer, the libc standard `calloc()` and `free()` are used.
