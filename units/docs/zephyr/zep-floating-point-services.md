---
id: "zep-floating-point-services"
type: "concept"
domain: "rtos"
title: "Floating Point Services"
summary: "The kernel allows threads to use floating point registers on board configurations that support these registers."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/other/float.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/other/float.rst"
license: "Apache-2.0"
mode: "V"
---

The kernel allows threads to use floating point registers on board
configurations that support these registers.


**Note:** Floating point services are currently available only for boards based on ARM Cortex-M SoCs supporting the Floating Point Extension, the Intel x86 architecture, the SPARC architecture and ARCv2 SoCs supporting the Floating Point Extension. The services provided are architecture specific. The kernel does not support the use of floating point registers by ISRs.
