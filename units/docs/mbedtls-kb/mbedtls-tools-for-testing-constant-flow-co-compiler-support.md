---
id: "mbedtls-tools-for-testing-constant-flow-co-compiler-support"
type: "concept"
domain: "security"
title: "Tools for testing constant-flow code: Compiler support"
summary: "In my (Manuel) ideal world, we would have some way to tell the compiler \"please try hard not introduce branches in this region of the code, and fail loudly if you can't\", but I don't think that's available anywhere yet."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/testing/testing-constant-flow.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/testing-constant-flow.md#compiler-support"
license: "Apache-2.0"
mode: "V"
---

In my (Manuel) ideal world, we would have some way to tell the compiler "please try hard not introduce branches in this region of the code, and fail loudly if you can't", but I don't think that's available anywhere yet.
