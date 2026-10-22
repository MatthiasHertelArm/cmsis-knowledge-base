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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Unsupported characters are found in the _'NAME'_ for the tag/attribute _'TAG'_. Specify the name using only supported characters from _'CHAR'_."
summary: "packchk checks a name attribute in the PDSC against a regular-expression pattern and prints M383 when the value contains characters the pattern does not allow."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M383`
`%TAG% '%NAME%' is not conformant to the pattern "%CHAR%"`

## Cause

packchk checks a name attribute in the PDSC against a regular-expression pattern and prints M383 when the value contains characters the pattern does not allow. The %TAG% is the element or attribute that holds the name, %NAME% is the offending value, and %CHAR% is the pattern the value must match. The source lines were not available, so this is taken from the message text and the README description only.

## Fix

Open the PDSC element named in the message and change the value of the named attribute so it uses only the characters allowed by the pattern shown in the message, then rerun packchk.

## Note

Trigger lines were not provided; the cause and fix rest on the message text and the README. The exact character set is only what the %CHAR% pattern in the printed message states.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
