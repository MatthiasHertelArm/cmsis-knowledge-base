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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file defines an interrupt entry whose number falls in the range of ARM Cortex-M core (system) exceptions, i.e. a negative IRQ number such as SysTick or other core interrupts. svdconv reports these because core interrupts are not …"
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M354`
`Interrupt '%NUM%:%NAME%' specifies a Core Interrupt. Core Interrupts must not be defined, they are set through <cpu><name>.`

## Cause

The SVD file defines an interrupt entry whose number falls in the range of ARM Cortex-M core (system) exceptions, i.e. a negative IRQ number such as SysTick or other core interrupts. svdconv reports these because core interrupts are not device peripheral interrupts and must not appear in the <peripheral><interrupt> list; they are configured through the <cpu><name> element instead. The %NUM% and %NAME% in the message are the offending interrupt's value and name from the SVD.

## Fix

Remove the <interrupt> element for the core interrupt (the one named in the message) from the peripheral in the SVD file. Keep the device's core type in the <cpu><name> element, which sets the core interrupts. Then rerun svdconv.

## Note

Written from the message text alone; the clone was not available, so the trigger condition in the source was not checked. The README was documented as covering this message but its text was not provided to me.
