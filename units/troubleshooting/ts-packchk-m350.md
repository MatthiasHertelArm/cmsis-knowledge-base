---
id: "ts-packchk-m350"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M350: No '…' component found for […] '…' (Compiler: … […])"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M350"
symptoms: ["M350", "No '%COMP%' component found for [%VENDOR%] '%MCU%' (Compiler: %COMPILER% [%OPTION%])"]
symptom_regex: "^No '.+?' component found for \\[.+?\\] '.+?' \\(Compiler: .+? \\[.+?\\]\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The package ([/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package)) defines a Vendor-MCU combination for which no component was defined. Define a component ([/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component)) or verify the _'VENDOR'_ - _'MCU'_ settings."
summary: "For a device (checked per processor, per TrustZone mode when Dtz is set, and per compiler named in the pack's conditions), no Device:Startup component (Cclass=\"Device\" Cgroup=\"Startup\") is available whose conditions accept that device. packchk looks in this pack and …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:168", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:571-636", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:92-123", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:848-870", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:191"]
---

## Symptom

`M350`
`No '%COMP%' component found for [%VENDOR%] '%MCU%' (Compiler: %COMPILER% [%OPTION%])`

## Cause

For a device (checked per processor, per TrustZone mode when Dtz is set, and per compiler named in the pack's conditions), no Device:Startup component (Cclass="Device" Cgroup="Startup") is available whose conditions accept that device. packchk looks in this pack and in PDSC files given with -i.

## Fix

Add a Device:Startup component with a condition matching the device, or widen its condition (Dname pattern, Dvendor, Tcompiler) to cover the reported device and compiler; if the startup code comes from another pack, pass that PDSC with -i.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:168`
- `tools/packchk/src/ValidateSemantic.cpp:571-636`
- `tools/packchk/src/ValidateSemantic.cpp:92-123`
- `tools/packchk/src/ValidateSemantic.cpp:848-870`
- `tools/packchk/README.md:191`
