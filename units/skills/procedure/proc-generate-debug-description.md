---
type: "procedure"
domain: "pack"
title: "generate-debug-description"
summary: "Add or review non-sequence CMSIS-Pack Debug Description content in an existing Device Family Pack PDSC, applying only user-confirmed definitions and reporting their XML placement, applicability, evidence, unresolved items, and validation results."
status: "draft"
source: "pack/generate-debug-description/SKILL.md"
preconditions: "An existing target `.pdsc`, selected family/subFamily/device/variant scope, affected `<processor>` descriptions, and a current `.agent-artifacts/<pdsc-stem>.debug-access-knowledge.md` record."
portability: "Support any existing CMSIS Device Family Pack whose selected scope and debug topology are documented. Do not assume a device family, debug probe, toolchain, or runtime target."
output: "Apply the confirmed non-sequence PDSC definitions and report their XML placement, applicability, evidence, unresolved items, and validation results."
sections: ["Execution Steps", "Expected Output", "Guardrails & Constraints", "Prerequisites & Context", "Target & Persona", "Validation Resources"]
id: "proc-generate-debug-description"
requires: ["proc-debug-access-knowledge", "proc-validate-pdsc-sequence-xml", "concept-description-contract"]
consumes: ["artifact-pdsc-stem-debug-access-knowledge-md"]
references: ["doc-open-cmsis-pack-github-io-open-cmsis-pack-spec-main-html-deb"]
description: "Add or review non-sequence CMSIS-Pack Debug Description content in an existing Device Family Pack PDSC. Use for debug, debugconfig, dbg_datapatch, debug-port, or access-port definitions after `proc-debug-access-knowledge` (`knowledge_get`) has established the required access facts. Do not collect knowledge, generate or update debugvars, implement device debug sequences, or generate CoreSight trace sequences."
triggers: ["debugconfig definitions", "dbg_datapatch definitions", "debug-port definitions", "access-port definitions", "after `proc-debug-access-knowledge` (`knowledge_get`) has established the required access facts"]
verification: ["Run `proc-validate-pdsc-sequence-xml` (`knowledge_get`) after applying the confirmed change.", "For a non-sequence-only change, inspect its file-wide block-format matches and record that the change introduced no C-like block content; resolve every relevant validation failure."]
stop_conditions: ["Require a current record covering the selected connection and non-sequence definitions; return to `proc-debug-access-knowledge` (`knowledge_get`) when it is absent, blocked, stale, contradictory, or insufficient.", "Present the debug-access knowledge record and proposed XML, then apply only user-confirmed changes.", "Return missing or contradictory hardware facts to `proc-debug-access-knowledge` (`knowledge_get`).", "Stop when no existing device description exists, the knowledge record is inadequate, user confirmation is absent, or XML/PDSC validation fails."]
unmapped: ["CMSIS Device Family Pack PDSC", "CMSIS-Pack Debug Description"]
stage2: "proc-generate-debug-description.json"
---

# Generate Debug Description

## Target & Persona

- **Role:** CMSIS-Pack Tool Integrator and Verification Engineer.
- **Objective:** Apply every verified non-sequence debug-description definition to the selected existing DFP scope.

## Prerequisites & Context

- **Expected input:** An existing target `.pdsc`, selected family/subFamily/device/variant scope, affected `<processor>` descriptions, and a current `.agent-artifacts/<pdsc-stem>.debug-access-knowledge.md` record.
- **Dependencies:** `proc-debug-access-knowledge` (`knowledge_get`); `proc-validate-pdsc-sequence-xml` (`knowledge_get`) for common PDSC/XML and block-format validation; the current [Open-CMSIS-Pack *Debug Description* specification](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html); and `references/description-contract.md`.
- **Portability:** Support any existing CMSIS Device Family Pack whose selected scope and debug topology are documented. Do not assume a device family, debug probe, toolchain, or runtime target.

## Execution Steps (Strict Workflow)

1. **Analysis:** Locate the target PDSC, selected scope, affected processors, and read-only debug-access knowledge record. Require a current record covering the selected connection and non-sequence definitions; return to `proc-debug-access-knowledge` (`knowledge_get`) when it is absent, blocked, stale, contradictory, or insufficient.
2. **Processing:** Read `references/description-contract.md` before editing. Translate only verified facts into correctly inherited or local `debugconfig`, `debug`, `debug-port`, `access-port`, and `dbg_datapatch` definitions. Present the debug-access knowledge record and proposed XML, then apply only user-confirmed changes.
3. **Validation:** Run `proc-validate-pdsc-sequence-xml` (`knowledge_get`) after applying the confirmed change. For a non-sequence-only change, inspect its file-wide block-format matches and record that the change introduced no C-like block content; resolve every relevant validation failure.
4. **Formatting:** Report emitted definitions, placement and applicability, sources, confidence, unresolved items, and validation results.

## Guardrails & Constraints (Strict Rules)

- **No fabrication:** Do not invent topology facts, addresses, protocols, patches, values, or applicability. Return missing or contradictory hardware facts to `proc-debug-access-knowledge` (`knowledge_get`).
- **Portability:** Do not introduce a device-family, debugger, toolchain, or runtime-target dependency unless authoritative inputs require it. Identify each required dependency in the output.
- **Critical blockers:** Stop when no existing device description exists, the knowledge record is inadequate, user confirmation is absent, or XML/PDSC validation fails.
- **Scope:** Generate only non-sequence definitions. Preserve `debugvars`, debug sequences, trace sequences, and unrelated PDSC content; direct runtime choices to the appropriate sequence skill.
- **Tone and style:** Respond factually and directly. Omit conversational filler.

## Expected Output

Apply the confirmed non-sequence PDSC definitions and report their XML placement, applicability, evidence, unresolved items, and validation results.

## Validation Resources

Read [the debug-description contract](references/description-contract.md) in full before editing. It defines grammar authority, placement rules, confirmation requirements, and the required `proc-validate-pdsc-sequence-xml` (`knowledge_get`) handoff.
