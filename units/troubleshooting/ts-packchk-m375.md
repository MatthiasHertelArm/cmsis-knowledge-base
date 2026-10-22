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
summary: "If a board element does not contain a `<mountedDevice>` element, then the examples for this board are not shown and example projects may not appear in the development tools."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:194", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1692-1698", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:213"]
---

## Symptom

`M375`
`No <mountedDevices> for Board '%BOARD%' found.`

## Cause

If a board element does not contain a `<mountedDevice>` element, then the examples for this board are not shown and example projects may not appear in the development tools. Refer to [/package/boards/board/mountedDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_mountedDevice) of [/package/boards](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_boards).

## Fix

Add the device the board carries: <mountedDevice deviceIndex="0" Dvendor="ARM:82" Dname="ARMCM4"/>. The message says <mountedDevices>; the element is <mountedDevice>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:194`
- `tools/packchk/src/ValidateSyntax.cpp:1692-1698`
- `tools/packchk/README.md:213`
