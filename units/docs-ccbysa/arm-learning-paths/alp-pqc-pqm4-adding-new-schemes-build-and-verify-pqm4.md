---
id: "alp-pqc-pqm4-adding-new-schemes-build-and-verify-pqm4"
type: "concept"
domain: "core"
title: "Implement post-quantum cryptography on Arm Cortex-M4: Add a KEM implementation to pqm4: Build and verify pqm4"
summary: "Clean and rebuild pqm4 with your target platform."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/pqc_pqm4/adding-new-schemes.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/pqc_pqm4/adding-new-schemes/#build-and-verify-pqm4"
license: "CC-BY-SA-4.0"
mode: "V"
---

Clean and rebuild pqm4 with your target platform.

#### Physical board

To clean and rebuild pqm4 on a physical board:

```bash
make clean
make -j4 PLATFORM=nucleo-l476rg
```

#### QEMU

To clean and rebuild pqm4 on QEMU:

```bash
make clean
make -j4 PLATFORM=mps2-an386
```

After cleaning and rebuilding, check that the new binaries were generated:

```bash
ls elf/ | grep newhope512cpa | grep '\.elf$'
```

The output is similar to:

```output
crypto_kem_newhope512cpa_m4_hashing.elf
crypto_kem_newhope512cpa_m4_speed.elf
crypto_kem_newhope512cpa_m4_stack.elf
crypto_kem_newhope512cpa_m4_test.elf
crypto_kem_newhope512cpa_m4_testvectors.elf
```
