---
id: "ts-packchk-m203"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M203: Error reading PDSC file(s) '…'!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M203"
symptoms: ["M203", "Error reading PDSC file(s) '%PATH%'!"]
symptom_regex: "^Error reading PDSC file\\(s\\) '.+?'!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Verify the PDSC file for consistency."
summary: "The folder that contains the PDSC holds more than one *.pdsc file, so packchk does not read the pack; M206 printed just before lists the files."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:87", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CreateModel.cpp:39-63", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CreateModel.cpp:112-117", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ParseOptions.cpp:222", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtefsutils/src/RteFsUtils.cpp:750-788", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:132"]
---

## Symptom

`M203`
`Error reading PDSC file(s) '%PATH%'!`

## Cause

The folder that contains the PDSC holds more than one *.pdsc file, so packchk does not read the pack; M206 printed just before lists the files. Despite its text, M203 is not a content error of the PDSC.

## Fix

Remove or rename the extra .pdsc files (old copies, backups) in the PDSC's folder, or add --ignore-other-pdsc when they must stay.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:87`
- `tools/packchk/src/CreateModel.cpp:39-63`
- `tools/packchk/src/CreateModel.cpp:112-117`
- `tools/packchk/src/ParseOptions.cpp:222`
- `libs/rtefsutils/src/RteFsUtils.cpp:750-788`
- `tools/packchk/README.md:132`
