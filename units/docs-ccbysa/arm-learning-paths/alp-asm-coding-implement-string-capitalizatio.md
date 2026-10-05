---
id: "alp-asm-coding-implement-string-capitalizatio"
type: "concept"
domain: "project"
title: "Write Arm Assembler functions: Writing assembly functions: Implement string-capitalization function"
summary: "You can implement a function to capitalize all the lower-case letters in the string. The function will load each character, check to see if it is a lower-case ASCII letter, and if so, capitalize it."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/asm/coding.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/asm/coding/#implement-string-capitalization-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can implement a function to capitalize all the lower-case letters in the string. The function will load each character, check to see if it is a lower-case `ASCII` letter, and if so, capitalize it. 

Each character in the string is represented with its ASCII code. For example, `A` is represented with a 65 (0x41), `B` with 66 (0x42), and so on up to `Z` which uses 90 (0x5a). The lower case letters start at `a` (97, or 0x61) and end with `z` (122, or 0x7a). Convert a lower case letter to upper case by subtracting 32 (0x20).

```C
__attribute__((naked)) void my_capitalize(char *str)
{
    __asm(
        "cap_loop:             \n\t\
            LDRB  r1, [r0]     \n\t\
            CMP   r1, #'a'-1   \n\t\
            BLS   cap_skip     \n\t\
            CMP   r1, #'z'     \n\t\
            BHI   cap_skip     \n\t\
            SUBS  r1,#32       \n\t\
            STRB  r1, [r0]     \n\t\
        cap_skip:              \n\t\
            ADDS  r0, r0, #1   \n\t\
            CMP   r1, #0       \n\t\
            BNE   cap_loop     \n\t\
            BX    lr           \n\t\
        "    
    );
}
```
The code loads the first byte into `r1`. If the value is less than `a` the code immediately proceeds to the next loop iteration. 

Note the first `CMP` instruction compares `r1` against the character immediately before `a` in the table. There is no `lower than` condition, just `lower or same` (LS).

To use the conditional `BLS` branch instruction, reduce by one the value `r1` is compared against.
