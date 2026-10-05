---
id: "mbedtls-alternative-ways-of-allocating-mem-using-the-mbed-tls-buffer-allocator"
type: "concept"
domain: "security"
title: "Alternative ways of allocating memory in Mbed TLS: Using the Mbed TLS buffer allocator"
summary: "If you want Mbed TLS to allocate everything inside a static buffer, you can enable the buffer allocator by defining MBEDTLS_MEMORY_BUFFER_ALLOC_C in the mbedtls_config.h file."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/using-static-memory-instead-of-the-heap.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/using-static-memory-instead-of-the-heap.md#using-the-mbed-tls-buffer-allocator"
license: "Apache-2.0"
mode: "V"
---

If you want Mbed TLS to allocate everything inside a static buffer, you can enable the buffer allocator by defining `MBEDTLS_MEMORY_BUFFER_ALLOC_C` in the `mbedtls_config.h` file.

Before calling any other Mbed TLS functions, enable the buffer allocator as follows:

    unsigned char memory_buf[100000];
    mbedtls_memory_buffer_alloc_init( memory_buf, sizeof(memory_buf) );
