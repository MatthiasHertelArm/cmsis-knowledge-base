---
id: "ts-svdconv-m210"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M210: Use new Format CMSIS-SVD >= V1.1 and add <CPU> Section."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M210"
symptoms: ["M210", "Use new Format CMSIS-SVD >= V1.1 and add <CPU> Section."]
symptom_regex: "^Use new Format CMSIS\\-SVD >= V1\\.1 and add <CPU> Section\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Update schema and add CPU section."
summary: "svdconv found an SVD file whose root element does not use the CMSIS-SVD schema version 1.1 or later, or that lacks the <cpu> section that the newer format expects."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M210`
`Use new Format CMSIS-SVD >= V1.1 and add <CPU> Section.`

## Cause

svdconv found an SVD file whose root element does not use the CMSIS-SVD schema version 1.1 or later, or that lacks the <cpu> section that the newer format expects. The README attributes the warning to an outdated schema version plus a missing CPU section in the input SVD.

## Fix

Open the input SVD file, update the root <device> element to the current CMSIS-SVD schema (version 1.1 or later, using the schema namespace and schemaVersion attribute shown in the current CMSIS-SVD examples), and add a <cpu> section inside <device> describing the processor. Then rerun svdconv on the updated file.

## Note

The source lines were not available, so the trigger condition and the exact attribute checked are not verified; the cause and fix come from the message text and the README. The message is a warning, so conversion may still complete.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
