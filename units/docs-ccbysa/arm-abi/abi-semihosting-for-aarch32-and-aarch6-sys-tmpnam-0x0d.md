---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-tmpnam-0x0d"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_TMPNAM (0x0D)`"
summary: "Returns a temporary name for a file identified by a system file identifier."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Returns a temporary name for a file identified by a system file identifier.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a three-word argument block:

**field 1**
    A pointer to a buffer.

**field 2**
    A target identifier for this filename. Its value must be an integer in the range 0-255.

**field 3**
    Contains the length of the buffer. The length must be at least the value of `L_tmpnam` on the host system.


#### Return


On exit, the RETURN REGISTER contains:

* 0 if the call is successful.

* –1 if an error occurs.

The buffer pointed to by the PARAMETER REGISTER contains the filename, prefixed with a suitable directory name.

If you use the same target identifier again, the same filename is returned.


**Note:** The returned string must be null-terminated.
