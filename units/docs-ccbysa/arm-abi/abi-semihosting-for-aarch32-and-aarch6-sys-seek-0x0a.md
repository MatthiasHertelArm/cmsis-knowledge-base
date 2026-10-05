---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-seek-0x0a"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_SEEK (0x0A)`"
summary: "Seeks to a specified position in a file using an offset specified from the start of the file."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Seeks to a specified position in a file using an offset specified from the start of the file.

The file is assumed to be a byte array and the offset is given in bytes.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a two-field data block:

**field 1**
    A handle for a seekable file object.

**field 2**
    The absolute byte position to seek to.


#### Return


On exit, the RETURN REGISTER contains:

* 0 if the request is successful.

* A negative value if the request is not successful. Use SYS_ERRNO (0x13) to read the value of the host `errno` variable describing the error.


**Note:** The effect of seeking outside the current extent of the file object is undefined.

- SYS_ERRNO (0x13)
