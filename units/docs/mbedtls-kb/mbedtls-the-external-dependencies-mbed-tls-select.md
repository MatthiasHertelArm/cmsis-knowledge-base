---
id: "mbedtls-the-external-dependencies-mbed-tls-select"
type: "concept"
domain: "security"
title: "The external dependencies Mbed TLS relies on: Select"
summary: "Only net_sockets.c uses select(), for the purposes of sleeping (only used in the example programs, not in the library) or providing blocking reads with timeouts."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/what-external-dependencies-does-mbedtls-rely-on.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/what-external-dependencies-does-mbedtls-rely-on.md#select"
license: "Apache-2.0"
mode: "V"
---

Only `net_sockets.c` uses `select()`, for the purposes of sleeping (only used in the example programs, not in the library) or providing blocking reads with timeouts. You can remove this dependency by using alternate I/O callbacks instead of `net_sockets.c` in the TLS layer.

**Functions covered:** `select()`
