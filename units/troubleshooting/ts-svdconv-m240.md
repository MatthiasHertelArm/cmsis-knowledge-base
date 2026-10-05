---
id: "ts-svdconv-m240"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M240: > unknown or not allowed on"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M240"
symptoms: ["M240", "Tag <%TAG%> unknown or not allowed on %LEVEL2%:%LEVEL%."]
symptom_regex: "^Tag <.+?> unknown or not allowed on .+?:.+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M240`
`Tag <%TAG%> unknown or not allowed on %LEVEL2%:%LEVEL%.`

## Cause

Correct SVD.

## Fix

_siehe Cause_
