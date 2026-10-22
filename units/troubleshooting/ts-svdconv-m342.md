---
id: "ts-svdconv-m342"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M342: Dim-extended … '…' must not have <headerStructName>"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M342"
symptoms: ["M342", "Dim-extended %LEVEL% '%NAME%' must not have <headerStructName>"]
symptom_regex: "^Dim\\-extended .+? '.+?' must not have <headerStructName>$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file declares a dimension-extended element (one using dim/dimIncrement, such as a register or cluster array) that also sets headerStructName. svdconv rejects this combination because headerStructName is only meaningful on a non-dim-extended peripheral or cluster, and the named …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M342 text; trigger not read, clone unavailable)"]
---

## Symptom

`M342`
`Dim-extended %LEVEL% '%NAME%' must not have <headerStructName>`

## Cause

The SVD file declares a dimension-extended element (one using dim/dimIncrement, such as a register or cluster array) that also sets headerStructName. svdconv rejects this combination because headerStructName is only meaningful on a non-dim-extended peripheral or cluster, and the named element is the one shown as %LEVEL% '%NAME%' in the message. The clone was not available, so this reading comes from the message text alone.

## Fix

Open the SVD file at the element named in the message and remove the headerStructName tag from that dim-extended element. If the header structure name is still needed, set it on the non-dimensioned peripheral that the array is derived from, then run svdconv again.

## Note

Source lines were not available, so the trigger condition and the exact placement rule are inferred from the message wording and the README entry; verify against SVDConv_Msgs.cpp before relying on the fix.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M342 text; trigger not read, clone unavailable)`
