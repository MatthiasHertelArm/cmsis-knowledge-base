---
id: "ts-svdconv-m210"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M210: Use new Format CMSIS-SVD >= V1.1 and add <CPU> Section."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M210"
symptoms: ["M210", "Use new Format CMSIS-SVD >= V1.1 and add <CPU> Section."]
symptom_regex: "^Use new Format CMSIS\\-SVD >= V1\\.1 and add <CPU> Section\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M210`
`Use new Format CMSIS-SVD >= V1.1 and add <CPU> Section.`

## Cause

Update schema and add CPU section.

## Fix

_siehe Cause_
