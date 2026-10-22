---
id: "ts-svdconv-m343"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M343: … '…' (@…) has same address as '…' …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M343"
symptoms: ["M343", "%LEVEL% '%NAME%' (@%ADDR%) has same address as '%NAME2%' %LINE%"]
symptom_regex: "^.+? '.+?' \\(@.+?\\) has same address as '.+?' .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "Two peripherals have the same base address, and the later one has no <alternatePeripheral> naming a peripheral already at that address."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:541", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:558", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:579", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:582", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:619", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:162"]
---

## Symptom

`M343`
`%LEVEL% '%NAME%' (@%ADDR%) has same address as '%NAME2%' %LINE%`

## Cause

Two peripherals have the same base address, and the later one has no <alternatePeripheral> naming a peripheral already at that address. If it has an <alternatePeripheral> that names none of them, M348 is printed first.

## Fix

Correct the later peripheral's <baseAddress>. If it really is another view of the same hardware, add <alternatePeripheral>NAME2</alternatePeripheral> to it, naming the peripheral given in the message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:541`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:558`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:579`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:582`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:619`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:162`
