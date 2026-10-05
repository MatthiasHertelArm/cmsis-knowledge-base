---
id: "ts-packchk-m607"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M607: Tag '…' does not allow wildcard specification: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M607"
symptoms: ["M607", "Tag '%TAG%' does not allow wildcard specification: '%NAME%'"]
symptom_regex: "^Tag '.+?' does not allow wildcard specification: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:242", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1729-1732", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:989-1036", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/CheckBoardMountedCompatibleDevices/BulbBoard_BSP/Keil.BulbBoard_BSP.pdsc:44"]
---

## Symptom

`M607`
`Tag '%TAG%' does not allow wildcard specification: '%NAME%'`

## Cause

A <mountedDevice> of a <board> uses a wildcard (*, ?, [ or ]) in Dname; a mounted device must name one device.

## Fix

Replace the pattern with the exact device or variant name, e.g. <mountedDevice deviceIndex="0" Dvendor="ARM:82" Dname="ARMCM4"/>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:242`
- `tools/packchk/src/ValidateSyntax.cpp:1729-1732`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:989-1036`
- `tools/packchk/test/data/CheckBoardMountedCompatibleDevices/BulbBoard_BSP/Keil.BulbBoard_BSP.pdsc:44`
