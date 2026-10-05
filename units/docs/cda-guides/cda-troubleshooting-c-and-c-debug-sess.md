---
id: "cda-troubleshooting-c-and-c-debug-sess"
type: "concept"
domain: "debug"
title: "Troubleshooting C and C++ debug sessions"
summary: "Notes for C and C++ programs on the host, through the C/C++ extension (cppdbg, with GDB or LLDB) or CodeLLDB, and for C/C++ firmware on Cortex-M through the CMSIS Debugger (gdbtarget: arm-none-eabi-gdb behind cdt-gdb-adapter)."
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@7db44ba:docs/agent-resources/troubleshooting/cpp.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/cpp.md"
license: "Apache-2.0"
mode: "V"
---

Notes for C and C++ programs on the host, through the C/C++ extension (`cppdbg`, with GDB or LLDB) or CodeLLDB, and for C/C++ firmware on Cortex-M through the CMSIS Debugger (`gdbtarget`: arm-none-eabi-gdb behind cdt-gdb-adapter). Probes, faults, peripherals and the memory map are covered in [embedded.md](https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/embedded.md) (`cmsis-developer-assistant://docs/troubleshooting/embedded`) and [cmsis-embedded-guide.md](https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/../cmsis-embedded-guide.md) (`cmsis-developer-assistant://docs/cmsis-embedded-guide`). Test each hypothesis at a stop rather than with a temporary `printf`: on firmware every print costs a rebuild, a reflash and different timing.
