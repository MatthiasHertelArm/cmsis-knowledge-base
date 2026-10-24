---
id: "ts-svdconv-m358"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M358: AddressBlock of Peripheral '…' … overlaps AddressBlock … in same peripheral …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M358"
symptoms: ["M358", "AddressBlock of Peripheral '%NAME%' %TEXT% overlaps AddressBlock %TEXT2% in same peripheral %LINE%"]
symptom_regex: "^AddressBlock of Peripheral '.+?' .+? overlaps AddressBlock .+? in same peripheral .*$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "Two <addressBlock>s of the same peripheral overlap. svdconv keeps both for compatibility."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1227", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1247", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1263", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:177", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:251"]
---

## Symptom

`M358`
`AddressBlock of Peripheral '%NAME%' %TEXT% overlaps AddressBlock %TEXT2% in same peripheral %LINE%`

## Cause

Two <addressBlock>s of the same peripheral overlap. svdconv keeps both for compatibility. Warning by default, error with --strict.

## Fix

Merge the blocks into one, or change their <offset>/<size> so they do not overlap.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1227`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1247`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1263`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:177`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:251`
