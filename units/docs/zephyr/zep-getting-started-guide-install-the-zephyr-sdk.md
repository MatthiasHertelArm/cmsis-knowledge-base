---
id: "zep-getting-started-guide-install-the-zephyr-sdk"
type: "concept"
domain: "project"
title: "Getting Started Guide: Install the Zephyr SDK"
summary: "The Zephyr Software Development Kit (SDK) contains toolchains for each of Zephyr's supported architectures. Those toolchains include the compiler, assembler, linker, and other programs required to build Zephyr applications for your target hardware."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/getting_started/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/getting_started/index.rst"
license: "Apache-2.0"
mode: "V"
---

The Zephyr Software Development Kit (SDK)
contains toolchains for each of Zephyr's supported architectures. Those
toolchains include the compiler, assembler, linker, and other programs
required to build Zephyr applications for your target hardware.

It also contains additional host tools, such as custom QEMU and OpenOCD builds
that are used to emulate, flash and debug Zephyr applications.

Install the Zephyr SDK with `west sdk install` from the Zephyr repository:


**Tip:** Use command options to choose the SDK installation destination or install only selected architecture toolchains. See `west sdk install --help` for details.


**Note:** If you want to install Zephyr SDK without using the `west sdk` command, please see toolchain_zephyr_sdk_install.
