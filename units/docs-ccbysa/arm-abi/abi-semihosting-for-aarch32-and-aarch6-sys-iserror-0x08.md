---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-iserror-0x08"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_ISERROR (0x08)`"
summary: "Determines whether the return code from another semihosting call is an error status or not."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Determines whether the return code from another semihosting call is an error status or not.

This call is passed a parameter block containing the error code to examine.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a one-field data block:

**field 1**
    The required status word to check.


#### Return


On exit, the RETURN REGISTER contains:

* 0 if the status field is not an error indication

* A nonzero value if the status field is an error indication.
