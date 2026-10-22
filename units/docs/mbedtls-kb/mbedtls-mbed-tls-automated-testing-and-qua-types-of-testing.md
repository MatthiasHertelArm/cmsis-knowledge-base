---
id: "mbedtls-mbed-tls-automated-testing-and-qua-types-of-testing"
type: "concept"
domain: "security"
title: "Mbed TLS automated testing and quality assurance: Types of testing"
summary: "Mbed TLS uses a Buildbot environment to run these tests on a number of different environments."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/generic/what-tests-and-checks-are-run-for-polarssl.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/generic/what-tests-and-checks-are-run-for-polarssl.md#types-of-testing"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS provids a variety of tests.

We automatically check:

* Compilation on different systems.
* Code coverage.
* Regressions, test vectors and corner cases.
* Interoperability with other SSL libraries.
* Different build configurations.
* Memory leaks.
* Memory integrity (bounds, initialization).

Mbed TLS uses a Buildbot environment to run these tests on a number of different environments.
