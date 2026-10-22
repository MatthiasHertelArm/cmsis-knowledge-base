---
id: "ts-packchk-m367"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M367: Redefined … '…' found, see Line …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M367"
symptoms: ["M367", "Redefined %TYPE% '%NAME%' found, see Line %LINE%"]
symptom_regex: "^Redefined .+? '.+?' found, see Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Remove duplicate device/variant entries. Refer to [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device)."
summary: "A PDSC element that must be unique within the pack (for example a device, variant, or other named item) appears more than once with the same name. packchk prints the duplicate's type and name and points to the line …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available)"]
---

## Symptom

`M367`
`Redefined %TYPE% '%NAME%' found, see Line %LINE%`

## Cause

A PDSC element that must be unique within the pack (for example a device, variant, or other named item) appears more than once with the same name. packchk prints the duplicate's type and name and points to the line of the earlier definition. The source lines were not available, so the exact check is inferred from the message text and the README.

## Fix

Open the PDSC file named in the log and find the element whose type and name match the message. Keep one definition and delete or rename the other, so each device or variant name appears only once in the family. Then run packchk again.

## Note

The source lines were not available, so the trigger condition is inferred from the message and README. The README gives the same fix, so it is consistent with the message text.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available)`
