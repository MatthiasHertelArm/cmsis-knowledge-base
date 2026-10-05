---
id: "ts-packchk-m311"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M311: Redefinition of"
status: "draft"
tool: "packchk"
severity: "error"
code: "M311"
symptoms: ["M311", "Redefinition of '%TAG%' : '%NAME%', see Line %LINE%"]
symptom_regex: "^Redefinition of '.+?' : '.+?', see Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M311`
`Redefinition of '%TAG%' : '%NAME%', see Line %LINE%`

## Cause

Remove the redefinition of element _'TAG'_ with name _'NAME'_.

## Fix

_siehe Cause_
