---
type: "concept"
domain: "bring-up"
title: "bring-up: which procedure"
summary: "bring-up: which procedure fits a task, and the usual order."
status: "draft"
source: "CMSIS-Developer-Assistant/scripts/skills.config.json"
id: "route-bring-up"
references: ["proc-board-debug-knowledge", "proc-check-pyocd-availability", "proc-cmsis-pack-docs", "proc-debug-access-knowledge", "proc-debug-knowledge", "proc-pyocd-detect-debug-topology", "proc-resolve-official-device-documentation", "proc-trace-knowledge"]
---

# bring-up: which procedure

Read the procedure with `knowledge_get` before acting on it, and follow its own prerequisites and guardrails. A `$name` inside a procedure is the procedure `proc-<name>`.

| If the task is to … | Procedure |
|---|---|
| Document a named board's supported debug and trace connector, jumper, pin-routing, and configuration choices without narrowing device-level Pack support, returning an evidenced option inventory and candidate runtime choices in conversation. | `proc-board-debug-knowledge` |
| Checks whether pyOCD is available, preferring the bundled copy of the active Visual Studio Code CMSIS Debugger extension and otherwise a runnable pyocd in the active shell, and returns one … | `proc-check-pyocd-availability` |
| Look up registers, peripherals, errata and board facts in the target's manuals, with page citations | `proc-cmsis-pack-docs` |
| Build a documentation-led, verifiable record of an existing SoC's reusable CMSIS debug access topology: processor association, debug port and access-port path, protocol, and dormant-state decision, in `.agent-artifacts/<pdsc-stem>.debug-access-knowledge.md` for user review. | `proc-debug-access-knowledge` |
| Build a documentation-led, verifiable knowledge record of an existing SoC's reset, unlock, authentication, boot, flash, processor-control, and low-power debug behavior after `proc-debug-access-knowledge` (`knowledge_get`) has established the reusable access topology, for … | `proc-debug-knowledge` |
| Capture supplementary, non-authoritative CMSIS debug and CoreSight topology evidence from the complete stdout/stderr of `pyocd gdbserver -vv --target cortex_m` after `proc-check-pyocd-availability` (`knowledge_get`) succeeds, returning the observation table and limitations in … | `proc-pyocd-detect-debug-topology` |
| Recover or conclusively account for an unavailable vendor device-documentation URL by finding the current official source and returning a traceable retrieval result. | `proc-resolve-official-device-documentation` |
| Build a documentation-led, verifiable knowledge record of an existing SoC's CoreSight trace paths, components, operating requirements, and constraints for subsequent generation of PDSC trace sequences, and present it for user … | `proc-trace-knowledge` |
