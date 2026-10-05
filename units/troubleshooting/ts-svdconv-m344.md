---
id: "ts-svdconv-m344"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M344: Register '…' (@…) is outside or does not fit any <addressBlock> specified for Peripheral '…' …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M344"
symptoms: ["M344", "Register '%NAME%' (@%ADDRSIZE%) is outside or does not fit any <addressBlock> specified for Peripheral '%NAME2%' %TEXT%"]
symptom_regex: "^Register '.+?' \\(@.+?\\) is outside or does not fit any <addressBlock> specified for Peripheral '.+?' .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:868", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:874", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:928", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:972", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:163", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:247"]
---

## Symptom

`M344`
`Register '%NAME%' (@%ADDRSIZE%) is outside or does not fit any <addressBlock> specified for Peripheral '%NAME2%' %TEXT%`

## Cause

A register's byte range (its offset in the peripheral, cluster offsets included, plus <size>/8) does not lie completely inside any of the peripheral's <addressBlock>s with <usage>registers</usage>; blocks with usage buffer or reserved do not count. TEXT lists the register's range and every address block. Warning by default, error with --strict.

## Fix

Extend an address block, or add one with <usage>registers</usage>, so that it covers the register; or correct the register's <addressOffset> or <size> if the register is misplaced.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:868`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:874`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:928`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:972`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:163`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:247`
