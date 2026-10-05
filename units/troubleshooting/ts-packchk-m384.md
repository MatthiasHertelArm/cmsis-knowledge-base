---
id: "ts-packchk-m384"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M384: Direct or indirect recursion detected. Skipping condition while search"
status: "draft"
tool: "packchk"
severity: "error"
code: "M384"
symptoms: ["M384", "Condition '%NAME%': Direct or indirect recursion detected. Skipping condition while searching for '%NAME2%'."]
symptom_regex: "^Condition '.+?': Direct or indirect recursion detected\\. Skipping condition while searching for '.+?'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M384`
`Condition '%NAME%': Direct or indirect recursion detected. Skipping condition while searching for '%NAME2%'.`

## Cause

Resolve recursion in condition _'NAME'_.

## Fix

_siehe Cause_
