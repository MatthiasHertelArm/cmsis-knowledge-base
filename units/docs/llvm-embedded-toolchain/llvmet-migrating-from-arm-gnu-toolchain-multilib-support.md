---
id: "llvmet-migrating-from-arm-gnu-toolchain-multilib-support"
type: "concept"
domain: "project"
title: "Migrating from Arm GNU Toolchain: Multilib support"
summary: "LLVM toolchain for Arm provides multilib support similar to the GNU toolchain, see Using the toolchain section in the README, however uses different command line options to control selection of semihosting."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/migrating.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/migrating.md#multilib-support"
license: "Apache-2.0"
mode: "V"
---

LLVM toolchain for Arm provides multilib support similar to the GNU toolchain,
see _Using the toolchain_ section in the [README](https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/main/README.md#using-the-toolchain),
however uses different command line options to control selection of semihosting.

|Use case|GNU options|LLVM options|
|--------|-----------|------------|
|No semihosting|`--specs=nosys.specs`|
|Semihosting|`--specs=rdimon.specs`|`-nostartfiles -lcrt0-semihost -lsemihost`|
|Newlib-nano|`--specs=nano.specs`|Not available: `picolibc` is an equivalent of `newlib-nano`.
