---
id: "zepb-kit-xmc72-evk-overview"
type: "concept"
domain: "bring-up"
title: "kit_xmc72_evk: Overview"
summary: "The KIT_XMC72_EVK is an evaluation kit based on the XMC™ 7200 family, featuring an XMC7200D_E272K8384 microcontroller with dual Arm® Cortex®-M7 cores and an Arm® Cortex®-M0+ core in a 272-pin BGA package. It is designed for industrial automation and control applications."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/infineon/kit_xmc72_evk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/infineon/kit_xmc72_evk/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The KIT_XMC72_EVK is an evaluation kit based on the XMC™ 7200 family,
featuring an XMC7200D_E272K8384 microcontroller with dual Arm®
Cortex®-M7 cores and an Arm® Cortex®-M0+ core in a 272-pin BGA
package. It is designed for industrial automation and control applications.

Key features include 8 MB flash, 1 MB SRAM, Gigabit Ethernet, CAN FD,
512-Mb QSPI NOR flash, and a comprehensive set of programmable analog and
digital peripherals.

The board supports Arduino headers and includes an onboard KitProg3
programmer/debugger with micro-B USB connectivity.

The KIT_XMC72_EVK is a multi-core board with three build targets:

- `kit_xmc72_evk/xmc7200d_e272k8384/m0p` — Cortex-M0+
- `kit_xmc72_evk/xmc7200d_e272k8384/m7_0` — Cortex-M7 core 0
- `kit_xmc72_evk/xmc7200d_e272k8384/m7_1` — Cortex-M7 core 1
