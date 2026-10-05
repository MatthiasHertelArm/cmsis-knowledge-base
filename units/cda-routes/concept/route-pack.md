---
type: "concept"
domain: "pack"
title: "CMSIS-Pack debug authoring: which procedure"
summary: "Author, validate and apply PDSC debug and trace sequences and debugvars: which procedure fits a task, and the usual order."
triggers: ["Author and maintain CMSIS-Pack Debug Description content in a Device Family Pack PDSC: device-specific debug sequences (unlock, debug-port setup, reset, bootloader, flash, debug authentication, multi-core start, sleep and low-power), CoreSight trace sequences (TraceStart, TraceCapture, TraceFlush, TraceStop), <debugvars> runtime variables, and the non-sequence <debug>, <debugconfig>, debug-port and access-port definitions — each evidence-backed, validated, and applied only after the user confirms. Use when the user wants to add, change, review, validate or apply PDSC debug or trace sequences or debugvars for a device; this skill routes to the specialised pack-authoring skills installed next to it. Not for a live debug session (cmsis-debug-live) or for first establishing a device's debug facts (cmsis-bring-up)."]
status: "draft"
source: "CMSIS-Developer-Assistant/scripts/skills.config.json"
id: "route-pack"
references: ["proc-apply-confirmed-pdsc-proposal", "proc-generate-debug-description", "proc-generate-debug-sequences", "proc-generate-trace-sequences", "proc-manage-pdsc-debugvars", "proc-prepare-pdsc-sequence-change", "proc-validate-pdsc-sequence-xml"]
---

# CMSIS-Pack debug authoring: which procedure

Read the procedure with `knowledge_get` before acting on it, and follow its own prerequisites and guardrails. A `$name` inside a procedure is the procedure `proc-<name>`.

| If the task is to … | Procedure |
|---|---|
| Apply a complete, explicitly confirmed CMSIS-Pack PDSC sequence or `debugvars` proposal from the active conversation unchanged, run the common and domain-specific validation, and return the application result in conversation. | `proc-apply-confirmed-pdsc-proposal` |
| Add or review non-sequence CMSIS-Pack Debug Description content in an existing Device Family Pack PDSC, applying only user-confirmed definitions and reporting their XML placement, applicability, evidence, unresolved items, and validation … | `proc-generate-debug-description` |
| Adds evidence-backed, device-specific non-trace CMSIS-Pack Debug Description sequences to an existing Device Family Pack PDSC, keeps a private proposal record, applies the confirmed change, and reports validation results. | `proc-generate-debug-sequences` |
| Add modular, evidence-backed CoreSight trace sequences to an existing CMSIS Device Family Pack PDSC, keep a private proposal record, apply the confirmed trace XML, and report trace paths, placement, placeholders, … | `proc-generate-trace-sequences` |
| Design a documented CMSIS-Pack PDSC `debugvars` runtime choice through the active conversation, returning the `__var` definition, sequence use, scope, collision result, and optional `.dbgconf` annotation without creating or updating workspace … | `proc-manage-pdsc-debugvars` |
| Prepare an evidence-backed CMSIS-Pack PDSC sequence-change summary through the active conversation before debug or trace sequence assembly: scope, sources, existing and inherited definitions, proposed placements, evidence, and open questions. | `proc-prepare-pdsc-sequence-change` |
| Validate common CMSIS-Pack PDSC sequence XML and C-like block formatting through the active conversation after a proposed or applied change, returning commands, inspected matches, failures, resolutions, and `PASS` or `FAIL`. | `proc-validate-pdsc-sequence-xml` |

## Typical order

1. Facts first: `$debug-access-knowledge`, then `$debug-knowledge` and/or `$trace-knowledge` (bring-up) must have produced their knowledge records.
2. `proc-prepare-pdsc-sequence-change` to scope the change, check inherited definitions and choose shared-versus-leaf placement.
3. `proc-generate-debug-description`, `proc-generate-debug-sequences`, `proc-generate-trace-sequences` or `proc-manage-pdsc-debugvars` for the content itself.
4. `proc-validate-pdsc-sequence-xml` on the proposal.
5. `proc-apply-confirmed-pdsc-proposal` only after the user has explicitly confirmed the edits.
