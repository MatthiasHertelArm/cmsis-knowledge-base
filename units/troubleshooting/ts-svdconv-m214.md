---
id: "ts-svdconv-m214"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M214: <dim> single-instantiation is not supported (use Array instead)."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M214"
symptoms: ["M214", "Peripheral '%NAME%' <dim> single-instantiation is not supported (use Array instead)."]
symptom_regex: "^Peripheral '.+?' <dim> single\\-instantiation is not supported \\(use Array instead\\)\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M214`
`Peripheral '%NAME%' <dim> single-instantiation is not supported (use Array instead).`

## Cause

Correct Regs to Reg[s].

## Fix

_siehe Cause_
