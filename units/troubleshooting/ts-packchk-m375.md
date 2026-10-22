---
id: "ts-packchk-m375"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M375: No <mountedDevices> for Board '…' found."
status: "draft"
tool: "packchk"
severity: "error"
code: "M375"
symptoms: ["M375", "No <mountedDevices> for Board '%BOARD%' found."]
symptom_regex: "^No <mountedDevices> for Board '.+?' found\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "If a board element does not contain a `<mountedDevice>` element, then the examples for this board are not shown and example projects may not appear in the development tools. Refer to [/package/boards/board/mountedDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_mountedDevice) of [/package/boards](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_boards)."
summary: "packchk prints this error when a board entry in the PDSC has no <mountedDevices> child element to list the devices mounted on that board."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M375`
`No <mountedDevices> for Board '%BOARD%' found.`

## Cause

packchk prints this error when a board entry in the PDSC has no <mountedDevices> child element to list the devices mounted on that board. The %BOARD% variable is the name of the board that lacks it. The README describes the consequence as the board's examples not being shown and example projects possibly missing in the development tools. The source lines were not available, so this is taken from the message text and the README rather than from the trigger code.

## Fix

Open the PDSC file, find the <board> element named in the message, and add a <mountedDevices> element with <mountedDevice> children that name the devices mounted on the board, as described in the Pack Specification for /package/boards/board/mountedDevice. Then rerun packchk.

## Note

Source lines were not provided, so the trigger condition is inferred from the message wording and README only. The README says mountedDevice is the element to add; the message says mountedDevices, which is the parent element. Verify against the source before relying on the exact element names.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
