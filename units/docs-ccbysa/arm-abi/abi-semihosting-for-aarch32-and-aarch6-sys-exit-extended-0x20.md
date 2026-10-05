---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-exit-extended-0x20"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_EXIT_EXTENDED (0x20)`"
summary: "This operation is only supported if the semihosting extension SH_EXT_EXIT_EXTENDED is implemented."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

This operation is only supported if the semihosting extension SH_EXT_EXIT_EXTENDED is implemented.

`SH_EXT_EXIT_EXTENDED` is reported using feature byte 0, bit 0. If this extension is supported, then the implementation provides a means to report a normal exit with a nonzero exit status in both 32-bit and 64-bit semihosting APIs.

The implementation must provide the semihosting call SYS_EXIT_EXTENDED (0x20) for both A64 and A32/T32 semihosting APIs.

SYS_EXIT_EXTENDED (0x20) is used by an application to report an exception or exit to the debugger directly. The most common use is to report that execution has completed, using `ADP_Stopped_ApplicationExit`.


#### Entry


On entry, the PARAMETER REGISTER contains a pointer to a two-field argument block:

**field 1**
    The exception type, which should be one of the set of reason codes that are documented for the SYS_EXIT (0x18) call. For example, `ADP_Stopped_ApplicationExit` or `ADP_Stopped_InternalError`.

**field 2**
    A subcode, whose meaning depends on the reason code in field 1. In particular, if field 1 is `ADP_Stopped_ApplicationExit` then field 2 is an exit status code, as passed to the C standard library `exit()` function. A simulator receiving this request must notify a connected debugger, if present, and then exit with the specified status.


#### Return


No return is expected from these calls.


**Note:** For the A64 API, this call is identical to the behavior of the mandatory SYS_EXIT (0x18) call. If this extension is supported, then both calls must be implemented.

- SYS_EXIT (0x18)
