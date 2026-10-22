---
id: "ts-svdconv-m381"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M381: Interrupt '…' Number '…' greater or equal <deviceNumInterrupts>: '…'."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M381"
symptoms: ["M381", "Interrupt '%NAME%' Number '%NUM%' greater or equal <deviceNumInterrupts>: '%NUM2%'."]
symptom_regex: "^Interrupt '.+?' Number '.+?' greater or equal <deviceNumInterrupts>: '.+?'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found an SVD interrupt whose number is greater than or equal to the device's declared interrupt count (deviceNumInterrupts)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M381`
`Interrupt '%NAME%' Number '%NUM%' greater or equal <deviceNumInterrupts>: '%NUM2%'.`

## Cause

svdconv found an SVD interrupt whose number is greater than or equal to the device's declared interrupt count (deviceNumInterrupts). The %NAME% is the peripheral interrupt name, %NUM% its number, and %NUM2% the device-wide limit it exceeds. The mismatch is between the interrupt numbers in the SVD and the device-level interrupt count given in the description.

## Fix

Check the SVD: the interrupt value for the named interrupt should be below the device's interrupt count. Either correct the interrupt number in the peripheral entry or raise the device interrupt count (deviceNumInterrupts) so it covers that number, then rerun svdconv.

## Note

Written from the message text alone, since the clone was not available to read the trigger; the cause and fix are inferred from the message wording and should be checked against the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
