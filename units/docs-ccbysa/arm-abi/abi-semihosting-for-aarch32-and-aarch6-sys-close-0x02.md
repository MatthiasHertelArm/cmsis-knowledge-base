---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-close-0x02"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_CLOSE (0x02)`"
summary: "Closes a file on the host system. The handle must reference a file that was opened with SYS_OPEN (0x01)."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Closes a file on the host system. The handle must reference a file that was opened with SYS_OPEN (0x01).


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a one-field argument block:

**field 1**
    Contains a handle for an open file.


#### Return


On exit, the RETURN REGISTER contains:

* 0 if the call is successful

* –1 if the call is not successful.

- SYS_OPEN (0x01)
