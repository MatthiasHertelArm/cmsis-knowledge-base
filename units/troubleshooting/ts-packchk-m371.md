---
id: "ts-packchk-m371"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M371: … Feature for '…': '…' unknown."
status: "draft"
tool: "packchk"
severity: "error"
code: "M371"
symptoms: ["M371", "%SECTION% Feature for '%MCU%': '%FEATURE%' unknown."]
symptom_regex: "^.+? Feature for '.+?': '.+?' unknown\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "This feature _'FEATURE'_ is unknwon to the specified _'MCU'_. Correct the feature ([/package/devices/family/.../feature](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_feature)) if this is a typo."
summary: "packchk checks the feature elements of a device in the PDSC and found a feature name for the given MCU that is not one of the features it knows."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M371`
`%SECTION% Feature for '%MCU%': '%FEATURE%' unknown.`

## Cause

packchk checks the feature elements of a device in the PDSC and found a feature name for the given MCU that is not one of the features it knows. The message names the section, the device and the offending feature value taken from the family's feature element in the pack description.

## Fix

Open the PDSC device or family entry named in the message and correct the feature element whose name is misspelled or not a recognized feature, then rerun packchk.

## Note

The source lines were not available, so the trigger and handling are not confirmed from code. The README cause text contains the typo 'unknwon'; the README also describes the feature as unknown to the MCU, which matches the message. Only the message text and README were used.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
