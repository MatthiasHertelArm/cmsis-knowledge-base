---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-readc-0x07"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_READC (0x07)`"
summary: "The PARAMETER REGISTER must contain 0. There are no other parameters or values possible."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Reads a byte from the console.


#### Entry


The PARAMETER REGISTER must contain 0. There are no other parameters or values possible.


#### Return


On exit, the RETURN REGISTER contains the byte read from the console.

- SYS_READ (0x06)
