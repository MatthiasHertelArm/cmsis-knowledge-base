---
id: "ts-packchk-m346"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M346: Referenced device(s) in"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M346"
symptoms: ["M346", "Referenced device(s) in '%BOARD%' not found: '%DEVICE%'"]
symptom_regex: "^Referenced device\\(s\\) in '.+?' not found: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M346`
`Referenced device(s) in '%BOARD%' not found: '%DEVICE%'`

## Cause

The device or devices specified for the board could not be found. Verify and correct the device name or the board name. Refer to [/package/boards/board/mountedDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_mountedDevice) and [/package/boards/board/compatibleDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_compatibleDevice).

## Fix

_siehe Cause_
