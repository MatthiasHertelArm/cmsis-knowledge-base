---
id: "ts-svdconv-m373"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M373: … <…> '…' already defined …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M373"
symptoms: ["M373", "%LEVEL% <%TAG%> '%NAME%' already defined %LINE%"]
symptom_regex: "^.+? <.+?> '.+?' already defined .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found an SVD element whose name (the NAME placeholder) was already declared earlier under the same tag (TAG), so the duplicate definition at the reported line overrides or conflicts with the earlier one."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M373`
`%LEVEL% <%TAG%> '%NAME%' already defined %LINE%`

## Cause

svdconv found an SVD element whose name (the NAME placeholder) was already declared earlier under the same tag (TAG), so the duplicate definition at the reported line overrides or conflicts with the earlier one. The message text names the tag and the first definition's line, so the input SVD has two elements with the same name at the same scope.

## Fix

Open the SVD file at the line reported in the message and at the earlier definition it refers to, then rename or remove one of the duplicate elements so each name is unique within its parent (for example, peripheral or register names). Re-run svdconv on the corrected file.

## Note

Source lines were not available, so the trigger is inferred from the message text only; the exact scope of the uniqueness check (peripheral, register, or other) is not verified. The README is said to document this message, but its text was not provided to confirm it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
