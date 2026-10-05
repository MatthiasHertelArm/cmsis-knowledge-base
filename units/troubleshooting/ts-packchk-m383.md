---
id: "ts-packchk-m383"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M383: is not conformant to the pattern"
status: "draft"
tool: "packchk"
severity: "error"
code: "M383"
symptoms: ["M383", "%TAG% '%NAME%' is not conformant to the pattern \"%CHAR%\""]
symptom_regex: "^.+? '.+?' is not conformant to the pattern \".+?\"$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M383`
`%TAG% '%NAME%' is not conformant to the pattern "%CHAR%"`

## Cause

Unsupported characters are found in the _'NAME'_ for the tag/attribute _'TAG'_. Specify the name using only supported characters from _'CHAR'_.

## Fix

_siehe Cause_
