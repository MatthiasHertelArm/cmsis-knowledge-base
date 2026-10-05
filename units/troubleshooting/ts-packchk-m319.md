---
id: "ts-packchk-m319"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M319: '…': '…' already defined for '…': '…', see Line …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M319"
symptoms: ["M319", "'%TAG%': '%NAME%' already defined for '%TAG2%': '%NAME2%', see Line %LINE%"]
symptom_regex: "^'.+?': '.+?' already defined for '.+?': '.+?', see Line .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:135", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1700-1711", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:989-1036", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/CheckBoardMountedCompatibleDevices/BulbBoard_BSP/Keil.BulbBoard_BSP.pdsc:39-43"]
---

## Symptom

`M319`
`'%TAG%': '%NAME%' already defined for '%TAG2%': '%NAME2%', see Line %LINE%`

## Cause

Two <mountedDevice> elements of the same <board> have the same deviceIndex value, which includes two mountedDevice elements that both omit deviceIndex. %NAME2% is the Dname of the earlier one and %LINE% its line.

## Fix

Give every <mountedDevice> of a board its own deviceIndex, e.g. deviceIndex="0" and deviceIndex="1".

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:135`
- `tools/packchk/src/ValidateSyntax.cpp:1700-1711`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:989-1036`
- `tools/packchk/test/data/CheckBoardMountedCompatibleDevices/BulbBoard_BSP/Keil.BulbBoard_BSP.pdsc:39-43`
