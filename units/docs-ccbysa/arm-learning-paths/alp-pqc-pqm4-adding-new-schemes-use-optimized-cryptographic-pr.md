---
id: "alp-pqc-pqm4-adding-new-schemes-use-optimized-cryptographic-pr"
type: "concept"
domain: "core"
title: "Implement post-quantum cryptography on Arm Cortex-M4: Add a KEM implementation to pqm4: Use optimized cryptographic primitives"
summary: "pqm4 provides optimized implementations of common primitives that you should use instead of bundling your own:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/pqc_pqm4/adding-new-schemes.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/pqc_pqm4/adding-new-schemes/#use-optimized-cryptographic-primitives"
license: "CC-BY-SA-4.0"
mode: "V"
---

pqm4 provides optimized implementations of common primitives that you should use instead of bundling your own:

- Keccak, SHA-3, and SHAKE: use `mupq/common/fips202.h`
- SHA-2: use `sha2.h`
- AES: use the assembly-optimized implementation in `common/aes.h`

The NewHope-512-CPA-KEM example uses the optimized Keccak code from `mupq/common/fips202.h`.
