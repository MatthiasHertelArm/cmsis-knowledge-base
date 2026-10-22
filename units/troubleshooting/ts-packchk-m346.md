---
id: "ts-packchk-m346"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M346: Referenced device(s) in '…' not found: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M346"
symptoms: ["M346", "Referenced device(s) in '%BOARD%' not found: '%DEVICE%'"]
symptom_regex: "^Referenced device\\(s\\) in '.+?' not found: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The device or devices specified for the board could not be found. Verify and correct the device name or the board name. Refer to [/package/boards/board/mountedDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_mountedDevice) and [/package/boards/board/compatibleDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_compatibleDevice)."
summary: "packchk prints this warning when a board description in the PDSC refers to a device, through mountedDevice or compatibleDevice, whose name does not match any device declared in the pack. %BOARD% is the board whose entry holds the reference …"
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M346`
`Referenced device(s) in '%BOARD%' not found: '%DEVICE%'`

## Cause

packchk prints this warning when a board description in the PDSC refers to a device, through mountedDevice or compatibleDevice, whose name does not match any device declared in the pack. %BOARD% is the board whose entry holds the reference and %DEVICE% is the device name that could not be resolved. The README attributes it to a misspelled device name or board name.

## Fix

Compare the device name in the board's mountedDevice or compatibleDevice entries with the Dname attributes of the device declarations in the same PDSC, and correct the spelling so it matches exactly. Then rerun packchk.

## Note

The source clone was not available, so the trigger and the handling could not be checked against code. The cause and fix are taken from the message text and the README. The 'in the same PDSC' scope is an assumption that should be verified.
