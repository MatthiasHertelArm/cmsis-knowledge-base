---
id: "ts-packchk-m359"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M359: Family has no Device(s) or Subfamilies: '…"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M359"
symptoms: ["M359", "Family has no Device(s) or Subfamilies: '%FAMILY%"]
symptom_regex: "^Family has no Device\\(s\\) or Subfamilies: '.+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The device family has no devices or subfamilies. Add the missing information ([/package/devices/family](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_family))."
summary: "The PDSC file declares a device family (a family element with a family attribute) that contains neither device entries nor subfamily entries. packchk reports the family name in place of %FAMILY%, which is the value of the family attribute …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M359`
`Family has no Device(s) or Subfamilies: '%FAMILY%`

## Cause

The PDSC file declares a device family (a family element with a family attribute) that contains neither device entries nor subfamily entries. packchk reports the family name in place of %FAMILY%, which is the value of the family attribute in the PDSC. Since the source was not available, this reading rests on the message text and the README statement only.

## Fix

Open the PDSC file, find the <family> element named in the message, and add either the <device> entries it should contain or <subFamily> entries under it. If the family is not needed, remove the empty <family> element.

## Note

Source lines were not available; the trigger condition and the fix are taken from the message text and the README only. The message is a warning, so the pack may still be built.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
