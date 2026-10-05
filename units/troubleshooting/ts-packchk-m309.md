---
id: "ts-packchk-m309"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M309: is specified)"
status: "draft"
tool: "packchk"
severity: "error"
code: "M309"
symptoms: ["M309", "Attribute '%TAG%' missing on '%TAG2%' (when '%TAG3%' is specified)"]
symptom_regex: "^Attribute '.+?' missing on '.+?' \\(when '.+?' is specified\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M309`
`Attribute '%TAG%' missing on '%TAG2%' (when '%TAG3%' is specified)`

## Cause

Add missing attribute _'TAG'_ or remove the attribute _'TAG3'_ in the element _'TAG2'_.

## Fix

_siehe Cause_
