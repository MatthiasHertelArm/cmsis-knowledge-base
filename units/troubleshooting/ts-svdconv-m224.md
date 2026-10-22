---
id: "ts-svdconv-m224"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M224: Deprecated: '…' Use '…' instead"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M224"
symptoms: ["M224", "Deprecated: '%NAME%' Use '%NAME2%' instead"]
symptom_regex: "^Deprecated: '.+?' Use '.+?' instead$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Update SVD file."
summary: "svdconv prints this warning when the SVD input uses an element or attribute name that the CMSIS SVD schema has deprecated, and it names the replacement to use."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M224`
`Deprecated: '%NAME%' Use '%NAME2%' instead`

## Cause

svdconv prints this warning when the SVD input uses an element or attribute name that the CMSIS SVD schema has deprecated, and it names the replacement to use. The %NAME% part is the deprecated name found in the SVD file, and %NAME2% is the name that should be used instead. The source lines were not available, so this reading is taken from the message text and the README's brief cause.

## Fix

Open the SVD file named in the svdconv output, find the element or attribute given as %NAME%, and rename it to %NAME2%. Then run svdconv again to confirm the warning is gone.

## Note

Source lines were not available, so the trigger location and the exact conditions for the warning could not be checked. The fix is inferred from the message wording and the README's 'Update SVD file' cause.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
