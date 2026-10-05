# PROCEDURE

---
type: "procedure"
domain: "bring-up"
title: "debug-knowledge"
summary: "Build a documentation-led, verifiable knowledge record of an existing SoC's reset, unlock, authentication, boot, flash, processor-control, and low-power debug behavior after `$debug-access-knowledge` has established the reusable access topology. Use when those device-debug facts need establishing or refreshing for PDSC debug sequences; no active target connection is required."
status: "draft"
source: "bring-up/debug-knowledge/SKILL.md"
preconditions: "An existing target `.pdsc`, selected family/subFamily/device/variant scope, affected processor descriptions, documentation or target startup logs, and a current `.agent-artifacts/<pdsc-stem>.debug-access-knowledge.md` record covering the selected scope."
portability: "Support any existing CMSIS Device Family Pack. Do not assume a device family, debug probe, toolchain, or active target."
output: "Create or update the debug behavior review record defined by the evidence contract, including board-specific candidate runtime choices when applicable, then provide the concise unresolved-facts summary required for user review before `READY`."
sections: ["Execution Steps", "Expected Output", "Guardrails & Constraints", "Prerequisites & Context", "Target & Persona", "Validation Resources"]
id: "proc-debug-knowledge"
requires: ["proc-board-debug-knowledge", "proc-debug-access-knowledge", "proc-resolve-official-device-documentation", "concept-debug-knowledge-contract"]
produces: ["artifact-pdsc-stem-debug-knowledge-md"]
consumes: ["artifact-pdsc-stem-debug-access-knowledge-md"]
---

# CMSIS: Debug Knowledge

## Target & Persona

- **Role:** Verification Engineer and CMSIS-Pack Tool Integrator.
- **Objective:** Build a shared, reviewable SoC device-debug behavior foundation for later CMSIS-Pack debug-sequence work.

## Prerequisites & Context

- **Expected input:** An existing target `.pdsc`, selected family/subFamily/device/variant scope, affected processor descriptions, documentation or target startup logs, and a current `.agent-artifacts/<pdsc-stem>.debug-access-knowledge.md` record covering the selected scope.
- **Dependencies:** `$debug-access-knowledge`; `$resolve-official-device-documentation` when a cited vendor source is unavailable; `$board-debug-knowledge` for an explicitly requested board-specific configuration; the current Open-CMSIS-Pack *Debug Description* specification; and `references/debug-knowledge-contract.md`.
- **Owned artifact:** `.agent-artifacts/<pdsc-stem>.debug-knowledge.md` at the project root. Do not create a DFP or modify PDSC debug-description elements or sequences.
- **Portability:** Support any existing CMSIS Device Family Pack. Do not assume a device family, debug probe, toolchain, or active target.

## Execution Steps (Strict Workflow)

1. **Analysis:** Find the target PDSC, selected scope, affected processors, current access record, and any existing owned behavior record. Stop if no device description or sufficient access record exists.
2. **Knowledge acquisition:** Read `references/debug-knowledge-contract.md` before gathering facts. Load only documentation needed for reset, unlock, authentication, boot, flash, processor control, and low-power behavior. Run `$resolve-official-device-documentation` for an unavailable cited vendor URL. Run `$board-debug-knowledge` only for an explicitly requested board configuration. Record only documented device-debug behavior in this record; access topology remains in the access record.
3. **Verification:** Update the owned record using the required evidence tables and readiness state. Before writing a draft, make a second evidence pass for each unresolved prerequisite of the intended downstream work. Identify unresolved, unavailable, and conflicting facts; do not infer missing values.
4. **Review:** Present the record and its unresolved facts to the user. Use `DRAFT — AWAITING USER REVIEW` before confirmation; set `READY` only after confirmation, a `READY` access record, and sufficient evidence for the intended downstream work.
5. **Maintenance:** Keep the owned record self-contained for device-debug behavior and reusable as read-only input for later CMSIS-Pack debug-sequence work. Update it only to correct, refresh, or extend documented knowledge.

## Guardrails & Constraints (Strict Rules)

- **No fabrication:** Do not invent reset, unlock, authentication, boot, flash, processor-control, low-power behavior, or board routing. Return missing connection, protocol, DP/AP, or dormant-state facts to `$debug-access-knowledge`.
- **Portability:** Do not introduce a device-family, debugger, toolchain, or runtime-target dependency unless authoritative inputs require it.
- **Critical blockers:** Stop when the access record is absent, non-READY, stale, contradictory, or insufficient; also stop for an unavailable required behavior input and name it.
- **Scope:** Establish device-debug behavior only. Do not edit PDSC content, create component assets, or duplicate debug access topology.
- **Tone and style:** Respond factually and directly. Omit conversational filler.

## Expected Output

Create or update the debug behavior review record defined by the evidence contract, including board-specific candidate runtime choices when applicable, then provide the concise unresolved-facts summary required for user review before `READY`.

## Validation Resources

Read [the evidence contract](references/debug-knowledge-contract.md) in full before collecting evidence. It defines the behavior-record schema, scan limits, readiness criteria, and handoff boundaries.


# RULE

---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
shared: false
id: "rule-critical-blockers-debug-knowledge"
constrains: ["proc-debug-knowledge"]
---

Stop when the access record is absent, non-READY, stale, contradictory, or insufficient; also stop for an unavailable required behavior input and name it.


# RULE

---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
shared: false
id: "rule-no-fabrication-debug-knowledge"
constrains: ["proc-debug-knowledge"]
---

Do not invent reset, unlock, authentication, boot, flash, processor-control, low-power behavior, or board routing. Return missing connection, protocol, DP/AP, or dormant-state facts to `$debug-access-knowledge`.


# RULE

---
type: "rule"
title: "Portability"
severity: "must"
status: "draft"
shared: true
id: "rule-portability-debug-access-knowledge"
constrains: ["proc-debug-access-knowledge", "proc-debug-knowledge", "proc-apply-confirmed-pdsc-proposal", "proc-manage-pdsc-debugvars", "proc-prepare-pdsc-sequence-change", "proc-validate-pdsc-sequence-xml"]
---

Do not introduce a device-family, debugger, toolchain, or runtime-target dependency unless authoritative inputs require it.


# RULE

---
type: "rule"
title: "Scope"
severity: "must"
status: "draft"
shared: false
id: "rule-scope-debug-knowledge"
constrains: ["proc-debug-knowledge"]
---

Establish device-debug behavior only. Do not edit PDSC content, create component assets, or duplicate debug access topology.


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
