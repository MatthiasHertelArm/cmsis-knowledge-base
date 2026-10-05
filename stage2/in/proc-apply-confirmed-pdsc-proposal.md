# PROCEDURE

---
type: "procedure"
domain: "pack"
title: "apply-confirmed-pdsc-proposal"
summary: "Apply a complete, explicitly confirmed CMSIS-Pack PDSC sequence or `debugvars` proposal provided through the active conversation and run its required validation. Use after a debug or trace proposal has been reviewed and the user has authorized edits to the named PDSC files; do not create agent-artifact records, infer missing technical behavior, or apply changes before confirmation."
status: "draft"
source: "pack/apply-confirmed-pdsc-proposal/SKILL.md"
preconditions: "Complete debug or trace proposal in conversation with exact XML and target paths, explicit confirmation for every user-owned file, and a named common plus domain-specific validation plan."
portability: "Support any existing CMSIS Device Family Pack. Do not assume a device family, debugger, toolchain, or active target."
output: "Return the application result in conversation. The calling generator updates its private proposal record only after all checks pass."
sections: ["Execution Steps", "Expected Output", "Guardrails & Constraints", "Prerequisites & Context", "Target & Persona", "Validation Resources"]
id: "proc-apply-confirmed-pdsc-proposal"
requires: ["proc-validate-pdsc-sequence-xml"]
---

# Apply Confirmed PDSC Proposal

## Target & Persona

- **Role:** CMSIS-Pack Tool Integrator and Verification Engineer.
- **Objective:** Apply one complete approved PDSC proposal unchanged and return its validated result.

## Prerequisites & Context

- **Expected input:** Complete debug or trace proposal in conversation with exact XML and target paths, explicit confirmation for every user-owned file, and a named common plus domain-specific validation plan.
- **Dependencies:** `$validate-pdsc-sequence-xml` and the calling domain skill's validation gates.
- **Portability:** Support any existing CMSIS Device Family Pack. Do not assume a device family, debugger, toolchain, or active target.

## Execution Steps (Strict Workflow)

1. **Analysis:** Re-read target files and check that the confirmed proposal still applies. Report meaningful drift and obtain a refreshed proposal rather than applying stale XML.
2. **Processing:** Apply the complete approved change in focused patches. Preserve unrelated PDSC and `.dbgconf` content; edit `.dbgconf` only when that file is explicitly confirmed.
3. **Validation:** Run `$validate-pdsc-sequence-xml`, then the calling skill's domain-specific checks. Resolve validation failures before completion.
4. **Formatting:** Return applied files, validation results, domain-specific results, and any explicitly deferred user-owned file in conversation.

## Guardrails & Constraints (Strict Rules)

- **No fabrication:** Do not infer missing behavior, alter the approved technical design, or claim completion without all required checks.
- **Portability:** Do not introduce a device-family, debugger, toolchain, or runtime-target dependency unless authoritative inputs require it.
- **Critical blockers:** Stop when the proposal, target, confirmation, or validation plan is incomplete; also stop on meaningful file drift or validation failure.
- **Scope:** Apply only the confirmed proposal. Do not create agent artifacts or make unrelated user-owned file changes.
- **Tone and style:** Respond factually and directly. Omit conversational filler.

## Expected Output

Return the application result in conversation. The calling generator updates its private proposal record only after all checks pass.

## Validation Resources

Run `$validate-pdsc-sequence-xml` for common syntax and block checks, then the current domain contract for debug or trace semantic checks.


# RULE

---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
shared: false
id: "rule-critical-blockers-apply-confirmed-pdsc-proposal"
constrains: ["proc-apply-confirmed-pdsc-proposal"]
---

Stop when the proposal, target, confirmation, or validation plan is incomplete; also stop on meaningful file drift or validation failure.


# RULE

---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
shared: false
id: "rule-no-fabrication-apply-confirmed-pdsc-proposal"
constrains: ["proc-apply-confirmed-pdsc-proposal"]
---

Do not infer missing behavior, alter the approved technical design, or claim completion without all required checks.


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
id: "rule-scope-apply-confirmed-pdsc-proposal"
constrains: ["proc-apply-confirmed-pdsc-proposal"]
---

Apply only the confirmed proposal. Do not create agent artifacts or make unrelated user-owned file changes.


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
