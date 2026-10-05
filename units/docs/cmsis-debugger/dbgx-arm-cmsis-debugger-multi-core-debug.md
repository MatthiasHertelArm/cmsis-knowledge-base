---
id: "dbgx-arm-cmsis-debugger-multi-core-debug"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Multi-Core Debug"
summary: "A GDB server provides multiple connections to the processor cores (identified with pname) of a device. The list below shows the output of pyOCD in the DEBUG CONSOLE of VS Code."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/README.md#multi-core-debug"
license: "Apache-2.0"
mode: "V"
---

A GDB server provides multiple connections to the processor cores (identified with `pname`) of a device. The list below shows the output of pyOCD in the DEBUG CONSOLE of VS Code.

```txt
0000680 I Target device: MCXN947VDF [cbuild_run]
0001585 I core 0: Cortex-M33 r0p4, pname: cm33_core0 [cbuild_run]
0001585 I core 1: Cortex-M33 r0p4, pname: cm33_core1 [cbuild_run]
0001585 I start-pname: cm33_core0 [cbuild_run]
0001600 I Semihost server started on port 4444 (core 0) [server]
0001636 I GDB server started on port 3333 (core 0) [gdbserver]
0001641 I Semihost server started on port 4445 (core 1) [server]
0001642 I GDB server started on port 3334 (core 1) [gdbserver]
0007560 I Client connected to port 3333! [gdbserver]
```

The `start-pname` indicates the processor that starts first and boots the system. A debug _launch_ command connects to this processor. Use a debug _attach_ command to connect to  processors that are running. The picture below highlights the parts of the user interface that interact with processors.

1. Select a processor and **Start Debug**. This connects the debugger.
2. **Select a Processor** in the debug toolbar, or
3. Click in **CALL STACK** on a thread or function name to select a processor.
4. The selected processor is also shown in the **CPU Time Status bar**. This processor context is used in the VARIABLES and WATCH view.

(figure: Multicore Debug)

> 📝 **Notes:**
>
> - The SEGGER JLink GDB server uses a _launch_ command to connect to a running processor whereas other GDB servers use an _attach_ command.
> - A [Disassembly View](#disassembly) opens only for a selected processor; otherwise the command is shown as disabled.
