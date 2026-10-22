---
id: "ts-svdconv-m389"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M389: Specified <deviceNumInterrupts>: '…' greater or equal '…': '…'."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M389"
symptoms: ["M389", "Specified <deviceNumInterrupts>: '%NUM%' greater or equal '%NAME%': '%NUM2%'."]
symptom_regex: "^Specified <deviceNumInterrupts>: '.+?' greater or equal '.+?': '.+?'\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "<cpu><deviceNumInterrupts> is larger than the maximum number of external interrupts of the core named in <cpu><name> (svdconv's table: 32 for CM0/CM0PLUS/CM1, 240 for CM3/CM4/CM7/CM23, 480 for CM33/CM55/CM85). svdconv reports it for every <interrupt> and drops each of them."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdInterrupt.cpp:125-152", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdTypes.cpp:112-127", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:111-131", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:210"]
---

## Symptom

`M389`
`Specified <deviceNumInterrupts>: '%NUM%' greater or equal '%NAME%': '%NUM2%'.`

## Cause

<cpu><deviceNumInterrupts> is larger than the maximum number of external interrupts of the core named in <cpu><name> (svdconv's table: 32 for CM0/CM0PLUS/CM1, 240 for CM3/CM4/CM7/CM23, 480 for CM33/CM55/CM85). svdconv reports it for every <interrupt> and drops each of them.

## Fix

Set <deviceNumInterrupts> to the real number of device interrupts, which cannot exceed the core's limit, or correct <cpu><name> if the wrong core is named.

## Note

Message says 'greater or equal' but the check is strictly greater; a value equal to the limit passes (SvdInterruptTest.cpp:112-116). The line number is that of each interrupt, not of <cpu>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdInterrupt.cpp:125-152`
- `tools/svdconv/SVDModel/src/SvdTypes.cpp:112-127`
- `tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:111-131`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:210`
