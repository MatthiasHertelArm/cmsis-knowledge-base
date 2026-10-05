---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-elapsed-0x30"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_ELAPSED (0x30)`"
summary: "Returns the number of elapsed target ticks since execution started."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Returns the number of elapsed target ticks since execution started.

Use SYS_TICKFREQ (0x31) to determine the tick frequency.


#### Entry (32-bit)


On entry, the PARAMETER REGISTER points to a two-field data block to be used for returning the number of elapsed ticks:

**field 1**
    The least significant field and is at the low address.

**field 2**
    The most significant field and is at the high address.


#### Entry (64-bit)


On entry the PARAMETER REGISTER points to a one-field data block to be used for returning the number of elapsed ticks:

**field 1**
    The number of elapsed ticks as a 64-bit value.


#### Return


On exit:

* On success, the RETURN REGISTER contains 0, the PARAMETER REGISTER is unchanged, and the data block pointed to by the PARAMETER REGISTER is filled in with the number of elapsed ticks.

* On failure, the RETURN REGISTER contains -1, and the PARAMETER REGISTER contains -1.


**Note:** Some semihosting implementations might not support this semihosting operation, and they always return -1 in the RETURN REGISTER.

- SYS_TICKFREQ (0x31)
