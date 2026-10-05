---
id: "zepb-kit-xmc72-evk-building"
type: "concept"
domain: "bring-up"
title: "kit_xmc72_evk: Building"
summary: "Here is an example for the hello_world application."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/infineon/kit_xmc72_evk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/infineon/kit_xmc72_evk/doc/index.html#building"
license: "Apache-2.0"
mode: "V"
---

Here is an example for the hello_world application.

The same for the first Cortex®-M7 core:

And the second Cortex®-M7 core:


**Note:** Only the Cortex®-M0+ core is enabled at startup. To enable the first Cortex®-M7 core, add the following to the Cortex®-M0+ application: `Cy_SysEnableCM7(CORE_CM7_0, CY_CORTEX_M7_0_APPL_ADDR);`. To enable the second Cortex®-M7 core: `Cy_SysEnableCM7(CORE_CM7_1, CY_CORTEX_M7_1_APPL_ADDR);`.
