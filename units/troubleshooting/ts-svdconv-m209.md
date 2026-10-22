---
id: "ts-svdconv-m209"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M209: CPU section not set. This is required for CMSIS Headerfile generation and debug support."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M209"
symptoms: ["M209", "CPU section not set. This is required for CMSIS Headerfile generation and debug support."]
symptom_regex: "^CPU section not set\\. This is required for CMSIS Headerfile generation and debug support\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Add CPU section."
summary: "The SVD input has no <cpu> section inside the device description, so svdconv cannot read the processor details it needs for CMSIS header generation and debug support."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M209`
`CPU section not set. This is required for CMSIS Headerfile generation and debug support.`

## Cause

The SVD input has no <cpu> section inside the device description, so svdconv cannot read the processor details it needs for CMSIS header generation and debug support. The source lines were not available, so this rests on the message text and the README.

## Fix

Add a <cpu> section to the SVD device element with the processor name, revision, endian, and the other required CPU fields, then rerun svdconv. Check the SVD against the CMSIS-SVD schema for the exact child elements the tool expects.

## Note

Trigger line not inspected because the clone was unavailable; the README cause is short and the exact required CPU fields are unverified. The README says only 'Add CPU section', so the required child elements are not confirmed.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
