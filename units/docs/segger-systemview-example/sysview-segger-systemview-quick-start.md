---
id: "sysview-segger-systemview-quick-start"
type: "concept"
domain: "trace"
title: "SEGGER-SystemView: Quick Start"
summary: "SEGGER-SystemView: Quick Start"
status: "draft"
collection: "segger-systemview-example"
source: "Arm-Examples/SEGGER-SystemView@9be0601:README.md"
doc_source: "https://github.com/Arm-Examples/SEGGER-SystemView/blob/9be0601/README.md#quick-start"
license: "Apache-2.0"
mode: "V"
---

1. Install
   [Keil Studio for VS Code](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack)
   from the VS Code marketplace.
2. Clone this repository, for example, using
   [Git in VS Code](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git),
   or download the ZIP file. Then open the repository root folder.
3. Let the related tools and software packs download and install. Review progress with **View > Output > CMSIS Solution**.
4. Connect the board to the PC.
5. Build and load the project with the CMSIS View
   [action buttons](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution#action-buttons).
6. Press the User button on the board 10 times. This ends the pyOCD session and the streaming.
7. In the SystemView application, open the file `.\out\SEGGER-SystemView+STM32H743ZITx.core0.ch1.bin`.
8. Inspect the system and RTOS activity.
