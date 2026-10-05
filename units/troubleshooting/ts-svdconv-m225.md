---
id: "ts-svdconv-m225"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M225: Upper/lower case mismatch"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M225"
symptoms: ["M225", "Upper/lower case mismatch: '%NAME%', should be '%NAME2%'"]
symptom_regex: "^Upper/lower case mismatch: '.+?', should be '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M225`
`Upper/lower case mismatch: '%NAME%', should be '%NAME2%'`

## Cause

Update SVD file.

## Fix

_siehe Cause_
