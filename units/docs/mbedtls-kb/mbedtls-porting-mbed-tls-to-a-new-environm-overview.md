---
id: "mbedtls-porting-mbed-tls-to-a-new-environm-overview"
type: "concept"
domain: "security"
title: "Porting Mbed TLS to a new environment or OS: Overview"
summary: "Mbed TLS has a modular design. Many of the modules are completely independent of any runtime, environment, or other module dependencies, with the exception of those dependent on the C library."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md#overview"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS has a modular design. Many of the modules are completely independent of any runtime, environment, or other module dependencies, with the exception of [those dependent on the C library](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../development/what-external-dependencies-does-mbedtls-rely-on.md).

The only parts of the library that potentially interact with the environment are:

* The network module `net_sockets.c` that can be disabled and replaced with a separate network stack. This can mean any transport layer stack that uses Mbed TLS.
* The timing module `timing.c` that can be disabled and replaced to suit the underlying OS or hardware drivers.
* Default sources of entropy in the entropy module and additional sources. You can register these.
* Optional functions that access a file system.
* Functions that need the current time from a real-time clock. You can disable them, although that limits what validation is possible for certificates.
* Functions that print messages, generally used for debug and diagnosis. You can disable or replace them to output messages to another platform-specific debug.

In short, in order to compile Mbed TLS for a bare-metal environment which already has a standard C library, [configure your build](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../compiling-and-building/how-do-i-configure-mbedtls.md) by disabling `MBEDTLS_NET_C`, `MBEDTLS_TIMING_C` and `MBEDTLS_ENTROPY_PLATFORM`, and potentially `MBEDTLS_FS_IO`, `MBEDTLS_HAVE_TIME_DATE` and `MBEDTLS_HAVE_TIME`.

This is more thoroughly documented in [`mbedtls_config.h`](https://github.com/api/config_8h.html).

The following sections give more detail on how to replace the missing parts.
