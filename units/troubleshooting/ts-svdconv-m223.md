---
id: "ts-svdconv-m223"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M223: does not match the tag <name> in the <device> section"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M223"
symptoms: ["M223", "Input File Name '%INFILE%' does not match the tag <name> in the <device> section: '%NAME%'"]
symptom_regex: "^Input File Name '.+?' does not match the tag <name> in the <device> section: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M223`
`Input File Name '%INFILE%' does not match the tag <name> in the <device> section: '%NAME%'`

## Cause

Correct the MCU name.

## Fix

_siehe Cause_
