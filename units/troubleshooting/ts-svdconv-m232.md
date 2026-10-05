---
id: "ts-svdconv-m232"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M232: must not have specifier"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M232"
symptoms: ["M232", "Tag <%TAG%> name '%NAME%' must not have specifier '%CHAR%'. Ignoring entry."]
symptom_regex: "^Tag <.+?> name '.+?' must not have specifier '.+?'\\. Ignoring entry\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M232`
`Tag <%TAG%> name '%NAME%' must not have specifier '%CHAR%'. Ignoring entry.`

## Cause

Correct SVD.

## Fix

_siehe Cause_
