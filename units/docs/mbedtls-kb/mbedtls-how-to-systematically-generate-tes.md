---
id: "mbedtls-how-to-systematically-generate-tes"
type: "concept"
domain: "security"
title: "How to systematically generate test data"
summary: "When adding new test functions or improving coverage of existing tests in Mbed TLS, a large number of test cases may need to be added. This can be time-consuming and error-prone when adding manually."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/add-test-generation.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-test-generation.md"
license: "Apache-2.0"
mode: "V"
---

When adding new test functions or improving coverage of existing tests in Mbed TLS,
a large number of test cases may need to be added.
This can be time-consuming and error-prone when adding manually.
Mbed TLS includes a Python framework which can be used to systematically generate test
case data from input values.
The framework is flexible, to support a variety of test functions, and uses inheritance
to reduce code repetition in similar test functions.

This document outlines the components of the framework, and how these interact, with a
step-by-step example showing how these components may be implemented.
