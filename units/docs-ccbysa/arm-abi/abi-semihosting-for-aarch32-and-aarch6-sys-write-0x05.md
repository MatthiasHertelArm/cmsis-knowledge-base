---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-write-0x05"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_WRITE (0x05)`"
summary: "Writes the contents of a buffer to a specified file at the current file position."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Writes the contents of a buffer to a specified file at the current file position.

The file position is specified either:

* Explicitly, by a SYS_SEEK (0x0A).

* Implicitly as one byte beyond the previous SYS_READ (0x06) or SYS_WRITE (0x05) request.

The file position is at the start of the file when the file is opened, and is lost when the file is closed.

Perform the file operation as a single action whenever possible. For example, do not split a write of 16KB into four 4KB chunks unless there is no alternative.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a three-field data block:

**field 1**
    Contains a handle for a file previously opened with SYS_OPEN (0x01).

**field 2**
    Points to the memory containing the data to be written.

**field 3**
    Contains the number of bytes to be written from the buffer to the file.


#### Return


On exit, the RETURN REGISTER contains:

* 0 if the call is successful.

* The number of bytes that are not written, if there is an error.

- SYS_WRITE0 (0x04)

- SYS_WRITEC (0x03)
