---
id: "ts-packchk-m397"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M397: File extension '.pdsc' must be lowercase: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M397"
symptoms: ["M397", "File extension '.pdsc' must be lowercase: '%PATH%'"]
symptom_regex: "^File extension '\\.pdsc' must be lowercase: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The PDSC file shall have lowercase extension `.pdsc` Correct extension of the PDSC file _'PATH'_."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:216", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:37", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:231", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtefsutils/src/RteFsUtils.cpp:750-788"]
---

## Symptom

`M397`
`File extension '.pdsc' must be lowercase: '%PATH%'`

## Cause

The PDSC file shall have lowercase extension `.pdsc` Correct extension of the PDSC file _'PATH'_.

## Fix

Rename the PDSC file so its extension is lowercase .pdsc.

## Note

No raise site for M397 (nor for the info message M068) at 30f5e81. Fix taken from the message and README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:216`
- `tools/packchk/src/PackChk_Msgs.cpp:37`
- `tools/packchk/README.md:231`
- `libs/rtefsutils/src/RteFsUtils.cpp:750-788`
