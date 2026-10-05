---
id: "ts-svdconv-m242"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M242: <dimArrayIndex> found, but no <dim>"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M242"
symptoms: ["M242", "%LEVEL% '%NAME%' <dimArrayIndex> found, but no <dim>"]
symptom_regex: "^.+? '.+?' <dimArrayIndex> found, but no <dim>$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M242`
`%LEVEL% '%NAME%' <dimArrayIndex> found, but no <dim>`

## Cause

Correct SVD.

## Fix

_siehe Cause_
