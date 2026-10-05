---
id: "ts-packchk-m506"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M506: RTE Model reports: …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M506"
symptoms: ["M506", "RTE Model reports: %MSG%"]
symptom_regex: "^RTE Model reports: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:229", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/RteModelReader.cpp:31-37", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteModel.cpp:420-434", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteComponent.cpp:55-62", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RtePackage.cpp:691-716"]
---

## Symptom

`M506`
`RTE Model reports: %MSG%`

## Cause

Validation of the RTE model reported a warning: #500 the same pack (vendor, name, version) is loaded twice, for example because the PDSC under test is also passed with -i; #520 the pack defines a component with the same component ID twice; #521 a condition id is defined more than once (the duplicate is ignored).

## Fix

Do not pass the checked PDSC, or a second copy of a pack, with -i; make every component definition unique (e.g. a different Cvariant); remove or rename duplicate condition ids.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:229`
- `tools/packchk/src/RteModelReader.cpp:31-37`
- `libs/rtemodel/src/RteModel.cpp:420-434`
- `libs/rtemodel/src/RteComponent.cpp:55-62`
- `libs/rtemodel/src/RtePackage.cpp:691-716`
