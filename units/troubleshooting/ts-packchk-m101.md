---
id: "ts-packchk-m101"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M101: Unknown error!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M101"
symptoms: ["M101", "Unknown error!"]
symptom_regex: "^Unknown error!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:72", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:117"]
---

## Symptom

`M101`
`Unknown error!`

## Cause

Contact Arm for clarifications

## Fix

_see Cause_

## Note

No raise site for M101 in tools/packchk/src or libs at 30f5e81; only the message table entry and the README row ('Contact Arm for clarifications') exist.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:72`
- `tools/packchk/README.md:117`
