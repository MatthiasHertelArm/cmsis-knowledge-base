---
id: "dbgx-arm-cmsis-debugger-target-interaction-while-running"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Debugger User Interface / Target interaction while running"
summary: "Depending on the debug view and the debug probe used, target interaction with a Cortex-M CPU may or may not possible while running. The following table shows target interaction capabilities while running (with J-Link GDB server or using pyOCD):"
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/README.md#target-interaction-while-running"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger User Interface_

Depending on the debug view and the debug probe used, target interaction with a Cortex-M CPU may or may not possible
while running. The following table shows target interaction capabilities while running (with J-Link GDB server or using
pyOCD):

| View | Read | Edit |
|------|------|------|
| [**Memory Inspector**](#memory-inspector) | ✅  | ✅  |
| [**Peripherals**](#peripherals)           | ✅  | ✅  |
| [**Live Watch**](#trace-and-live-view)    | ✅  | ❌ |
| [**Component Viewer**](#component-viewer) | ✅  | ❌ |
| [**Core Peripherals**](#core-peripherals) | ✅  | ❌ |
| [**VARIABLES**](#variables)               | ❌ | ❌ |
| [**WATCH**](#watch)                       | ❌ | ❌ |
| [**CALL STACK**](#call-stack)             | ❌ | ❌ |
