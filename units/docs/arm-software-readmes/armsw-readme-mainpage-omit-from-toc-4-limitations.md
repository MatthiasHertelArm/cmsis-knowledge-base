---
id: "armsw-readme-mainpage-omit-from-toc-4-limitations"
type: "concept"
domain: "optimization"
title: "README {#mainpage} <!-- omit from toc -->: 4 Limitations"
summary: "README {#mainpage} <!-- omit from toc -->: 4 Limitations"
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/Arm-2D@3dd16b2:README.md"
doc_source: "https://github.com/ARM-software/Arm-2D/blob/3dd16b2/README.md#4-limitations"
license: "Apache-2.0"
mode: "V"
---

### 4.1 The Generic Limitations

- The library focuses on Cortex-M processors and is also available for other platforms, e.g. Cortex-A processors and other 32/64 bit architectures.
- The library supports the following compilers:
  - Arm Compiler 5 (**Deprecated**)
  - Arm Compiler 6
  - GCC
  - LLVM
  - IAR
- The library focus on **Accelerating Low Level Pixel Processing**
  - In principle, the library will **NOT** provide APIs for content creation, such as drawing shapes, text display, etc., but simple point drawing and colour-filling APIs.
    - We provides demos to illustrate how to draw basic shapes using User-Defined-OPCODE.
  - In principle, the library will **NOT** provide a ready-to-use element tree, or GUI message handling, but some meta data structrues that homebrew GUI developers can use directly(or take as references). 

### 4.2 The Temporary Limitations

- The library currently only provides default software algorithms in C and a **[Helium](https://developer.arm.com/architectures/instruction-sets/simd-isas/helium) based acceleration library**.
- Most of the example projects are created in MDK.
