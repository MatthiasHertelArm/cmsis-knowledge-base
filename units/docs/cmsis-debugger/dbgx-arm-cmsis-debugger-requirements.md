---
id: "dbgx-arm-cmsis-debugger-requirements"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Requirements"
summary: "Arm CMSIS Debugger: Requirements"
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/README.md#requirements"
license: "Apache-2.0"
mode: "V"
---

- **GDB** supporting the GDB remote protocol. `arm-none-eabi-gdb` is included in CMSIS Debugger extension. To use a different GDB installation, enter the full path/filename to the executable in the `gdb:` node of the `launch.json` file.

- **pyOCD** for connecting to a target. pyOCD is included in CMSIS Debugger extension. To use a different pyOCD installation, enter the full path/filename to the executable in the `target:` `server:` node of the `launch.json` file.

- **SEGGER® J-LINK®** is an alternative GDB server for target connection. Install the latest
[J-LINK Software and Documentation Pack](https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack)
from [SEGGER](https://www.segger.com/). Ensure all required drivers and host platform-specific settings are done. The extension expects that the `PATH` environment variable is set to the J-Link executables.
