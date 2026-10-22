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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Multiple defitions of device or variant _'NAME'_ are found. Use unique names for the devices listed in the message _'MSG'_. Refer to [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device) and [/package/devices/family/.../device/variant](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_variant)"
summary: "The PDSC contains two or more device or variant elements that resolve to the same name, so packchk cannot tell them apart."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the given lines; message text only)"]
---

## Symptom

`M392`
`Redefined Device or Variant '%NAME%': %MSG%`

## Cause

The PDSC contains two or more device or variant elements that resolve to the same name, so packchk cannot tell them apart. The %NAME% part is the duplicated device or variant name and %MSG% gives the details of the clash. The README describes this as multiple definitions of the same device or variant name in the family/device/variant hierarchy.

## Fix

Open the PDSC file and search for the name shown in the message. Rename one of the duplicated device or variant entries so each Dname (device) and variant Dvariant name in the family is unique, then run packchk again.

## Note

Source lines were not available, so the trigger condition and the exact detail carried by %MSG% are unverified; the cause is inferred from the message text and README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the given lines; message text only)`
