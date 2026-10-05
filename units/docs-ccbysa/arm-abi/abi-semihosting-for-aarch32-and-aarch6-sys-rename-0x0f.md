---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-rename-0x0f"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_RENAME (0x0F)`"
summary: "On entry, the PARAMETER REGISTER contains a pointer to a four-field data block:"
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Renames a specified file.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a four-field data block:

**field 1**
    A pointer to the name of the old file.

**field 2**
    The length of the old filename.

**field 3**
    A pointer to the new filename.

**field 4**
    The length of the new filename.

Both strings are null-terminated.


#### Return


On exit, the RETURN REGISTER contains:

* 0 if the rename is successful.

* A nonzero, host-specific error code if the rename fails.
