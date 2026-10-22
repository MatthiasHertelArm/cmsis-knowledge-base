---
id: "ethint-cmsis-ethos-u-integration-example-quick-start-in-vs-code"
type: "concept"
domain: "edge-ai"
title: "CMSIS Ethos-U integration example: Quick start in VS Code"
summary: "2. Prepare the AppKit-E8 board as described in the board layer README. The device needs its ATOC and debug stubs programmed with Alif SETOOLS before this example can run."
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@9b906f5:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/README.md#quick-start-in-vs-code"
license: "Apache-2.0"
mode: "V"
---

1. Install [Keil Studio for VS Code](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack).
   Clone this repository and open its root folder in VS Code. Use **Arm Tools:
   Activate Environment** if prompted; [Arm Tools Environment Manager](https://marketplace.visualstudio.com/items?itemName=Arm.environment-manager)
   installs the compiler, CMSIS-Toolbox, and build tools listed in
   [`vcpkg-configuration.json`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/vcpkg-configuration.json). Activate an Arm Compiler
   license if you choose AC6; GCC is also supported.

2. Prepare the AppKit-E8 board as described in the
   [board layer README](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/Board/AppKit-E8_M55_HP/README.md). The device needs its
   ATOC and debug stubs programmed with Alif SETOOLS before this example can run.
   Use the `SE` position of SW4 for SETOOLS, then set SW4 to `U4` for UART4 test
   output through the PRG USB connector (J3).

3. Open the **CMSIS** view and select **Open Solution in Workspace**. Choose
   [`Test-Ethos-U85.csolution.yml`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/Test-Ethos-U85.csolution.yml), then select
   the `AppKit-E8-U85` target, its `J-Link` target set, and the `Debug` build.
   Use the CMSIS **Build** action; the extension installs any missing public
   software packs. The supplied models target Ethos-U85 with 256 MACs and shared
   SRAM, so this is the starting configuration.

4. Use the CMSIS **Load and Run** or **Load and Debug** action with the board's
   J-Link connection. Open the board's UART4 virtual COM port to view the output.
   A successful test ends with `2 of 2 checks passed` and `TEST RESULT: PASS`.

For Ethos-U55, open [`Test-Ethos-U55.csolution.yml`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/Test-Ethos-U55.csolution.yml)
and select `AppKit-E8-U55`. Recompile the models for U55 before running them;
see the [model converter guide](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/script/README.md) and the configuration table below.

The solutions also include `SSE-300-U55` and `SSE-320-U85` targets for Corstone
FVPs. Their board layers are in [`Board/Corstone-300/`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/Board/Corstone-300/)
and [`Board/Corstone-320/`](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/Board/Corstone-320/).
