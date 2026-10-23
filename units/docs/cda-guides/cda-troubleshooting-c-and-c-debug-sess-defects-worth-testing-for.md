---
id: "cda-troubleshooting-c-and-c-debug-sess-defects-worth-testing-for"
type: "concept"
domain: "debug"
title: "Troubleshooting C and C++ debug sessions: Defects worth testing for"
summary: "Troubleshooting C and C++ debug sessions: Defects worth testing for"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@29d444c:docs/agent-resources/troubleshooting/cpp.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/29d444c/docs/agent-resources/troubleshooting/cpp.md#defects-worth-testing-for"
license: "Apache-2.0"
mode: "V"
---

- **Uninitialised local:** stop on the function's first line and read the variable before its first assignment. In a debug build it often still holds the previous call's value, which looks plausible.
- **Out-of-bounds write:** a neighbour changes although no code writes it. `-exec watch neighbour` stops on the store that does; compare the index with `sizeof(buf) / sizeof(buf[0])` and `&buf[N]` with `&neighbour`.
- **Dangling pointer:** a pointer to a local of a function that has returned points into the stack below the current `$sp` (stacks grow downwards on Arm and x86). Memory behind a freed pointer changes under you; `-exec watch -l *p` stops at the store that changes it. On the host, a build with `-fsanitize=address` stops at the first invalid access.
- **Integer overflow and signed/unsigned mix-ups:** evaluate the sub-expressions in the program's own types. `len - 1` wraps to the maximum when an unsigned `len` is 0, `a * b` overflows in `int` before the result reaches a `long long`, and `-1 < sizeof(x)` is false. Plain `char` is unsigned with arm-none-eabi-gcc and signed on x86: evaluate `(int)c`.
- **Missing `volatile`:** a flag set by an interrupt handler or another thread reads 1 in `evaluate_expression`, yet the loop that polls it keeps spinning. `-exec disassemble` shows the load hoisted out of the loop, which only happens in optimised builds. ISR-shared data needs `volatile`; data shared between threads needs `_Atomic` or `std::atomic`.
