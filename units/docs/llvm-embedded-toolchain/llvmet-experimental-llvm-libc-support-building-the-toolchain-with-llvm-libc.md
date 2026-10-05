---
id: "llvmet-experimental-llvm-libc-support-building-the-toolchain-with-llvm-libc"
type: "concept"
domain: "project"
title: "Experimental LLVM libc support: Building the toolchain with LLVM libc"
summary: "Configure the toolchain with the CMake setting -DLLVM_TOOLCHAIN_C_LIBRARY=llvmlibc to build a version of the toolchain based on LLVM libc."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/llvmlibc.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/llvmlibc.md#building-the-toolchain-with-llvm-libc"
license: "Apache-2.0"
mode: "V"
---

> **NOTE:** Building the LLVM libc package is only supported on Linux
> and macOS.

Configure the toolchain with the CMake setting
`-DLLVM_TOOLCHAIN_C_LIBRARY=llvmlibc` to build a version of the
toolchain based on LLVM libc.

If you also add `-DLLVM_TOOLCHAIN_LIBRARY_OVERLAY_INSTALL=on` then the
`package-llvm-toolchain` CMake target will generate an overlay package
similar to the [newlib overlay
package](https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/main/docs/newlib.md).
If you unpack this over an existing installation of the toolchain,
then you can switch to LLVM libc by adding `--config=llvmlibc.cfg` on
the command line.
