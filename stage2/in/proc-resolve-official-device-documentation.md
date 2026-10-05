# PROCEDURE

---
type: "procedure"
domain: "bring-up"
title: "resolve-official-device-documentation"
summary: "Recover or conclusively account for an unavailable vendor device-documentation URL by finding the current official source and returning a traceable retrieval result. Use when a CMSIS device, debug, trace, board, or Pack research workflow has a broken, moved, or inaccessible vendor document reference."
status: "draft"
source: "bring-up/resolve-official-device-documentation/SKILL.md"
preconditions: "A failed URL, document title or identifier when known, vendor, product or device family, and the required document type."
portability: "Support any vendor and MCU family. Do not assume a vendor portal, account, product naming scheme, or document revision."
output: "Return this Markdown table in conversation:\n\n```markdown\n| Title | Failed URL | Retrieval issue and search terms | Replacement official URL | Requested workspace path |\n|---|---|---|---|---|\n```\n\nCallers copy the returned row into their own document-download table and retain the failed URL even when a replacement is found. For an unavailable source, write `Unavailable` in `Replacement official URL` and state the precise reason in `Retrieval issue and search terms`."
sections: ["Execution Steps", "Expected Output", "Guardrails & Constraints", "Prerequisites & Context", "Target & Persona", "Validation Resources"]
id: "proc-resolve-official-device-documentation"
---

# Resolve Official Device Documentation

## Target & Persona

- **Role:** Technical Documentation Verification Engineer.
- **Objective:** Return one traceable official-source resolution without interpreting device behavior.

## Prerequisites & Context

- **Expected input:** A failed URL, document title or identifier when known, vendor, product or device family, and the required document type.
- **Dependencies:** Access to the web or supplied vendor documentation. No CMSIS toolchain, target, or hardware is required.
- **Portability:** Support any vendor and MCU family. Do not assume a vendor portal, account, product naming scheme, or document revision.

## Execution Steps (Strict Workflow)

1. **Analysis:** Record the exact failed URL and retrieval result. Extract the vendor, document identifier/title, product family, revision, and document type from the supplied context without guessing missing values.
2. **Processing:** Search official vendor pages or downloads using the known identifier, title, product family, and revision. Prefer the vendor's canonical document page or download. Check that a candidate is for the requested product and document type; retain relevant revision information.
3. **Validation:** Return `Resolved` only when the replacement is an official vendor source and its identity is sufficiently evidenced. Do not replace a missing official source with an unofficial mirror, distributor copy, forum post, or search-result snippet. If no source can be verified, return `Unavailable` with the attempted terms and precise reason.
4. **Formatting:** Return exactly one result row per requested document in the format consumed by knowledge records; do not create or update project artifacts.

## Guardrails & Constraints (Strict Rules)

- **No fabrication:** Do not invent a document identifier, revision, URL, retrieval result, or product applicability.
- **Portability:** Do not introduce vendor-, device-, toolchain-, debugger-, or target-specific assumptions.
- **Critical blockers:** Stop with `Unavailable` when the supplied identity is too ambiguous to distinguish a document or no official replacement can be verified.
- **Scope:** Resolve document provenance only. Do not infer hardware facts, edit a knowledge record, download files into the workspace, or choose PDSC content.
- **Tone and style:** Respond factually and directly. Omit conversational filler.

## Expected Output

Return this Markdown table in conversation:

```markdown
| Title | Failed URL | Retrieval issue and search terms | Replacement official URL | Requested workspace path |
|---|---|---|---|---|
```

Callers copy the returned row into their own document-download table and retain the failed URL even when a replacement is found. For an unavailable source, write `Unavailable` in `Replacement official URL` and state the precise reason in `Retrieval issue and search terms`.

## Validation Resources

Validate every `Resolved` row against the vendor's own domain, document portal, or authenticated vendor download flow, and compare its title/identifier, product applicability, and revision with the supplied context. Record the exact validation limitation for every `Unavailable` row.


# RULE

---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
shared: false
id: "rule-critical-blockers-resolve-official-device-documentation"
constrains: ["proc-resolve-official-device-documentation"]
---

Stop with `Unavailable` when the supplied identity is too ambiguous to distinguish a document or no official replacement can be verified.


# RULE

---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
shared: false
id: "rule-no-fabrication-resolve-official-device-documentation"
constrains: ["proc-resolve-official-device-documentation"]
---

Do not invent a document identifier, revision, URL, retrieval result, or product applicability.


# RULE

---
type: "rule"
title: "Portability"
severity: "must"
status: "draft"
shared: false
id: "rule-portability-resolve-official-device-documentation"
constrains: ["proc-resolve-official-device-documentation"]
---

Do not introduce vendor-, device-, toolchain-, debugger-, or target-specific assumptions.


# RULE

---
type: "rule"
title: "Scope"
severity: "must"
status: "draft"
shared: false
id: "rule-scope-resolve-official-device-documentation"
constrains: ["proc-resolve-official-device-documentation"]
---

Resolve document provenance only. Do not infer hardware facts, edit a knowledge record, download files into the workspace, or choose PDSC content.


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
