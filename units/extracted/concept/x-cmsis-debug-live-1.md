---
id: "x-cmsis-debug-live-1"
type: "concept"
domain: "debug"
title: "Cortex-M breakpoint budget (FPB comparators)"
status: "draft"
extracted_from: "proc-cmsis-debug-live"
source: "cmsis-debug-live/SKILL.md"
---

Breakpoints in flash use the FPB comparators: commonly **6** on Cortex-M4/M7, **4** on Cortex-M0+. Past that, breakpoints silently fail to bind or the adapter reports an error. `clear_all_breakpoints` between hypotheses. In RAM, software breakpoints are unlimited.
