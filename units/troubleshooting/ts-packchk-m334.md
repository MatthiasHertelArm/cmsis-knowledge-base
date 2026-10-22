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
doc_cause: "Specified file 'PATH' does not contain version information. It is recommended to specify versions for configuration files. Add attribute version with the file version in the `<file>` tag that defines the _'PATH'_ file in the PDSC. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
summary: "packchk prints this warning when a configuration file listed in the PDSC has no version attribute on its <file> element."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message M334 text, source lines not available in this clone)"]
---

## Symptom

`M334`
`Config File has no version: '%PATH%'`

## Cause

packchk prints this warning when a configuration file listed in the PDSC has no version attribute on its <file> element. The %PATH% in the message is the path of that file as written in the PDSC. The README describes the same condition, so the message reflects the PDSC entry rather than the file contents.

## Fix

Open the PDSC, find the <file> element whose name matches the path shown in the message, and add a version attribute with the file's version, for example <file category="header" name="Config/config.h" version="1.0.0"/>. Then rerun packchk.

## Note

Source lines were not available, so the trigger is taken from the message text and the README only. The example file name and category are illustrative, not from the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message M334 text, source lines not available in this clone)`
