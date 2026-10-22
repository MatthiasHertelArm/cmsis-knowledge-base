---
id: "ts-svdconv-m331"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M331: Interrupt '…' Number '…' greater or equal '…' maximum Interrupts: '…'."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M331"
symptoms: ["M331", "Interrupt '%NAME%' Number '%NUM%' greater or equal '%NAME2%' maximum Interrupts: '%NUM2%'."]
symptom_regex: "^Interrupt '.+?' Number '.+?' greater or equal '.+?' maximum Interrupts: '.+?'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found an interrupt in the SVD whose number is greater than or equal to the device's maximum interrupt count, so the interrupt cannot be placed in the vector table it was checked against."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M331`
`Interrupt '%NAME%' Number '%NUM%' greater or equal '%NAME2%' maximum Interrupts: '%NUM2%'.`

## Cause

svdconv found an interrupt in the SVD whose number is greater than or equal to the device's maximum interrupt count, so the interrupt cannot be placed in the vector table it was checked against. The message names the offending interrupt, its number, the reference the maximum came from, and the maximum value. The exact trigger was not available in the source lines given, so this is inferred from the message text.

## Fix

Open the SVD file and find the interrupt named in the message; check its <value> against the device's interrupt count, and correct the interrupt number or the maximum interrupt setting so that the number is below the maximum, then rerun svdconv.

## Note

The clone was not available, so the trigger condition and the source of the maximum were not verified; the cause and fix rest on the message text alone.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
