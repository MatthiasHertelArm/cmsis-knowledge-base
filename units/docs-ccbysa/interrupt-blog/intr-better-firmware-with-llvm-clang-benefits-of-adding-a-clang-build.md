---
id: "intr-better-firmware-with-llvm-clang-benefits-of-adding-a-clang-build"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Benefits of Adding a Clang Build"
summary: "Many embedded projects use GCC, or one of other proprietary compilers such as IAR or the ARM Compiler. You do not have to stop using your current compiler for builds to start benefiting from LLVM/Clang."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#benefits-of-adding-a-clang-build"
license: "CC-BY-SA-4.0"
mode: "V"
---

Many embedded projects use GCC, or one of other proprietary compilers such as IAR or the ARM
Compiler. You _do not_ have to stop using your current compiler for builds to start benefiting from
LLVM/Clang.

Adding a Clang build target to your pre-existing project has the following benefits:

- Static analysis! (More on this in the following sections)
- Makes your codebase less dependent on a single compiler feature set and makes it easier to transition from one compiler to another in the future (for example, a proprietary one to a free one).
- Two sets of error flags is better than one. You can use both compilers `-Werror` equivalent to maximize the issues you
  find before needing to do any debug on target.
- By compiling with Clang, you are setting yourself up nicely for running unit tests and simulated
  builds on host platforms.
