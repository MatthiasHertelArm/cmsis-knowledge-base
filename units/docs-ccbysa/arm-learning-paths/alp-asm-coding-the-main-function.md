---
id: "alp-asm-coding-the-main-function"
type: "concept"
domain: "project"
title: "Write Arm Assembler functions: Writing assembly functions: The main function"
summary: "Create the main C function. This function creates two character arrays, a and b, and calls two functions, my_strcpy and my_capitalize, that shall be implemented later."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/asm/coding.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/asm/coding/#the-main-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create the `main` C function. This function creates two character arrays, `a` and `b`, and calls two functions, `my_strcpy` and `my_capitalize`, that shall be implemented later.

```C
void my_strcpy(const char *src, char *dst);
void my_capitalize(char *str);

int main(void)
{
    const char a[] = "Hello world!";
    char b[20];

    my_strcpy(a, b);
    my_capitalize(b);

    return 0;
}
```
