---
id: "aig-gcc-arm-gnu"
type: "concept"
domain: "project"
title: "Arm GNU Toolchain"
summary: "Arm GNU Toolchain is a community-supported, pre-built GNU compiler toolchain for Arm-based CPUs. In this guide, you'll learn how to install the toolchain directly from the Arm GNU Toolchain downloads page."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/gcc/arm-gnu.md"
doc_source: "https://learn.arm.com/install-guides/gcc/arm-gnu/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Arm GNU Toolchain is a community-supported, pre-built GNU compiler toolchain for Arm-based CPUs. In this guide, you'll learn how to install the toolchain directly from the [Arm GNU Toolchain downloads page](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads). This is the recommended approach for bare-metal and embedded targets such as `arm-none-eabi`.

For a cross-compiler targeting Arm Linux (for example `aarch64-linux-gnu` or `arm-linux-gnueabihf`), see the [Cross-compiler](https://learn.arm.com/install-guides/gcc/arm-gnu/../cross) install guide instead, which installs those toolchains using the Linux package manager.

There are many versions of the [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain) available. We generally recommend the latest version, as this will contain the latest optimization improvements and support for the latest Arm IP. 

However there are reasons you may wish to use earlier compiler versions, so older versions are also available.

See also [Where can I get older versions of the Arm GNU Toolchain and GCC for Arm Platforms?](https://developer.arm.com/documentation/ka005611/latest)
