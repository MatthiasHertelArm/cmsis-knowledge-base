---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-exit-0x18"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_EXIT (0x18)`"
summary: "An application calls this operation to report an exception to the debugger directly. The most common use is to report that execution has completed, using ADP_Stopped_ApplicationExit."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

**Note:** SYS_EXIT (0x18) was called `angel_SWIreason_ReportException` in previous versions of the documentation.

An application calls this operation to report an exception to the debugger directly. The most common use is to report that execution has completed, using `ADP_Stopped_ApplicationExit`.


**Note:** This semihosting operation provides no means for 32-bit callers to indicate an application exit with a specified exit code. Semihosting callers may prefer to check for the presence of the SH_EXT_EXIT_EXTENDED extension and use the SYS_EXIT_EXTENDED (0x20) operation instead, if it is available.


#### Entry (32-bit)


On entry, the PARAMETER register is set to a reason code describing the cause of the trap. Not all semihosting client implementations will necessarily trap every corresponding event. These reason codes are defined in the following tables.

The following table shows reason codes relating to hardware exceptions. Exception handlers can use these operations to report an exception that has not been handled:


+-----------------------------------+-------------------+
| Name                              | Hexadecimal value |
+-----------------------------------+-------------------+
| `ADP_Stopped_BranchThroughZero` | `0x20000`       |
+-----------------------------------+-------------------+
| `ADP_Stopped_UndefinedInstr`    | `0x20001`       |
+-----------------------------------+-------------------+
| `ADP_Stopped_SoftwareInterrupt` | `0x20002`       |
+-----------------------------------+-------------------+
| `ADP_Stopped_PrefetchAbort`     | `0x20003`       |
+-----------------------------------+-------------------+
| `ADP_Stopped_DataAbort`         | `0x20004`       |
+-----------------------------------+-------------------+
| `ADP_Stopped_AddressException`  | `0x20005`       |
+-----------------------------------+-------------------+
| `ADP_Stopped_IRQ`               | `0x20006`       |
+-----------------------------------+-------------------+
| `ADP_Stopped_FIQ`               | `0x20007`       |
+-----------------------------------+-------------------+
The following table shows reason codes relating to software events:


+-------------------------------------+-------------------+
| Name                                | Hexadecimal value |
+-------------------------------------+-------------------+
| `ADP_Stopped_BreakPoint`          | `0x20020`       |
+-------------------------------------+-------------------+
| `ADP_Stopped_WatchPoint`          | `0x20021`       |
+-------------------------------------+-------------------+
| `ADP_Stopped_StepComplete`        | `0x20022`       |
+-------------------------------------+-------------------+
| `ADP_Stopped_RunTimeErrorUnknown` | `0x20023`       |
+-------------------------------------+-------------------+
| `ADP_Stopped_InternalError`       | `0x20024`       |
+-------------------------------------+-------------------+
| `ADP_Stopped_UserInterruption`    | `0x20025`       |
+-------------------------------------+-------------------+
| `ADP_Stopped_ApplicationExit`     | `0x20026`       |
+-------------------------------------+-------------------+
| `ADP_Stopped_StackOverflow`       | `0x20027`       |
+-------------------------------------+-------------------+
| `ADP_Stopped_DivisionByZero`      | `0x20028`       |
+-------------------------------------+-------------------+
| `ADP_Stopped_OSSpecific`          | `0x20029`       |
+-------------------------------------+-------------------+

#### Entry (64-bit)


On entry, the PARAMETER REGISTER contains a pointer to a two-field argument block:

**field 1**
    The exception type, which is one of the set of reason codes in the above tables.

**field 2**
    A subcode, whose meaning depends on the reason code in field 1.

In particular, if field 1 is `ADP_Stopped_ApplicationExit` then field 2 is an exit status code, as passed to the C standard library `exit()` function. A simulator receiving this request must notify a connected debugger, if present, and then exit with the specified status.


#### Return


No return is expected from these calls. However, it is possible for the debugger to request that the application continues by performing an `RDI_Execute` request or equivalent. In this case, execution continues with the registers as they were on entry to the operation, or as subsequently modified by the debugger.

- SYS_EXIT_EXTENDED (0x20)
