---
id: "ts-packchk-m392"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M392: Redefined Device or Variant '…': …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M392"
symptoms: ["M392", "Redefined Device or Variant '%NAME%': %MSG%"]
symptom_regex: "^Redefined Device or Variant '.+?': .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Multiple defitions of device or variant _'NAME'_ are found."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:211", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1349-1352", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1413-1431", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:226"]
---

## Symptom

`M392`
`Redefined Device or Variant '%NAME%': %MSG%`

## Cause

Multiple defitions of device or variant _'NAME'_ are found. Use unique names for the devices listed in the message _'MSG'_. Refer to [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device) and [/package/devices/family/.../device/variant](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_variant)

## Fix

Rename one of the device or variant definitions so each name is unique, or remove the duplicate; the message lists every place the name is used.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:211`
- `tools/packchk/src/ValidateSyntax.cpp:1349-1352`
- `tools/packchk/src/ValidateSyntax.cpp:1413-1431`
- `tools/packchk/README.md:226`
