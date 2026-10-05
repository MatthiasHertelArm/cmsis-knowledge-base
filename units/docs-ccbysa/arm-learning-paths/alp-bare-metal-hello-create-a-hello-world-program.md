---
id: "alp-bare-metal-hello-create-a-hello-world-program"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create and build a Hello World example project: Create a \"Hello World!\" program"
summary: "Start with a simple C program, and use the armclang compiler and armlink linker tools to compile and generate an executable image."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/hello.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/hello/#create-a-hello-world-program"
license: "CC-BY-SA-4.0"
mode: "V"
---

Start with a simple C program, and use the `armclang` compiler and `armlink` linker tools to compile and generate an executable image.

Use your favorite editor to create a new source file called `hello.c` with the following contents:

```C
#include <stdio.h>

int main(void) {
  printf("Hello World!\n");
  return 0;
}
```
