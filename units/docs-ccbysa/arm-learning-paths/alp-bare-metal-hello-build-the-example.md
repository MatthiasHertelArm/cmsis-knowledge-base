---
id: "alp-bare-metal-hello-build-the-example"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create and build a Hello World example project: Build the example"
summary: "This command invokes the compiler to compile hello.c for the Armv8-A architecture and generate an ELF object file hello.o:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/hello.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/hello/#build-the-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

This command invokes the compiler to compile `hello.c` for the Armv8-A architecture and generate an ELF object file `hello.o`:

```console
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a hello.c
```

### Understanding the command line

The options used in this command are:
- `-c` tells the compiler to stop after compiling to object code. The link step to create the final executable will be performed later.
- `-g` tells the compiler to include debug information in the image.
- `--target=aarch64-arm-none-eabi` tells the compiler to target `AArch64` code (rather than `AArch32`).
- `-march=armv8-a` explicitly selects the architecture version. Alternatively you can specify a particular processor with `-mcpu`.
