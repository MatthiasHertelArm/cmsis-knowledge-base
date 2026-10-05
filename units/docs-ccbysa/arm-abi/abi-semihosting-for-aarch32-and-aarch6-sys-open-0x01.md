---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-open-0x01"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_OPEN (0x01)`"
summary: "The file path is specified either as relative to the current directory of the host process, or absolute, using the path conventions of the host operating system."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Opens a file on the host system.

The file path is specified either as relative to the current directory of the host process, or absolute, using the path conventions of the host operating system.

Semihosting implementations must support opening the special path name `:semihosting-features` as part of the semihosting extensions reporting mechanism. See Semihosting extensions for details.

ARM targets interpret the special path name `:tt` as meaning the console input stream, for an open-read or the console output stream, for an open-write. Opening these streams is performed as part of the standard startup code for those applications that reference the C `stdio` streams.

The semihosting extension `SH_EXT_STDOUT_STDERR` allows the semihosting caller to open separate output streams corresponding to `stdout` and `stderr`. This extension is reported using feature byte 0, bit 1. Use SYS_OPEN (0x01) with the special path name `:semihosting-features` to access the feature bits. See Semihosting extensions for details.

If this extension is supported, the implementation must support the following additional semantics to SYS_OPEN (0x01):

* If the special path name `:tt` is opened with an `fopen` mode requesting write access (`w`, `wb`, `w+`, or `w+b`), then this is a request to open `stdout`.

*    If the special path name `:tt` is opened with a mode requesting append access (`a`, `ab`, `a+`, or `a+b`), then this is a request to open `stderr`.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a three-field argument block:

**field 1**
    A pointer to a null-terminated string containing a file or device name.

**field 2**
    An integer that specifies the file opening mode. The `Value of mode` table gives the valid values for the integer, and their corresponding ISO C `fopen()` mode.

**field 3**
    An integer that gives the length of the string pointed to by field 1.

    The length does not include the terminating null character that must be present.


+------------------------------+-------+--------+--------+---------+-------+--------+--------+---------+-------+--------+--------+---------+
| Mode                         |   0   |   1    |   2    |   3     |   4   |   5    |   6    |   7     |   8   |   9    |   10   |   11    |
+------------------------------+-------+--------+--------+---------+-------+--------+--------+---------+-------+--------+--------+---------+
| ISO C fopen mode (Note 1) | `r` | `rb` | `r+` | `r+b` | `w` | `wb` | `w+` | `w+b` | `a` | `ab` | `a+` | `a+b` |
+------------------------------+-------+--------+--------+---------+-------+--------+--------+---------+-------+--------+--------+---------+

**Note:** .. _Note 1: 1. The non-ANSI option `t` is not supported.


#### Return


On exit, the RETURN REGISTER contains:

* A nonzero handle if the call is successful.

* –1 if the call is not successful.
