---
id: "mbedtls-writing-a-proof-of-concept-for-a-v-what-is-a-proof-of-concept-poc"
type: "concept"
domain: "security"
title: "Writing a proof-of-concept for a vulnerability: What is a proof-of-concept (PoC)?"
summary: "A PoC for a security issue is an artifact that demonstrates a vulnerability. It can take different forms, typically an input file, a small program, or a test case."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/attacks/poc-guidelines.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/attacks/poc-guidelines.md#what-is-a-proof-of-concept-poc"
license: "Apache-2.0"
mode: "V"
---

A PoC for a security issue is an artifact that demonstrates a vulnerability. It can take different forms, typically an input file, a small program, or a test case. It should illustrate how an attacker can cause a security property to be violated in a victim program.

A PoC does not need to be a full exploit. It only needs to produce observable evidence that a security property is violated.
