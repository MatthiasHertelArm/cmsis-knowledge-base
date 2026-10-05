---
id: "alp-cmsis-rtx-vs-create-configure-debug-with-the-fvp"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil Studio (VS Code): Create csolution project: Configure debug with the FVP"
summary: "From the Selected Configuration drop-down, select New Configuration > Launch FVP. Edit the Configuration Name if desired."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/create.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/create/#configure-debug-with-the-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

1. Select **Run and Debug** from the Extensions icon list.
2. Select the gear icon to open `launch.json`. This file defines the debug instance.
3. Right-click on `launch.json` and select **Open Run and Debug Configuration**.

From the **Selected Configuration** drop-down, select **New Configuration** > **Launch FVP**. Edit the **Configuration Name** if desired.

From the **Target** > **Configuration Database Entry** drop-down, select **MPS2_Cortex_M4** > **Cortex-M4**.

Leave other fields as default. Observe that `launch.json` has been updated.

Close the file to save your configuration.
