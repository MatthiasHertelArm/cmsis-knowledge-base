---
id: "mbedtls-porting-mbed-tls-to-a-new-environm-networking"
type: "concept"
domain: "security"
title: "Porting Mbed TLS to a new environment or OS: Networking"
summary: "The provided network module net_sockets.c works on Windows and Unix systems that implement the BSD sockets API."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md#networking"
license: "Apache-2.0"
mode: "V"
---

The provided network module `net_sockets.c` works on Windows and Unix systems that implement the BSD sockets API. It is optionally used by the SSL/TLS module through callback functions, and can be disabled at compilation without affecting the rest of the library.

The callbacks can be replaced by coding your own functions for blocking or non-blocking write and read with optional timeout, based on the network or transport layer stack of your choice. Substitute functions must match the API expected by the function [`mbedtls_ssl_set_bio()`](https://github.com/api/ssl_8h.html).
