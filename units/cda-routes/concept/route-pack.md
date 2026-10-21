---
type: "concept"
domain: "pack"
title: "pack: which procedure"
summary: "pack: which procedure fits a task, and the usual order."
status: "draft"
source: "CMSIS-Developer-Assistant/scripts/skills.config.json"
license: "Apache-2.0"
id: "route-pack"
references: ["proc-apply-confirmed-pdsc-proposal", "proc-generate-debug-description", "proc-generate-debug-sequences", "proc-generate-trace-sequences", "proc-manage-pdsc-debugvars", "proc-prepare-pdsc-sequence-change", "proc-validate-pdsc-sequence-xml"]
---

# pack: which procedure

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
