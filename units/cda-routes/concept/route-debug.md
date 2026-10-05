---
type: "concept"
domain: "debug"
title: "Live debugging: which procedure"
summary: "Live debugging: which procedure fits a task, and the usual order."
status: "draft"
source: "CMSIS-Developer-Assistant/scripts/skills.config.json"
id: "route-debug"
references: ["proc-cmsis-debug-live", "proc-debugger-troubleshooting", "proc-fvp-debug-setup"]
---

# Live debugging: which procedure

Read the procedure with `knowledge_get` before acting on it, and follow its own prerequisites and guardrails. A `$name` inside a procedure is the procedure `proc-<name>`.

| If the task is to … | Procedure |
|---|---|
| Investigate a firmware runtime bug on a live Cortex-M debug session: faults, hangs, wrong values, silent peripherals | `proc-cmsis-debug-live` |
| Find out why a debug or flash session fails to start, connect or program | `proc-debugger-troubleshooting` |
| Make Load & Debug and Run work against an Arm FVP model | `proc-fvp-debug-setup` |
