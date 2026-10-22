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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Remove duplicate device/variant entries. Refer to [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device)."
summary: "packchk found a second definition of the same device or variant name (%MCU%) in the PDSC while scanning the devices section, and it reports the line of the earlier definition in %LINE%."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message M365 text: Redefined %DEVTYPE% '%MCU%' found, see Line %LINE%)"]
---

## Symptom

`M365`
`Redefined %DEVTYPE% '%MCU%' found, see Line %LINE%`

## Cause

packchk found a second definition of the same device or variant name (%MCU%) in the PDSC while scanning the devices section, and it reports the line of the earlier definition in %LINE%. The duplicate entry is typically a device or variant listed twice under the same family, or the same name repeated across the pack's device entries.

## Fix

Open the PDSC file, search for the device or variant name reported in the message, and remove or rename the duplicate <device> or <variant> element so each name appears once. Then rerun packchk on the pack.

## Note

The source lines were not available, so the trigger condition is inferred from the message text and the README cause only; the exact check and which line number %LINE% refers to could not be confirmed.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message M365 text: Redefined %DEVTYPE% '%MCU%' found, see Line %LINE%)`
