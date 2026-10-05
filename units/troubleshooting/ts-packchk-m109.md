---
id: "ts-packchk-m109"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M109: Constructing RTE Model failed!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M109"
symptoms: ["M109", "Constructing RTE Model failed!"]
symptom_regex: "^Constructing RTE Model failed!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:80", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/RteModelReader.cpp:121-140", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:121"]
---

## Symptom

`M109`
`Constructing RTE Model failed!`

## Cause

Contact Arm for clarifications

## Fix

_see Cause_

## Note

Unreachable at 30f5e81: M109 is logged under 'if(!bOk)' right after the code returned early when bOk was false (RteModelReader.cpp:127-140), so it never prints. No PDSC cause exists.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:80`
- `tools/packchk/src/RteModelReader.cpp:121-140`
- `tools/packchk/README.md:121`
