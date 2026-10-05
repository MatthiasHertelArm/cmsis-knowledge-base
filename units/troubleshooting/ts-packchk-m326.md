---
id: "ts-packchk-m326"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M326: Absolute Paths or Drive references are not allowed, use Paths relative"
status: "draft"
tool: "packchk"
severity: "error"
code: "M326"
symptoms: ["M326", "Path is not conformant: '%PATH%':   Absolute Paths or Drive references are not allowed, use Paths relative to PDSC file."]
symptom_regex: "^Path is not conformant: '.+?':   Absolute Paths or Drive references are not allowed, use Paths relative to PDSC file\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M326`
`Path is not conformant: '%PATH%':   Absolute Paths or Drive references are not allowed, use Paths relative to PDSC file.`

## Cause

The path needs to be relative to the PDSC file so that a dependency of a certain file system does not occur.

## Fix

_siehe Cause_
