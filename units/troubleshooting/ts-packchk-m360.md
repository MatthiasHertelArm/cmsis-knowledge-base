---
id: "ts-packchk-m360"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M360: Subfamily has no Device(s): '…"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M360"
symptoms: ["M360", "Subfamily has no Device(s): '%SUBFAMILY%"]
symptom_regex: "^Subfamily has no Device\\(s\\): '.+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Add the missing information. Refer to [/package/devices/family/subFamily](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_subFamily)."
summary: "packchk prints this warning when a subFamily element in the PDSC family section has no device entries under it, so the subFamily name shown in the message (%SUBFAMILY%) has no Device elements associated with it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M360`
`Subfamily has no Device(s): '%SUBFAMILY%`

## Cause

packchk prints this warning when a subFamily element in the PDSC family section has no device entries under it, so the subFamily name shown in the message (%SUBFAMILY%) has no Device elements associated with it. The source lines were not available, so this is inferred from the message text and the README rather than read from the trigger code.

## Fix

Open the PDSC file, find the <subFamily> element named in the message, and add the missing <device> entries for it under the matching <family> element, or remove the <subFamily> element if it is not needed. Then run packchk again.

## Note

Trigger condition read from the message text and README only; the clone was not available to confirm the exact check in PackChk_Msgs.cpp. The README points to the pdsc subFamily reference for the element structure.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
