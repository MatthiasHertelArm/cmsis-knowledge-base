---
id: "ts-svdconv-m353"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M353: Peripheral group name '…' should not end with '_'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M353"
symptoms: ["M353", "Peripheral group name '%NAME%' should not end with '_'"]
symptom_regex: "^Peripheral group name '.+?' should not end with '_'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints this warning when a peripheral group name in the SVD file ends with an underscore character."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M353`
`Peripheral group name '%NAME%' should not end with '_'`

## Cause

svdconv prints this warning when a peripheral group name in the SVD file ends with an underscore character. The %NAME% placeholder is the offending group name as written in the SVD input. The tool flags it as a naming-style issue, so the SVD is accepted but the name is considered non-conforming.

## Fix

Open the SVD input and rename the peripheral group so it does not end with '_' (for example, drop the trailing underscore from the name shown in the message). Then rerun svdconv. The README documents this message, but its exact fix text was not available to confirm here.

## Note

Source lines were not available in the clone, so the trigger condition and the handling are inferred from the message text and the README entry only. Verify the exact check in SVDConv_Msgs.cpp before relying on the cause wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
