---
id: "aig-install-guides-llvm-embedded"
type: "concept"
domain: "project"
title: "Arm Toolchain for Embedded"
summary: "Arm Toolchain for Embedded (ATfE) is a free, open-source LLVM-based toolchain for bare-metal Arm development. It targets Cortex-M, Cortex-R, and Cortex-A processors from Armv6-M and newer, and includes clang, lld, libc++, compiler-rt, and picolibc."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/llvm-embedded.md"
doc_source: "https://learn.arm.com/install-guides/llvm-embedded/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Arm Toolchain for Embedded (ATfE) is a free, open-source LLVM-based toolchain for bare-metal Arm development. It targets Cortex-M, Cortex-R, and Cortex-A processors from Armv6-M and newer, and includes `clang`, `lld`, `libc++`, `compiler-rt`, and `picolibc`.

ATfE is the successor to the LLVM Embedded Toolchain for Arm. The [LLVM Embedded Toolchain for Arm repository](https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm) is deprecated; use ATfE for LLVM 20 and later.

Pre-built binaries are available for Windows (x86_64), macOS (universal), and Linux (x86_64 and AArch64) hosts.

**Toolchain version:**
The following steps use Arm Toolchain for Embedded version 22.1.0. The same steps work with other versions. Replace the version number in file names and URLs with your version of choice. To find the latest version, see [Arm Toolchain releases](https://github.com/arm/arm-toolchain/releases).
