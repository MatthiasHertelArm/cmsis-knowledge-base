---
id: "llvmet-experimental-newlib-support-using-pre-built-newlib-library-package"
type: "concept"
domain: "project"
title: "Experimental newlib support: Using pre-built `newlib` library package"
summary: "Experimental newlib support: Using pre-built `newlib` library package"
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/newlib.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/newlib.md#using-pre-built-newlib-library-package"
license: "Apache-2.0"
mode: "V"
---

1. Install LLVM Embedded Toolchain for Arm
1. Download corresponding `LLVM-ET-Arm-newlib-overlay` package
and extract it on top of the main toolchain folder.

    * Note: The overlay package copies all the `newlib` library variants into the
    `lib/clang-runtimes/newlib` subdirectory, so that they do not collide with
    the `picolibc` variants in `lib/clang-runtimes`.
    It also adds the `newlib.cfg` into the `bin` directory,
    which switches the `--sysroot` to the `newlib` subdirectory above. 

1. Add the `newlib.cfg` config file to the command line to use `newlib`
library variants instead of `picolibc`.
1. Add `-lrdimon` and `-lcrt0-rdimon` to the command line to use semihosting
or `-lnosys` and `-lcrt0-nosys` otherwise.
1. You may use the provided default linker script by adding `-T redboot.ld`
to the command line.

Example:
```
$ clang --config=newlib.cfg --target=arm-none-eabi -march=armv7m -T redboot.ld -lrdimon -lcrt0-rdimon -o hello hello.c
```
