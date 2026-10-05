---
id: "alp-pqc-pqm4-adding-new-schemes-understand-schemes-in-pqm4"
type: "concept"
domain: "core"
title: "Implement post-quantum cryptography on Arm Cortex-M4: Add a KEM implementation to pqm4: Understand schemes in pqm4"
summary: "pqm4 ships with a curated set of NIST-standardized schemes, but you can extend it with additional algorithms."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/pqc_pqm4/adding-new-schemes.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/pqc_pqm4/adding-new-schemes/#understand-schemes-in-pqm4"
license: "CC-BY-SA-4.0"
mode: "V"
---

pqm4 ships with a curated set of NIST-standardized schemes, but you can extend it with additional algorithms. You might want to do this to evaluate an experimental scheme, test a custom Cortex-M4 assembly optimization, or contribute a new implementation to the community.

A scheme in pqm4 is a self-contained cryptographic algorithm implementation. Each scheme lives in its own directory under `crypto_kem/`, and pqm4's build system automatically discovers and compiles it alongside the existing schemes.
