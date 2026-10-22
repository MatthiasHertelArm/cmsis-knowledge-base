---
id: "zep-arm-cortex-m-developer-guide-cmsis"
type: "concept"
domain: "rtos"
title: "Arm Cortex-M Developer Guide: CMSIS"
summary: "Cortex-M CMSIS headers are provided through standalone module repositories:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/arch/arm_cortex_m.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/arch/arm_cortex_m.rst"
license: "Apache-2.0"
mode: "V"
---

Cortex-M CMSIS headers are provided through standalone module repositories:

- **CMSIS 5**: [zephyrproject-rtos/cmsis](https://github.com/zephyrproject-rtos/cmsis)
- **CMSIS 6**: [zephyrproject-rtos/CMSIS_6](https://github.com/zephyrproject-rtos/CMSIS_6)

Zephyr has begun transitioning to **CMSIS 6** as the default source for Cortex-M core headers.
However, at present, Zephyr includes headers from **both** the CMSIS 6 and legacy CMSIS 5 modules.

The legacy CMSIS 5 headers remain available primarily for compatibility with vendor HALs, while all
new architecture-level development should use **CMSIS 6** headers whenever possible.

`CONFIG_CPU_CORTEX_M` selects `CONFIG_HAS_CMSIS_CORE` to signify that
CMSIS headers are available for all supported Cortex-M variants.
