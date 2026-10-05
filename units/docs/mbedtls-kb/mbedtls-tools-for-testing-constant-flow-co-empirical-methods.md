---
id: "mbedtls-tools-for-testing-constant-flow-co-empirical-methods"
type: "concept"
domain: "security"
title: "Tools for testing constant-flow code: Empirical methods"
summary: "There appear to be some empirical testing tools available for testing constant time code. Tools such as dudect work by running the program with different inputs and trying to detect statistically different execution times."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/testing/testing-constant-flow.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/testing-constant-flow.md#empirical-methods"
license: "Apache-2.0"
mode: "V"
---

There appear to be some empirical testing tools available for testing constant time code. Tools such as [dudect](https://github.com/oreparaz/dudect#dudect-dude-is-my-code-constant-time) work by running the program with different inputs and trying to detect statistically different execution times. While these tools may not provide formal guarantees of safety against side-channel attacks it could be a useful, and easy to implement, metric for constant time code.
