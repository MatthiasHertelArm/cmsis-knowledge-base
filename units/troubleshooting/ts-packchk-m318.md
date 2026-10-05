---
id: "ts-packchk-m318"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M318: Attribute '…' must not have '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M318"
symptoms: ["M318", "Attribute '%TAG%' must not have '%TAG2%'"]
symptom_regex: "^Attribute '.+?' must not have '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "A <compatibleDevice> element of a <board> carries a Dfamily or DsubFamily attribute; packchk wants compatible devices listed one by one with Dname."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:134", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1773-1781", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:989-1036", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/CheckBoardMountedCompatibleDevices/BulbBoard_BSP/Keil.BulbBoard_BSP.pdsc:45"]
---

## Symptom

`M318`
`Attribute '%TAG%' must not have '%TAG2%'`

## Cause

A <compatibleDevice> element of a <board> carries a Dfamily or DsubFamily attribute; packchk wants compatible devices listed one by one with Dname. In the text, %TAG% is the element (compatibleDevice) and %TAG2% the attribute, although it reads 'Attribute ... must not have ...'.

## Fix

Remove Dfamily and DsubFamily and add one <compatibleDevice> per device, e.g. <compatibleDevice deviceIndex="0" Dvendor="Cypress:19" Dname="S6E1A12C0A"/>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:134`
- `tools/packchk/src/ValidateSyntax.cpp:1773-1781`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:989-1036`
- `tools/packchk/test/data/CheckBoardMountedCompatibleDevices/BulbBoard_BSP/Keil.BulbBoard_BSP.pdsc:45`
