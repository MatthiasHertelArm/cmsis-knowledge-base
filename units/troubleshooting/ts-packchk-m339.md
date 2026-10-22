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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The path specified contains a filename. Correct the path infomation and remove the filename. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
summary: "packchk found an include path entry in the PDSC (a file element with category include, or a component/bundle include) that points at an existing file instead of a directory."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text 'M339 | Include Path '%PATH%' must not be a file!', trigger not available in the given lines)"]
---

## Symptom

`M339`
`Include Path '%PATH%' must not be a file!`

## Cause

packchk found an include path entry in the PDSC (a file element with category include, or a component/bundle include) that points at an existing file instead of a directory. The %PATH% in the message is that entry as written in the pack description. The README attributes this to a filename left in the path, which is the usual reason.

## Fix

Open the PDSC file element named in the message and change its path so it names the directory that contains the headers, not a file inside it. Remove the trailing filename, for example change include path "Device/Include/device.h" to "Device/Include". Then rerun packchk.

## Note

Source lines were not available, so the trigger condition is inferred from the message text and the README; confidence is capped at medium. The README links to the PDSC components page for the file element.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text 'M339 | Include Path '%PATH%' must not be a file!', trigger not available in the given lines)`
