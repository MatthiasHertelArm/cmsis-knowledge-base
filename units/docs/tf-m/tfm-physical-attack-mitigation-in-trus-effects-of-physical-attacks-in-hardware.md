---
id: "tfm-physical-attack-mitigation-in-trus-effects-of-physical-attacks-in-hardware"
type: "concept"
domain: "security"
title: "Physical attack mitigation in Trusted Firmware-M: Effects of physical attacks in hardware and in software execution"
summary: "The change in the behavior of the hardware and software cannot be seen in advance when performing a physical attack. On circuit-level they manifest in bit faults."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/tfm_physical_attack_mitigation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_physical_attack_mitigation.html#effects-of-physical-attacks-in-hardware-and-in-software-execution"
license: "BSD-3-Clause"
mode: "V"
---

The change in the behavior of the hardware and software cannot be seen in
advance when performing a physical attack. On circuit-level they manifest
in bit faults. These bit faults can cause varied effects in the behavior of
the device micro-architecture:

  - Instruction decoding pipeline is flushed.
  - Altering instructions when decoding.
  - Altering data when fetching or storing.
  - Altering register content, and the program counter.
  - Flip bits in register or memory.

These phenomenons happen at random and cannot be observed directly but the
effect can be traced in software execution. On the software level the following
can happen:

  - A few instructions are skipped. This can lead to taking different branch
    than normal.
  - Corrupted CPU register or data fetch could alter the result of a comparison
    instruction. Or change the value returned from a function.
  - Corrupted data store could alter the config of peripherals.
  - Very precise attacks with laser can flip bits in any register or in memory.

This is a complex domain. Faults are not well-understood. Different fault models
exist but all of them target a specific aspect of fault injection. One of the
most common and probably the easily applicable fault model is the instruction
skip.
