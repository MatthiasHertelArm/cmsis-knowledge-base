---
id: "mbedtls-deprecations-deprecating-functions"
type: "concept"
domain: "security"
title: "Deprecations: Deprecating functions"
summary: "To deprecate a function, the following actions must be taken:  In the header file (e.g. include/mbedtls/xyz.h):  Surround the function declaration with #if !defined(MBEDTLS_DEPRECATED_REMOVED)."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/deprecation.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/deprecation.md#deprecating-functions"
license: "Apache-2.0"
mode: "V"
---

To deprecate a function, the following actions must be taken:
* In the header file (e.g. `include/mbedtls/xyz.h`):
    * Surround the function declaration with `#if !defined(MBEDTLS_DEPRECATED_REMOVED)`.
    * Add a line to the docstring consisting of the keyword `\deprecated` followed by the reason for deprecation and (where applicable) the function it is superseded by.
    * Add the `MBEDTLS_DEPRECATED` annotation to the function prototype (so `int foo();` becomes `int MBEDTLS_DEPRECATED foo();`).
    * Make sure the header file includes `mbedtls/platform_util.h` (this contains the definition of `MBEDTLS_DEPRECATED`).
* In the source file (e.g. `library/xyz.c`):
    * Surround the function definition with `#if !defined(MBEDTLS_DEPRECATED_REMOVED)`.
    * If the function is superseded, ensure there is no code duplication between the old function and the new one. Typically this means refactoring the old function to be a simple wrapper around the new function.
* In a new file in ChangeLog.d (e.g. `ChangeLog.d/change-xyz-api.txt`)
    * Add an entry under the heading `New deprecations` that describes the deprecation. See [the ChangeLog readme](https://github.com/Mbed-TLS/mbedtls/blob/development/ChangeLog.d/00README.md) for more information on the format of ChangeLog entries.
* In the function's unit tests (see [the test guidelines](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/test_suites.md) for more information on unit tests):
    * Add `MBEDTLS_TEST_DEPRECATED` to the `depends_on:` line in the `.function` file that tests the deprecated function.
    * If there are test functions that can test either the deprecated function or the replacement, they may use the directive `#if defined(MBEDTLS_TEST_DEPRECATED)` to select the function to use.
