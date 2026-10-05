---
id: "mbedtls-mbed-tls-abstraction-layers-additional-function-abstraction"
type: "concept"
domain: "security"
title: "Mbed TLS abstraction layers: Additional function abstraction"
summary: "These are additional functions from external libraries or OS that are needed only in some circumstances, for example, threading library support."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/generic/abstraction-layers.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/generic/abstraction-layers.md#additional-function-abstraction"
license: "Apache-2.0"
mode: "V"
---

These are additional functions from external libraries or OS that are needed only in some circumstances, for example, threading library support.

Examples: threading.

These abstractions are implemented in their own module and enabled or disabled with a single define, for example, `MBEDTLS_THREADING_C` in `mbedtls_config.h`. They may also require additional configuration options. The threading library, for example, requires you to indicate which threading library you are using: pthread or an alternative.
