---
id: "zepb-arm-v2m-mps2-armv6-m-an383-overview"
type: "concept"
domain: "bring-up"
title: "ARM V2M MPS2 Armv6-m (AN383): Overview"
summary: "Currently mps2/an383 is the only mps2 Armv6-m based board target supported in Zephyr. It provides support for the ARM Cortex-M0+ (AN383) CPU and the following devices:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/arm/mps2/doc/mps2_armv6m.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

Currently `mps2/an383` is the only mps2 Armv6-m based board target supported in Zephyr.
It provides support for the ARM Cortex-M0+ (AN383) CPU and the following devices:

- Nested Vectored Interrupt Controller (NVIC)
- System Tick System Clock (SYSTICK)
- Cortex-M System Design Kit UART

In addition to enabling actual hardware usage, this board target can
also use FVP. to emulate the AN383 platform running on the MPS2+.

More information about the board can be found at the V2M MPS2 Website.

The Application Note AN383 can be found at Application Note AN383.


**Note:** This board target makes no claims about its suitability for use with actual MPS2 hardware systems using AN383, or any other hardware system. It has been tested on FVP.
