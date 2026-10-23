---
id: "dbgx-arm-cmsis-debugger-debugger-user-interface"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Debugger User Interface"
summary: "Many features of the CMSIS Debugger extension are exposed in the Run and Debug view of VS Code."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/README.md#debugger-user-interface"
license: "Apache-2.0"
mode: "V"
---

Many features of the CMSIS Debugger extension are exposed in the **Run and Debug** view of VS Code.

1. **Start debugging** selects a configuration: _launch_ to start download/debug, _attach_ to connect with a running system.
2. **Debug Toolbar** has buttons for the most common debugging actions that control execution.
3. The **Trace and Live View** shows the **LIVE WATCH** window.
4. **Debug Statusbar** shows the time spent running the application.
5. The **Debug Console** can be used to interact with the debugger on the command line.

(figure: Run and Debug view)

Most editor features are available during debugging. For example, developers can use Find and edit source code to correct program errors.

The **Run and Debug** view provides:

- [**VARIABLES**](#variables) section, which includes local function variables and CPU register values.
- [**WATCH**](#watch) section, which allows viewing user-defined expressions, for example, variable values.
- [**CALL STACK**](#call-stack) section that shows active RTOS threads along with the call stack.
- [**BREAKPOINTS**](#breakpoints) section for managing stop points in application execution to inspect the state.

> 📌 **TIP**
>
> Click on a _line number badge_ to navigate to the source code line.

Other debugger specific views or features:

- [**CPU Time**](#cpu-time) shows execution timing and statistics of the past five breakpoints.
- [**Live Watch**](#trace-and-live-view) offers run-time viewing of user-defined expressions, for example, variable
  values.
- [**Component Viewer**](#component-viewer) shows detailed information to help analyze the operation of software
  components.
- [**Core Peripherals**](#core-peripherals) view gives insight into the programming of CPU specific core peripherals.
- [**Peripherals**](#peripherals) show the device peripheral registers and allow changing their values.
- [**Memory Inspector**](#memory-inspector) provides a powerful and configurable memory viewer.
- [**Disassembly**](#disassembly) shows assembly instructions and supports run control, for example with stepping and
  breakpoints.
- [**Debug Console**](#debug-console) lists debug output messages and allows entering expressions or GDB commands.
- [**Serial Monitor**](#serial-monitor) uses serial or TCP communication to interact with application I/O functions
  (`printf`, `getc`, etc.).
- [**Multi-Core Debug**](#multi-core-debug) to view and control several processors in a device.
