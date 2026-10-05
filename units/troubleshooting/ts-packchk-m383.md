---
id: "ts-packchk-m383"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M383: … '…' is not conformant to the pattern \"…\""
status: "draft"
tool: "packchk"
severity: "error"
code: "M383"
symptoms: ["M383", "%TAG% '%NAME%' is not conformant to the pattern \"%CHAR%\""]
symptom_regex: "^.+? '.+?' is not conformant to the pattern \".+?\"$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Unsupported characters are found in the _'NAME'_ for the tag/attribute _'TAG'_. Specify the name using only supported characters from _'CHAR'_."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:202", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:307-324", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:577-581", "Open-CMSIS-Pack/devtools@30f5e817:libs/rteutils/src/RteUtils.cpp:187-194", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:221"]
---

## Symptom

`M383`
`%TAG% '%NAME%' is not conformant to the pattern "%CHAR%"`

## Cause

A device or variant name (Dname or Dvariant) contains characters other than letters, digits, '-', '_' and '/'.

## Fix

Rename the device or variant using only A-Z, a-z, 0-9, '-', '_' (no spaces, dots or parentheses), and update the references to it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:202`
- `tools/packchk/src/ValidateSemantic.cpp:307-324`
- `tools/packchk/src/ValidateSemantic.cpp:577-581`
- `libs/rteutils/src/RteUtils.cpp:187-194`
- `tools/packchk/README.md:221`
