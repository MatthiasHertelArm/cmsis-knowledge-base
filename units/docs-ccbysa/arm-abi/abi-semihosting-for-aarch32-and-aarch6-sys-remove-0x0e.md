---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-remove-0x0e"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_REMOVE (0x0E)`"
summary: "Deletes a specified file on the host filing system."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Deletes a specified file on the host filing system.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a two-field argument block:

**field 1**
    Points to a null-terminated string that gives the path name of the file to be deleted.

**field 2**
    The length of the string.


#### Return


On exit, the RETURN REGISTER contains:

* 0 if the delete is successful

* A nonzero, host-specific error code if the delete fails.
