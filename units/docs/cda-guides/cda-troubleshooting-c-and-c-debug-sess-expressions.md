---
id: "cda-troubleshooting-c-and-c-debug-sess-expressions"
type: "concept"
domain: "debug"
title: "Troubleshooting C and C++ debug sessions: Expressions"
summary: "evaluate_expression takes C or C++ as the debugger reads it, in the frame VS Code has in focus (normally the top frame of the stop):"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@7db44ba:docs/agent-resources/troubleshooting/cpp.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/cpp.md#expressions"
license: "Apache-2.0"
mode: "V"
---

`evaluate_expression` takes C or C++ as the debugger reads it, in the frame VS Code has in focus (normally the top frame of the stop):

- Members, elements, addresses: `cfg.mode`, `node->next->len`, `buf[7]`, `&buf[0]`, `sizeof(buf) / sizeof(buf[0])`.
- A raw address, or memory reinterpreted through a cast: `*(uint32_t *)0x20000100`, `((struct msg_hdr *)rx)->len`.
- Registers: `$pc` and `$sp` everywhere, `$lr` and `$r0` on 32-bit Arm, `$x0` on AArch64, `$rip` on x86-64.
- Hex: append `,x` (`status,x`); `cppdbg` and the CMSIS Debugger both accept it.
- Out of scope in GDB: `'uart.c'::rx_count` for a static in another file, `parse::depth` for a static inside a function. For a caller's locals, take its `frameId` from `get_call_stack` and call `get_frame_variables`.
- On GDB-based adapters a struct evaluates to `{...}` and an array to its length, like `[16]`. Ask for members and elements, or print the whole value: `-exec print cfg`, `-exec print/x *ptr@16` (16 elements behind `ptr`), `-exec x/16xb ptr` (raw bytes).
- Assignments, `++` and calls change the program: `crc(buf, 4)` executes `crc`, on firmware on the target itself. Keep inspection free of side effects unless the change is the experiment.
- On the CMSIS Debugger an expression GDB cannot evaluate comes back as `Error: could not evaluate expression`; `-exec print <expr>` reports GDB's own reason.
