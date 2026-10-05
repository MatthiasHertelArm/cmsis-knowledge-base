---
id: "dbgx-arm-cmsis-debugger-debug-toolbar"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Debugger User Interface / Debug toolbar"
summary: "During debugging, the Debug toolbar contains actions to control the flow of the debug session, such as stepping through code, pausing execution, and stopping the debug session."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/README.md#debug-toolbar"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger User Interface_

During debugging, the **Debug toolbar** contains actions to control the flow of the debug session, such as stepping through code, pausing execution, and stopping the debug session.

(figure: Debug toolbar)

| Action | Description |
|--------|-------------|
| Continue/Pause | **Continue**: Resume normal program execution (up to the next breakpoint).<br>**Pause**: Inspect code executing at the current location. |
| Step Over | Execute the next statement as a single command without inspecting or following its component steps. |
| Step Into | Enter the next statement to follow its execution line-by-line. |
| Step Out | When inside a function, return to the earlier execution context by completing remaining lines of the current method as though it were a single command. |
| Restart | Terminate the current program execution and start debugging again using the current run configuration. |
| Stop/Disconnect | **Stop**: Terminate the current debug session.<br>**Disconnect:** Detach debugger from a core without changing the execution status (running/pause). |
| Debug Session | For multi-core devices, the list of active debug sessions and switch between them. |
| Reset Target | Reset the target device. |
