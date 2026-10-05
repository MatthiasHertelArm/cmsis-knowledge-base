---
id: "ts-packchk-m321"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M321: DS5 project requires '.project' file."
status: "draft"
tool: "packchk"
severity: "error"
code: "M321"
symptoms: ["M321", "DS5 project requires '.project' file."]
symptom_regex: "^DS5 project requires '\\.project' file\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "An <example> has an <environment name=\"DS5\"> (name compared case-insensitively) whose load path does not end in an Eclipse '.project' file."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:137", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:282-290", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:143-157", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:350-366"]
---

## Symptom

`M321`
`DS5 project requires '.project' file.`

## Cause

An <example> has an <environment name="DS5"> (name compared case-insensitively) whose load path does not end in an Eclipse '.project' file.

## Fix

Set load to the example's .project file, relative to the example folder, e.g. <environment name="DS5" load=".project"/>, and ship .project and .cproject in that folder.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:137`
- `tools/packchk/src/CheckFiles.cpp:282-290`
- `tools/packchk/src/CheckFiles.cpp:143-157`
- `tools/packchk/src/CheckFiles.cpp:350-366`
