---
id: "abi-procedure-call-standard-for-the-ar-interworking"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: The Base Procedure Call Standard / Interworking"
summary: "Part of: The Base Procedure Call Standard"
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Base Procedure Call Standard_

The AAPCS requires that all sub-routine call and return sequences support
inter-working between Arm and Thumb states.  The implications on compiling
for various Arm Architectures are as follows.

Calls via function pointers should use one of the following, as appropriate:

```asm

blx   Rm    ; For normal sub-routine calls
```
```asm

bx    Rm    ; For tail calls
```
Calls to functions that use `bl<cond>`, `b`, or `b<cond>`
will need a linker-generated veneer if a state change is required, so it may
sometimes be more efficient to use a sequence that permits use of an
unconditional `bl` instruction.

Return sequences may use load-multiple operations that directly load the PC
or a suitable `bx` instruction.

The following traditional return must not be used if inter-working might be
required.

```asm

mov   pc, Rm
```
In addition to the constraints for Arm v5, the following additional
restrictions apply to Arm v4T.

Calls using `bl` that involve a state change also require a
linker-generated stub.

Calls via function pointers must use a sequence equivalent to the Arm-state
code

```asm

mov   lr, pc
bx    Rm
```
However, this sequence does not work for Thumb state, so usually a
`bl` to a veneer that does the `bx` instruction must be used.

Return sequences must restore any saved registers and then use a `bx`
instruction to return to the caller.

The Arm v4 Architecture supports neither Thumb state nor the `bx`
instruction, therefore it is not strictly compatible with the AAPCS.

It is recommended that code for Arm v4 be compiled using Arm v4T
inter-working sequences but with all `bx` instructions subject to
relocation by an `R_ARM_V4BX` relocation [AAELF32_]. A
linker linking for Arm V4 can then change all instances of:

```asm

bx    Rm
```
Into:

```asm

mov   pc, Rm
```
But relocatable files remain compatible with this standard.
