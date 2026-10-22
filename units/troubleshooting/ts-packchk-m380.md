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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "No description was found for the device _'MCU'_ from _'VENDOR'_. Use description attribute to provide information about the device, its subfamily, or family. Refer to [/package/devices/family/.../description](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_description)."
summary: "packchk prints this warning when a device entry in the PDSC for the vendor and MCU named in the message has no description element at the family, subfamily or device level, so the tool has no text to show …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (source lines not available in this review; trigger inferred from the message text and README)"]
---

## Symptom

`M380`
`No description found for [%VENDOR%] '%MCU%'`

## Cause

packchk prints this warning when a device entry in the PDSC for the vendor and MCU named in the message has no description element at the family, subfamily or device level, so the tool has no text to show for it. The variable parts are the vendor and the device name as they appear in the PDSC. The README describes the same condition and points at the description element of the family in the PDSC.

## Fix

Add a description element for the device, its subfamily or its family in the PDSC, for example <family Dvendor="VENDOR" ...><description>Short device description</description></family>, using the device name from the message, then rerun packchk.

## Note

Source lines were not available, so the trigger condition is taken from the message and README only; the exact check in PackChk_Msgs.cpp was not verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (source lines not available in this review; trigger inferred from the message text and README)`
