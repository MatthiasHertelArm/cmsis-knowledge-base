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
summary: "packchk found the same device name defined a second time in the PDSC, once as a device and once as a variant (or the reverse), so the name is redefined."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available)"]
---

## Symptom

`M366`
`Redefined %DEVTYPEEXIST% as %DEVTYPE% '%MCU%' found, see Line %LINE%`

## Cause

packchk found the same device name defined a second time in the PDSC, once as a device and once as a variant (or the reverse), so the name is redefined. The message names the earlier kind (%DEVTYPEEXIST%), the current kind (%DEVTYPE%), the device name (%MCU%) and the line of the duplicate (%LINE%). The README gives the same cause but the source lines were not available to confirm the trigger.

## Fix

Open the PDSC at the line reported in the message and remove or rename the duplicate device or variant entry so that each device name is defined only once, as described in the PDSC device element specification.

## Note

Source lines were not available, so the trigger condition and the exact line reference are taken from the message text and the README alone.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available)`
