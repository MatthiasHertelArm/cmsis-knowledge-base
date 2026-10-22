---
id: "ts-svdconv-m517"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M517: SFD Code generation: Forbidden Trigraph '??…' found in '…'."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M517"
symptoms: ["M517", "SFD Code generation: Forbidden Trigraph '??%CHAR%' found in '%NAME%'."]
symptom_regex: "^SFD Code generation: Forbidden Trigraph '\\?\\?.+?' found in '.+?'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD source contains a C trigraph sequence '??' followed by a character (here shown as '%CHAR%') inside a name field (here '%NAME%') that svdconv copies into generated SFD code."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M517`
`SFD Code generation: Forbidden Trigraph '??%CHAR%' found in '%NAME%'.`

## Cause

The SVD source contains a C trigraph sequence '??' followed by a character (here shown as '%CHAR%') inside a name field (here '%NAME%') that svdconv copies into generated SFD code. Trigraphs are replaced by the C preprocessor, so the generated code would change meaning, and the tool warns about it.

## Fix

Find the named element in the SVD file and remove or rewrite the '??' sequence in its name or description, for example by replacing the question marks or the offending character with a different character, then run svdconv again.

## Note

Trigger and handling were not checked in the source because the clone was not available; the cause is inferred from the message text and the README entry, so confidence is capped at medium.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
