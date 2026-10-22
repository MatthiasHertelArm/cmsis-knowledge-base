---
id: "dbgx-arm-cmsis-debugger-debugger-configuration"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Debugger Configuration"
summary: "VS Code uses the file .vscode/launch.json to configure target-specific debug parameters such as project files, device, and debug adapter. The Arm CMSIS Solution automatically generates this file based on the csolution project with all required settings, streamlining this setup."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/README.md#debugger-configuration"
license: "Apache-2.0"
mode: "V"
---

VS Code uses the file `.vscode/launch.json` to configure target-specific debug parameters such as project files, device, and debug adapter. The Arm CMSIS Solution automatically generates this file based on the _csolution project_ with all [required settings](https://mdk-packs.github.io/vscode-cmsis-solution-docs/debug.html#configure-run-and-debug), streamlining this setup. It provides both _launch_ and _attach_ configurations; for a multi-processor system, each core gets an _attach_ configuration, while the start core also gets a _launch_ configuration.

To start debugging, the CMSIS Solution offers action buttons and menu commands.

(figure: CMSIS-View - action buttons)

- **Load & Debug application** starts the CMSIS Debugger with _launch_ configuration.
- **Load & Run application** starts program execution and the GDB server; use then _attach_ configurations to connect to the running system.
- **Target Information** (...) shows the available debugger adapters.
