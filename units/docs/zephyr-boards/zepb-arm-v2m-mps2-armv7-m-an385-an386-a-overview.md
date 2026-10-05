---
id: "zepb-arm-v2m-mps2-armv7-m-an385-an386-a-overview"
type: "concept"
domain: "bring-up"
title: "ARM V2M MPS2 Armv7-m (AN385/AN386/AN500): Overview"
summary: "The mps2/an385, mps2/an386, and mps2/an500 board targets are three of the mps2 Armv7-m based board targets supported in Zephyr."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/arm/mps2/doc/mps2_armv7m.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The `mps2/an385`, `mps2/an386`, and `mps2/an500` board targets are three of
the mps2 Armv7-m based board targets supported in Zephyr. This document
provides details about the support provided for these three Armv7-m mps2 board targets
(**AN385**, **AN386**, **AN500**) and the following devices:

- Nested Vectored Interrupt Controller (NVIC)
- System Tick System Clock (SYSTICK)
- Cortex-M System Design Kit UART

In addition to enabling actual hardware usage, these board targets can
also use FVP to emulate the platforms running on the MPS2+.

More information about the board can be found at the V2M MPS2 Website.

The application note for each of the board can be found as follows:

- AN385 can be found at Application Note AN385
- AN386 can be found at Application Note AN386
- AN500 can be found at Application Note AN500

AN385 is also supported to run with QEMU, and is set to run with QEMU by default.


**Note:** These board targets makes no claims about its suitability for use with actual MPS2 hardware systems, or any other hardware system.
