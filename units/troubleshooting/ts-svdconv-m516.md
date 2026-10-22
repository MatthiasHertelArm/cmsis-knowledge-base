---
id: "ts-svdconv-m516"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M516: SFD Code generation: Unsupported character found in '…' : …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M516"
symptoms: ["M516", "SFD Code generation: Unsupported character found in '%NAME%' : %HEX%."]
symptom_regex: "^SFD Code generation: Unsupported character found in '.+?' : .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints this warning while generating SFD (scatter/device) output when a name taken from the SVD input, shown as %NAME%, contains a character that the SFD code generator cannot emit. %HEX% is the code of that character."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M516`
`SFD Code generation: Unsupported character found in '%NAME%' : %HEX%.`

## Cause

svdconv prints this warning while generating SFD (scatter/device) output when a name taken from the SVD input, shown as %NAME%, contains a character that the SFD code generator cannot emit. %HEX% is the code of that character. The SVD file therefore uses a character outside the set the generator accepts in that identifier.

## Fix

Find the element named in the message in the SVD file and rename it so it uses only plain letters, digits and underscores, then rerun svdconv. If the name comes from a vendor SVD you cannot edit, check the generated SFD output for the affected identifier and treat it as a known limitation.

## Note

The source lines were not available, so the trigger condition and the allowed character set are inferred from the message text and the README entry, not confirmed from the code. The fix assumes the offending character sits in a name the user can edit in the SVD.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
