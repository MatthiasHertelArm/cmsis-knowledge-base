---
id: "ts-svdconv-m225"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M225: Upper/lower case mismatch: '…', should be '…'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M225"
symptoms: ["M225", "Upper/lower case mismatch: '%NAME%', should be '%NAME2%'"]
symptom_regex: "^Upper/lower case mismatch: '.+?', should be '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Update SVD file."
summary: "The SVD file uses an identifier whose letter case differs from the spelling svdconv expects, for example a register or field name written in a different case than the canonical form. svdconv reports the name it found (%NAME%) and …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M225`
`Upper/lower case mismatch: '%NAME%', should be '%NAME2%'`

## Cause

The SVD file uses an identifier whose letter case differs from the spelling svdconv expects, for example a register or field name written in a different case than the canonical form. svdconv reports the name it found (%NAME%) and the name it expects (%NAME2%). The README gives only 'Update SVD file' as the cause, and the source lines were not available to confirm the exact check.

## Fix

Open the SVD file at the element named in the message and change the spelling of %NAME% to %NAME2%, then run svdconv again. Re-run the build to confirm the warning is gone.

## Note

Source lines were not available, so the trigger condition is inferred from the message text and the README rather than read from the code. Only the warning text and the README cause and fix were used.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
