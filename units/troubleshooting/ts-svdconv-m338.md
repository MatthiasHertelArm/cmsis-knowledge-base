---
id: "ts-svdconv-m338"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M338: Field '…' … (…) overlaps '…' … (…) …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M338"
symptoms: ["M338", "Field '%NAME%' %BITRANGE% (%ACCESS%) overlaps '%NAME2%' %BITRANGE2% (%ACCESS2%) %LINE%"]
symptom_regex: "^Field '.+?' .+? \\(.+?\\) overlaps '.+?' .+? \\(.+?\\) .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "Two fields of one register share at least one bit. svdconv checks the read view and the write view separately: a read-only field and a write-only field may overlap, but two fields that are both readable or both writable …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:494", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:510", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:642", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:646", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1107", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1116", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:157"]
---

## Symptom

`M338`
`Field '%NAME%' %BITRANGE% (%ACCESS%) overlaps '%NAME2%' %BITRANGE2% (%ACCESS2%) %LINE%`

## Cause

Two fields of one register share at least one bit. svdconv checks the read view and the write view separately: a read-only field and a write-only field may overlap, but two fields that are both readable or both writable may not (fields without <access> count as read-write). The later field is dropped.

## Fix

Correct the bit ranges so the fields do not overlap. If the same bits mean different things on read and on write, describe them as two fields with <access>read-only</access> and <access>write-only</access>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdRegister.cpp:494`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:510`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:642`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:646`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1107`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1116`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:157`
