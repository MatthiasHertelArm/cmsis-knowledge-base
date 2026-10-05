---
id: "mbedtls-writing-a-proof-of-concept-for-a-v-considerations-for-particular-classes-of"
type: "concept"
domain: "security"
title: "Writing a proof-of-concept for a vulnerability: Considerations for particular classes of vulnerabilities"
summary: "If the vulnerability is a memory corruption (buffer overflow, use-after-free, double free, etc.), then the PoC only needs to reach the stage where the memory is corrupted. It is not useful to demonstrate concrete effects beyond that."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/attacks/poc-guidelines.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/attacks/poc-guidelines.md#considerations-for-particular-classes-of-vulnerabilities"
license: "Apache-2.0"
mode: "V"
---

### PoC for memory corruption

If the vulnerability is a memory corruption (buffer overflow, use-after-free, double free, etc.), then the PoC only needs to reach the stage where the memory is corrupted. It is not useful to demonstrate concrete effects beyond that.

Our preferred tool for analyzing memory corruption is AddressSanitizer (ASan). If a program causes ASan to crash from correct use of the library, that is a good PoC.

### Side channels

Leakage through side channels is often difficult to reproduce and often requires complicated analysis. If you are writing an academic paper about a side channel attack, you do not need to share your tooling. We may be interested on a personal basis, but it is usually not practically useful for our triage and fixing.
