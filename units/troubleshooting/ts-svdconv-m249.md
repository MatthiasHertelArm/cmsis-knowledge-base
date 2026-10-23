---
id: "ts-svdconv-m249"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M249: Dimension expansion exceeds the per-input limit of … generated indices and model copies."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M249"
symptoms: ["M249", "Dimension expansion exceeds the per-input limit of %NUM% generated indices and model copies."]
symptom_regex: "^Dimension expansion exceeds the per\\-input limit of .+? generated indices and model copies\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Reduce the total expanded model size."
summary: "The SVD input declares a register or cluster array (dim) whose expansion produces more generated indices and model copies than the svdconv per-input limit allows."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M249`
`Dimension expansion exceeds the per-input limit of %NUM% generated indices and model copies.`

## Cause

The SVD input declares a register or cluster array (dim) whose expansion produces more generated indices and model copies than the svdconv per-input limit allows. The %NUM% placeholder is the configured limit value. Because the source lines were not available, this reading is based only on the message text.

## Fix

Reduce the dimension count or the dimIncrement range of the offending dim element in the SVD file, or split the large array into smaller groups, then rerun svdconv. Check the README entry for this message for any documented limit or option.

## Note

Source lines were unavailable, so the trigger condition and the exact limit are not verified. The message is documented in the README but its README text was not provided here.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
