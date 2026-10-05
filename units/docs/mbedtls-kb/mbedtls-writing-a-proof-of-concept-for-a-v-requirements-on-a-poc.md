---
id: "mbedtls-writing-a-proof-of-concept-for-a-v-requirements-on-a-poc"
type: "concept"
domain: "security"
title: "Writing a proof-of-concept for a vulnerability: Requirements on a PoC"
summary: "This section discusses requirements on a PoC."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/attacks/poc-guidelines.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/attacks/poc-guidelines.md#requirements-on-a-poc"
license: "Apache-2.0"
mode: "V"
---

This section discusses requirements on a PoC. We have found that submissions based on LLM (large language models, “AI”) often fail to distinguish an attacker from the victim, or target internal interfaces in the victim, and that leads to unfounded claims. Please pay careful attention to these requirements in any LLM-assisted report.

### Separate the victim from the attacker

The PoC should make it clear what part is the victim and what part is the attacker. The attacker tries to cause something bad to happen. The victim suffers consequences from the bad thing, such as incorrect operation, leaking secret data, etc.

In some types of vulnerability, the victim is a correct program and the attacker only needs to supply a data file that is passed as input to this program. For example, to demonstrate a parser bug, the PoC generally consists of a small victim program (possibly one of the sample programs provided with the library), and the attacker is instantiated through a specially crafted input file.

In some types of vulnerabilities, especially bugs in the TLS protocol, the attacker needs to have a more active role. In such cases, it is often helpful to split the PoC into a victim program and an attacker program. The attacker does not have to use Mbed TLS, although if it does, this can help us understand what the attacker is doing. For example, for a vulnerability that lets a client attack a TLS server, the preferred PoC consists of an attacker TLS client, combined with one of the sample or test TLS servers provided with Mbed TLS.

### Correct API use in the victim

The victim program must only use documented APIs, and must use them correctly according to the library documentation and according to the use of the C language. In particular:

* Only use functions declared in a public header (headers installed by `make install` or `cmake --install`). Private functions might not check for invalid inputs if they are only meant to be called from higher-level functions that check the inputs first.
* Do not access private fields of structures (do not define `MBEDTLS_ALLOW_PRIVATE_ACCESS`, and do not access `foo.private_xxx` explicitly). Private fields may not have the meaning that you expect, and modifying them has undefined behavior.
* Obey the rules of the C language: if the application code violates these rules, the behavior of the library is undefined. This includes rules given in function documentation: for example, if a function requires a “pointer to N bytes”, and the function crashes when you pass a null pointer, that's a programmer error, not a library bug.

Any violation of these rules disqualifies the PoC.

### Reproduction instructions

Please provide complete instructions to reproduce the problem, such as:

* The exact version of the product that the PoC works against. This should be the latest release in a supported branch of [TF-PSA-Crypto](https://github.com/Mbed-TLS/TF-PSA-Crypto/blob/development/BRANCHES.md) or [Mbed TLS](https://github.com/Mbed-TLS/mbedtls/blob/development/BRANCHES.md), or a more recent commit on a supported branch.
* The compile-time configuration of the library.
* The platform and compiler that you used.
* Instructions for compiling the PoC, if it's in the form of a separate program.
* Instructions for running the PoC, if it's more complicated than building and running a program with no arguments.
