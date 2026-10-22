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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The specified condition refers to a device that does not exist. Define the device ([/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device)) or correct the information for the condition ([/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition))."
summary: "A condition in the PDSC refers to a device, through its device or family attributes, that packchk cannot find among the devices the pack defines."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M364`
`No Devices for Condition '%COND% [%VENDOR%] %MCU%' available.`

## Cause

A condition in the PDSC refers to a device, through its device or family attributes, that packchk cannot find among the devices the pack defines. The %COND%, %VENDOR% and %MCU% parts of the message name the condition and the device it tried to match. The README attributes this to a device that does not exist in the pack or to a wrong condition entry.

## Fix

Check the condition named in the message in the PDSC conditions section and confirm the device, vendor and family it refers to are spelled as they appear in the devices section. Either add the missing device under the family's devices element or correct the condition's device attributes so they match an existing device.

## Note

The clone was not available, so the trigger and the surrounding handling could not be read; cause and fix come from the message text and the README only. The README cause is taken as the basis.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
