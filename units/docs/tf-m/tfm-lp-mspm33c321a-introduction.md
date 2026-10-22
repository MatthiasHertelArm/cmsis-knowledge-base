---
id: "tfm-lp-mspm33c321a-introduction"
type: "concept"
domain: "security"
title: "LP_MSPM33C321A: Introduction"
summary: "The LP_MSPM33C321A LaunchPad is a development board based on the Texas Instruments MSPM33C321A microcontroller."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/ti/LP_MSPM33C321A/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/ti/LP_MSPM33C321A/.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

The LP_MSPM33C321A LaunchPad is a development board based on the Texas Instruments
MSPM33C321A microcontroller. The device features an Arm Cortex-M33 core with
TrustZone-M support, 1 MB main flash, 32 KB data flash, and 256 KB SRAM, making
it suitable for PSA Certified implementations.

This platform port supports TF-M regression tests (Secure and Non-Secure) and
PSA Arch tests with Isolation Level 1.


**Note:** Only the GNU Arm Embedded toolchain (12.3 or later) is supported.


**Note:** BL2 (MCUboot) is not supported. The secure image executes directly from flash at `0x10000000` with no bootloader.
