---
id: "mbedtls-alternative-ways-of-allocating-mem-using-the-buffer-allocator-elsewhere"
type: "concept"
domain: "security"
title: "Alternative ways of allocating memory in Mbed TLS: Using the buffer allocator elsewhere"
summary: "The buffer allocator itself has no internal dependencies on any of the rest of Mbed TLS. So you can use it within your own codebase as well."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/using-static-memory-instead-of-the-heap.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/using-static-memory-instead-of-the-heap.md#using-the-buffer-allocator-elsewhere"
license: "Apache-2.0"
mode: "V"
---

The buffer allocator itself has no internal dependencies on any of the rest of Mbed TLS. So you can use it within your own codebase as well.

<!-- This guide from Mbed TLS explains how to prevent use of malloc() and free() within Mbed TLS and use your another (more static) dynamic memory allocator. malloc, free, memory allocation, dynamic memory, heap, stack, buffer_alloc -->
