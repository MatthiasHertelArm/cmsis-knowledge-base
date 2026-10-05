---
id: "tfm-rp2350-introduction"
type: "concept"
domain: "security"
title: "RP2350: Introduction"
summary: "RP2350 features a dual-core Arm Cortex-M33 processor with 520 kiB on-chip SRAM, support for up to 16 MB of off-chip flash and a wide range of flexible I/O option including I2C, SPI, and - uniquely - Programmable I/O (PIO)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/rpi/rp2350/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/rpi/rp2350/.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

RP2350 features a dual-core Arm Cortex-M33 processor with 520 kiB on-chip SRAM,
support for up to 16 MB of off-chip flash and a wide range of flexible I/O option
including I2C, SPI, and - uniquely - Programmable I/O (PIO). With its security
features RP2350 offers significant enhancements over RP2040.

This platform port supports TF-M regression tests (Secure and Non-Secure)
with Isolation Level 1 and 2.


**Note:** Only the GNU toolchain is supported.


**Note:** Only the "profile_medium" predefined profile is supported.
