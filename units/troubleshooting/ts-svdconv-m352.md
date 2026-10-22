---
id: "ts-svdconv-m352"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M352: AddressBlock of Peripheral '…' (@…) … overlaps '…' (@…) … …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M352"
symptoms: ["M352", "AddressBlock of Peripheral '%NAME%' (@%ADDR%) %TEXT% overlaps '%NAME2%' (@%ADDR2%) %TEXT2% %LINE%"]
symptom_regex: "^AddressBlock of Peripheral '.+?' \\(@.+?\\) .+? overlaps '.+?' \\(@.+?\\) .+? .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file declares two address blocks of the same peripheral whose address ranges overlap, so svdconv warns that the block named in the message (the first %NAME%, at %ADDR%) overlaps the second one (%NAME2%, at %ADDR2%)."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M352`
`AddressBlock of Peripheral '%NAME%' (@%ADDR%) %TEXT% overlaps '%NAME2%' (@%ADDR2%) %TEXT2% %LINE%`

## Cause

The SVD file declares two address blocks of the same peripheral whose address ranges overlap, so svdconv warns that the block named in the message (the first %NAME%, at %ADDR%) overlaps the second one (%NAME2%, at %ADDR2%). The %TEXT% and %TEXT2% fields describe the address block extents and %LINE% gives the position in the SVD file. The exact trigger condition could not be checked against source because the clone is not available.

## Fix

Open the SVD file at the reported line and correct the <addressBlock> offset and size values of the two listed blocks so that their ranges do not overlap, matching the device reference manual; then rerun svdconv.

## Note

Source lines were not provided, so the trigger and the README text were not verified; the cause and fix rest on the message wording alone.
