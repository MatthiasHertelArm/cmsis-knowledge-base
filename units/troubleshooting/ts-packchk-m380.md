---
id: "ts-packchk-m380"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M380: No description found for […] '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M380"
symptoms: ["M380", "No description found for [%VENDOR%] '%MCU%'"]
symptom_regex: "^No description found for \\[.+?\\] '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "No description was found for the device _'MCU'_ from _'VENDOR'_. Use description attribute to provide information about the device, its subfamily, or family. Refer to [/package/devices/family/.../description](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_description)."
summary: "The <description> element that applies to the device (from device, subFamily or family level) is present but empty."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:199", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:332-349", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteItem.cpp:740-745", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:218"]
---

## Symptom

`M380`
`No description found for [%VENDOR%] '%MCU%'`

## Cause

The <description> element that applies to the device (from device, subFamily or family level) is present but empty. Devices have no description attribute; the description is the <description> element.

## Fix

Write the device text into the <description> element at device, subFamily or family level.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:199`
- `tools/packchk/src/ValidateSemantic.cpp:332-349`
- `libs/rtemodel/src/RteItem.cpp:740-745`
- `tools/packchk/README.md:218`
