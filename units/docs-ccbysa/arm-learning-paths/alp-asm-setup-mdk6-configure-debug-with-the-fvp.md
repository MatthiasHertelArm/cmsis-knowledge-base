---
id: "alp-asm-setup-mdk6-configure-debug-with-the-fvp"
type: "concept"
domain: "project"
title: "Write Arm Assembler functions: Setting up a Project in Keil Studio (VS Code): Configure debug with the FVP"
summary: "Select Run and Debug from the Extensions icon list."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/asm/setup_mdk6.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/asm/setup_mdk6/#configure-debug-with-the-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

Select `Run and Debug` from the Extensions icon list.

Click the gear icon to open `launch.json`. This is the file that defines the debug instance.

Right-click on `launch.json` and select `Open Run and Debug Configuration`.

From the `Selected Configuration` pull-down, select `New Configuration` > `Launch FVP`. Edit the `Configuration Name` if desired.

From the `Target` > `Configuration Database Entry` pull-down, select `MPS2_Cortex_M4` > `Cortex-M4`.

Other fields can be left as default. Close the file to save. Observe that `launch.json` has been updated.
