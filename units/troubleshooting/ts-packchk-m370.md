---
id: "ts-packchk-m370"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M370: URL is not conformant: '…': Backslashes are not allowed in URL, use forward slashes."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M370"
symptoms: ["M370", "URL is not conformant: '%URL%':   Backslashes are not allowed in URL, use forward slashes."]
symptom_regex: "^URL is not conformant: '.+?':   Backslashes are not allowed in URL, use forward slashes\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Use standard URL notation using forward slashes (/)."
summary: "A path attribute or license entry in the PDSC holds a URL (http, https, ftp or ftps) that contains backslashes."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:189", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/RteModelReader.cpp:52-67", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:155-174", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:208"]
---

## Symptom

`M370`
`URL is not conformant: '%URL%':   Backslashes are not allowed in URL, use forward slashes.`

## Cause

A path attribute or license entry in the PDSC holds a URL (http, https, ftp or ftps) that contains backslashes.

## Fix

Write the URL with forward slashes only.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:189`
- `tools/packchk/src/RteModelReader.cpp:52-67`
- `tools/packchk/src/ValidateSyntax.cpp:155-174`
- `tools/packchk/README.md:208`
