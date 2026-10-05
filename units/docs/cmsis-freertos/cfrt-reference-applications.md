---
id: "cfrt-reference-applications"
type: "concept"
domain: "rtos"
title: "Reference Applications"
summary: "The CMSIS-Pack Reference Application relies on defined interfaces (APIs) and is a hardware-agnostic application that can be used with any development board that provides the required pre-configured interfaces."
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:CMSIS/RTOS2/FreeRTOS/RefApp/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/CMSIS/RTOS2/FreeRTOS/RefApp/README.md"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Pack `Reference Application` relies on defined interfaces (APIs) and is a hardware-agnostic
application that can be used with any development board that provides the required pre-configured interfaces.
It requires a [software layer](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#software-layers)
that provides pre-configured interfaces for the specific target hardware. In practice, a board layer for
the target development board is required to build the Reference Application.

Use [Arm Keil Studio extensions for VS Code](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack)
to [deploy this example](https://mdk-packs.github.io/vscode-cmsis-solution-docs/create_app.html#configure-a-solution)
to your development board.

See [CMSIS-Toolbox - Reference Applications](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/)
to learn more about the concept of reference application in Open CMSIS Pack.
