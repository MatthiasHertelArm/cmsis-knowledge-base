---
id: "ts-packchk-m375"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M375: No <mountedDevices> for Board"
status: "draft"
tool: "packchk"
severity: "error"
code: "M375"
symptoms: ["M375", "No <mountedDevices> for Board '%BOARD%' found."]
symptom_regex: "^No <mountedDevices> for Board '.+?' found\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M375`
`No <mountedDevices> for Board '%BOARD%' found.`

## Cause

If a board element does not contain a `<mountedDevice>` element, then the examples for this board are not shown and example projects may not appear in the development tools. Refer to [/package/boards/board/mountedDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_mountedDevice) of [/package/boards](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_boards).

## Fix

_siehe Cause_
