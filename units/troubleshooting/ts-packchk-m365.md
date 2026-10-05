---
id: "ts-packchk-m365"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M365: Redefined … '…' found, see Line …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M365"
symptoms: ["M365", "Redefined %DEVTYPE% '%MCU%' found, see Line %LINE%"]
symptom_regex: "^Redefined .+? '.+?' found, see Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Remove duplicate device/variant entries. Refer to [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:184", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1892-1952", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1277-1300", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:76-108", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:204"]
---

## Symptom

`M365`
`Redefined %DEVTYPE% '%MCU%' found, see Line %LINE%`

## Cause

Two device leaves of the same kind (two <device> elements without variants, or two <variant> elements) have the same name in the PDSC.

## Fix

Rename or remove one of them so that every Dname and Dvariant is unique.

## Note

At 30f5e81 the function that raises M365 (ValidateSyntax::CheckDevices) is never called from Check(); the same duplication is reported as M392.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:184`
- `tools/packchk/src/ValidateSyntax.cpp:1892-1952`
- `tools/packchk/src/ValidateSyntax.cpp:1277-1300`
- `tools/packchk/src/ValidateSyntax.cpp:76-108`
- `tools/packchk/README.md:204`
