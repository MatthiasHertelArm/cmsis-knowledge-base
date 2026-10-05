---
id: "ts-svdconv-m330"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M330: Interrupt '…' Number not set."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M330"
symptoms: ["M330", "Interrupt '%NAME%' Number not set."]
symptom_regex: "^Interrupt '.+?' Number not set\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An <interrupt> has no <value> (its interrupt number)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdInterrupt.cpp:113", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdInterrupt.cpp:142", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:172", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:149"]
---

## Symptom

`M330`
`Interrupt '%NAME%' Number not set.`

## Cause

An <interrupt> has no <value> (its interrupt number). The interrupt is dropped.

## Fix

Add the interrupt number, counted from 0 for the first device-specific interrupt, for example <interrupt><name>UART0</name><value>5</value></interrupt>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdInterrupt.cpp:113`
- `tools/svdconv/SVDModel/src/SvdInterrupt.cpp:142`
- `tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:172`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:149`
