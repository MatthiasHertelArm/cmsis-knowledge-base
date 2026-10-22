---
id: "ts-packchk-m314"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M314: Filename '…' contains whitespaces, this is not recommended"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M314"
symptoms: ["M314", "Filename '%NAME%' contains whitespaces, this is not recommended"]
symptom_regex: "^Filename '.+?' contains whitespaces, this is not recommended$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "A file path referenced in the PDSC (file, book, algorithm, image, svd, example doc, environment load, csolution layer or template) contains a space character."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:130", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:578-591", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:343-345", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:370-372", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:765-791", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/FileNameHasSpace/TestVendor.FileNameHasSpacePack.pdsc:73"]
---

## Symptom

`M314`
`Filename '%NAME%' contains whitespaces, this is not recommended`

## Cause

A file path referenced in the PDSC (file, book, algorithm, image, svd, example doc, environment load, csolution layer or template) contains a space character.

## Fix

Rename the file or folder without spaces (use '_' or '-') and update the reference in the PDSC.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:130`
- `tools/packchk/src/CheckFiles.cpp:578-591`
- `tools/packchk/src/CheckFiles.cpp:343-345`
- `tools/packchk/src/CheckFiles.cpp:370-372`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:765-791`
- `tools/packchk/test/data/FileNameHasSpace/TestVendor.FileNameHasSpacePack.pdsc:73`
