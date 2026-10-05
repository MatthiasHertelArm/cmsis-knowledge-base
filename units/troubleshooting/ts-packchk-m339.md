---
id: "ts-packchk-m339"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M339: Include Path '…' must not be a file!"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M339"
symptoms: ["M339", "Include Path '%PATH%' must not be a file!"]
symptom_regex: "^Include Path '.+?' must not be a file!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The path specified contains a filename. Correct the path infomation and remove the filename. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:157", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:862-868", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:180"]
---

## Symptom

`M339`
`Include Path '%PATH%' must not be a file!`

## Cause

A <file category="include"> entry does not name an existing folder: it points to a file, or to a path that does not exist.

## Fix

Set name to the include folder with a trailing '/', e.g. <file category="include" name="Include/"/>; list single header files with category="header" instead.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:157`
- `tools/packchk/src/CheckFiles.cpp:862-868`
- `tools/packchk/README.md:180`
