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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdInterrupt.cpp:132", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdInterrupt.cpp:160", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdInterrupt.cpp:161", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:107", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:217", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:150"]
---

## Symptom

`M331`
`Interrupt '%NAME%' Number '%NUM%' greater or equal '%NAME2%' maximum Interrupts: '%NUM2%'.`

## Cause

An <interrupt>'s <value> is equal to or above the number of external interrupts the core in <cpu><name> supports (for example 240 for CM3, 480 for CM33). The message prints that limit minus 1, the highest number allowed. The interrupt is dropped.

## Fix

Check the <value>: it counts from 0 for the first device interrupt, not from exception number 16. Also check <cpu><name>; if it is missing or unknown, svdconv assumes CM3 with 240 interrupts.

## Note

Wording: 'Number 240 greater or equal CM3 maximum Interrupts: 239' reads as if 239 were not allowed; 239 is the highest valid number.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdInterrupt.cpp:132`
- `tools/svdconv/SVDModel/src/SvdInterrupt.cpp:160`
- `tools/svdconv/SVDModel/src/SvdInterrupt.cpp:161`
- `tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:107`
- `tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:217`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:150`
