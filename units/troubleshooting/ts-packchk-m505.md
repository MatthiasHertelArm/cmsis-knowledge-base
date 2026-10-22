---
id: "ts-packchk-m505"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M505: RTE Model reports: …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M505"
symptoms: ["M505", "RTE Model reports: %MSG%"]
symptom_regex: "^RTE Model reports: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Validation of the RTE model built from the loaded PDSC files found an error and prints it as '<pack>: <element> '<id>': error #<n>: <text>'."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:228", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/RteModelReader.cpp:20-44", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/RteModelReader.cpp:142-154", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteItem.cpp:470-474", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteItem.cpp:1048-1066", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteComponent.cpp:47-53", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteCondition.cpp:160-192", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteCondition.cpp:360-372", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteDevice.cpp:525-553", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteExample.cpp:46-53"]
---

## Symptom

`M505`
`RTE Model reports: %MSG%`

## Cause

Validation of the RTE model built from the loaded PDSC files found an error and prints it as '<pack>: <element> '<id>': error #<n>: <text>'. Typical cases: #501 a component definition with errors such as a condition attribute naming an undefined condition; #502 a condition with an empty expression, mixed B/C/D/T attributes in one expression, or a component expression without Cclass or Cgroup; #503 condition recursion; #530 a device or variant without <processor>; #531 a device property whose Pname names no processor, or an invalid example.

## Fix

Fix the element named in the message at the reported line (define the condition, split the expression, add Cclass/Cgroup, add the <processor>, correct Pname); the M500 lines that follow give the details.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:228`
- `tools/packchk/src/RteModelReader.cpp:20-44`
- `tools/packchk/src/RteModelReader.cpp:142-154`
- `libs/rtemodel/src/RteItem.cpp:470-474`
- `libs/rtemodel/src/RteItem.cpp:1048-1066`
- `libs/rtemodel/src/RteComponent.cpp:47-53`
- `libs/rtemodel/src/RteCondition.cpp:160-192`
- `libs/rtemodel/src/RteCondition.cpp:360-372`
- `libs/rtemodel/src/RteDevice.cpp:525-553`
- `libs/rtemodel/src/RteExample.cpp:46-53`
