---
id: "abi-procedure-call-standard-for-the-ar-machine-registers"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: The Base Procedure Call Standard / Machine Registers"
summary: "Part of: The Base Procedure Call Standard"
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Base Procedure Call Standard_

The Arm architecture defines a core instruction set plus a number of
additional instructions implemented by co-processors.  The core instruction
set can access the core registers and co-processors can provide additional
registers which are available for specific operations.


#### Core registers


There are 16, 32-bit core (integer) registers visible to the Arm and Thumb
instruction sets. These are labeled r0-r15 or R0-R15. Register names may
appear in assembly language in either upper case or lower case. In this
specification upper case is used when the register has a fixed role in the
procedure call standard. The following table summarizes the uses of the
core registers in this standard.  In addition to the core registers there is
one status register (CPSR) that is available for use in conforming code.


+----------+---------+---------+-----------------------------------------+
| Register | Synonym | Special | Role in the procedure call standard     |
+==========+=========+=========+=========================================+
| r15      |         | PC      | The Program Counter.                    |
+----------+---------+---------+-----------------------------------------+
| r14      |         | LR      | The Link Register.                      |
+----------+---------+---------+-----------------------------------------+
| r13      |         | SP      | The Stack Pointer.                      |
+----------+---------+---------+-----------------------------------------+
| r12      |         | IP      | The Intra-Procedure-call scratch        |
|          |         |         | register.                               |
+----------+---------+---------+-----------------------------------------+
| r11      | v8      | FP      | Frame Pointer or Variable-register 8.   |
+----------+---------+---------+-----------------------------------------+
| r10      | v7      |         | Variable-register 7.                    |
+----------+---------+---------+-----------------------------------------+
| r9       | v6      | SB      | Platform register or Variable-register  |
|          |         |         | 6.                                      |
|          |         | TR      |                                         |
|          |         |         | The meaning of this register is defined |
|          |         |         | by the platform standard.               |
+----------+---------+---------+-----------------------------------------+
| r8       | v5      |         | Variable-register 5.                    |
+----------+---------+---------+-----------------------------------------+
| r7       | v4      |         | Variable-register 4.                    |
+----------+---------+---------+-----------------------------------------+
| r6       | v3      |         | Variable-register 3.                    |
+----------+---------+---------+-----------------------------------------+
| r5       | v2      |         | Variable-register 2.                    |
+----------+---------+---------+-----------------------------------------+
| r4       | v1      |         | Variable-register 1.                    |
+----------+---------+---------+-----------------------------------------+
| r3       | a4      |         | Argument / scratch register 4.          |
+----------+---------+---------+-----------------------------------------+
| r2       | a3      |         | Argument / scratch register 3.          |
+----------+---------+---------+-----------------------------------------+
| r1       | a2      |         | Argument / result / scratch register 2. |
+----------+---------+---------+-----------------------------------------+
| r0       | a1      |         | Argument / result / scratch register 1. |
+----------+---------+---------+-----------------------------------------+
The first four registers r0-r3 (a1-a4) are used to pass argument values into
a subroutine and to return a result value from a function. They may also be
used to hold intermediate values within a routine (but, in general, only
`between` subroutine calls).

Register r12 (IP) may be used by a linker as a scratch register between a
routine and any subroutine it calls (for details, see
Use of IP by the linker). It can also be used within a routine to hold
intermediate values between subroutine calls.

In some variants r11 (FP) may be used as a frame pointer in order to
chain frame activation records into a linked list.

The role of register r9 is platform specific. A virtual platform may assign
any role to this register and must document this usage. For example, it may
designate it as the static base (SB) in a position-independent data model,
or it may designate it as the thread register (TR) in an environment with
thread-local storage.  The usage of this register may require that the value
held is persistent across all calls. A virtual platform that has no need for
such a special register may designate r9 as an additional callee-saved
variable register, v6.

Typically, the registers r4-r8, r10 and r11 (v1-v5, v7 and v8) are used to
hold the values of a routine’s local variables. Of these, only v1-v4 can be
used uniformly by the whole Thumb instruction set, but the AAPCS does not
require that Thumb code only use those registers.

A subroutine must preserve the contents of the registers r4-r8, r10, r11 and
SP (and r9 in PCS variants that designate r9 as v6).

In all variants of the procedure call standard, registers r12-r15 have
special roles. In these roles they are labeled IP, SP, LR and PC.

The CPSR is a global register with the following properties:

*  The N, Z, C, V and Q bits (bits 27-31) and the GE[3:0] bits (bits 16-19)
   are undefined on entry to or return from a public interface.  The Q and
   GE[3:0] bits may only be modified when executing on a processor where
   these features are present.

*  On Arm Architecture 6, the E bit (bit 8) can be used in applications
   executing in little-endian mode, or in big-endian-8 mode to temporarily
   change the endianness of data accesses to memory.  An application must
   have a designated endianness and at entry to and return from any public
   interface the setting of the E bit must match the designated endianness
   of the application.

*  The T bit (bit 5) and the J bit (bit 24) are the execution state bits.
   Only instructions designated for modifying these bits may change them.

*  The A, I, F and M[4:0] bits (bits 0-7) are the privileged bits and may
   only be modified by applications designed to operate explicitly in a
   privileged mode.

*  All other bits are reserved and must not be modified.  It is not defined
   whether the bits read as zero or one, or whether they are preserved across
   a public interface.


##### Handling values larger than 32 bits


Fundamental types larger than 32 bits may be passed as parameters to, or
returned as the result of, function calls.  When these types are in core
registers the following rules apply:

*  A double-word sized type is passed in two consecutive registers (e.g., r0
   and r1, or r2 and r3).  The content of the registers is as if the value
   had been loaded from memory representation with a single `LDM`
   instruction.

*  A 128-bit containerized vector is passed in four consecutive registers.
   The content of the registers is as if the value had been loaded from
   memory with a single `LDM` instruction.


#### Co-processor Registers


A machine’s register set may be extended with additional registers that are
accessed via instructions in the co-processor instruction space.  To the
extent that such registers are not used for passing arguments to and from
subroutine calls the use of co-processor registers is compatible with the
base standard.  Each co-processor may provide an additional set of rules
that govern the usage of its registers.


**Note:** Even though co-processor registers are not used for passing arguments, some elements of the run-time support for a language may require knowledge of all co-processors in use in an application in order to function correctly (for example, `setjmp()` in C and exceptions in C++).


##### VFP register usage conventions


The VFP-v2 co-processor has 32 single-precision registers, s0-s31, which may
also be accessed as 16 double-precision registers, d0-d15 (with d0
overlapping s0, s1; d1 overlapping s2, s3; etc). In addition there are 3 or
more system registers, depending on the implementation. VFP-v3 adds 16 more
double-precision registers d16-d31, but there are no additional
single-precision counterparts. The Advanced SIMD Extension and the M-profile
vector Extension (MVE) use the VFP register set. The Advanced SIMD Extension
uses the double-precision registers for 64-bit vectors and further defines
quad-word registers (with q0 overlapping d0, d1; and q1 overlapping d2, d3;
etc) for 128-bit vectors. MVE uses 128-bit vectors in the same quad-word
registers.

Registers s16-s31 (d8-d15, q4-q7) must be preserved across subroutine calls;
registers s0-s15 (d0-d7, q0-q3) do not need to be preserved (and can be used
for passing arguments or returning results in standard procedure-call
variants). Registers d16-d31 (q8-q15), if present, do not need to be
preserved.

The FPSCR and VPR registers are the only status registers that may be accessed
by conforming code. FPSCR is a global register with the following properties:

*  The condition code bits (28-31), the cumulative saturation (QC) bit (27)
   and the cumulative exception-status bits (0-4 and 7) are not preserved
   across a public interface.

*  The exception-control bits (8-12 and 15), rounding mode bits (22-23) and
   flush-to-zero bits (24) may be modified by calls to specific support
   functions that affect the global state of the application.

*  The length bits (16-18) must be 0b100 when using M-profile Vector Extension,
   0b000 when using VFP vector mode and otherwise preserved across a public
   interface.

*  The stride bits (20-21) must be zero on entry to and return from a public
   interface.

*  All other bits are reserved and must not be modified.  It is not defined
   whether the bits read as zero or one, or whether they are preserved
   across a public interface.

VPR is a global register with the following properties:

*  The VPT mask bits (16-23) must be zero on entry to and return from a public
   interface.

*  The predication bits (0-15) are not preserved across a public interface.

*  All other bits are reserved and must not be modified. It is not defined
   whether the bits read as zero or one, or whether they are preserved across
   a public interface.
