---
id: "x-cmsis-debug-live-2"
type: "concept"
domain: "debug"
title: "Logpoints still halt the core on every hit"
status: "draft"
extracted_from: "proc-cmsis-debug-live"
source: "cmsis-debug-live/SKILL.md"
license: "Apache-2.0"
---

`add_logpoint` prints and resumes rather than halting — but the core still stops on every hit while GDB formats and prints. In an ISR or a hot loop that changes the timing you are trying to measure. For those, prefer `read_cycle_counter` around the region, or have the firmware fill a RAM buffer you read back with `read_memory`.

GDB infers nothing about types, so `{expr}` defaults to `%d` and you write `{expr:%s}` / `{expr:%f}` / `{expr:%p}` when it is not an integer. On the CMSIS Debugger a logpoint is a GDB `dprintf`: its text goes to VS Code's Debug Console, not to you, and `list_breakpoints` counts its hits.
