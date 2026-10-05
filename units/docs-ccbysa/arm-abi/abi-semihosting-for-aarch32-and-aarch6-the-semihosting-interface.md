---
id: "abi-semihosting-for-aarch32-and-aarch6-the-semihosting-interface"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: The semihosting interface"
summary: "Semihosting is supported for ARM A and R profiles using the A64, A32, and T32 instruction sets, and for M profile using the T32 instruction set."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

Semihosting is supported for ARM A and R profiles using the A64, A32, and T32 instruction sets, and for M profile using the T32 instruction set.

Semihosting operations are requested using a trap instruction, which is a software instruction that generates exceptions from program control. Semihosting callers issue trap instructions, and the semihosting implementation then handles the resulting exception to perform the required semihosting operation. The trap instruction can be `SVC`, `HLT`, or `BKPT`, as indicated in the `Semihosting Trap Instructions and Encodings` table:


+---------------+-----------------+-------------------+----------------+
| Profile       | Instruction Set |   Instruction     |  Opcode        |
+===============+=================+===================+================+
| A+R Profile   | A64             | `HLT #0xF000`   | `0xD45E0000` |
|               +-----------------+-------------------+----------------+
|               | A32             | `SVC #0x123456` | `0xEF123456` |
|               |                 +-------------------+----------------+
|               |                 | `HLT #0xF000`   | `0xE10F0070` |
|               +-----------------+-------------------+----------------+
|               | T32             | `SVC #0xAB`     | `0xDFAB`     |
|               |                 +-------------------+----------------+
|               |                 | `HLT #0x3C`     | `0xBABC`     |
+---------------+-----------------+-------------------+----------------+
| M--Profile    | T32             | `BKPT #0xAB`    | `0xBEAB`     |
+---------------+-----------------+-------------------+----------------+
For A32 and T32 on A+R Profile, semihosting can use either an `SVC` or an `HLT` trap instruction. Semihosting implementations must support both trap instructions across all versions of the ARM architecture.


**Note:** This requirement includes supporting the `HLT` encodings on ARMv7 and earlier processors, even though `HLT` is only defined as an instruction in ARMv8. This may require the semihosting implementation to trap the `UNDEF` exception.

The `HLT` encodings are new in version 2.0 of the semihosting specification. Where possible, have semihosting callers continue to use the previously existing trap instructions to ensure compatibility with legacy semihosting implementations. These trap instructions are `HLT` for A64, `SVC` on A+R profile A32 or T32, and `BKPT` on M profile. However, it is necessary to change from SVC to HLT instructions to support AArch32 semihosting properly in a mixed AArch32/AArch64 system.


**Note:** ARM encourages semihosting callers to implement support for trapping using `HLT` on A32 and T32 as a configurable option. ARM strongly discourages semihosting callers from mixing the `HLT` and `SVC` mechanisms within the same executable.

The OPERATION NUMBER REGISTER must contain the number of the semihosting operation to be performed. This number is given in parentheses after the operation name in the following sections. For example, SYS_OPEN (0x01).

Parameters are passed to the operation using the
PARAMETER REGISTER. For most operations, the PARAMETER REGISTER must contain a pointer to a data block that holds the parameters. In some cases a single parameter is passed directly in the PARAMETER REGISTER, or no parameters are passed at all.

Results are returned in the RETURN REGISTER, either as an explicit return value or as a pointer to a data block. If no result is returned, assume that the RETURN REGISTER is corrupted. Some operations also return information in the PARAMETER REGISTER.

Multi-byte values in memory must be formatted as pure little-endian or pure big-endian to match the endianness mapping configuration of the processor.

The `Registers and field size` table shows the specific registers that are used, and the size of the fields in the data block, which depend on whether the caller is 32-bit or 64-bit.


+---------------------------+---------+---------+
|                           | 32-bit  | 64-bit  |
+===========================+=========+=========+
| OPERATION NUMBER REGISTER | `R0`  | `W0`  |
+---------------------------+---------+---------+
| PARAMETER REGISTER        | `R1`  | `X1`  |
+---------------------------+---------+---------+
| RETURN REGISTER           | `R0`  | `X0`  |
+---------------------------+---------+---------+
| Data block field size     | 32 bits | 64 bits |
+---------------------------+---------+---------+

**Note:** The operation number is passed in `W0` for the 64-bit ABI, which is the bottom 32 bits of the 64-bit register `X0`. Semihosting implementations must not assume that the top 32 bits of `X0` are 0.

A few semihosting operations have other differences between the 32-bit and 64-bit versions. These differences are described in the documentation of those operations.

The available semihosting operation numbers are allocated as follows:

`0x00-0x31`
    Used by ARM.
`0x32-0xFF`
    Reserved for future use by ARM.
`0x100-0x1FF`
    Reserved for user applications. These semihosting operation numbers are not used by ARM. However if you are writing your own `SVC` operations, you are advised to use a different `SVC` number, rather than using the semihosted `SVC` number and these operation type numbers.
`0x200-0xFFFFFFFF`
    Undefined and currently unused. ARM recommends that you do not use these semihosting operation numbers.


**Note:** Previous versions of the semihosting specification included the operation numbers `0x17` (`angel_SWIreason_EnterSVC`) and `0x19` (`angelSWI_Reason_SyncCacheRange`). These semihosting operation numbers are now reserved, and are not to be used or implemented.


### Related information


  - [A32 and T32 instruction sets](https://developer.arm.com/docs/dui0801/latest/overview-of-the-arm-architecture/a32-and-t32-instruction-sets)

  - [A64 instruction set](https://developer.arm.com/docs/dui0801/latest/overview-of-the-arm-architecture/a64-instruction-set)
