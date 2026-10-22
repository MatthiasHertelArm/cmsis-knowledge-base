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
symptom_regex: "^AddressBlock of Peripheral '.+?' .+? overlaps AddressBlock .+? in same peripheral .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file declares two address blocks inside the same peripheral whose address ranges overlap, so the address space of one block intersects the other. svdconv reports the peripheral name and the two overlapping blocks as the variable parts …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M358`
`AddressBlock of Peripheral '%NAME%' %TEXT% overlaps AddressBlock %TEXT2% in same peripheral %LINE%`

## Cause

The SVD file declares two address blocks inside the same peripheral whose address ranges overlap, so the address space of one block intersects the other. svdconv reports the peripheral name and the two overlapping blocks as the variable parts of the message. The source lines were not available, so this is inferred from the message text and the README wording rather than confirmed in code.

## Fix

Open the SVD file at the named peripheral and compare the <addressBlock> offset and size entries. Adjust the offset or size of one of the two blocks so their ranges no longer overlap, then rerun svdconv. If the overlap is intentional in the device documentation, confirm that against the reference manual before changing the SVD.

## Note

The clone was not available, so no line numbers could be cited and the trigger condition is taken from the message text only. The exact overlap rule and whether the message is a warning that still produces output were not verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
