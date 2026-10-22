---
id: "mbedtls-the-external-dependencies-mbed-tls-signals-and-alarms"
type: "concept"
domain: "security"
title: "The external dependencies Mbed TLS relies on: Signals and alarms"
summary: "Both net_sockets.c and timing.c use signal handlers. The timing.c file uses them as support code for example programs. The signal handlers in net_sockets.c serve a more direct purpose."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/what-external-dependencies-does-mbedtls-rely-on.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/what-external-dependencies-does-mbedtls-rely-on.md#signals-and-alarms"
license: "Apache-2.0"
mode: "V"
---

Both `net_sockets.c` and `timing.c` use signal handlers. The `timing.c` file uses them as support code for example programs. The signal handlers in `net_sockets.c` serve a more direct purpose. You can remove this dependency by disabling or adapting the example programs and using alternate I/O callbacks instead of `net_sockets.c` in the TLS layer.

**Functions covered:** `signal()`

Only `timing.c` uses `alarm()`. This code is only used in example programs as support code, not in the actual library. You can remove this dependency.

**Functions covered:** `alarm()`
