---
id: "ts-svdconv-m365"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M365: Register '…' (…) (@…) has same address or overlaps '…' (…) (@…) …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M365"
symptoms: ["M365", "Register '%NAME%' (%ACCESS%) (@%ADDRSIZE%) has same address or overlaps '%NAME2%' (%ACCESS2%) (@%ADDRSIZE2%) %LINE%"]
symptom_regex: "^Register '.+?' \\(.+?\\) \\(@.+?\\) has same address or overlaps '.+?' \\(.+?\\) \\(@.+?\\) .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:653", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:671", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:732", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:737", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1071", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:184"]
---

## Symptom

`M365`
`Register '%NAME%' (%ACCESS%) (@%ADDRSIZE%) has same address or overlaps '%NAME2%' (%ACCESS2%) (@%ADDRSIZE2%) %LINE%`

## Cause

Two registers occupy the same address or overlapping bytes, and the later one has no matching <alternateRegister> or <alternateGroup>. This warning variant of M339 is used when the clash is not a plain same-address one between top-level registers: one register is in a cluster or a dim array/list, the start addresses differ (partial overlap), or the access types differ (for example read-write against read-only).

## Fix

Correct <addressOffset> or <size> if the overlap is a mistake. If the registers are intended views of the same address, add <alternateRegister> naming the other register (NAME2 in the message) or an <alternateGroup> to the later register.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:653`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:671`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:732`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:737`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1071`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:184`
