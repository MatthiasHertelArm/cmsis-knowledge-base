---
id: "mbedtls-spectre-and-meltdown-introduction"
type: "concept"
domain: "security"
title: "Spectre and Meltdown: Introduction"
summary: "Spectre and Meltdown are security flaws, recently and independently discovered by researchers at Google Project Zero and other organizations [[1]] [[2]] [[3]]."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/attacks/spectre_and_meltdown.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/attacks/spectre_and_meltdown.md#introduction"
license: "Apache-2.0"
mode: "V"
---

Spectre and Meltdown are security flaws, recently and independently discovered by
researchers at Google Project Zero and other organizations [[1]] [[2]] [[3]].
The originality of the Meltdown and Spectre attacks is that they exploit
security vulnerabilities in the microarchitecture of modern microprocessors,
even if the microprocessors have been implemented correctly against their own
architecture. What this means is that an attacker could recover sensitive data
by taking advantage of information leaks present in the hardware, even if the
processor preserves the correct behavior from the programmer's point of view.

In this article, we provide a brief description of these attacks, analyze
their impact on Mbed TLS and provide mitigations.
