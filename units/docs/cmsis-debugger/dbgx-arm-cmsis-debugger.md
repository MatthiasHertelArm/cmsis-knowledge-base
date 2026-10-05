---
id: "dbgx-arm-cmsis-debugger"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger"
summary: "The Arm® CMSIS Debugger extension pack is a comprehensive debug platform for Arm Cortex-M processor-based devices that uses the GDB/MI protocol."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/README.md"
license: "Apache-2.0"
mode: "V"
---

The Arm® CMSIS Debugger extension pack is a comprehensive debug platform for Arm Cortex-M processor-based devices that uses the GDB/MI protocol.

- Supports single and [multi-core](#multi-core-debug) processor systems.
- Built-in RTOS kernel support for FreeRTOS, RTX, ThreadX, and Zephyr.
- Wide debug adapter support for CMSIS-DAP (ULink, MCULink, NuLink, etc.), JLink, and ST-Link.
- Can be combined with other VS Code debug extensions, such as those for Linux application debugging.

The Arm CMSIS Debugger includes [pyOCD](https://pyocd.io/) for target connection and Flash download, [GNU GDB](https://www.sourceware.org/gdb/documentation/) for core debug features, and adds these VS Code extensions:

- [CDT™ GDB Debug Adapter Extension](https://marketplace.visualstudio.com/items?itemName=eclipse-cdt.cdt-gdb-vscode) for starting applications (_launch_) or connecting to running systems (_attach_).
- [Memory Inspector](https://marketplace.visualstudio.com/items?itemName=eclipse-cdt.memory-inspector) provides a powerful and configurable memory viewer.
- [Peripheral Inspector](https://marketplace.visualstudio.com/items?itemName=eclipse-cdt.peripheral-inspector) provides a structured view to device peripheral registers during debugging.
- [Serial Monitor](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-serial-monitor) to view output from and send messages to serial (UART) or TCP ports.

For RTOS awareness, we recommend installing this extension manually:

- [RTOS Views](https://marketplace.visualstudio.com/items?itemName=mcu-debug.rtos-views) provides insights into resources of popular RTOS implementations at runtime.

This extension is [free to use](https://marketplace.visualstudio.com/items/Arm.vscode-cmsis-debugger/license) and you can install it individually or as part of the [Arm Keil® Studio pack](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack). For optimum debugger experience, use it with extensions from Arm (included in the Arm Keil Studio pack) and from other parties:

- [Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) a user interface for _csolution projects_ that simplifies the [Run and Debug configuration](https://mdk-packs.github.io/vscode-cmsis-solution-docs/debug.html#configure-run-and-debug).
- [Arm Tools Environment Manager](https://marketplace.visualstudio.com/items?itemName=Arm.environment-manager) installs tools (compiler, simulation models, and utilities) for software development.
- [RTOS Views](https://marketplace.visualstudio.com/items?itemName=mcu-debug.rtos-views) provides insights into resources of popular RTOS implementations at runtime.
