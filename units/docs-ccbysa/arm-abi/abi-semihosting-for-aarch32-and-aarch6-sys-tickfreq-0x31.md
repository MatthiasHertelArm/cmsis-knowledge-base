---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-tickfreq-0x31"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_TICKFREQ (0x31)`"
summary: "The PARAMETER REGISTER must contain 0 on entry to this routine."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Returns the tick frequency.


#### Entry


The PARAMETER REGISTER must contain 0 on entry to this routine.


#### Return


On exit, the RETURN REGISTER contains either:

* The number of ticks per second.

* –1 if the target does not know the value of one tick.


**Note:** Some semihosting implementations might not support this semihosting operation, and they always return -1 in the RETURN REGISTER.
