---
id: "tfm-bl1-immutable-bootloader-bl1-fi-and-dpa-mitigations"
type: "concept"
domain: "security"
title: "BL1 Immutable bootloader: BL1 FI and DPA mitigations"
summary: "BL1 reuses the FI countermeasures used in the TF-M runtime, which are found in lib/fih/."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/bl1.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/bl1.html#bl1-fi-and-dpa-mitigations"
license: "BSD-3-Clause"
mode: "V"
---

BL1 reuses the FI countermeasures used in the TF-M runtime, which are found in
`lib/fih/`.

BL1 implements countermeasures against fault injection. The functions with these
countermeasures are found in `bl1/bl1_1/shared_lib/util.c`

`bl_fih_memeql` tests if memory regions have the same value

- It inserts random delays to improve resilience to FIH attacks
- It performs loop integrity checks
- It uses FIH constructs
