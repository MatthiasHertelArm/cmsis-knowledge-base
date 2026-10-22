---
id: "ts-packchk-m340"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M340: Include Path '…' must end with '/'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M340"
symptoms: ["M340", "Include Path '%PATH%' must end with '/'"]
symptom_regex: "^Include Path '.+?' must end with '/'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Include paths must end with a slash or backslash. Verify and correct the path name. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file)."
summary: "packchk prints this warning when an include path given in the PDSC (for example a component's include directory entry) does not end with a '/' or '\\' separator."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text M340, source lines not available in this session)"]
---

## Symptom

`M340`
`Include Path '%PATH%' must end with '/'`

## Cause

packchk prints this warning when an include path given in the PDSC (for example a component's include directory entry) does not end with a '/' or '\' separator. The %PATH% in the message is the offending path as written in the pack description. The README states this rule; the source itself was not available to confirm the exact check.

## Fix

Open the PDSC file, find the element named in the message with the path %PATH%, and add a trailing slash so the path ends with '/' (for example 'Device/Include/' instead of 'Device/Include'). Then rerun packchk.

## Note

Trigger and handling taken from the message text and the README only; the clone was not available, so the exact check location was not verified. The README's wording 'slash or backslash' is not confirmed against source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text M340, source lines not available in this session)`
