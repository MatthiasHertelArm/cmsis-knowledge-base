---
id: "mbedtls-tools-for-testing-constant-flow-co-static-analyzers-and-formal-guarantees"
type: "concept"
domain: "security"
title: "Tools for testing constant-flow code: Static analyzers and formal guarantees"
summary: "In recent years there seems to be more interest from the programming languages community in eliminating side-channel attacks by providing some form of formal guarantee of safety."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/testing/testing-constant-flow.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/testing/testing-constant-flow.md#static-analyzers-and-formal-guarantees"
license: "Apache-2.0"
mode: "V"
---

In recent years there seems to be more interest from the programming languages community in eliminating side-channel attacks by providing some form of formal guarantee of safety. These methods usually involve making a new (or modifying a) language/compiler that can detect the incorrect usage of secrets.

References:
- <http://cuda.dcc.ufmg.br/flowtracker/>
- <https://ranjitjhala.github.io/static/fact_dsl.pdf>
- <https://eprint.iacr.org/2019/1393.pdf#section.4> (section IV, useful summary of recent ideas)

Pros:
- Often provides some guarantee of safety
- Can sometimes transform more readable unsafe code into safe code.

Cons:
- May involve rewriting sections of constant-time code
- Still potential for safe code but unsafe binaries
