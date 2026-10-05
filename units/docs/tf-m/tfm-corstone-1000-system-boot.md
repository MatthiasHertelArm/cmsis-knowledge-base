---
id: "tfm-corstone-1000-system-boot"
type: "concept"
domain: "security"
title: "Corstone-1000: System boot"
summary: "Corstone-1000: System boot"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/arm/corstone1000/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/corstone1000/.html#system-boot"
license: "BSD-3-Clause"
mode: "V"
---

- The SoC reset brings Secure Enclave (SE), that is Cortex-M0+, out of rest.
- SE executes the BL1_1 ROM code which handles the hardware initialization. On
  the first boot, it handles the provisioning and the hashes of the keys used
  for image verification are saved in the OTP memory. The BL1_2 binary is also
  saved in the OTP.
- BL1_1 loads BL1_2 from OTP, verifies and transfers the execution to it.
- BL1_2 loads, verifies and transfers the execution to BL2 which is based on
  MCUBoot.
- BL2 loads and verifies TF-M and the host's initial boot loader image.
- BL2 transfers the execution to the TF-M.
- During TF-M initialization, the host is taken out of rest.


**Note:** In the current implementation the provisioning bundle, that is used by the BL1_1, is also stored in ROM.
