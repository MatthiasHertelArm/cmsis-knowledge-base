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
summary: "The SVD file declares a peripheral whose address block (base address plus the block's offset and size) extends beyond the 32-bit address space, so the end of the block would wrap past 0xFFFFFFFF."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M380`
`AddressBlock of Peripheral '%NAME%' (@%ADDR%) %TEXT% does not fit into 32Bit Address Space.`

## Cause

The SVD file declares a peripheral whose address block (base address plus the block's offset and size) extends beyond the 32-bit address space, so the end of the block would wrap past 0xFFFFFFFF. The %NAME% and %ADDR% placeholders are the peripheral name and its base address from the SVD, and %TEXT% describes the offending address block. The source lines were not available, so this is inferred from the message text alone.

## Fix

Open the SVD file, find the peripheral named in the message and check its baseAddress together with the addressBlock offset and size of its address block; correct the values so the block ends at or below 0xFFFFFFFF, then run svdconv again.

## Note

Source lines were unavailable; the cause is inferred from the message wording. The fix assumes the peripheral base address or the address block values are wrong in the SVD.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
