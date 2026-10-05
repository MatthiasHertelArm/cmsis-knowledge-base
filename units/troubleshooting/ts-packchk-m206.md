---
id: "ts-packchk-m206"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M206: Multiple PDSC file found in package"
status: "draft"
tool: "packchk"
severity: "error"
code: "M206"
symptoms: ["M206", "Multiple PDSC file found in package: %FILES%"]
symptom_regex: "^Multiple PDSC file found in package: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M206`
`Multiple PDSC file found in package: %FILES%`

## Cause

Only one PDSC file is allowed in a package. Remove unnecessary PDSC files. The message lists all \*.pdsc files found.

## Fix

_siehe Cause_
