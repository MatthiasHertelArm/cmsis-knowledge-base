---
id: "cda-troubleshooting-c-and-c-debug-sess-build-for-the-debugger"
type: "concept"
domain: "debug"
title: "Troubleshooting C and C++ debug sessions: Build for the debugger"
summary: "Troubleshooting C and C++ debug sessions: Build for the debugger"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@29d444c:docs/agent-resources/troubleshooting/cpp.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/29d444c/docs/agent-resources/troubleshooting/cpp.md#build-for-the-debugger"
license: "Apache-2.0"
mode: "V"
---

- Compile with debug information (`-g`) and little optimisation (`-Og` or `-O0`). In a csolution the build-type carries both: `debug: on` and `optimize: debug` (or `none`).
- The session has to run what you just built: `stop_debugging`, `cmsis_action build`, then `cmsis_action load_and_debug` for firmware; start a host program again. A stale ELF or an unflashed board puts breakpoints and line numbers in the wrong places.
- `<optimized out>` means the variable has no home at this PC. Read it where it is computed or used, or rebuild with less optimisation.
- From `-O1` upwards, stepping jumps back and forth because the compiler interleaves the instructions of neighbouring lines and merges inlined functions into their callers. Follow the logic in a debug build; keep the optimised one for what only happens there.
- A defect that vanishes at `-O0` or under the debugger points to undefined behaviour (an uninitialised read, an out-of-bounds write, a missing `volatile`) or to timing.
