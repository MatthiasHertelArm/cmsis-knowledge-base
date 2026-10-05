---
id: "alp-asm-setup-mdk6-create-a-new-project-csolution"
type: "concept"
domain: "project"
title: "Write Arm Assembler functions: Setting up a Project in Keil Studio (VS Code): Create a new project (csolution)"
summary: "Keil Studio projects are based on the CMSIS Solution standard."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/asm/setup_mdk6.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/asm/setup_mdk6/#create-a-new-project-csolution"
license: "CC-BY-SA-4.0"
mode: "V"
---

Keil Studio projects are based on the [CMSIS Solution](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/YML-Input-Format.md) standard.

Open the `VS Code` IDE, and select `File` > `New File` from the `File` menu. (`Ctrl`+`Alt`+`Windows`+`N`). You will be prompted for the type of file. Select `New Solution` (`Arm CMSIS Solution`).

The `Create New Solution` window will open. Click the `Target Device` pulldown, and search for `ARMCM4`.

From the `Templates, Reference Applications, and Examples` pulldown, select `Blank Solution`.

Ensure `Arm Compiler 6` is the selected compiler.

Enter an appropriate `Solution Name`. This will define the folder name that the project will be created into. You can also change the folder location if necessary.

Click `Create`. You will be prompted to open the solution in the current window, or open a new window.
