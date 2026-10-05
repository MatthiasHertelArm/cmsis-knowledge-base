---
id: "abi-procedure-call-standard-for-the-ar-parameter-passing"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: The Base Procedure Call Standard / Parameter Passing"
summary: "Part of: The Base Procedure Call Standard"
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Base Procedure Call Standard_

The base standard provides for passing arguments in core registers (r0-r3)
and on the stack.  For subroutines that take a small number of parameters,
only registers are used, greatly reducing the overhead of a call.

Parameter passing is defined as a two-level conceptual model

*  A mapping from a source language argument onto a machine type

*  The marshalling of machine types to produce the final parameter list

The mapping from the source language onto the machine type is specific for
each language and is described separately (the C and C++ language bindings
are described in Arm C and C++ Language Mappings). The result is an ordered list of
arguments that are to be passed to the subroutine.

In the following description there are assumed to be a number of
co-processors available for passing and receiving arguments.  The
co-processor registers are divided into different classes.  An argument may
be a candidate for at most one co-processor register class.  An argument
that is suitable for allocation to a co-processor register is known as a
Co-processor Register Candidate (CPRC).

In the base standard there are no arguments that are candidates for a
co-processor register class.

A variadic function is always marshaled as for the base standard.

For a caller, sufficient stack space to hold stacked arguments is assumed to
have been allocated prior to marshaling: in practice the amount of stack
space required cannot be known until after the argument marshalling has been
completed.  A callee can modify any stack space used for receiving parameter
values from the caller.

When a Composite Type argument is assigned to core registers (either fully
or partially), the behavior is as if the argument had been stored to memory
at a word-aligned (4-byte) address and then loaded into consecutive
registers using a suitable load-multiple instruction.

This stage is performed exactly once, before processing of the arguments
commences.


+-------------------------+-------------------------------------------------------------------------+
| .. _Rule A.1:           | The Next Core Register Number (NCRN) is set to r0.                      |
|                         |                                                                         |
| A.1                     |                                                                         |
+-------------------------+-------------------------------------------------------------------------+
| .. _Rule A.2.cp:        | `Co-processor argument register initialization is performed.` |
|                         |                                                                         |
| `A.2.cp`      |                                                                         |
+-------------------------+-------------------------------------------------------------------------+
| .. _Rule A.3:           | The next stacked argument address (NSAA) is set to the current          |
|                         | stack-pointer value (SP).                                               |
| A.3                     |                                                                         |
+-------------------------+-------------------------------------------------------------------------+
| .. _Rule A.4:           | If the subroutine is a function that returns a result in                |
|                         | memory, then the address for the result is placed in r0 and             |
| A.4                     | the NCRN is set to r1.                                                  |
+-------------------------+-------------------------------------------------------------------------+
For each argument in the list the first matching rule from the following
list is applied.


+-------------------------+--------------------------------------------------------------------------+
| .. _Rule B.1:           | If the argument is a Composite Type whose size cannot be                 |
|                         | statically determined by both the caller and callee, the                 |
| B.1                     | argument is copied to memory and the argument is replaced by a           |
|                         | pointer to the copy.                                                     |
+-------------------------+--------------------------------------------------------------------------+
| .. _Rule B.2:           | If the argument is an integral Fundamental Data Type that is             |
|                         | smaller than a word, then it is zero- or sign-extended to a              |
| B.2                     | full word and its size is set to 4 bytes. If the argument is a           |
|                         | Half-precision Floating Point Type its size is set to 4 bytes            |
|                         | as if it had been copied to the least significant bits of a              |
|                         | 32-bit register and the remaining bits filled with unspecified           |
|                         | values.                                                                  |
+-------------------------+--------------------------------------------------------------------------+
| .. _Rule B.3.cp:        | :emphasis:`If the argument is a CPRC then any preparation rules for that |
|                         | co-processor register class are applied.`                                |
| `B.3.cp`      |                                                                          |
+-------------------------+--------------------------------------------------------------------------+
| .. _Rule B.4:           | If the argument is a Composite Type whose size is not a                  |
|                         | multiple of 4 bytes, then its size is rounded up to the                  |
| B.4                     | nearest multiple of 4.                                                   |
+-------------------------+--------------------------------------------------------------------------+
| .. _Rule B.5:           | If the argument is an alignment adjusted type its value is               |
|                         | passed as a copy of the actual value. The copy will have an              |
| B.5                     | alignment defined as follows.                                            |
|                         |                                                                          |
|                         | *  For a Fundamental Data Type, the alignment is the natural             |
|                         |    alignment of that type, after any promotions.                         |
|                         |                                                                          |
|                         | *  For a Composite Type, the alignment of the copy will have             |
|                         |    4-byte alignment if its natural alignment is ≤ 4 and 8-byte           |
|                         |    alignment if its natural alignment is ≥ 8                             |
|                         |                                                                          |
|                         | The alignment of the copy is used for applying marshaling                |
|                         | rules.                                                                   |
+-------------------------+--------------------------------------------------------------------------+
For each argument in the list the following rules are applied in turn until the
argument has been allocated.


+-------------------------+-------------------------------------------------------------------------+
| .. _Rule C.1.cp:        | :emphasis:`If the argument is a CPRC and there are sufficient           |
|                         | unallocated co-processor registers of the appropriate class,            |
| `C.1.cp`      | the argument is allocated to co-processor registers.`                   |
+-------------------------+-------------------------------------------------------------------------+
| .. _Rule C.2.cp:        | :emphasis:`If the argument is a CPRC then any co-processor registers in |
|                         | that class that are unallocated are marked as unavailable.              |
| `C.2.cp`      | The NSAA is adjusted upwards until it is correctly aligned for          |
|                         | the argument and the argument is copied to the memory at the            |
|                         | adjusted NSAA.  The NSAA is further incremented by the size of          |
|                         | the argument.  The argument has now been allocated.`                    |
+-------------------------+-------------------------------------------------------------------------+
| .. _Rule C.3:           | If the argument requires double-word alignment (8-byte), the            |
|                         | NCRN is rounded up to the next even register number.                    |
| C.3                     |                                                                         |
+-------------------------+-------------------------------------------------------------------------+
| .. _Rule C.4:           | If the size in words of the argument is not more than r4 minus          |
|                         | NCRN, the argument is copied into core registers, starting at           |
| C.4                     | the NCRN. The NCRN is incremented by the number of registers            |
|                         | used.  Successive registers hold the parts of the argument              |
|                         | they would hold if its value were loaded into those registers           |
|                         | from memory using an LDM instruction. The argument has now              |
|                         | been allocated.                                                         |
+-------------------------+-------------------------------------------------------------------------+
| .. _Rule C.5:           | If the NCRN is less than r4 and the NSAA is equal to the SP,            |
|                         | the argument is split between core registers and the stack.             |
| C.5                     | The first part of the argument is copied into the core                  |
|                         | registers starting at the NCRN up to and including r3.  The             |
|                         | remainder of the argument is copied onto the stack, starting            |
|                         | at the NSAA.  The NCRN is set to r4 and the NSAA is                     |
|                         | incremented by the size of the argument minus the amount                |
|                         | passed in registers.  The argument has now been allocated.              |
+-------------------------+-------------------------------------------------------------------------+
| .. _Rule C.6:           | The NCRN is set to r4.                                                  |
|                         |                                                                         |
| C.6                     |                                                                         |
+-------------------------+-------------------------------------------------------------------------+
| .. _Rule C.7:           | If the argument required double-word alignment (8-byte), then           |
|                         | the NSAA is rounded up to the next double-word address.                 |
| C.7                     |                                                                         |
+-------------------------+-------------------------------------------------------------------------+
| .. _Rule C.8:           | The argument is copied to memory at the NSAA.  The NSAA is              |
|                         | incremented by the size of the argument.                                |
| C.8                     |                                                                         |
+-------------------------+-------------------------------------------------------------------------+
It should be noted that the above algorithm makes provision for languages
other than C and C++ in that it provides for passing arrays by value and for
passing arguments of dynamic size.  The rules are defined in a way that
allows the caller to be always able to statically determine the amount of
stack space that must be allocated for arguments that are not passed in
registers, even if the function is variadic.

Several further observations can also be made:

*  The initial stack slot address is the value of the stack pointer that
   will be passed to the subroutine. It may therefore be necessary to run
   through the above algorithm twice during compilation, once to determine
   the amount of stack space required for arguments and a second time to
   assign final stack slot addresses.

*  A double-word aligned type will always start in an even-numbered core
   register, or at a double-word aligned address on the stack even if it is
   not the first member of an aggregate.

*  Arguments are allocated first to registers and only excess arguments are
   placed on the stack.

*  Arguments that are Fundamental Data Types can either be entirely in
   registers or entirely on the stack.

*  At most one argument can be split between registers and memory according
   to `Rule C.5`.

*  CPRCs may be allocated to co-processor registers or the stack – they may
   never be allocated to core registers.

*  Since an argument may be a candidate for at most one class of
   co-processor register, then the rules for multiple co-processors (should
   they be present) may be applied in any order without affecting the
   behavior.

*  An argument may only be split between core registers and the stack if all
   preceding CPRCs have been allocated to co-processor registers.
