---
id: "tfm-musca-b1-platform-specifics-daplink-firmware"
type: "concept"
domain: "security"
title: "Musca-B1 Platform Specifics: DAPLink Firmware"
summary: "The code on Musca-B1 is running from embedded flash. Make sure that the DAPLink FW for eFlash is downloaded to the board."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/arm/musca_b1/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/musca_b1/.html#daplink-firmware"
license: "BSD-3-Clause"
mode: "V"
---

The code on Musca-B1 is running from embedded flash. Make sure that the DAPLink
FW for eFlash is downloaded to the board. You can find on the
[Arm Developer page](https://developer.arm.com/documentation/110409/0100/Musca-B1-firmware-update-and-boot-recovery)
A short description of how to update the DAPLink FW can be found there as well.

Warm reset of eFlash is not supported on Musca_B1. TF-M may not boot after
a warm reset. Further information on the hardware limitation can be
found on [Arm Developer page](https://developer.arm.com/documentation/110409/0100/Musca-B1-warm-reset-of-eFlash).
