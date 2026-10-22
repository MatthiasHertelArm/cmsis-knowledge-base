---
id: "ts-packchk-m104"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M104: Path empty when searching for other PDSC files"
status: "draft"
tool: "packchk"
severity: "error"
code: "M104"
symptoms: ["M104", "Path empty when searching for other PDSC files"]
symptom_regex: "^Path empty when searching for other PDSC files$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:75", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CreateModel.cpp:39-43", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:119"]
---

## Symptom

`M104`
`Path empty when searching for other PDSC files`

## Cause

Execute the check in verbose mode and try to identify the PDSC file intended for use. Correct the PDSC.

## Fix

_see Cause_

## Note

No raise site for M104 at 30f5e81: CheckForOtherPdscFiles returns false without a message for an empty path (CreateModel.cpp:41-43). The README advice (run verbose, identify the PDSC) cannot be tied to code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:75`
- `tools/packchk/src/CreateModel.cpp:39-43`
- `tools/packchk/README.md:119`
