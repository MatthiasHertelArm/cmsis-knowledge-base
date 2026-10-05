---
id: "mbedtls-porting-mbed-tls-to-a-new-environm-timing"
type: "concept"
domain: "security"
title: "Porting Mbed TLS to a new environment or OS: Timing"
summary: "The provided timing module timing.c works on Windows, Linux and BSD (including OS X)."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md#timing"
license: "Apache-2.0"
mode: "V"
---

The provided timing module `timing.c` works on Windows, Linux and BSD (including OS X). It is only optionally used by the SSL/TLS module through callback functions for DTLS and can be disabled at compilation without affecting the rest of the library.

If you are not using DTLS, you do not need a timing function. If you are using DTLS, you need to write your own timer callbacks suitable to pass to the function [`mbedtls_ssl_set_timer_cb()`](https://github.com/api/ssl_8h.html). This is discussed in more detail in our [DTLS tutorial](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/dtls-tutorial.md).
