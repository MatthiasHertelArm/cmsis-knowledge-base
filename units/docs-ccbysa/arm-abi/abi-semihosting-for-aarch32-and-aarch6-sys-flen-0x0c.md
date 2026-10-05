---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-flen-0x0c"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_FLEN (0x0C)`"
summary: "On entry, the PARAMETER REGISTER contains a pointer to a one-field argument block:"
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Returns the length of a specified file.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a one-field argument block:

**field 1**
    A handle for a previously opened, seekable file object.


#### Return


On exit, the RETURN REGISTER contains:

* The current length of the file object, if the call is successful.

* –1 if an error occurs.
