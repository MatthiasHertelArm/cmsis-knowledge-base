---
id: "alp-cmsis-rtx-vs-create-configure-cmsis-options"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil Studio (VS Code): Create csolution project: Configure CMSIS options"
summary: "Enable the following components:  CMSIS > Core  CMSIS > OSTick > SysTick  CMSIS > RTOS2 > Keil RTX  Device > Startup"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/create.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/create/#configure-cmsis-options"
license: "CC-BY-SA-4.0"
mode: "V"
---

1. Select **CMSIS** from the Extensions icon list in VS Code. You'll see the project structure.
2. Hover over the top-level project and select **Manage Software Components** to add CMSIS software packs to your project.

Enable the following components:
* `CMSIS > Core`
* `CMSIS > OSTick > SysTick`
* `CMSIS > RTOS2 > Keil RTX`
* `Device > Startup`

You may need to select **Software packs: All packs** from the drop-down.

If prompted in the **Validation** pane, select the latest available version for each. Use the `CMSIS-RTX` pack if others are shown.

Close this view to save.
