---
id: "zep-semihosting-guide-overview"
type: "concept"
domain: "rtos"
title: "Semihosting Guide: Overview"
summary: "Semihosting is a mechanism that enables code running on ARM, RISC-V and Xtensa targets to communicate and use the Input/Output facilities on a host computer that is running a debugger or emulator."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/arch/semihost.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/arch/semihost.rst"
license: "Apache-2.0"
mode: "V"
---

Semihosting is a mechanism that enables code running on ARM, RISC-V and Xtensa
targets to communicate and use the Input/Output facilities on a host computer
that is running a debugger or emulator.

More complete documentation on the available functionality is available at the
ARM Github documentation.

The RISC-V functionality borrows from the ARM definitions, as described at the
RISC-V Github documentation.

Semihosting implementation on Xtensa supports GDB File-I/O extension, which is
explained in GDB File-I/O Remote Protocol.
