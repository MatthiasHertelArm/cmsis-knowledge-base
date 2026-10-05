---
id: "alp-pqc-pqm4-introduction-why-post-quantum-cryptography"
type: "concept"
domain: "core"
title: "Implement post-quantum cryptography on Arm Cortex-M4: Understand pqm4 and post-quantum cryptography: Why post-quantum cryptography matters for embedded systems"
summary: "Classical public-key schemes such as RSA and elliptic curve cryptography will become insecure after sufficiently powerful quantum computers exist."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/pqc_pqm4/introduction.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/pqc_pqm4/introduction/#why-post-quantum-cryptography-matters-for-embedded-systems"
license: "CC-BY-SA-4.0"
mode: "V"
---

Classical public-key schemes such as RSA and elliptic curve cryptography will become insecure after sufficiently powerful quantum computers exist. Embedded devices are particularly exposed because they often remain deployed for 10 to 20 years, which is longer than the expected timeline for quantum threats to mature.

NIST has standardized the following core PQC primitives to replace classical schemes:

- ML-KEM (FIPS 203): a key encapsulation mechanism (KEM) for establishing shared secrets, replacing ECDH in protocols such as TLS
- ML-DSA (FIPS 204): a digital signature algorithm for authentication and integrity, replacing ECDSA

These algorithms demand more computation, memory, and code size than their classical counterparts, making evaluating them on real Cortex-M4 hardware non-trivial. In this Learning Path, you'll focus on KEM implementations.
