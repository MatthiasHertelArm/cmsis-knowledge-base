---
id: "cda-troubleshooting-c-and-c-debug-sess-breakpoints-that-do-not-bind-or-never-hi"
type: "concept"
domain: "debug"
title: "Troubleshooting C and C++ debug sessions: Breakpoints that do not bind or never hit"
summary: "Troubleshooting C and C++ debug sessions: Breakpoints that do not bind or never hit"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@29d444c:docs/agent-resources/troubleshooting/cpp.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/29d444c/docs/agent-resources/troubleshooting/cpp.md#breakpoints-that-do-not-bind-or-never-hit"
license: "Apache-2.0"
mode: "V"
---

- **No code on the line:** a declaration without initialiser, a comment, a lone brace, or code the optimiser removed. `evaluate_expression("-exec info line main.c:42")` reports where the line's code starts, or that it has none.
- **Different source paths:** the debug information records the paths of the build (a container, CI, another checkout), so a breakpoint on the workspace path matches nothing. Map them: `sourceFileMap` in a `cppdbg` entry, `set substitute-path <build-dir> <workspace-dir>` for GDB.
- **Another binary:** the session runs something other than the build of this source; see above.
- **Many copies:** a line in a header, an inline function or a template exists once per inlining or instantiation, so one breakpoint gets several locations and every copy stops. On Cortex-M each location takes one of the few FPB comparators. A template that is never instantiated has no code to stop in.
- **What GDB really set:** `-exec info breakpoints` lists each breakpoint with its address and hit count, `<PENDING>` when nothing matched and `<MULTIPLE>` with one sub-entry per location.
- On Cortex-M, breakpoints beyond the comparator budget do not bind; `get_debug_instructions` with topic `breakpoints` has the numbers.
