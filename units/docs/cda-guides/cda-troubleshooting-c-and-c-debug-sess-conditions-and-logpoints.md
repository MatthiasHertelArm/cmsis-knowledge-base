---
id: "cda-troubleshooting-c-and-c-debug-sess-conditions-and-logpoints"
type: "concept"
domain: "debug"
title: "Troubleshooting C and C++ debug sessions: Conditions and logpoints"
summary: "Troubleshooting C and C++ debug sessions: Conditions and logpoints"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@7db44ba:docs/agent-resources/troubleshooting/cpp.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/cpp.md#conditions-and-logpoints"
license: "Apache-2.0"
mode: "V"
---

- A `condition` on `add_breakpoint` is a C expression for the debugger: `i == 100`, `p != 0 && p->len > 64`, `name[0] == 'e'`. Keep calls such as `strcmp` out of it; they run in the program at every hit.
- The debugger tests the condition after the program has stopped at the breakpoint and resumes it when the condition is false. The FPB of a Cortex-M has no condition logic, so the core halts on every hit, and in an ISR or a fast loop each of those halts costs milliseconds through the probe. On the host a busy conditional breakpoint slows the program the same way.
- `add_logpoint` prints to VS Code's Debug Console and lets the program run on. No tool returns that output: it serves a user who watches the console, and values you need yourself come from a conditional breakpoint and a read at the stop. `cppdbg` fills in `{expr}` placeholders itself; on the CMSIS Debugger the tool sets the logpoint as a GDB `dprintf`, which fills them in (`{expr:%08lx}` picks the printf conversion) and whose hits `list_breakpoints` counts. On Cortex-M each hit halts the core as well.
