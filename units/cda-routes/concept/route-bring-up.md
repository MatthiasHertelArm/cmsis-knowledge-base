---
type: "concept"
domain: "bring-up"
title: "Device debug and trace knowledge: which procedure"
summary: "Establish verifiable device debug and trace facts from documentation: which procedure fits a task, and the usual order."
triggers: ["Establish documentation-led, verifiable device debug and trace facts for an SoC or board before CMSIS-Pack debug content is authored: the debug access topology (processor association, debug-port and access-port path, protocol, dormant state), reset, unlock, authentication, boot, flash and low-power debug behaviour, CoreSight trace paths and components, board connector, jumper and pin-routing choices, supplementary pyOCD topology scans, pyOCD availability, and recovery of moved or broken vendor documentation URLs. Use when the user asks how a device is debugged, what its debug or trace topology is, wants a debug or trace knowledge record (.agent-artifacts) built or refreshed, or before generating PDSC debug or trace sequences; this skill routes to the specialised bring-up skills installed next to it. No live target connection is required; for a live session use cmsis-debug-live."]
status: "draft"
source: "CMSIS-Developer-Assistant/scripts/skills.config.json"
id: "route-bring-up"
references: ["proc-board-debug-knowledge", "proc-check-pyocd-availability", "proc-cmsis-pack-docs", "proc-debug-access-knowledge", "proc-debug-knowledge", "proc-pyocd-detect-debug-topology", "proc-resolve-official-device-documentation", "proc-trace-knowledge"]
---

# Device debug and trace knowledge: which procedure

Read the procedure with `knowledge_get` before acting on it, and follow its own prerequisites and guardrails. A `$name` inside a procedure is the procedure `proc-<name>`.

| If the task is to … | Procedure |
|---|---|
| Document a named board's supported debug and trace connector, jumper, pin-routing, and configuration choices without narrowing device-level Pack support. | `proc-board-debug-knowledge` |
| Checks whether pyOCD is available, preferring the bundled copy of the active Visual Studio Code CMSIS Debugger extension and otherwise a runnable pyocd in the active shell, and returns one … | `proc-check-pyocd-availability` |
| Look up registers, peripherals, errata and board facts in the target's manuals, with page citations | `proc-cmsis-pack-docs` |
| Build a documentation-led, verifiable record of an existing SoC's reusable CMSIS debug access topology: processor association, debug port and access-port path, protocol, and dormant-state decision. | `proc-debug-access-knowledge` |
| Build a documentation-led, verifiable knowledge record of an existing SoC's reset, unlock, authentication, boot, flash, processor-control, and low-power debug behavior after `$debug-access-knowledge` has established the reusable access topology. | `proc-debug-knowledge` |
| Capture supplementary, non-authoritative CMSIS debug and CoreSight topology evidence from the complete stdout/stderr of `pyocd gdbserver -vv --target cortex_m` after `$check-pyocd-availability` succeeds. | `proc-pyocd-detect-debug-topology` |
| Recover or conclusively account for an unavailable vendor device-documentation URL by finding the current official source and returning a traceable retrieval result. | `proc-resolve-official-device-documentation` |
| Build a documentation-led, verifiable knowledge record of an existing SoC's CoreSight trace paths, components, operating requirements, and constraints for subsequent generation of PDSC trace sequences. | `proc-trace-knowledge` |

## Typical order

1. `proc-debug-access-knowledge` first — the access topology every other record builds on.
2. `proc-debug-knowledge` and/or `proc-trace-knowledge` for behaviour and trace facts; `proc-board-debug-knowledge` only for an explicitly board-specific question.
3. `proc-check-pyocd-availability`, then `proc-pyocd-detect-debug-topology`, when documentation leaves a required observation open.
4. `proc-resolve-official-device-documentation` whenever a vendor document link is dead or has moved.
