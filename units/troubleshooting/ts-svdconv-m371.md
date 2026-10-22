---
id: "ts-svdconv-m371"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M371: … '…' <headerStructName> is equal to hierarchical name"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M371"
symptoms: ["M371", "%LEVEL% '%NAME%' <headerStructName> is equal to hierarchical name"]
symptom_regex: "^.+? '.+?' <headerStructName> is equal to hierarchical name$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file defines a peripheral, cluster or register whose name equals the header struct name that svdconv would generate for it, so the generated C header would reuse the same identifier for two different things."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M371`
`%LEVEL% '%NAME%' <headerStructName> is equal to hierarchical name`

## Cause

The SVD file defines a peripheral, cluster or register whose name equals the header struct name that svdconv would generate for it, so the generated C header would reuse the same identifier for two different things. The %LEVEL% and %NAME% in the message identify which element (peripheral, cluster or register) carries the clashing name. The exact trigger is not visible in the supplied lines, so this reading is inferred from the message text.

## Fix

Open the SVD file, find the element named in the message, and rename it or set a distinct headerStructName so the generated struct name no longer equals its hierarchical name. Then rerun svdconv.

## Note

Source lines were not available; the cause and fix rest on the message text and the README claim that the message is documented, so confidence is capped at medium. The meaning of headerStructName versus the hierarchical name should be checked against the source before relying on the exact wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
