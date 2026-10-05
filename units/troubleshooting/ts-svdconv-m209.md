---
id: "ts-svdconv-m209"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M209: CPU section not set. This is required for CMSIS Headerfile generation "
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M209"
symptoms: ["M209", "CPU section not set. This is required for CMSIS Headerfile generation and debug support."]
symptom_regex: "^CPU section not set\\. This is required for CMSIS Headerfile generation and debug support\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M209`
`CPU section not set. This is required for CMSIS Headerfile generation and debug support.`

## Cause

Add CPU section.

## Fix

_siehe Cause_
