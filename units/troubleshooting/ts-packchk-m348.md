---
id: "ts-packchk-m348"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M348: Feature redefined for '…', see Line …: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M348"
symptoms: ["M348", "Feature redefined for '%MCU%', see Line %LINE%: '%PROP%'"]
symptom_regex: "^Feature redefined for '.+?', see Line .+?: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "This feature _'FEATURE'_ has been defined already on the same level in line _'REF\\_LINE'_. The feature characteristics defined on line _'LINE'_ overwrite those from _'REF\\_LINE'_. Correct the feature ([/package/devices/family/.../feature](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_feature))."
summary: "Two feature elements with the same name are defined at the same level of the device hierarchy in the PDSC, so the later one overwrites the earlier one."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M348`
`Feature redefined for '%MCU%', see Line %LINE%: '%PROP%'`

## Cause

Two feature elements with the same name are defined at the same level of the device hierarchy in the PDSC, so the later one overwrites the earlier one. The message names the device (%MCU%), the line of the earlier definition (%LINE%) and the feature property (%PROP%) that was redefined. The source lines were not available here, so this reading comes from the message and the README text only.

## Fix

Open the PDSC file and find the feature element for the named device at the line given in the message. Keep one feature definition per name at that level, remove or rename the duplicate, and correct the feature characteristics so the intended values are kept.

## Note

The source clone was not available, so the trigger condition and the exact line references could not be checked against the code. The README cause and fix were used as the basis. The README text uses _'LINE'_ and _'REF_LINE'_ placeholders that do not match the message's %LINE% variable, so the README wording is not a direct match for this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
