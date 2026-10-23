---
id: "mbedtls-mbed-tls-ci-failure-faq-other-failed-checks-on-github"
type: "concept"
domain: "security"
title: "Mbed TLS CI failure FAQ: Other failed checks on GitHub"
summary: "If the pre-test checks failed, nothing was tested. Check the logs on Jenkins."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/testing/understanding-ci-failures.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/testing/understanding-ci-failures.md#other-failed-checks-on-github"
license: "Apache-2.0"
mode: "V"
---

### Pre-test checks failed

If the pre-test checks failed, nothing was tested. Check the logs on Jenkins.

### Internal CI failed

Unfortunately, only Arm employees can have access to the Internal CI.

The Internal CI and OpenCI run the same tests, so please resolve failures on OpenCI first. If OpenCI passes but the corresponding Internal CI check fails, please ask an Arm employee for assistance.

### DCO check failed

Please see the [DCO section in the CI guide](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/testing/testing-ci.md#dco).
