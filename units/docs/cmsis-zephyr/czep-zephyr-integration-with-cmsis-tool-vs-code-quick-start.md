---
id: "czep-zephyr-integration-with-cmsis-tool-vs-code-quick-start"
type: "concept"
domain: "project"
title: "Zephyr Integration with CMSIS-Toolbox: VS Code quick start"
summary: "Zephyr Integration with CMSIS-Toolbox: VS Code quick start"
status: "draft"
collection: "cmsis-zephyr"
source: "Arm-Examples/CMSIS-Zephyr@ef8713c:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/README.md#vs-code-quick-start"
license: "Apache-2.0"
mode: "V"
---

1. Install [Keil Studio for VS Code](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack) from the VS Code marketplace.
2. [Install upstream Zephyr](#zephyr-installation) and [configure its environment variables](#configure-vs-code).
3. Clone this repository (for example using [Git in VS Code](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git)) or download the ZIP file. Then open the repository folder in VS Code.
4. In VS Code, open the [CMSIS View](https://mdk-packs.github.io/vscode-cmsis-solution-docs/userinterface.html#2-main-area-of-the-cmsis-view) and then the [Manage Solution dialog](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution#manage-solution-view) to select the target board and one project.
5. In the CMSIS view, use the [Action buttons](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution#action-buttons) to build, load, and debug the example on your hardware.

> [!TIP]
> If configuration or build errors occur, use **Clean All 'out' and 'tmp' directories** from the CMSIS view menu to remove stale CMake cache files before rebuilding.
