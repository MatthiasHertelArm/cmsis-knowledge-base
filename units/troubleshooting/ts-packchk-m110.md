---
id: "ts-packchk-m110"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M110: Verifying RTE Model failed"
status: "draft"
tool: "packchk"
severity: "error"
code: "M110"
symptoms: ["M110", "Verifying RTE Model failed"]
symptom_regex: "^Verifying RTE Model failed$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Contact Arm for clarifications"
summary: "Validation of the RTE model built from the PDSC (and any -i reference PDSCs) found invalid items, for example a condition attribute that names an undefined condition."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:81", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/RteModelReader.cpp:142-154", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/RteModelReader.cpp:20-44", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteItem.cpp:1048-1066", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1201-1247", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/CsolutionTag/TestVendor.CsolutionTag.pdsc:39", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:122"]
---

## Symptom

`M110`
`Verifying RTE Model failed`

## Cause

Validation of the RTE model built from the PDSC (and any -i reference PDSCs) found invalid items, for example a condition attribute that names an undefined condition. The details follow right after as 'RTE Model reports' messages (M500, M505, M506).

## Fix

Work through the 'RTE Model reports' lines after M110 and fix each named element (define or correct the condition id, add the missing <processor>, remove duplicates); M110 goes away with them.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:81`
- `tools/packchk/src/RteModelReader.cpp:142-154`
- `tools/packchk/src/RteModelReader.cpp:20-44`
- `libs/rtemodel/src/RteItem.cpp:1048-1066`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1201-1247`
- `tools/packchk/test/data/CsolutionTag/TestVendor.CsolutionTag.pdsc:39`
- `tools/packchk/README.md:122`
