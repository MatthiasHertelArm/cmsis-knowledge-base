---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-read-0x06"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_READ (0x06)`"
summary: "Reads the contents of a file into a buffer."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Reads the contents of a file into a buffer.

The file position is specified either:

* Explicitly by a SYS_SEEK (0x0A).

* Implicitly one byte beyond the previous SYS_READ (0x06) or SYS_WRITE (0x05) request.

The file position is at the start of the file when it is opened, and is lost when the file is closed. Perform the file operation as a single action whenever possible. For example, do not split a read of 16KB into four 4KB chunks unless there is no alternative.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a three-field data block:

**field 1**
    Contains a handle for a file previously opened with SYS_OPEN (0x01).

**field 2**
    Points to a buffer.

**field 3**
    Contains the number of bytes to read to the buffer from the file.


#### Return


On exit, the RETURN REGISTER contains the number of bytes not filled in the buffer (`buffer_length - bytes_read`) as follows:

* If the RETURN REGISTER is 0, the entire buffer was successfully filled.

* If the RETURN REGISTER is the same as field 3, no bytes were read (EOF can be assumed).

* If the RETURN REGISTER contains a value smaller than field 3, the read succeeded but the buffer was only partly filled. For interactive devices, this is the most common return value.

- SYS_READC (0x07)
