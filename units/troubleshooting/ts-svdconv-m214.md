---
id: "ts-svdconv-m214"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M214: Peripheral '…' <dim> single-instantiation is not supported (use Array instead)."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M214"
symptoms: ["M214", "Peripheral '%NAME%' <dim> single-instantiation is not supported (use Array instead)."]
symptom_regex: "^Peripheral '.+?' <dim> single\\-instantiation is not supported \\(use Array instead\\)\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct Regs to Reg[s]."
summary: "A <peripheral> with <dim> uses the list form %s in its <name> (e.g."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:597-610", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:66-69", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:81"]
---

## Symptom

`M214`
`Peripheral '%NAME%' <dim> single-instantiation is not supported (use Array instead).`

## Cause

A <peripheral> with <dim> uses the list form %s in its <name> (e.g. TIMER%s). svdconv supports dim peripherals only as arrays with [%s] at the end of the name, and drops the peripheral.

## Fix

Use the array form, e.g. <name>TIMER[%s]</name> with <dim> and <dimIncrement> (peripherals take no <dimIndex>), or write each instance as its own <peripheral>, using derivedFrom to share the registers.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:597-610`
- `tools/svdconv/SVDModel/src/SvdDimension.cpp:66-69`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:81`
