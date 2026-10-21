---
type: "procedure"
domain: "pack"
title: "generate-debug-sequences"
summary: "Adds evidence-backed, device-specific non-trace CMSIS-Pack Debug Description sequences to an existing Device Family Pack PDSC, keeps a private proposal record, applies the confirmed change, and reports validation results."
status: "draft"
source: "pack/generate-debug-sequences/SKILL.md"
license: "Apache-2.0"
preconditions: "Existing target `.pdsc`, selected family/subFamily/device/variant scope, affected processors and non-trace sequences, documented device behavior, and current `.agent-artifacts/<pdsc-stem>.debug-access-knowledge.md` and `.agent-artifacts/<pdsc-stem>.debug-knowledge.md` records."
portability: "Support any existing CMSIS Device Family Pack with documented device-specific behavior. Do not assume a device family, debug probe, toolchain, or active target; use a target only when available for validation."
output: "Create or update the private `.agent-artifacts/<pdsc-stem>.debug-sequences.md` proposal record, including proposed debugvars; apply the confirmed non-trace PDSC change; and report applicability, placement, evidence, low-power behavior, `.dbgconf` proposals, and validation results."
sections: ["Execution Steps", "Expected Output", "Guardrails & Constraints", "Prerequisites & Context", "Target & Persona", "Validation Resources"]
id: "proc-generate-debug-sequences"
requires: ["proc-apply-confirmed-pdsc-proposal", "proc-debug-access-knowledge", "proc-debug-knowledge", "proc-manage-pdsc-debugvars", "proc-prepare-pdsc-sequence-change", "proc-validate-pdsc-sequence-xml", "concept-debug-sequence-contract"]
consumes: ["artifact-pdsc-stem-debug-access-knowledge-md", "artifact-pdsc-stem-debug-knowledge-md", "artifact-pdsc-stem-debug-sequences-md"]
references: ["doc-open-cmsis-pack-github-io-open-cmsis-pack-spec-main-html-deb"]
description: "Add evidence-backed, device-specific non-trace CMSIS-Pack Debug Description sequences to an existing Device Family Pack PDSC. Use for device unlock, debug-port setup, reset, bootloader, flash, debug-authentication, multi-core startup, or reliable debug through sleep, deep-sleep, and device low-power modes after `proc-debug-access-knowledge` (`knowledge_get`) and `proc-debug-knowledge` (`knowledge_get`) have established the required facts; use the shared PDSC preparation, debugvars, application, and XML-validation skills for their respective integration work; do not use for CoreSight trace setup."
triggers: ["device unlock", "debug-port setup", "debug-authentication", "multi-core startup", "reliable debug through sleep, deep-sleep, and device low-power modes"]
verification: ["Run `proc-apply-confirmed-pdsc-proposal` (`knowledge_get`) with `proc-validate-pdsc-sequence-xml` (`knowledge_get`) as the common validation step", "Compare every overridden predefined sequence against its current specification default", "Perform documented low-power checks when a target is available", "Set `APPLIED` only after all checks pass"]
stop_conditions: ["Stop when the knowledge record is inadequate, a required specification default is unavailable, confirmation is absent, or any validation fails.", "Return insufficient access facts to `proc-debug-access-knowledge` (`knowledge_get`) and behavior facts to `proc-debug-knowledge` (`knowledge_get`).", "Present it with the proposed XML and obtain confirmation.", "Do not modify `.dbgconf` without explicit confirmation."]
unmapped: ["Device Family Pack PDSC", "CMSIS-Pack Debug Description sequences", "debugvars", ".dbgconf"]
stage2: "proc-generate-debug-sequences.json"
---

# Generate Debug Sequences

## Target & Persona

- **Role:** CMSIS-Pack Tool Integrator and Verification Engineer.
- **Objective:** Implement every verified device-specific non-trace behavior in the selected existing DFP scope.

## Prerequisites & Context

- **Expected input:** Existing target `.pdsc`, selected family/subFamily/device/variant scope, affected processors and non-trace sequences, documented device behavior, and current `.agent-artifacts/<pdsc-stem>.debug-access-knowledge.md` and `.agent-artifacts/<pdsc-stem>.debug-knowledge.md` records.
- **Dependencies:** `proc-debug-access-knowledge` (`knowledge_get`); `proc-debug-knowledge` (`knowledge_get`); `proc-prepare-pdsc-sequence-change` (`knowledge_get`); `proc-manage-pdsc-debugvars` (`knowledge_get`); `proc-apply-confirmed-pdsc-proposal` (`knowledge_get`); `proc-validate-pdsc-sequence-xml` (`knowledge_get`); current [Open-CMSIS-Pack *Debug Description* specification](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html); and `references/debug-sequence-contract.md`.
- **Portability:** Support any existing CMSIS Device Family Pack with documented device-specific behavior. Do not assume a device family, debug probe, toolchain, or active target; use a target only when available for validation.

## Execution Steps (Strict Workflow)

1. **Analysis:** Read the debug-access and device-debug behavior records and run `proc-prepare-pdsc-sequence-change` (`knowledge_get`) with `domain=debug`, passing verified facts in conversation. Require current connection facts and documented low-power behavior; return insufficient access facts to `proc-debug-access-knowledge` (`knowledge_get`) and behavior facts to `proc-debug-knowledge` (`knowledge_get`).
2. **Processing:** Read `references/debug-sequence-contract.md` and assemble only verified non-trace sequences with correct CPU applicability, placement, predefined-default provenance, and low-power behavior. In every newly authored C-like sequence expression, add concise comments that explain each command or logical command group's verified purpose, including affected register names and modified or read bit-field names whenever the verified sources identify them. For every documented user runtime choice, run `proc-manage-pdsc-debugvars` (`knowledge_get`) with prepared placement context and merge its returned definition and sequence use into this skill's private record.
3. **Validation:** Create or update `.agent-artifacts/<pdsc-stem>.debug-sequences.md` as this skill's private proposal record. Record scope, evidence, applicability, proposed debugvars, proposed XML, `.dbgconf` proposals, unresolved items, and `PROPOSED` status. Present it with the proposed XML and obtain confirmation. Then run `proc-apply-confirmed-pdsc-proposal` (`knowledge_get`) with `proc-validate-pdsc-sequence-xml` (`knowledge_get`) as the common validation step; compare every overridden predefined sequence against its current specification default and perform documented low-power checks when a target is available. Set `APPLIED` only after all checks pass.
4. **Formatting:** Report applicability, placement, sources, low-power results, `.dbgconf` proposals, unresolved items, and validation results. Do not provide the private proposal record as input to a helper or another skill.

## Guardrails & Constraints (Strict Rules)

- **No fabrication:** Do not invent reset, unlock, authentication, boot, flash, processor-control, low-power, register, delay, or connection behavior.
- **Portability:** Do not introduce a device-family, debugger, toolchain, or runtime-target dependency unless authoritative inputs require it. Identify every required dependency in the output.
- **Critical blockers:** Stop when the knowledge record is inadequate, a required specification default is unavailable, confirmation is absent, or any validation fails.
- **Scope:** Generate only non-trace sequences and related documented runtime choices. Preserve trace configuration and unrelated PDSC content; do not modify `.dbgconf` without explicit confirmation.
- **Tone and style:** Respond factually and directly. Omit conversational filler.

## Expected Output

Create or update the private `.agent-artifacts/<pdsc-stem>.debug-sequences.md` proposal record, including proposed debugvars; apply the confirmed non-trace PDSC change; and report applicability, placement, evidence, low-power behavior, `.dbgconf` proposals, and validation results.

## Validation Resources

Read [the debug-sequence contract](references/debug-sequence-contract.md) in full before assembly. Use `proc-validate-pdsc-sequence-xml` (`knowledge_get`) for common PDSC checks, compare overridden predefined sequences with current specification defaults, and perform documented low-power checks when a target is available.
