---
id: "ts-packchk-m366"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M366: Redefined … as … '…' found, see Line …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M366"
symptoms: ["M366", "Redefined %DEVTYPEEXIST% as %DEVTYPE% '%MCU%' found, see Line %LINE%"]
symptom_regex: "^Redefined .+? as .+? '.+?' found, see Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Device has been redefined as variant or vice versa. Remove duplicate device/variant entries. Refer to [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device)."
summary: "The same name is used once for a <device> without variants and once for a <variant>, so one leaf device is defined as both."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:185", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1918-1946", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1277-1300", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:76-108", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:205"]
---

## Symptom

`M366`
`Redefined %DEVTYPEEXIST% as %DEVTYPE% '%MCU%' found, see Line %LINE%`

## Cause

The same name is used once for a <device> without variants and once for a <variant>, so one leaf device is defined as both.

## Fix

Rename one of them so that every Dname and Dvariant is unique.

## Note

At 30f5e81 the function that raises M366 (ValidateSyntax::CheckDevices) is never called from Check(); the same duplication is reported as M392.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:185`
- `tools/packchk/src/ValidateSyntax.cpp:1918-1946`
- `tools/packchk/src/ValidateSyntax.cpp:1277-1300`
- `tools/packchk/src/ValidateSyntax.cpp:76-108`
- `tools/packchk/README.md:205`
