---
id: "ts-svdconv-m249"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M249: Dimension expansion exceeds the per-input limit of … generated indices and model copies."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M249"
symptoms: ["M249", "Dimension expansion exceeds the per-input limit of %NUM% generated indices and model copies."]
symptom_regex: "^Dimension expansion exceeds the per\\-input limit of .+? generated indices and model copies\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M249`
`Dimension expansion exceeds the per-input limit of %NUM% generated indices and model copies.`

## Cause

Reduce the total expanded model size.

## Fix

_see Cause_
