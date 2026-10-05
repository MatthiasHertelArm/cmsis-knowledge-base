---
id: "ts-svdconv-m354"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M354: specifies a Core Interrupt. Core Interrupts must not be defined, they "
status: "draft"
tool: "svdconv"
severity: "error"
code: "M354"
symptoms: ["M354", "Interrupt '%NUM%:%NAME%' specifies a Core Interrupt. Core Interrupts must not be defined, they are set through <cpu><name>."]
symptom_regex: "^Interrupt '.+?:.+?' specifies a Core Interrupt\\. Core Interrupts must not be defined, they are set through <cpu><name>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M354`
`Interrupt '%NUM%:%NAME%' specifies a Core Interrupt. Core Interrupts must not be defined, they are set through <cpu><name>.`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_
