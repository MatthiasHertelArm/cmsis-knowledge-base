---
id: "mbedtls-deprecations-partial-deprecation"
type: "concept"
domain: "security"
title: "Deprecations: Partial deprecation"
summary: "From time to time it is necessary to deprecate one specific aspect of a function. For example, calling a function in a particular mode or with a particular parameter may be deprecated."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/deprecation.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/deprecation.md#partial-deprecation"
license: "Apache-2.0"
mode: "V"
---

From time to time it is necessary to deprecate one specific aspect of a function. For example, calling a function in a particular mode or with a particular parameter may be deprecated. In this case, simply add a line to the function's doxygen description explaining the deprecation. For example:
```c
/**
 * \brief           This function divides x by y
 *
 * \deprecated      It is deprecated to call this function with y = 0.
 *                  Future versions of this function will return an error
 *                  when called with y = 0, rather than returning INT_MAX as
 *                  is the current behaviour.
 *
 * ...
 */
```
