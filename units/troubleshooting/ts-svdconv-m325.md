---
id: "ts-svdconv-m325"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M325: CPU Revision is not set"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M325"
symptoms: ["M325", "CPU Revision is not set"]
symptom_regex: "^CPU Revision is not set$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints this error when the SVD file's device description has no <cpu> element with a <revision> value, so the CPU revision cannot be determined."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M325`
`CPU Revision is not set`

## Cause

svdconv prints this error when the SVD file's device description has no <cpu> element with a <revision> value, so the CPU revision cannot be determined. The trigger is inferred from the message text only, since the source lines were not available.

## Fix

Open the SVD file and add or complete the <cpu> block under <device>, including a <revision> entry (for example rXpY), then rerun svdconv. Check the vendor's SVD against the device reference manual if the revision is unknown.

## Note

Written from the message and the file name only; the trigger line was not checked. The README is documented as covering this message, but its text was not provided to confirm the cause and fix.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
