---
id: "tfm-hw-crypto-key-integration-in-tf-m-requirements"
type: "concept"
domain: "security"
title: "HW crypto key integration in TF-M secure boot: Requirements"
summary: "HW crypto key integration in TF-M secure boot: Requirements"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/secure_boot_hw_key_integration.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_hw_key_integration.html#requirements"
license: "BSD-3-Clause"
mode: "V"
---

- Multiple independent vendor scenario must be supported, when more than one
  ROTPK is provisioned to the device.
- The corresponding public key for image verification must be identifiable and
  verifiable.
- Key identity must be immutable and anchored to the device itself.
- Key(s) can be provisioned independently from bootloader.
