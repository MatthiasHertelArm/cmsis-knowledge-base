---
id: "ts-svdconv-m128"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M128: SfrCC2 reports warnings!"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M128"
symptoms: ["M128", "SfrCC2 reports warnings!"]
symptom_regex: "^SfrCC2 reports warnings!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check SVD file."
summary: "svdconv prints this warning after the SfrCC2 checker has finished the SVD file and found warnings in it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M128`
`SfrCC2 reports warnings!`

## Cause

svdconv prints this warning after the SfrCC2 checker has finished the SVD file and found warnings in it. The message itself names no specific register or field; the detail is in the warnings printed before it. The SVD input contains values or structure that the checker flags.

## Fix

Read the warning lines printed just before M128 and correct the SVD file at the register or field they name, then run svdconv again. If the warnings do not explain the problem, check the SVD against the CMSIS-SVD schema.

## Note

Source lines were not available, so the trigger and the exact condition could not be verified. The cause is inferred from the message text and the README entry 'Check SVD file.' The message body is a generic summary, so the actionable detail sits in the preceding warnings.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
