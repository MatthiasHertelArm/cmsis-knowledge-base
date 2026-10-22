---
id: "mbedtls-porting-mbed-tls-to-a-new-environm-file-system-access"
type: "concept"
domain: "security"
title: "Porting Mbed TLS to a new environment or OS: File system access"
summary: "Several modules include functions that access the file system. You can disable all of them at compilation time without affecting the rest of the library."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md#file-system-access"
license: "Apache-2.0"
mode: "V"
---

Several modules include functions that access the file system. You can disable all of them at compilation time without affecting the rest of the library.

Every function that accesses the file system is only a convenience wrapper around a function that does the same job with memory buffers, so there is nothing to replace. Use the functions that work on buffers.
