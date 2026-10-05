---
id: "alp-pqc-pqm4-running-tests-and-benchm-understand-generated-pqm4-bina"
type: "concept"
domain: "edge-ai"
title: "Implement post-quantum cryptography on Arm Cortex-M4: Run pqm4 tests and benchmarks: Understand generated pqm4 binaries"
summary: "After building pqm4, a set of binaries is generated for each scheme and implementation. You can use these binaries to verify correctness, measure performance, and analyze resource usage on your Cortex-M4 board or in QEMU."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/pqc_pqm4/running-tests-and-benchmarks.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/pqc_pqm4/running-tests-and-benchmarks/#understand-generated-pqm4-binaries"
license: "CC-BY-SA-4.0"
mode: "V"
---

After building pqm4, a set of binaries is generated for each scheme and implementation. You can use these binaries to verify correctness, measure performance, and analyze resource usage on your Cortex-M4 board or in QEMU.

For example, building ML-KEM-768 produces binaries with names in this pattern:

```output
bin/crypto_kem_ml-kem-768_<impl>_<type>.bin
```

The `<impl>` field identifies the implementation variant. The exact suffix depends on the scheme:

- `m4fspeed`: Cortex-M4F implementation optimized for speed (used by ML-KEM)
- `m4fstack`: Cortex-M4F implementation optimized for stack size (used by ML-KEM)
- `m4f`: Cortex-M4F implementation used by some schemes such as BIKE
- `clean`: clean reference implementation from PQClean

The `clean` variant uses a different file prefix: `mupq_pqclean_crypto_kem_<scheme>_clean_<type>.elf`

The `<type>` field identifies what the binary measures. The following section explains each type and how you can run them.
