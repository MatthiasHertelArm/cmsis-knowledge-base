---
id: "ts-packchk-m364"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M364: No Devices for Condition '… […] …' available."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M364"
symptoms: ["M364", "No Devices for Condition '%COND% [%VENDOR%] %MCU%' available."]
symptom_regex: "^No Devices for Condition '.+? \\[.+?\\] .+?' available\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:183", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckConditions.cpp:152-188", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckComponents.cpp:155-188", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:203"]
---

## Symptom

`M364`
`No Devices for Condition '%COND% [%VENDOR%] %MCU%' available.`

## Cause

The specified condition refers to a device that does not exist. Define the device ([/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device)) or correct the information for the condition ([/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition)).

## Fix

Correct Dname (and Dvendor) in the condition expression to an existing device or variant, or pass the DFP's PDSC with -i so its devices are known.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:183`
- `tools/packchk/src/CheckConditions.cpp:152-188`
- `tools/packchk/src/CheckComponents.cpp:155-188`
- `tools/packchk/README.md:203`
