---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-istty-0x09"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_ISTTY (0x09)`"
summary: "Checks whether a file is connected to an interactive device."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Checks whether a file is connected to an interactive device.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a one-field argument block:

**field 1**
    A handle for a previously opened file object.


#### Return


On exit, the RETURN REGISTER contains:

* 1 if the handle identifies an interactive device.

* 0 if the handle identifies a file.

* A value other than 1 or 0 if an error occurs.
