---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-errno-0x13"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_ERRNO (0x13)`"
summary: "Returns the value of the C library errno variable that is associated with the semihosting implementation."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Returns the value of the C library `errno` variable that is associated with the semihosting implementation.

The `errno` variable can be set by a number of C library semihosted functions, including:

* SYS_REMOVE (0x0E)

* SYS_OPEN (0x01)

* SYS_CLOSE (0x02)

* SYS_READ (0x06)

* SYS_WRITE (0x05)

* SYS_SEEK (0x0A).

Whether `errno` is set or not, and to what value, is entirely host-specific, except where the ISO C standard defines the behavior.


#### Entry


There are no parameters. The PARAMETER REGISTER must be 0.


#### Return


On exit, the RETURN REGISTER contains the value of the C library `errno` variable.

- SYS_CLOSE (0x02)

- SYS_OPEN (0x01)

- SYS_READ (0x06)

- SYS_REMOVE (0x0E)

- SYS_SEEK (0x0A)

- SYS_WRITE (0x05)
