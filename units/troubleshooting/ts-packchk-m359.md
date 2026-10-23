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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The device family has no devices or subfamilies."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:178", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1337-1347", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:198"]
---

## Symptom

`M359`
`Family has no Device(s) or Subfamilies: '%FAMILY%`

## Cause

The device family has no devices or subfamilies. Add the missing information ([/package/devices/family](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_family)).

## Fix

Add <device> elements (or a <subFamily> with devices) to the <family>, or remove the empty family.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:178`
- `tools/packchk/src/ValidateSyntax.cpp:1337-1347`
- `tools/packchk/README.md:198`
