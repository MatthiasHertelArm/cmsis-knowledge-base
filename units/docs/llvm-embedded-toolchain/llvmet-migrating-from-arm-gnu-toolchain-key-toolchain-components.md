---
id: "llvmet-migrating-from-arm-gnu-toolchain-key-toolchain-components"
type: "concept"
domain: "project"
title: "Migrating from Arm GNU Toolchain: Key toolchain components"
summary: "Migrating from Arm GNU Toolchain: Key toolchain components"
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/migrating.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/migrating.md#key-toolchain-components"
license: "Apache-2.0"
mode: "V"
---

|Component|GNU toolchain (`arm-none-eabi-`)|LLVM toolchain|
|---------|-------------|--------------|
|C, C++ compiler​|`gcc`, `g++`|`clang`, `clang++`​|​
|Assembler​|`as`​|`clang` integrated assembler​|
|Linker​|`ld`​|`lld`​|
|Binutils​|`objdump`, `readelf`, ...|`llvm-objdump`, `llvm-readelf`, ...|
|Compiler runtime library​|`libgcc​`|`compiler-rt`​|
|Unwinder​|`libgcc`​|`libunwind`​|
|C standard library​|`newlib`, `newlib-nano`|`picolibc`|​
|C++ ABI library​|`libsupc++.a`|`libc++abi`​|​
|C++ standard library​|`libstdc++​`|`libc++`​|
