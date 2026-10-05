---
id: "cda-troubleshooting-c-and-c-debug-sess-raw-debugger-commands"
type: "concept"
domain: "debug"
title: "Troubleshooting C and C++ debug sessions: Raw debugger commands"
summary: "evaluateexpression(\"-exec <command>\") hands a command to the debugger and returns what it prints."
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@7db44ba:docs/agent-resources/troubleshooting/cpp.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/cpp.md#raw-debugger-commands"
license: "Apache-2.0"
mode: "V"
---

`evaluate_expression("-exec <command>")` hands a command to the debugger and returns what it prints.

- On the CMSIS Debugger the tool translates `-exec` into that adapter's own prefix, `>`; `>info breakpoints` is accepted there too. On `cppdbg`, `-exec` is the extension's own prefix: the command goes to GDB, or to LLDB when the entry sets `"MIMode": "lldb"` (then in LLDB syntax: `breakpoint list`, `register read`, `memory read`).
- CodeLLDB (`lldb`) takes console input as an LLDB command by default and prints command output only to the Debug Console. Put `?` in front of expressions there: `?count`, or `?/nat` for casts and function calls.
- Worth knowing: `-exec info breakpoints`, `-exec info line main.c:42`, `-exec x/8xw 0x20000000`, `-exec print/x flags`, `-exec ptype struct msg_hdr`, `-exec info frame`, `-exec disassemble /s`.
- Watchpoints and catchpoints have no tool: `-exec watch g_state` stops right after a store changes `g_state`, and `-exec catch throw` stops in `__cxa_throw` with the throwing function one frame up. Note the number GDB prints and remove it with `-exec delete <n>` when done, because `clear_all_breakpoints` does not know it. On Cortex-M a watchpoint takes one of the few DWT comparators.
- Leave everything else to the tools. Breakpoints belong to `add_breakpoint`, `remove_breakpoint` and `clear_all_breakpoints`: a GDB-only `-exec break` is invisible to them and duplicates what they manage. Run control belongs to `continue_execution` and the step tools, which wait for the stop; after a raw `-exec continue`, call `wait_for_stop`. Reset a target with `reset`, not with `-exec monitor reset`.
