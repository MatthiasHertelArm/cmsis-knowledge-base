---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-get-cmdline-0x15"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_GET_CMDLINE (0x15)`"
summary: "Returns the command line that is used for the call to the executable, that is, argc and argv."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Returns the command line that is used for the call to the executable, that is, `argc` and `argv`.


#### Entry


On entry, the PARAMETER REGISTER points to a two-field data block to be used for returning the command string and its length:

**field 1**
    A pointer to a buffer of at least the size that is specified in field 2.

**field 2**
    The length of the buffer in bytes.


#### Return


On exit:

If the call is successful, then the RETURN REGISTER contains 0, the PARAMETER REGISTER is unchanged, and the data block is updated as follows:

**field 1**
    A pointer to a null-terminated string of the command line.

**field 2**
    The length of the string in bytes.

If the call is not successful, then the RETURN REGISTER contains -1.


**Note:** The semihosting implementation might impose limits on the maximum length of the string that can be transferred. However, the implementation must be able to support a command-line length of at least 80 bytes.
