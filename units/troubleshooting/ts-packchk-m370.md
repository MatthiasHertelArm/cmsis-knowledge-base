---
id: "ts-packchk-m370"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M370: Backslashes are not allowed in URL, use forward slashes."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M370"
symptoms: ["M370", "URL is not conformant: '%URL%':   Backslashes are not allowed in URL, use forward slashes."]
symptom_regex: "^URL is not conformant: '.+?':   Backslashes are not allowed in URL, use forward slashes\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M370`
`URL is not conformant: '%URL%':   Backslashes are not allowed in URL, use forward slashes.`

## Cause

Use standard URL notation using forward slashes (/).

## Fix

_siehe Cause_
