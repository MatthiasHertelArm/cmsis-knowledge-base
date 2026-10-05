---
id: "mbedtls-deprecations"
type: "concept"
domain: "security"
title: "Deprecations"
summary: "To ensure backwards-compatibility between versions of Mbed TLS, elements of the public interface may not be removed except during the release of a new major version."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/deprecation.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/deprecation.md"
license: "Apache-2.0"
mode: "V"
---

To ensure backwards-compatibility between versions of Mbed TLS, elements of the public interface may not be removed except during the release of a new major version. Instead, they may be 'deprecated', indicating to users that they will be removed in the future.

When a build is made with `MBEDTLS_DEPRECATED_WARNING` defined, a compiler warning will be generated to warn a user that a function or constant will be removed at some point in the future, notifying users that they should change to a replacement function or constant at their own convenience. Note: this only works when using GCC-like compilers that recognize `__attribute__((deprecated))`.

To find examples of past deprecations, look at the previous major version of Mbed TLS.
