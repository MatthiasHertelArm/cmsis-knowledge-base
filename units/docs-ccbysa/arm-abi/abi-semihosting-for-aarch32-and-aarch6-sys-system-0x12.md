---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-system-0x12"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_SYSTEM (0x12)`"
summary: "Passes a command to the host command-line interpreter."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Passes a command to the host command-line interpreter.

This enables you to execute a system command such as `dir`, `ls`, or `pwd`. The terminal I/O is on the host, and is not visible to the target.


**Caution:** The command that is passed to the host is executed on the host. Ensure that any command passed has no unintended consequences.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a two-field argument block:

**field 1**
    Points to a string to be passed to the host command-line interpreter.

**field 2**
    The length of the string.


#### Return


On exit, the RETURN REGISTER contains the return status.
