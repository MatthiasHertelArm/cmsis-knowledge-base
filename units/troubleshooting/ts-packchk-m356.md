---
id: "ts-packchk-m356"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M356: Path '…' does not specify a file!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M356"
symptoms: ["M356", "Path '%PATH%' does not specify a file!"]
symptom_regex: "^Path '.+?' does not specify a file!$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "A <file> element with a category other than \"include\" names a folder instead of a file, e.g. name=\"Files/\"."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:174", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:840-878", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:650-676", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/FilenameIsDir/TestVendor.FilenameIsDirPack.pdsc:30"]
---

## Symptom

`M356`
`Path '%PATH%' does not specify a file!`

## Cause

A <file> element with a category other than "include" names a folder instead of a file, e.g. name="Files/".

## Fix

Point name at a file; if the folder is meant as include path, use <file category="include" name="Files/"/>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:174`
- `tools/packchk/src/CheckFiles.cpp:840-878`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:650-676`
- `tools/packchk/test/data/FilenameIsDir/TestVendor.FilenameIsDirPack.pdsc:30`
