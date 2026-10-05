---
id: "llvmet-llvm-embedded-toolchain-for-arm-c-support"
type: "concept"
domain: "project"
title: "LLVM Embedded Toolchain for Arm: C++ support"
summary: "C++ is partially supported with the use of libc++ and libc++abi from LLVM. Features that are not supported include: - Multithreading"
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:README.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/README.md#c-support"
license: "Apache-2.0"
mode: "V"
---

C++ is partially supported with the use of libc++ and libc++abi from LLVM. Features
that are not supported include:
 - Multithreading

LLVM Embedded Toolchain for Arm uses the unstable libc++ ABI version. This ABI
uses all the latest libc++ improvements and bugfixes, but may result in link
errors when linking against objects compiled against older versions of the ABI.
For more information see https://libcxx.llvm.org/DesignDocs/ABIVersioning.html.
