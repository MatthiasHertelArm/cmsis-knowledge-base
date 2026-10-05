---
id: "abi-procedure-call-standard-for-the-ar-processes-memory-and-the-stack"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: The Base Procedure Call Standard / Processes, Memory and the Stack"
summary: "Part of: The Base Procedure Call Standard"
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Base Procedure Call Standard_

The AAPCS applies to a **single thread of execution** or
**process** (hereafter referred to as a process). A process has a
**program state** defined by the underlying machine registers and the
contents of the memory it can access. The memory a process can access,
without causing a run-time fault, may vary during the execution of the
process.

The memory of a process can normally be classified into five categories:

*  code (the program being executed), which must be readable, but need not
   be writable, by the process.

*  read-only static data.

*  writable static data.

*  the heap.

*  the stack.

Writable static data may be further sub-divided into initialized,
zero-initialized and uninitialized data. Except for the stack there is no
requirement for each class of memory to occupy a single contiguous region of
memory. A process must always have some code and a stack, but need not have
any of the other categories of memory.

The heap is an area (or areas) of memory that are managed by the process
itself (for example, with the C `malloc` function). It is typically used
for the creation of dynamic data objects.

A conforming program must only execute instructions that are in areas of
memory designated to contain code.


#### The Stack


The stack is a contiguous area of memory that may be used for storage of
local variables and for passing additional arguments to subroutines when
there are insufficient argument registers available.

The stack implementation is **full-descending**, with the current
extent of the stack held in the register SP (r13). The stack will, in
general, have both a **base** and a **limit** though in
practice an application may not be able to determine the value of either.

The stack may have a fixed size or be dynamically extendable (by adjusting
the stack-limit downwards).

The rules for maintenance of the stack are divided into two parts: a set of
constraints that must be observed at all times, and an additional constraint
that must be observed at a public interface.


##### Universal stack constraints


At all times the following basic constraints must hold:

*  Stack-limit ≤ SP ≤ stack-base. The stack pointer must lie within the
   extent of the stack.

*  SP mod 4 = 0. The stack must at all times be aligned to a word boundary.

*  A process may only store data in the closed interval of the entire stack
   delimited by [SP, stack base - 1] (where SP is the value of register r13).


**Note:** This implies that instructions of the following form can fail to satisfy the stack discipline constraints, even when `reg` points within the extent of the stack. .. code-block:: text ldmxx    reg, {..., sp, ...}             // reg != sp If execution of the instruction is interrupted after sp has been loaded, the stack extent will not be restored, so restarting the instruction might violate the third constraint.


##### Stack constraints at a public interface


The stack must also conform to the following constraint at a public
interface:

* SP mod 8 = 0. The stack must be double-word aligned.


##### Stack probing


In order to ensure stack integrity a process may emit stack probes immediately
prior to allocating additional stack space (moving SP from SP_old to SP_new).
Stack probes must be in the region of [SP_new, SP_old - 1] and may be either
read or write operations. The minimum interval for stack probing is defined by
the target platform but must be a minimum of 4KBytes. No recoverable data can
be saved below the currently allocated stack region.


##### The Frame Pointer


A platform may require the construction of a list of stack frames
describing the current call hierarchy in a program.

Each frame shall link to the frame of its caller by means of a Frame
Record of two 32-bit values on the stack.  The frame record for the
innermost frame (belonging to the most recent routine invocation)
shall be pointed to by the Frame Pointer register (FP).  The lowest
addressed word shall point to the previous frame record and the
highest addressed word shall contain the value passed in LR on entry
to the current function.  The end of the frame record chain is
indicated by the address zero in the address for the previous frame.
The location of the frame record within a stack frame is not
specified.  The frame pointer register must not be updated until the
new frame record has been fully constructed.


**Note:** There will always be a short period during construction or destruction of each frame record during which the frame pointer will point to the caller’s record.

A platform shall mandate the minimum level of conformance with respect
to the maintenance of frame records.  The options are, in decreasing
level of functionality:

- It may require the frame pointer to address a valid frame record at
  all times, except that small subroutines which do not modify the
  link register may elect not to create a frame record

- It may require the frame pointer to address a valid frame record at
  all times, except that any subroutine may elect not to create a
  frame record

- It may permit the frame pointer register to be used as a
  general-purpose callee-saved register, but provide a
  platform-specific mechanism for external agents to reliably locate
  the chain of frame records

- It may elect not to maintain a frame chain and to use the frame
  pointer register as a general-purpose callee-saved register.


**Note:** Unlike the APCS and its variants, the same frame pointer register is used for both the Arm and Thumb ISAs (including the Thumb-1 variant), this ensures that the frame chain can be constructed even when generating code that interworks between both the Arm and Thumb instruction sets.  It is expected that Thumb-1 code will rarely, if ever, want to create stack frames - the choice of a high register therefore ensures that such code can conform minimally to the requirements of having a valid value stored in the frame pointer register without noticably reducing the number of registers available to normal code. The AAPCS does not specify where, within a function's stack frame record, the frame chain data structure resides.  This permits implementors the freedom to use whatever location will result in the most efficient code needed to establish the frame chain record. As a result, even in Thumb-1, the overhead for establishing the frame will rarely exceed three additional instructions in the function entry sequence and two additional instructions in the return sequence.
