---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-writec-0x03"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_WRITEC (0x03)`"
summary: "Writes a character byte, pointed to by the PARAMETER REGISTER, to the debug channel."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Writes a character byte, pointed to by the PARAMETER REGISTER, to the debug channel.

When executed under an ARM debugger, the character appears on the host debugger console.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to the character.


#### Return


None. The RETURN REGISTER is corrupted.

- SYS_WRITE (0x05)

- SYS_WRITE0 (0x04)
