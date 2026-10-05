---
id: "rtx-create-an-rtx5-project-additional-requirements-for-rtx-on-corte"
type: "concept"
domain: "rtos"
title: "Create an RTX5 Project: Additional requirements for RTX on Cortex-A"
summary: "Cortex-A based microcontrollers are less unified with respect to the interrupt and timer implementations used compared to M-class devices. Thus RTX requires additional components when an A-class device is used, namely CMSIS-Core IRQ Controller (API) and OS Tick (API) implementations."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/project.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/project.md#additional-requirements-for-rtx-on-cortex-a"
license: "Apache-2.0"
mode: "V"
---

Cortex-A based microcontrollers are less unified with respect to the interrupt and timer implementations used compared to M-class devices. Thus RTX requires additional components when an A-class device is used, namely [CMSIS-Core IRQ Controller (API)](https://arm-software.github.io/CMSIS_6/latest/Core_A/group__irq__ctrl__gr.html) and OS Tick (API) implementations.

(figure: Keil uVision Run-Time Environment for RTX5 on Cortex-A)

The default implementations provided along with CMSIS are

- Arm [Generic Interrupt Controller (GIC)](https://arm-software.github.io/CMSIS_6/latest/Core_A/group__GIC__functions.html)
- Arm Cortex-A5, Cortex-A9 [Private Timer (PTIM)](https://arm-software.github.io/CMSIS_6/latest/Core_A/group__PTM__timer__functions.html)
- Arm Cortex-A7 [Generic Physical Timer (GTIM)](https://arm-software.github.io/CMSIS_6/latest/Core_A/group__PL1__timer__functions.html)

For devices not implementing GIC, PTIM nor GTIM please refer to the according device family pack and select the proper implementations.

\endif
