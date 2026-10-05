---
id: "ts-svdconv-m243"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M243: <dimArrayIndex> found, but <dim> does not describe an array"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M243"
symptoms: ["M243", "%LEVEL% '%NAME%' <dimArrayIndex> found, but <dim> does not describe an array"]
symptom_regex: "^.+? '.+?' <dimArrayIndex> found, but <dim> does not describe an array$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M243`
`%LEVEL% '%NAME%' <dimArrayIndex> found, but <dim> does not describe an array`

## Cause

Correct SVD.

## Fix

_siehe Cause_
