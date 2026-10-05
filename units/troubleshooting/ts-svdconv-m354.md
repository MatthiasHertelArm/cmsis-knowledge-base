---
id: "ts-svdconv-m354"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M354: Interrupt '…:…' specifies a Core Interrupt. Core Interrupts must not be defined, they are set …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M354"
symptoms: ["M354", "Interrupt '%NUM%:%NAME%' specifies a Core Interrupt. Core Interrupts must not be defined, they are set through <cpu><name>."]
symptom_regex: "^Interrupt '.+?:.+?' specifies a Core Interrupt\\. Core Interrupts must not be defined, they are set through <cpu><name>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An <interrupt> has the name of a Cortex-M core exception (for example NonMaskableInt, HardFault, MemoryManagement, BusFault, UsageFault, SecureFault, SVCall, DebugMonitor, PendSV, SysTick), as provided for the core in <cpu><name>."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:648", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:671", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:674", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:280", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdTypes.cpp:83", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:173"]
---

## Symptom

`M354`
`Interrupt '%NUM%:%NAME%' specifies a Core Interrupt. Core Interrupts must not be defined, they are set through <cpu><name>.`

## Cause

An <interrupt> has the name of a Cortex-M core exception (for example NonMaskableInt, HardFault, MemoryManagement, BusFault, UsageFault, SecureFault, SVCall, DebugMonitor, PendSV, SysTick), as provided for the core in <cpu><name>. Core exceptions come from the CPU type and must not be listed; the interrupt is dropped.

## Fix

Delete <interrupt> entries for core exceptions and list only the device-specific interrupts, numbered from 0.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:648`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:671`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:674`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:280`
- `tools/svdconv/SVDModel/src/SvdTypes.cpp:83`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:173`
