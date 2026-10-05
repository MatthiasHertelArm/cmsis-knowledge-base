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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An <interrupt> <value> is greater than or equal to <cpu><deviceNumInterrupts>."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdInterrupt.cpp:113-158", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:117-123", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:159-168", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:202"]
---

## Symptom

`M381`
`Interrupt '%NAME%' Number '%NUM%' greater or equal <deviceNumInterrupts>: '%NUM2%'.`

## Cause

An <interrupt> <value> is greater than or equal to <cpu><deviceNumInterrupts>. Valid numbers run from 0 to deviceNumInterrupts-1, so the interrupt is dropped.

## Fix

Correct the interrupt's <value>, or raise <deviceNumInterrupts> to the highest interrupt number plus one.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdInterrupt.cpp:113-158`
- `tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:117-123`
- `tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:159-168`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:202`
