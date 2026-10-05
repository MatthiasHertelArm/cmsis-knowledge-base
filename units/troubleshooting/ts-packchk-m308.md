---
id: "ts-packchk-m308"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M308: missing on"
status: "draft"
tool: "packchk"
severity: "error"
code: "M308"
symptoms: ["M308", "Attribute '%TAG%' missing on '%TAG2%'"]
symptom_regex: "^Attribute '.+?' missing on '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M308`
`Attribute '%TAG%' missing on '%TAG2%'`

## Cause

Element _'TAG2'_ requires attribute _'TAG'_, but it was not found. Add missing attribute.

## Fix

_siehe Cause_
