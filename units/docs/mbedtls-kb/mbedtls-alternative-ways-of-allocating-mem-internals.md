---
id: "mbedtls-alternative-ways-of-allocating-mem-internals"
type: "concept"
domain: "security"
title: "Alternative ways of allocating memory in Mbed TLS: Internals"
summary: "Internally, there are just two function pointers mbedtls_calloc() and mbedtls_free() that are called within Mbed TLS for each dynamic memory allocation or de-allocation."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/using-static-memory-instead-of-the-heap.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/using-static-memory-instead-of-the-heap.md#internals"
license: "Apache-2.0"
mode: "V"
---

Internally, there are just two function pointers `mbedtls_calloc()` and `mbedtls_free()` that are called within Mbed TLS for each dynamic memory allocation or de-allocation.

    extern void * (*mbedtls_calloc)( size_t n, size_t size );
    extern void (*mbedtls_free)( void *ptr );

The prototypes for these functions are identical to the `libc` standard `calloc()` and `free()`. Without any further calls, the default `libc` names are assigned to these pointers.

### No libc equivalents

If your system does not have a `libc` equivalent, you will get compile errors as `calloc()` or `free()` cannot be found.

Defining `MBEDTLS_PLATFORM_NO_STD_FUNCTIONS` in the `mbedtls_config.h` file prevents Mbed TLS from ever knowing about those functions.

### Providing your own hooks

If your operating system already provides an alternative to the `libc` allocator functions, you can set them with:

    int mbedtls_platform_set_calloc_free( void * (*calloc_func)( size_t, size_t ),
                                          void (*free_func)( void * ) );
