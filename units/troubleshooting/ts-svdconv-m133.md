---
id: "ts-svdconv-m133"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M133: SFR generation is only supported on Windows (requires SfrCC2.exe)."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M133"
symptoms: ["M133", "SFR generation is only supported on Windows (requires SfrCC2.exe)."]
symptom_regex: "^SFR generation is only supported on Windows \\(requires SfrCC2\\.exe\\)\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M133`
`SFR generation is only supported on Windows (requires SfrCC2.exe).`

## Cause

Generate SFR output on Windows with SfrCC2.exe installed alongside SVDConv, or use `--generate=sfd` for SFD output.

## Fix

_siehe Cause_
