---
id: "alp-asm-coding-register-usage-and-the-arm-pro"
type: "concept"
domain: "project"
title: "Write Arm Assembler functions: Writing assembly functions: Register usage and the Arm Procedure Call Standard"
summary: "There are certain register use conventions which must be followed for the assembly code to coexist with the C code."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/asm/coding.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/asm/coding/#register-usage-and-the-arm-procedure-call-standard"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are certain register use conventions which must be followed for the assembly code to coexist with the C code.

### Calling functions and passing arguments

When a function calls a subroutine, it places the return address in the link register `lr`. The arguments (if any) are passed in registers `r0-r3`, starting with `r0`.

If there are more than four arguments, or they are too large to fit in the 32-bit registers, they are passed on the stack.

### Temporary storage

Registers `r0-r3` and `r12` can be used for temporary storage if they were not used for arguments, or if the argument value is no longer needed. These registers are corruptible by the subroutine.

### Preserved registers

Registers `r4-r11` must be preserved by a subroutine. If any must be used, they must be saved before use, and restored before returning. This is typically done by pushing them to, and popping from, the stack.

### Returning from subroutines

Because the return address has been stored in the link register, the `BX lr` instruction will reload the `pc` with the return address value from the `lr`. If the function returns a value, it will be passed through register `r0`.
