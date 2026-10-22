---
id: "mbedtls-tools-for-testing-constant-flow-co"
type: "concept"
domain: "security"
title: "Tools for testing constant-flow code"
summary: "Code that manipulates secret values (private keys, etc.) needs to be constant-flow (often called constant-time, though the requirements are actually stricter than \"the total running time is a constant\"), that is contain no branches that depend on secret …"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/testing/testing-constant-flow.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/testing/testing-constant-flow.md"
license: "Apache-2.0"
mode: "V"
---

*This document is an investigation into test tooling. For usage in Mbed TLS and TF-PSA-Crypto unit tests, see “[Mbed TLS test guidelines — Constant-flow testing](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/testing/../development/test_suites.md#constant-flow-testing)”.*

Code that manipulates secret values (private keys, etc.) needs to be constant-flow (often called constant-time, though the requirements are actually stricter than "the total running time is a constant"), that is contain no branches that depend on secret values, and no memory accesses at addresses depending on a secret value, in order to avoid leaking the secret value through side channels.

Ideally, this should not only be enforced by code review, but also tested or checked by tools. This pages list some available options.
