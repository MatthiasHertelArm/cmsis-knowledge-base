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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The device or devices specified for the board could not be found."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:164", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1734-1739", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1793-1798", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:989-1036", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:187"]
---

## Symptom

`M346`
`Referenced device(s) in '%BOARD%' not found: '%DEVICE%'`

## Cause

The device or devices specified for the board could not be found. Verify and correct the device name or the board name. Refer to [/package/boards/board/mountedDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_mountedDevice) and [/package/boards/board/compatibleDevice](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_compatibleDevice).

## Fix

Correct Dname and Dvendor of the <mountedDevice> or <compatibleDevice> to an existing device or variant, or pass the DFP's PDSC with -i so its devices are known.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:164`
- `tools/packchk/src/ValidateSyntax.cpp:1734-1739`
- `tools/packchk/src/ValidateSyntax.cpp:1793-1798`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:989-1036`
- `tools/packchk/README.md:187`
