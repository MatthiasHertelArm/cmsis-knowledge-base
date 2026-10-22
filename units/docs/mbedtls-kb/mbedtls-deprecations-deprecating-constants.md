---
id: "mbedtls-deprecations-deprecating-constants"
type: "concept"
domain: "security"
title: "Deprecations: Deprecating constants"
summary: "Numeric and string constants can also be deprecated by wrapping them in the macros MBEDTLS_DEPRECATED_NUMERIC_CONSTANT() and MBEDTLS_DEPRECATED_STRING_CONSTANT() respectively. For example, the code:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/deprecation.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/deprecation.md#deprecating-constants"
license: "Apache-2.0"
mode: "V"
---

Numeric and string constants can also be deprecated by wrapping them in the macros `MBEDTLS_DEPRECATED_NUMERIC_CONSTANT()` and `MBEDTLS_DEPRECATED_STRING_CONSTANT()` respectively. For example, the code:
```c
const int X = 42;
```
would become:
```c
const int X = MBEDTLS_DEPRECATED_NUMERIC_CONSTANT(42);
```
The file where the constant is defined must include `mbedtls/platform_util.h` as it contains the definition of `MBEDTLS_DEPRECATED_NUMERIC_CONSTANT`.

Any testcases (in `.data` files) that use the deprecated constant must have `MBEDTLS_TEST_DEPRECATED` added to their `depends_on:` line.
