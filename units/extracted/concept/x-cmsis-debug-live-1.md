---
id: "x-cmsis-debug-live-1"
type: "concept"
domain: "debug"
title: "Cortex-M breakpoint budget (FPB code comparators)"
status: "draft"
extracted_from: "proc-cmsis-debug-live"
source: "cmsis-debug-live/SKILL.md"
license: "Apache-2.0"
---

Breakpoints in flash use the FPB code comparators: **4** on Cortex-M0/M0+/M23, **6** on M3/M4, **8** on M7/M33/M55/M85 — the table of topic `breakpoints`. A device can implement fewer; `FP_CTRL` at `0xE0002000` gives the count on the target. Past it, breakpoints silently fail to bind or the adapter reports an error. `list_breakpoints` before adding one; between hypotheses, `remove_breakpoint` for the ones you set (`clear_all_breakpoints` deletes the user's too). In RAM, software breakpoints are unlimited.
