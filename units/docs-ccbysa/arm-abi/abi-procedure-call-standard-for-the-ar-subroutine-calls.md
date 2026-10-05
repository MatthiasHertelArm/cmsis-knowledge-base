---
id: "abi-procedure-call-standard-for-the-ar-subroutine-calls"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: The Base Procedure Call Standard / Subroutine Calls"
summary: "Part of: The Base Procedure Call Standard"
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Base Procedure Call Standard_

Both the Arm and Thumb instruction sets contain a primitive subroutine call
instruction, BL, which performs a branch-with-link operation.  The effect of
executing BL is to transfer the sequentially next value of the program
counter – the **return** address – into the link register (LR) and the
destination address into the program counter (PC). Bit 0 of the link
register will be set to 1 if the BL instruction was executed from Thumb
state, and to 0 if executed from Arm state. The result is to transfer
control to the destination address, passing the return address in LR as an
additional parameter to the called subroutine.

Control is returned to the instruction following the BL when the return
address is loaded back into the PC (see Interworking).

A subroutine call can be synthesized by any instruction sequence that has
the effect:

```

   LR[31:1] ← return address
   LR[0]    ← code type at return address (0 Arm, 1 Thumb)
   PC       ← subroutine address
   ...
return address:
```
For example, in Arm-state, to call a subroutine addressed by r4 with control
returning to the following instruction, do

```asm

MOV  LR, PC
BX   r4
...
```

**Note:** The equivalent sequence will not work from Thumb state because the instruction that sets LR does not copy the Thumb-state bit to LR[0].

In Arm Architecture v5 both Arm and Thumb state provide a BLX instruction
that will call a subroutine addressed by a register and correctly sets the
return address to the sequentially next value of the program counter.


#### Use of IP by the linker


Both the Arm- and Thumb-state BL instructions are unable to address the full
32-bit address space, so it may be necessary for the linker to insert a
veneer between the calling routine and the called subroutine.  Veneers may
also be needed to support Arm-Thumb inter-working or dynamic linking.  Any
veneer inserted must preserve the contents of all registers except IP (r12)
and the condition code flags; a conforming program must assume that a veneer
that alters IP may be inserted at any branch instruction that is exposed to
a relocation that supports inter-working or long branches.


**Note:** `R_ARM_CALL`, `R_ARM_JUMP24`, `R_ARM_PC24`, `R_ARM_THM_CALL`, `R_ARM_THM_JUMP24` and `R_ARM_THM_JUMP19` are examples of the ELF relocation types with this property.  See AAELF32_ for full details.

.. _Result Return (base PCS):
