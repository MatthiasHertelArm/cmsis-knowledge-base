---
id: "dbgx-arm-cmsis-debugger-extension-functionality"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Extension Functionality"
summary: "This extension adds functionality to work seamlessly with other extensions."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/README.md#extension-functionality"
license: "Apache-2.0"
mode: "V"
---

This extension adds functionality to work seamlessly with other extensions.

- A [debug configuration provider](https://code.visualstudio.com/api/references/vscode-api#DebugConfigurationProvider)
for the type `gdbtarget` which comes with the [CDT GDB Debug Adapter Extension](https://marketplace.visualstudio.com/items?itemName=eclipse-cdt.cdt-gdb-vscode).
This provider manages the use of tools shipped with the extension:
    - If option `target`>`server` is set to `pyocd`, then it expands to the absolute path of the built-in pyOCD distribution.
- CMSIS specific _launch_ configuration items for the `*` debugger type, i.e. visible for all debugger types.
It depends on the actually used debug adapter type if this information is known and utilized.
