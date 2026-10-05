---
id: "alp-armds-build-understanding-the-compiler-opt"
type: "concept"
domain: "project"
title: "Get started with Arm Development Studio: Import and build example project: Understanding the compiler options"
summary: "If invoking the compiler directly, a minimal set of compiler options are needed, specifying whether or not you are compiling for  AArch32 (--target=arm-arm-none-eabi) or  AArch64 (--target=arm64-arm-none-eabi) targets."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/armds/build.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/armds/build/#understanding-the-compiler-options"
license: "CC-BY-SA-4.0"
mode: "V"
---

If invoking the compiler directly, a minimal set of compiler options are needed, specifying whether or not you are compiling for
* AArch32 (`--target=arm-arm-none-eabi`) or
* AArch64 (`--target=arm64-arm-none-eabi`) targets.

You must also specify a specific Arm Architecture (`-march`) or processor (`-mcpu`).

Use the list option (`-march=list` or `-mcpu=list`) to see all valid arguments for these options. For example:

```console
armclang --target=arm-arm-none-eabi -mcpu=list
```

Full details of available command line options are given in the [Arm Compiler for Embedded Reference Guide](https://developer.arm.com/documentation/101754/latest/armclang-Reference/armclang-Command-line-Options).
