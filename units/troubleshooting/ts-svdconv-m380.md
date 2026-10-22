---
id: "ts-svdconv-m380"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M380: AddressBlock of Peripheral '…' (@…) … does not fit into 32Bit Address Space."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M380"
symptoms: ["M380", "AddressBlock of Peripheral '%NAME%' (@%ADDR%) %TEXT% does not fit into 32Bit Address Space."]
symptom_regex: "^AddressBlock of Peripheral '.+?' \\(@.+?\\) .+? does not fit into 32Bit Address Space\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An <addressBlock> of a peripheral ends beyond 0xFFFFFFFF: the peripheral <baseAddress> plus the block's <offset> and <size> - 1 does not fit into 32 bits. svdconv ignores that address block."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1205-1225", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:201", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:257"]
---

## Symptom

`M380`
`AddressBlock of Peripheral '%NAME%' (@%ADDR%) %TEXT% does not fit into 32Bit Address Space.`

## Cause

An <addressBlock> of a peripheral ends beyond 0xFFFFFFFF: the peripheral <baseAddress> plus the block's <offset> and <size> - 1 does not fit into 32 bits. svdconv ignores that address block.

## Fix

Correct the peripheral's <baseAddress> or the address block's <offset> and <size> so the block ends at or below 0xFFFFFFFF; <size> is the length of the block, not its end address.

## Note

Error under --strict. TEXT prints the range as [end ... start]; ADDR is cast to 32 bits.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1205-1225`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:201`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:257`
