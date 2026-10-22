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
summary: "An <addressBlock> of one peripheral overlaps an address block of another peripheral (absolute range = <baseAddress> + <offset>, <size> bytes)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:686", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:704", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:721", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:734", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:749", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:171"]
---

## Symptom

`M352`
`AddressBlock of Peripheral '%NAME%' (@%ADDR%) %TEXT% overlaps '%NAME2%' (@%ADDR2%) %TEXT2% %LINE%`

## Cause

An <addressBlock> of one peripheral overlaps an address block of another peripheral (absolute range = <baseAddress> + <offset>, <size> bytes). A peripheral that has an <alternatePeripheral> is not checked from its own side, and pairs where one names the other as alternate are skipped; other overlapping pairs are usually reported once from each side.

## Fix

Correct the <baseAddress> or the address block's <offset>/<size> so the ranges do not overlap. If one peripheral is an alias of the other, mark it with <alternatePeripheral>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:686`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:704`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:721`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:734`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:749`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:171`
