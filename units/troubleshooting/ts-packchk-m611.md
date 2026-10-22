---
id: "ts-packchk-m611"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M611: Multiple devices or variants defined by '[…] …'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M611"
symptoms: ["M611", "Multiple devices or variants defined by '[%VENDOR%] %MCU%'"]
symptom_regex: "^Multiple devices or variants defined by '\\[.+?\\] .+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The message text indicates that the PDSC defines the same device or variant name for the given vendor and MCU more than once, so packchk cannot tell which definition applies."
cause_origin: "source-analysis"
confidence: "low"
---

## Symptom

`M611`
`Multiple devices or variants defined by '[%VENDOR%] %MCU%'`

## Cause

The message text indicates that the PDSC defines the same device or variant name for the given vendor and MCU more than once, so packchk cannot tell which definition applies. The variable parts are the vendor (%VENDOR%) and the device name (%MCU%). This is inferred from the message wording only, because the source lines for the trigger were not available.

## Fix

Search the pack's PDSC file for every device or variant entry with the reported name and vendor, then remove or rename the duplicates so each device or variant name is defined once.

## Note

The source clone was unavailable, so the trigger condition and the handling were not read from tools/packchk/src/PackChk_Msgs.cpp. Cause and fix come from the message text and should be checked against the source. The README does not document this message.
