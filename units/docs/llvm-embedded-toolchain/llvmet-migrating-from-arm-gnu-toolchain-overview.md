---
id: "llvmet-migrating-from-arm-gnu-toolchain-overview"
type: "concept"
domain: "project"
title: "Migrating from Arm GNU Toolchain: Overview"
summary: "Arm GNU Toolchain is the GNU Toolchain for the Arm Architecture released by Arm and traditionally used for embedded development."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/migrating.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/migrating.md#overview"
license: "Apache-2.0"
mode: "V"
---

[Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain)
is the GNU Toolchain for the Arm Architecture released by Arm and traditionally
used for embedded development.

Generally the LLVM toolchain tries to be a drop in replacement for the GNU toolchain,
however there may be some missing features or small incompatibilities.

Some known differences and migration strategies are summarized below.
