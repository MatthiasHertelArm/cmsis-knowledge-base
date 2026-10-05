---
id: "ts-packchk-m327"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M327: Backslashes are not recommended, use forward slashes."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M327"
symptoms: ["M327", "Path is not conformant: '%PATH%':   Backslashes are not recommended, use forward slashes."]
symptom_regex: "^Path is not conformant: '.+?':   Backslashes are not recommended, use forward slashes\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M327`
`Path is not conformant: '%PATH%':   Backslashes are not recommended, use forward slashes.`

## Cause

Paths to files should adhere to the POSIX standard using forward slashes (/).

## Fix

_siehe Cause_
