---
id: "ts-svdconv-m339"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M339: Register '…' (…) (@…) has same address or overlaps '…' (…) (@…) …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M339"
symptoms: ["M339", "Register '%NAME%' (%ACCESS%) (@%ADDRSIZE%) has same address or overlaps '%NAME2%' (%ACCESS2%) (@%ADDRSIZE2%) %LINE%"]
symptom_regex: "^Register '.+?' \\(.+?\\) \\(@.+?\\) has same address or overlaps '.+?' \\(.+?\\) \\(@.+?\\) .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "Two registers placed directly in a peripheral start at the same address with the same access, and the later one has neither an <alternateRegister> naming the other nor an <alternateGroup>."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:653", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:671", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:732", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:739", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1071", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:553", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:158"]
---

## Symptom

`M339`
`Register '%NAME%' (%ACCESS%) (@%ADDRSIZE%) has same address or overlaps '%NAME2%' (%ACCESS2%) (@%ADDRSIZE2%) %LINE%`

## Cause

Two registers placed directly in a peripheral start at the same address with the same access, and the later one has neither an <alternateRegister> naming the other nor an <alternateGroup>. A read-only and a write-only register may share an address; overlaps inside clusters or dim arrays, partial overlaps and overlaps between registers of different access are reported as warning M365 instead.

## Fix

If the address is wrong, correct the later register's <addressOffset>. If both registers are views of the same address, add <alternateRegister>NAME2</alternateRegister> (the register named in the message) or an <alternateGroup> to the later register.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:653`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:671`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:732`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:739`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1071`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:553`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:158`
