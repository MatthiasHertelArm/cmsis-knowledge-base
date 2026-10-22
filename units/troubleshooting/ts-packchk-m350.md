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
summary: "The PDSC declares a device (vendor and MCU) for which no matching component was defined in the package, so packchk cannot find the component named in the message for that device."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M350`
`No '%COMP%' component found for [%VENDOR%] '%MCU%' (Compiler: %COMPILER% [%OPTION%])`

## Cause

The PDSC declares a device (vendor and MCU) for which no matching component was defined in the package, so packchk cannot find the component named in the message for that device. The variable parts are the missing component name, the vendor and MCU from the device entry, and the compiler and option being checked.

## Fix

Open the package's PDSC file and either add a component entry (the component name shown in the message) covering this vendor and MCU, or correct the vendor and MCU settings so they match an existing component definition.

## Note

The source clone was not available, so the trigger and handling are taken from the message text and README only; the exact condition in the source could not be verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
