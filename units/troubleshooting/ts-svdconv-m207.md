---
id: "ts-svdconv-m207"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M207: Expression marker found but no <dim> specified: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M207"
symptoms: ["M207", "Expression marker found but no <dim> specified: '%NAME%'"]
symptom_regex: "^Expression marker found but no <dim> specified: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Specify dimension."
summary: "The SVD register or peripheral name contains an expression marker (a bracketed index such as [%s] or %s in the name) but the element has no <dim> element that would supply the values for it. svdconv cannot expand the …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M207 trigger not reviewed; clone not available)"]
---

## Symptom

`M207`
`Expression marker found but no <dim> specified: '%NAME%'`

## Cause

The SVD register or peripheral name contains an expression marker (a bracketed index such as [%s] or %s in the name) but the element has no <dim> element that would supply the values for it. svdconv cannot expand the name, so it stops with this error. The %NAME% in the message is the offending name as written in the SVD.

## Fix

Either add a <dim> (and matching <dimIncrement>, and <dimIndex> if needed) to the element in the SVD so the marker can be expanded, or remove the expression marker from the name if the element is not meant to be an array. The README only says to specify the dimension.

## Note

Source lines were not available, so the trigger condition is inferred from the message text and the README; the exact check and which element kinds it applies to are unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M207 trigger not reviewed; clone not available)`
