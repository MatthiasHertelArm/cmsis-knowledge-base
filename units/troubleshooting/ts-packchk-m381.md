---
id: "ts-packchk-m381"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M381: Vendor names are not equal: '["
status: "draft"
tool: "packchk"
severity: "warning"
code: "M381"
symptoms: ["M381", "Vendor names are not equal: '[%VENDOR%] %MCU%', MCU '[%VENDOR2%] %MCU2%', see Line %LINE%"]
symptom_regex: "^Vendor names are not equal: '\\[.+?\\] .+?', MCU '\\[.+?\\] .+?', see Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M381`
`Vendor names are not equal: '[%VENDOR%] %MCU%', MCU '[%VENDOR2%] %MCU2%', see Line %LINE%`

## Cause

Vendor name specified in the Dvendor attribute for the `<mountedDevice>` tag does not match the actual device vendor name. Verify and correct vendor name. Refer to [/package/boards/board/mountedDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_mountedDevice).

## Fix

_siehe Cause_
