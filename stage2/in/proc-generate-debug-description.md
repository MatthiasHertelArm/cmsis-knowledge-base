# PROCEDURE

---
type: "procedure"
domain: "pack"
title: "generate-debug-description"
summary: "Add or review non-sequence CMSIS-Pack Debug Description content in an existing Device Family Pack PDSC. Use for debug, debugconfig, dbg_datapatch, debug-port, or access-port definitions after `$debug-access-knowledge` has established the required access facts. Do not collect knowledge, generate or update debugvars, implement device debug sequences, or generate CoreSight trace sequences."
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
---

# Generate Debug Description

## Target & Persona

- **Role:** CMSIS-Pack Tool Integrator and Verification Engineer.
- **Objective:** Apply every verified non-sequence debug-description definition to the selected existing DFP scope.

## Prerequisites & Context

- **Expected input:** An existing target `.pdsc`, selected family/subFamily/device/variant scope, affected `<processor>` descriptions, and a current `.agent-artifacts/<pdsc-stem>.debug-access-knowledge.md` record.
- **Dependencies:** `$debug-access-knowledge`; `$validate-pdsc-sequence-xml` for common PDSC/XML and block-format validation; the current [Open-CMSIS-Pack *Debug Description* specification](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html); and `references/description-contract.md`.
- **Portability:** Support any existing CMSIS Device Family Pack whose selected scope and debug topology are documented. Do not assume a device family, debug probe, toolchain, or runtime target.

## Execution Steps (Strict Workflow)

1. **Analysis:** Locate the target PDSC, selected scope, affected processors, and read-only debug-access knowledge record. Require a current record covering the selected connection and non-sequence definitions; return to `$debug-access-knowledge` when it is absent, blocked, stale, contradictory, or insufficient.
2. **Processing:** Read `references/description-contract.md` before editing. Translate only verified facts into correctly inherited or local `debugconfig`, `debug`, `debug-port`, `access-port`, and `dbg_datapatch` definitions. Present the debug-access knowledge record and proposed XML, then apply only user-confirmed changes.
3. **Validation:** Run `$validate-pdsc-sequence-xml` after applying the confirmed change. For a non-sequence-only change, inspect its file-wide block-format matches and record that the change introduced no C-like block content; resolve every relevant validation failure.
4. **Formatting:** Report emitted definitions, placement and applicability, sources, confidence, unresolved items, and validation results.

## Guardrails & Constraints (Strict Rules)

- **No fabrication:** Do not invent topology facts, addresses, protocols, patches, values, or applicability. Return missing or contradictory hardware facts to `$debug-access-knowledge`.
- **Portability:** Do not introduce a device-family, debugger, toolchain, or runtime-target dependency unless authoritative inputs require it. Identify each required dependency in the output.
- **Critical blockers:** Stop when no existing device description exists, the knowledge record is inadequate, user confirmation is absent, or XML/PDSC validation fails.
- **Scope:** Generate only non-sequence definitions. Preserve `debugvars`, debug sequences, trace sequences, and unrelated PDSC content; direct runtime choices to the appropriate sequence skill.
- **Tone and style:** Respond factually and directly. Omit conversational filler.

## Expected Output

Apply the confirmed non-sequence PDSC definitions and report their XML placement, applicability, evidence, unresolved items, and validation results.

## Validation Resources

Read [the debug-description contract](references/description-contract.md) in full before editing. It defines grammar authority, placement rules, confirmation requirements, and the required `$validate-pdsc-sequence-xml` handoff.


# RULE

---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
shared: false
id: "rule-critical-blockers-generate-debug-description"
constrains: ["proc-generate-debug-description"]
---

Stop when no existing device description exists, the knowledge record is inadequate, user confirmation is absent, or XML/PDSC validation fails.


# RULE

---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
shared: false
id: "rule-no-fabrication-generate-debug-description"
constrains: ["proc-generate-debug-description"]
---

Do not invent topology facts, addresses, protocols, patches, values, or applicability. Return missing or contradictory hardware facts to `$debug-access-knowledge`.


# RULE

---
type: "rule"
title: "Portability"
severity: "must"
status: "draft"
shared: true
id: "rule-portability-generate-debug-description"
constrains: ["proc-generate-debug-description", "proc-generate-debug-sequences", "proc-generate-trace-sequences"]
refines: ["rule-portability"]
delta_of: "rule-portability"
---

Do not introduce a device-family, debugger, toolchain, or runtime-target dependency unless authoritative inputs require it. Identify each required dependency in the output.

## Delta zu rule-portability

unless authoritative inputs require it. Identify each required dependency in the output.


# RULE

---
type: "rule"
title: "Scope"
severity: "must"
status: "draft"
shared: false
id: "rule-scope-generate-debug-description"
constrains: ["proc-generate-debug-description"]
---

Generate only non-sequence definitions. Preserve `debugvars`, debug sequences, trace sequences, and unrelated PDSC content; direct runtime choices to the appropriate sequence skill.


# RULE

---
type: "rule"
title: "Tone and style"
severity: "must"
status: "draft"
shared: true
id: "rule-tone-and-style"
constrains: ["proc-add-cmsis-target", "proc-apply-confirmed-pdsc-proposal", "proc-board-debug-knowledge", "proc-check-cmsis-environment", "proc-check-pyocd-availability", "proc-check-zephyr-environment", "proc-cmsis-stream", "proc-create-csolution-github-action", "proc-debug-access-knowledge", "proc-debug-knowledge", "proc-evaluate-ethos-u-variants", "proc-generate-debug-description", "proc-generate-debug-sequences", "proc-generate-trace-sequences", "proc-identify-cmsis-board-layer", "proc-identify-cmsis-board-support", "proc-identify-zephyr-board", "proc-manage-pdsc-debugvars", "proc-prepare-pdsc-sequence-change", "proc-pyocd-detect-debug-topology", "proc-resolve-official-device-documentation", "proc-start-zephyr-project", "proc-validate-pdsc-sequence-xml"]
canonical: true
---

Respond factually and directly. Omit conversational filler.
