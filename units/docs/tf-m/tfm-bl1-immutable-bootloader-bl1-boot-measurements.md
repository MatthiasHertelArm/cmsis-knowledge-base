---
id: "tfm-bl1-immutable-bootloader-bl1-boot-measurements"
type: "concept"
domain: "security"
title: "BL1 Immutable bootloader: BL1 boot measurements"
summary: "BL1 outputs boot measurements in the same format as BL2, utilising the same shared memory area. These measurements can then be included in the attestation token, allowing the attestation of the version of the boot stage after BL1."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/bl1.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/bl1.html#bl1-boot-measurements"
license: "BSD-3-Clause"
mode: "V"
---

BL1 outputs boot measurements in the same format as BL2, utilising the same
shared memory area. These measurements can then be included in the attestation
token, allowing the attestation of the version of the boot stage after BL1.
