---
id: "mbedtls-porting-mbed-tls-to-a-new-environm-default-entropy-sources"
type: "concept"
domain: "security"
title: "Porting Mbed TLS to a new environment or OS: Default entropy sources"
summary: "The entropy pool, part of the RNG module, collects and securely mixes entropy from a variety of sources. On Windows and different Unix platforms that provide /dev/urandom, a default OS-based source is registered."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md#default-entropy-sources"
license: "Apache-2.0"
mode: "V"
---

The entropy pool, part of the RNG module, collects and securely mixes entropy from a variety of sources. On Windows and different Unix platforms that provide `/dev/urandom`, a default OS-based source is registered. You can disable it at compilation without affecting the rest of the library.

This source can be replaced by coding one or more entropy-collection functions that implement the API expected by the function [`mbedtls_entropy_add_source()`](https://github.com/api/entropy_8h.html) and registering it with that function at runtime, or if it is based on a hardware source, at compilation time with `MBEDTLS_ENTROPY_HARDWARE_ALT`.

Please note that, for security reasons, the entropy module will refuse to output anything until a declared-strong source has been registered.

**Warning:** Evaluating the strength of the sources provided is the responsibility of those doing the platform port.
