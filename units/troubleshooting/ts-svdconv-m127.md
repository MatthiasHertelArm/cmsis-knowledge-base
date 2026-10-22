---
id: "ts-svdconv-m127"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M127: SfrCC2 reports errors!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M127"
symptoms: ["M127", "SfrCC2 reports errors!"]
symptom_regex: "^SfrCC2 reports errors!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check SVD file."
summary: "svdconv prints this message when its SFR checking component (SfrCC2) reports errors while validating the SVD input."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M127`
`SfrCC2 reports errors!`

## Cause

svdconv prints this message when its SFR checking component (SfrCC2) reports errors while validating the SVD input. The message itself does not name the offending register or field, so the specific problem must be located from the SVD file and the preceding messages in the log. The README only says to check the SVD file.

## Fix

Read the messages printed just before M127 in the build log, they identify the register or field that failed the check. Correct the corresponding entries in the SVD file (for example, inconsistent or out-of-range register, field or bit-width values) and run svdconv again.

## Note

Source lines were not available, so the trigger and handling could not be checked; the cause is inferred from the message text and the README entry. The README's cause ('Check SVD file.') is generic.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
