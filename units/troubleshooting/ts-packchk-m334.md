---
id: "ts-packchk-m334"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M334: Config File has no version: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M334"
symptoms: ["M334", "Config File has no version: '%PATH%'"]
symptom_regex: "^Config File has no version: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Specified file 'PATH' does not contain version information."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:150", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:378-380", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:598-617", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:175"]
---

## Symptom

`M334`
`Config File has no version: '%PATH%'`

## Cause

Specified file 'PATH' does not contain version information. It is recommended to specify versions for configuration files. Add attribute version with the file version in the `<file>` tag that defines the _'PATH'_ file in the PDSC. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file).

## Fix

Add version to the <file attr="config"> element, e.g. <file category="header" attr="config" name="Config/RTE_Device.h" version="1.0.0"/>, and raise it when the file changes.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:150`
- `tools/packchk/src/CheckFiles.cpp:378-380`
- `tools/packchk/src/CheckFiles.cpp:598-617`
- `tools/packchk/README.md:175`
