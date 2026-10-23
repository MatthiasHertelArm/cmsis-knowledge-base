---
id: "ts-svdconv-m382"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M382: … '…': … '…' does not fit into … width: … Bit."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M382"
symptoms: ["M382", "%LEVEL% '%NAME%': %NAME2% '%HEXNUM%' does not fit into %LEVEL% width: %NUM% Bit."]
symptom_regex: "^.+? '.+?': .+? '.+?' does not fit into .+? width: .+? Bit\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A register's <resetValue> or <resetMask> has bits set above the register width (e.g. 0x1FF for an 8-bit register); the width is the register's effective <size>, which may be inherited from the peripheral or device. svdconv replaces the value with 0."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:684-711", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:203", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:259"]
---

## Symptom

`M382`
`%LEVEL% '%NAME%': %NAME2% '%HEXNUM%' does not fit into %LEVEL% width: %NUM% Bit.`

## Cause

A register's <resetValue> or <resetMask> has bits set above the register width (e.g. 0x1FF for an 8-bit register); the width is the register's effective <size>, which may be inherited from the peripheral or device. svdconv replaces the value with 0.

## Fix

Make <resetValue> and <resetMask> fit the register width, e.g. <resetMask>0xFF</resetMask> for <size>8</size>, or correct the register's <size> if that is what is wrong.

## Note

Error under --strict. NAME2 says which of the two values failed (Reset Value or Reset Mask).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdRegister.cpp:684-711`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:203`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:259`
