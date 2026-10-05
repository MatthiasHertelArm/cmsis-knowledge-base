---
id: "llvmet-experimental-newlib-support-building-newlib-library-package"
type: "concept"
domain: "project"
title: "Experimental newlib support: Building `newlib` library package"
summary: "Configure the toolchain with the CMake setting -DLLVM_TOOLCHAIN_C_LIBRARY=newlib to build a newlib-based version of the toolchain."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/newlib.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/newlib.md#building-newlib-library-package"
license: "Apache-2.0"
mode: "V"
---

> **NOTE:**  Building `newlib` package is only supported on Linux and macOS.

Configure the toolchain with the CMake setting
`-DLLVM_TOOLCHAIN_C_LIBRARY=newlib` to build a newlib-based version of
the toolchain.

If you also add `-DLLVM_TOOLCHAIN_LIBRARY_OVERLAY_INSTALL=on` then the
`package-llvm-toolchain` CMake target will generate the `newlib`
overlay package.

Note that the `-DLLVM_TOOLCHAIN_LIBRARY_OVERLAY_INSTALL=on` option
only generates the `newlib` package, but does not install it as part
of the `install` CMake target.
