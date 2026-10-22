---
id: "ts-packchk-m381"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M381: Vendor names are not equal: '[…] …', MCU '[…] …', see Line …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M381"
symptoms: ["M381", "Vendor names are not equal: '[%VENDOR%] %MCU%', MCU '[%VENDOR2%] %MCU2%', see Line %LINE%"]
symptom_regex: "^Vendor names are not equal: '\\[.+?\\] .+?', MCU '\\[.+?\\] .+?', see Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Vendor name specified in the Dvendor attribute for the `<mountedDevice>` tag does not match the actual device vendor name. Verify and correct vendor name. Refer to [/package/boards/board/mountedDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_mountedDevice)."
summary: "packchk found a mountedDevice entry in a board's PDSC whose vendor name differs from the vendor name of the device it refers to."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text for M381; source lines not available in this session)"]
---

## Symptom

`M381`
`Vendor names are not equal: '[%VENDOR%] %MCU%', MCU '[%VENDOR2%] %MCU2%', see Line %LINE%`

## Cause

packchk found a mountedDevice entry in a board's PDSC whose vendor name differs from the vendor name of the device it refers to. The message reports the mounted device's vendor and MCU name in the first pair of placeholders and the device's own vendor and MCU in the second pair, with the PDSC line number. The README attributes this to the Dvendor attribute of the mountedDevice element not matching the actual device vendor name.

## Fix

Open the PDSC at the line given in the message and compare the Dvendor attribute of the mountedDevice element with the vendor name used in the device definition it refers to. Correct the Dvendor value so it matches the device's vendor name exactly, then rerun packchk.

## Note

Answered from the message text and the README only, since the source clone was not available; the trigger condition and exact comparison were not verified in the code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text for M381; source lines not available in this session)`
