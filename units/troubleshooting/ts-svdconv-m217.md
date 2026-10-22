---
id: "ts-svdconv-m217"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M217: Forbidden Trigraph '??…' found in '…'."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M217"
symptoms: ["M217", "Forbidden Trigraph '??%CHAR%' found in '%NAME%'."]
symptom_regex: "^Forbidden Trigraph '\\?\\?.+?' found in '.+?'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD input contains a C trigraph sequence '??' followed by a character (the %CHAR% part) inside a name field (%NAME%)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M217`
`Forbidden Trigraph '??%CHAR%' found in '%NAME%'.`

## Cause

The SVD input contains a C trigraph sequence '??' followed by a character (the %CHAR% part) inside a name field (%NAME%). Trigraphs are an obsolete C feature that some compilers rewrite, so svdconv warns that such text may be altered when the generated output is compiled. The exact source lines were not available, so this is inferred from the message text and the warning's wording rather than confirmed in the code.

## Fix

Find the element named in the message in the SVD file and remove the '??' sequence from its name or description, for example by replacing it with a different character or spelling. Then run svdconv again.

## Note

Source lines were not available; the trigger condition and the cause are inferred from the message text only. The README entry is documented but its text was not provided for comparison.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
