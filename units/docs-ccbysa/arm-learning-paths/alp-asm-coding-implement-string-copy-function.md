---
id: "alp-asm-coding-implement-string-copy-function"
type: "concept"
domain: "project"
title: "Write Arm Assembler functions: Writing assembly functions: Implement string-copy function"
summary: "The function my_strcpy has two arguments (src, dst). Each is a 32-bit long pointer to a character array."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/asm/coding.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/asm/coding/#implement-string-copy-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

The function `my_strcpy` has two arguments (`src`, `dst`). Each is a 32-bit long pointer to a character array. In this case, a pointer fits into a register, so argument `src` is passed through register `r0` and `dst` is passed through `r1`.

Our function will load a character from memory, save it into the destination pointer and increment both pointers until the end of the string.

```C
__attribute__((naked)) void my_strcpy(const char *src, char *dst)
{
    __asm(
        "loop:              \n\t\
            LDRB  r2, [r0]  \n\t\
            ADDS  r0, #1    \n\t\
            STRB  r2, [r1]  \n\t\
            ADDS  r1, #1    \n\t\
            CMP   r2, #0    \n\t\
            BNE   loop      \n\t\
            BX    lr        \n\t\
    "    
    );
}
```
Observe that `r0-r2` are corrupted by this function, and will contain different values when the function returns.
