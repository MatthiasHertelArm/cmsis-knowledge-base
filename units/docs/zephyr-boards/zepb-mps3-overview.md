---
id: "zepb-mps3-overview"
type: "concept"
domain: "bring-up"
title: "mps3: Overview"
summary: "The mps3 board configuration is used by Zephyr applications that run on the MPS3 board. It provides support for multiple Arm FPGA images and simulation models:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/arm/mps3/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/arm/mps3/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The mps3 board configuration is used by Zephyr applications that run
on the MPS3 board. It provides support for multiple Arm FPGA images and
simulation models:

- AN536 supports Arm Cortex-R52 CPU
- AN547 and AN552 support Arm Cortex-M55 CPU
- AN555 support Arm Cortex-M85 CPU
- Corstone-300 and Corstone-310 FVPs are supported for selected Cortex-M
  configurations

Depending on the selected board target, it provides support for the following
devices:

- Nested Vectored Interrupt Controller (NVIC)
- System Tick System Clock (SYSTICK)
- Generic Interrupt Controller v3 (GICv3)
- Arm architectural timer
- Cortex-M System Design Kit GPIO
- Cortex-M System Design Kit UART
- Ethos-U55 NPU

Corstone-300 FVP/Corstone-310 FVP (Fixed Virtual Platforms) are complete
simulations of Arm systems, including processor, memory and peripherals.
They are available free of charge for Linux and Windows systems.
The FVPs have been selected for simulation since they provide access to the
Ethos-U55 NPU, which is unavailable in QEMU or other simulation platforms.

The AN536 Cortex-R52x2 subsystem is supported with QEMU using the `mps3-an536` machine.



### Zephyr board options
