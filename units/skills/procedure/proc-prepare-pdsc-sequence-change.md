---
type: "procedure"
domain: "pack"
title: "prepare-pdsc-sequence-change"
summary: "Prepare an evidence-backed CMSIS-Pack PDSC sequence-change summary through the active conversation before debug or trace sequence assembly: scope, sources, existing and inherited definitions, proposed placements, evidence, and open questions."
status: "draft"
source: "pack/prepare-pdsc-sequence-change/SKILL.md"
license: "Apache-2.0"
preconditions: "Existing target `.pdsc`, selected device-tree scope, `debug` or `trace` domain, verified facts and source references, and the requested outcome."
portability: "Support any existing CMSIS Device Family Pack. Do not assume a device family, debug probe, toolchain, or active target."
output: "Return the prepared-change summary in conversation. Do not create or update workspace files."
sections: ["Execution Steps", "Expected Output", "Guardrails & Constraints", "Prerequisites & Context", "Target & Persona", "Validation Resources"]
id: "proc-prepare-pdsc-sequence-change"
requires: ["proc-debug-access-knowledge", "proc-debug-knowledge", "proc-trace-knowledge"]
references: ["doc-open-cmsis-pack-github-io-open-cmsis-pack-spec-main-html-deb"]
description: "Prepare an evidence-backed CMSIS-Pack PDSC sequence-change summary through the active conversation before debug or trace sequence assembly. Use when scoping a PDSC sequence change, checking verified knowledge facts and inherited definitions, or selecting shared-versus-leaf placement; do not create, read, or update agent-artifact records."
triggers: ["scoping a PDSC sequence change", "checking verified knowledge facts and inherited definitions", "selecting shared-versus-leaf placement"]
verification: ["Cross-check every proposed placement against the selected descendants and identify missing facts with their required source category.", "Use the selected PDSC subtree and the current Debug Description specification to verify inheritance, placement, and sequence context before returning the summary."]
stop_conditions: ["Stop when the target PDSC, selected scope, current specification, or required verified facts are insufficient."]
unmapped: ["CMSIS-Pack PDSC", "debugvars", "sequences"]
stage2: "proc-prepare-pdsc-sequence-change.json"
---

# Prepare PDSC Sequence Change

## Target & Persona

- **Role:** CMSIS-Pack Tool Integrator and Verification Engineer.
- **Objective:** Return a verified placement and scope summary for one debug or trace PDSC sequence change.

## Prerequisites & Context

- **Expected input:** Existing target `.pdsc`, selected device-tree scope, `debug` or `trace` domain, verified facts and source references, and the requested outcome.
- **Dependencies:** Current [Open-CMSIS-Pack *Debug Description* specification](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html); verified facts derived from `proc-debug-access-knowledge` (`knowledge_get`), `proc-debug-knowledge` (`knowledge_get`), or `proc-trace-knowledge` (`knowledge_get`) when applicable.
- **Portability:** Support any existing CMSIS Device Family Pack. Do not assume a device family, debug probe, toolchain, or active target.

## Execution Steps (Strict Workflow)

1. **Analysis:** Locate the selected family/subFamily/device/variant subtree, existing `<debugvars>` and `<sequences>` definitions, and inherited definitions.
2. **Processing:** Check that the verified facts support the requested outcome, read the current specification for grammar and execution context, and recommend the topmost selected common placement. Put only proven deviations on outer leaf variants.
3. **Validation:** Cross-check every proposed placement against the selected descendants and identify missing facts with their required source category. Do not fill gaps with variables or assumptions.
4. **Formatting:** Return a prepared-change summary in conversation: scope, sources, existing/inherited definitions, proposed placements, affected processors where relevant, evidence, and open questions.

## Guardrails & Constraints (Strict Rules)

- **No fabrication:** Do not invent device behavior, addresses, sequence defaults, applicability, or placement facts.
- **Portability:** Do not introduce a device-family, toolchain, debugger, or runtime-target dependency unless authoritative inputs require it.
- **Critical blockers:** Stop when the target PDSC, selected scope, current specification, or required verified facts are insufficient.
- **Scope:** Prepare shared integration analysis only. Do not design debug behavior, trace topology, variables, XML, or user-owned file changes.
- **Tone and style:** Respond factually and directly. Omit conversational filler.

## Expected Output

Return the prepared-change summary in conversation. Do not create or update workspace files.

## Validation Resources

Use the selected PDSC subtree and the current Debug Description specification to verify inheritance, placement, and sequence context before returning the summary.
